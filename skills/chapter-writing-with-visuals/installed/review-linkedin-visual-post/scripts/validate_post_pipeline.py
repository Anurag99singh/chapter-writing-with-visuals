#!/usr/bin/env python3
"""Validate complete-base provenance and portrait-only final changes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageOps


ALLOWED_RENDER_METHOD = "integrated-image-generation"
ALLOWED_AFTER_BASE = {
    "validate-dimensions",
    "format-preserving-export",
    "mobile-preview",
    "place-portrait",
    "review",
}


def circular_mask(size: int) -> Image.Image:
    scale = 4
    large = Image.new("L", (size * scale, size * scale), 0)
    ImageDraw.Draw(large).ellipse(
        (0, 0, size * scale - 1, size * scale - 1), fill=255
    )
    return large.resize((size, size), Image.Resampling.LANCZOS)


def load_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"Expected a JSON object in {path}")
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, type=Path)
    parser.add_argument("--final", required=True, type=Path)
    parser.add_argument("--trace", required=True, type=Path)
    parser.add_argument("--portrait-verification", required=True, type=Path)
    parser.add_argument("--x", required=True, type=int)
    parser.add_argument("--y", required=True, type=int)
    parser.add_argument("--diameter", required=True, type=int)
    parser.add_argument("--inset", required=True, type=int)
    args = parser.parse_args()

    errors: list[str] = []
    base = Image.open(args.base).convert("RGB")
    final = Image.open(args.final).convert("RGB")
    if base.size != (1080, 1350):
        errors.append(f"portrait-ready base is {base.size}, expected (1080, 1350)")
    if final.size != base.size:
        errors.append(f"final size {final.size} differs from base size {base.size}")

    width, height = base.size
    if args.inset < 0 or args.inset * 2 >= args.diameter:
        errors.append("invalid portrait inset")
    if (
        args.x < 0
        or args.y < 0
        or args.x + args.diameter > width
        or args.y + args.diameter > height
    ):
        errors.append("portrait slot falls outside the canvas")

    inner = args.diameter - 2 * args.inset
    difference = ImageChops.difference(base, final).convert("L")
    allowed = Image.new("L", base.size, 0)
    allowed.paste(
        circular_mask(inner).point(lambda value: 255 if value else 0),
        (args.x + args.inset, args.y + args.inset),
    )
    outside = ImageChops.multiply(difference, ImageOps.invert(allowed))
    outside_bbox = outside.getbbox()
    if outside_bbox is not None:
        errors.append(f"pixels changed outside portrait interior: {outside_bbox}")
    if difference.getbbox() is None:
        errors.append("base and final are identical; portrait insertion is not evidenced")

    verification = load_json(args.portrait_verification)
    if verification.get("verified") is not True:
        errors.append("portrait verification does not report verified=true")
    if verification.get("outside_change_bbox") is not None:
        errors.append("portrait verification reports changes outside the slot")

    trace = load_json(args.trace)
    required = {
        "portrait_ready_base",
        "final_image",
        "communication_mode",
        "exact_copy",
        "generation_prompt",
        "render_method",
        "complete_poster_generated_together",
        "separate_component_assets",
        "semantic_edits_after_generation",
        "composition_sentence",
        "discarded_complete_attempts",
        "slot_geometry",
        "canvas",
        "font_sizes_px",
        "space_allocation",
        "operations_after_base",
    }
    missing = sorted(required - set(trace))
    if missing:
        errors.append("render trace missing fields: " + ", ".join(missing))
    if trace.get("render_method") != ALLOWED_RENDER_METHOD:
        errors.append(f"unapproved render method: {trace.get('render_method')!r}")
    if trace.get("complete_poster_generated_together") is not True:
        errors.append("trace does not confirm that the complete poster was generated together")
    if trace.get("separate_component_assets") is not False:
        errors.append("trace permits separately created component assets")
    if trace.get("semantic_edits_after_generation") is not False:
        errors.append("trace permits semantic edits after image generation")
    generation_prompt = trace.get("generation_prompt")
    if not isinstance(generation_prompt, str) or len(generation_prompt.strip()) < 100:
        errors.append("generation_prompt is missing or implausibly short")
    composition_sentence = trace.get("composition_sentence")
    if not isinstance(composition_sentence, str) or len(composition_sentence.strip()) < 30:
        errors.append("composition_sentence is missing or implausibly short")
    discarded_attempts = trace.get("discarded_complete_attempts")
    if not isinstance(discarded_attempts, int) or isinstance(discarded_attempts, bool) or discarded_attempts < 0:
        errors.append("discarded_complete_attempts must be a non-negative integer")
    if trace.get("communication_mode") not in {"text-led", "diagram-led"}:
        errors.append("communication_mode must be text-led or diagram-led")
    exact_copy = trace.get("exact_copy")
    if isinstance(exact_copy, str):
        if len(exact_copy.strip()) < 20:
            errors.append("exact_copy is missing or implausibly short")
    elif isinstance(exact_copy, (dict, list)):
        if not exact_copy:
            errors.append("exact_copy is empty")
    else:
        errors.append("exact_copy must be a string, object, or list")

    expected_slot = {
        "x": args.x,
        "y": args.y,
        "diameter": args.diameter,
        "inset": args.inset,
    }
    if trace.get("slot_geometry") != expected_slot:
        errors.append("trace slot_geometry does not match validator arguments")
    if trace.get("canvas") != {"width": width, "height": height}:
        errors.append("trace canvas does not match the image dimensions")

    font_sizes = trace.get("font_sizes_px")
    if not isinstance(font_sizes, dict):
        errors.append("font_sizes_px must be an object")
    else:
        for role, minimum in {"body": 30, "labels": 28, "takeaway": 34}.items():
            value = font_sizes.get(role)
            if not isinstance(value, (int, float)) or value < minimum:
                errors.append(f"{role} font size must be at least {minimum}px")

    allocation = trace.get("space_allocation")
    if not isinstance(allocation, dict):
        errors.append("space_allocation must be an object")
    elif trace.get("communication_mode") == "text-led":
        text_share = allocation.get("text")
        graphic_share = allocation.get("graphic")
        if not isinstance(text_share, (int, float)) or text_share < 0.55:
            errors.append("text-led composition must allocate at least 55% to text")
        if not isinstance(graphic_share, (int, float)) or graphic_share > 0.35:
            errors.append("text-led composition must allocate no more than 35% to graphics")
    operations = trace.get("operations_after_base")
    if not isinstance(operations, list):
        errors.append("operations_after_base must be a list")
    else:
        disallowed = [op for op in operations if op not in ALLOWED_AFTER_BASE]
        if disallowed:
            errors.append("disallowed operations after base: " + ", ".join(map(str, disallowed)))
        if "place-portrait" not in operations:
            errors.append("operations_after_base does not include place-portrait")

    result = {
        "verdict": "PASS" if not errors else "FAIL",
        "base": str(args.base.resolve()),
        "final": str(args.final.resolve()),
        "outside_change_bbox": list(outside_bbox) if outside_bbox else None,
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
