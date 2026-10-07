#!/usr/bin/env python3
"""Export editable Aseprite art and encode local opaque UI BMPs as RGB565.

Requires Aseprite on the Mac. Produces project assets only.
"""
import shutil
import struct
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASEPRITE = Path('/Applications/Aseprite.app/Contents/MacOS/aseprite')
PANELS = ('menu.bmp', 'player.bmp', 'menu-mascot.bmp', 'menu-neck.bmp')


def encode_rgb565(path):
    """Pack an opaque Aseprite RGB/RGBA BMP into RGB565, without dithering."""
    source = path.read_bytes()
    width, height = struct.unpack_from('<ii', source, 18)
    bits = struct.unpack_from('<H', source, 28)[0]
    compression = struct.unpack_from('<I', source, 30)[0]
    rgb24 = bits == 24 and compression == 0
    rgba32 = bits == 32 and compression == 3 and source[54:70] == struct.pack(
        '<IIII', 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    if source[:2] != b'BM' or not (rgb24 or rgba32) or min(width, height) <= 0:
        raise ValueError(f'Expected a bottom-up Aseprite RGB/RGBA BMP: {path}')
    source_offset = struct.unpack_from('<I', source, 10)[0]
    pixel_bytes = bits // 8
    source_stride = (width * pixel_bytes + 3) & ~3
    if len(source) < source_offset + source_stride * height:
        raise ValueError(f'Truncated BMP: {path}')
    stride = (width * 2 + 3) & ~3
    pixels = bytearray(stride * height)
    for y in range(height):
        for x in range(width):
            offset = source_offset + y * source_stride + x * pixel_bytes
            blue, green, red = source[offset:offset + 3]
            if rgba32 and source[offset + 3] != 255:
                raise ValueError(f'Panel conversion requires opaque pixels: {path}')
            word = (red >> 3) << 11 | (green >> 2) << 5 | (blue >> 3)
            struct.pack_into('<H', pixels, y * stride + x * 2, word)
    pixel_offset = 66  # File header, BITMAPINFOHEADER and RGB565 channel masks.
    header = struct.pack('<2sIHHI', b'BM', pixel_offset + len(pixels), 0, 0, pixel_offset)
    header += struct.pack('<IiiHHIIiiII', 40, width, height, 1, 16, 3, len(pixels), 2835, 2835, 0, 0)
    header += struct.pack('<III', 0xF800, 0x07E0, 0x001F)
    path.write_bytes(header + pixels)


def main():
    if not ASEPRITE.is_file():
        raise SystemExit('Install Aseprite before exporting native art.')
    subprocess.run(
        [str(ASEPRITE), '-b', '--script', 'design/piplupos/export-native.lua'],
        cwd=ROOT, check=True,
    )
    assets = ROOT / 'themes/piplupos/assets'
    # Rockbox dithers 24-bit backdrops but not ordinary sprite images.
    # Native 16-bit bitfields keep the shared panel shade consistent.
    for name in PANELS:
        encode_rgb565(assets / name)
    delayed = ROOT / 'themes/piplupos-delayed/assets'
    for asset in assets.glob('*.bmp'):
        shutil.copy2(asset, delayed / asset.name)
    print('Exported local PiplupOS assets with consistent RGB565 panels.')


if __name__ == '__main__':
    main()
