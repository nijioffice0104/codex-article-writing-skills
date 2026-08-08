#!/usr/bin/env python3
"""Normalize one Coconala blog image to an exact canvas and byte ceiling."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def normalize(source: Path, destination: Path, width: int, height: int, max_kb: int) -> tuple[int, int]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        fitted = ImageOps.fit(
            image.convert("RGB"),
            (width, height),
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        for quality in range(88, 39, -3):
            fitted.save(destination, "JPEG", quality=quality, optimize=True, progressive=True)
            if destination.stat().st_size <= max_kb * 1024:
                return destination.stat().st_size, quality
    raise RuntimeError(f"Could not reduce {source} to {max_kb} KB")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=670)
    parser.add_argument("--max-kb", type=int, default=700)
    args = parser.parse_args()
    size, quality = normalize(args.source, args.destination, args.width, args.height, args.max_kb)
    print(f"{args.destination}\t{args.width}x{args.height}\t{size} bytes\tquality={quality}")


if __name__ == "__main__":
    main()
