#!/usr/bin/env python3
"""Validate basic delivery requirements for a LinkedIn single-image post."""

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageStat


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    args = parser.parse_args()

    if not args.image.is_file():
        print(f"ERROR: file not found: {args.image}")
        return 2

    with Image.open(args.image) as image:
        width, height = image.size
        errors = []
        warnings = []

        if (width, height) != (1080, 1350):
            errors.append(f"expected 1080x1350, found {width}x{height}")
        if image.mode not in {"RGB", "RGBA"}:
            warnings.append(f"unexpected color mode: {image.mode}")

        rgb = image.convert("RGB")
        stat = ImageStat.Stat(rgb.resize((64, 80)))
        if max(stat.var) < 80:
            warnings.append("image has unusually low visual contrast")

        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1

        print(f"OK: {args.image.name} is 1080x1350")
        for warning in warnings:
            print(f"WARNING: {warning}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
