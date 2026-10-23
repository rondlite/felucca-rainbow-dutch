#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Written in October 2026 by rondlite, for the Dutch translation of Josh's Rainbow mode
"""The landing page's pictures in Dutch: the poster of the friends with their Dutch names (tools/kid_nl.py) and the card
a shared link shows.
  python3 tools/landing/images_nl.py landing
The friends are the firmware's own pictures (tools/gen_kid_art.py FRIENDS), 1.5 times their size, ten to a row; the
secret friend is left out. The card has landing/screen-5.png on it. The font is the UI's Inter Tight (assets/fonts,
SIL OFL 1.1)."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import gen_kid_art   # noqa: E402
import kid_nl        # noqa: E402

W, H, COLS, CELL, ROW, TOP = 1080, 1350, 10, 108, 106, 178
BG, INK, SOFT = (36, 24, 48), (255, 255, 255), (214, 196, 236)
STRIPE = [(236, 52, 64), (255, 140, 30), (255, 216, 46), (80, 200, 90), (56, 128, 244), (150, 88, 226)]
THANKS = ("Met dank aan u/veecheech, u/theskyisfalling1, u/lastapoc, u/nutty_cartoon, u/ReallyLongLake, u/Yablan "
          "en u/litomanu")


def font(size, weight):
    f = ImageFont.truetype(str(ROOT / "assets" / "fonts" / "InterTight[wght].ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def centred(d, y, text, f, fill):
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill)


def poster(out):
    friends = [(n, f) for n, f in gen_kid_art.FRIENDS if n != gen_kid_art.SECRET_FRIEND]
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    for i, c in enumerate(STRIPE):
        d.rectangle([i * W // 6, 0, (i + 1) * W // 6 - 1, 9], fill=c)
    centred(d, 38, f"Maak kennis met de {len(friends)} vriendjes", font(50, 800), INK)
    centred(d, 112, "elk met een eigen geluid, lucht en lievelingsritme", font(27, 400), SOFT)
    for i, (name, f) in enumerate(friends):
        x, y = (i % COLS) * CELL, TOP + (i // COLS) * ROW
        pic = f().im.resize((72, 72), Image.NEAREST)
        im.paste(pic, (x + (CELL - 72) // 2, y), pic)
        nl = kid_nl.NAMES.get(name, name)
        lines = [nl]
        for size in (13, 12):                                     # (as big as fits the cell; else two lines)
            f13 = font(size, 700)
            if d.textlength(nl, font=f13) <= CELL - 6:
                break
        else:
            if kid_nl.cut(nl):
                lines, f13 = list(kid_nl.cut(nl)), font(12, 700)
            else:                                                 # (one long word: smaller)
                f13 = next(font(z, 700) for z in (11, 10, 9) if d.textlength(nl, font=font(z, 700)) <= CELL - 4 or z == 9)
        for j, line in enumerate(lines):
            w = d.textlength(line, font=f13)
            d.text((x + (CELL - w) / 2, y + 76 + j * 12), line, font=f13, fill=INK)
    centred(d, H - 52, THANKS, font(19, 500), SOFT)
    im.save(out, optimize=True)


def card(out, shot):
    cw, chh = 1200, 630
    im = Image.new("RGB", (cw, chh), BG)
    d = ImageDraw.Draw(im)
    for i, c in enumerate(STRIPE):
        d.rectangle([i * cw // 6, 0, (i + 1) * cw // 6 - 1, 11], fill=c)
    d.rounded_rectangle([44, 89, 44 + 452, 89 + 452], 24, fill=(14, 10, 20))
    im.paste(Image.open(shot).convert("RGB").resize((400, 400), Image.NEAREST), (70, 115))
    d.text((548, 128), "Regenboogmodus", font=font(64, 800), fill=INK)
    d.text((550, 210), "voor de M-VAVE FM-1, in het Nederlands", font=font(28, 500), fill=(186, 150, 255))
    for i, line in enumerate(["94 vriendjes, 21 ritmes, 6 trucjes", "elke toets laat zijn noot zien in kleur",
                              "elke draaiknop doet iets", "gratis en open source, ook in je browser"]):
        y = 300 + i * 58
        d.ellipse([552, y + 9, 568, y + 25], fill=STRIPE[i])
        d.text((586, y), line, font=font(27, 400), fill=SOFT)
    im.save(out, optimize=True)


if __name__ == "__main__":
    folder = Path(sys.argv[1])
    poster(folder / "friends.png")
    card(folder / "card.png", folder / "screen-5.png")
