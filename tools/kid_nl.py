# SPDX-License-Identifier: GPL-3.0-only
# Written in October 2026 by rondlite, for the Dutch translation of Josh's Rainbow mode
"""Rainbow mode in Dutch: every word it shows, in one place (read by tools/gen_kid_art.py).

  NAMES   the friends and the look-alikes' stand-ins: KID_NAME in kid_art.h is written in Dutch
  HATS    the hats: KID_HAT_NAME
  WORDS   the band's other words, by where they show: KID_NL in kid_art.h, English -> Dutch, looked up by kid_nl()
          (firmware/src/kid.c) where the words reach the screen; the English stays in kid.c, so its preset names (matched
          by name) and Felucca's own screens are untouched

A word or name with no Dutch here shows in English (gen_kid_art.py says which). Kept in English on purpose: names
(GOO, GOOBERT, APRIL, BEAT BOT, RODEO), the beats that are a style (ROCK, DISCO, HIP HOP, ...), the songs with no Dutch
version of the same tune, the note letters (C D E F G A B, the Dutch ones too) and 8VA / 15MA.

The band's font: capitals, digits 1 3 4 5 7 8 9, # ! - ? and spaces; no accents (so no ë: FEE-, not FEEËN-).
check() stops the build when a Dutch word would not fit where it shows (each place below has its own room).
"""
import re

FONT = re.compile(r"[A-Z1345789#!?-]+( +[A-Z1345789#!?-]+)*")

# the friends (gen_kid_art.py FRIENDS) and the stand-ins (STAND_INS): one line at scale 4 (9 letters) or 3 (13), or two
# lines at 3, cut at the space or hyphen nearest the middle (13 letters a line, 19 in all)
NAMES = {
    "DUCKY": "EENDJE", "PINK DUCKY": "ROZE EENDJE", "COOL DUCKY": "STOER EENDJE", "AXOLOTL": "AXOLOTL",
    "UNICORN": "EENHOORN", "GIRAFFE": "GIRAF", "GOO": "GOO", "GOOBERT": "GOOBERT", "BLUE PUP": "BLAUWE PUP",
    "RED MONSTER": "RODE MONSTER", "BLUE MONSTER": "BLAUWE MONSTER", "APRIL": "APRIL", "SCISSORS": "SCHAAR",
    "GHOST": "SPOOK", "WEB HERO": "WEBHELD", "BUTTERFLY": "VLINDER", "KITTY": "KATJE", "FROG": "KIKKER",
    "ROBOT": "ROBOT", "RAINBOW": "REGENBOOG", "PRINCESS DUCKY": "PRINSES EENDJE", "RED PUP": "RODE PUP",
    "YELLOW BIRD": "GELE VOGEL", "SLIMY": "SLIJMPJE", "BUNNY": "KONIJNTJE", "PANDA": "PANDA", "PENGUIN": "PINGUIN",
    "OWL": "UIL", "BEE": "BIJ", "LADYBUG": "LIEVEHEERS-BEESTJE", "DINO": "DINO", "WHALE": "WALVIS",
    "OCTOPUS": "OCTOPUS", "FISH": "VIS", "TURTLE": "SCHILDPAD", "ICE CREAM": "IJSJE", "CUPCAKE": "CUPCAKE",
    "ROCKET": "RAKET", "STRAWBERRY": "AARDBEI", "STAR": "STER", "T-REX": "T-REX", "SKELETON": "SKELET",
    "RANCHER": "COWBOY", "RODEO": "RODEO", "VACUUM": "STOFZUIGER", "SPACE HERO": "RUIMTEHELD", "BEAT BOT": "BEAT BOT",
    "TOY DRUM": "TROMMELTJE", "BONGO": "BONGO", "MONKEY": "AAPJE", "ELEPHANT": "OLIFANT", "RACE CAR": "RACEAUTO",
    "JELLYFISH": "KWAL", "BEAR": "BEER", "SNOWMAN": "SNEEUWPOP", "CRAB": "KRAB", "WOLF": "WOLF", "CAMEL": "KAMEEL",
    "SCIENTIST": "PROFESSOR", "FLYTRAP": "VLIEGENVANGER", "SUNFLOWER": "ZONNEBLOEM", "SPIDER MOM": "SPINNENMAMA",
    "DRAGON DUCK": "DRAKENEEND", "SPIDER GRANDMA": "SPINNENOMA", "NIGHT LIGHT": "NACHTLAMPJE",
    "GREEN QUEEN": "GROENE KONINGIN", "KING AXOLOTL": "KONING AXOLOTL", "FAIRY MONSTER": "ELFENMONSTER",
    "MORNING GLORY": "OCHTENDGLORIE", "GROUCH": "MOPPERAAR", "TIGER CUB": "TIJGERTJE", "RACCOON": "WASBEER",
    "GOLDENROD": "GULDENROEDE", "PIANO PAL": "PIANOMAATJE", "FLUTE BIRD": "FLUITVOGEL", "SAX CAT": "SAXKAT",
    "COW": "KOE", "PIG": "VARKEN", "SHEEP": "SCHAAP", "SHARK": "HAAI", "SEAHORSE": "ZEEPAARDJE", "STARFISH": "ZEESTER",
    "SNAIL": "SLAK", "CATERPILLAR": "RUPS", "FIREFLY": "GLIMWORM", "TRICERATOPS": "TRICERATOPS",
    "STEGOSAURUS": "STEGOSAURUS", "PIZZA": "PIZZA", "DONUT": "DONUT", "BANANA": "BANAAN", "TRAIN": "TREIN",
    "FIRE TRUCK": "BRANDWEERAUTO", "SCHOOL BUS": "SCHOOLBUS", "HELICOPTER": "HELIKOPTER", "GOLD DUCKY": "GOUDEN EENDJE",
    # the stand-ins
    "SPOTTY PUP": "STIPPELPUP", "FOX": "VOS", "FUZZY": "PLUIZEBOL", "BIG BLUE": "BLAUWE REUS", "SPIDER": "SPIN",
    "PUMPKIN": "POMPOEN", "CHICK": "KUIKEN", "BAT": "VLEERMUIS", "HORSE": "PAARD", "CACTUS": "CACTUS",
    "ALIEN": "MARSMANNETJE", "RAINBOW MOM": "REGENBOOGMAMA", "GREEN GRANNY": "GROENE OMA", "PIXIE": "ELFJE",
    "ALLEY CAT": "STRAATKAT", "LION CUB": "LEEUWTJE", "SQUIRREL": "EEKHOORN",
}

# the hats (gen_kid_art.py HATS): the band names one on HOME held, then KNOB 4 (scale 3: 13 letters, two lines)
HATS = {
    "PARTY": "FEESTHOED", "CROWN": "KROON", "TOP HAT": "HOGE HOED", "BUCKET": "VISSERSHOED", "WIZARD": "TOVERHOED",
    "BEANIE": "MUTS", "WESTERN": "COWBOYHOED", "CHEF": "KOKSMUTS", "PROPELLER": "PROPELLERPET", "FLOWERS": "BLOEMEN",
    "STAR": "STER",
}

# where a word shows: (the most it may be wide in px, two lines allowed)  (a letter is 6 x scale px, less one scale)
PLACES = {
    "big": (232, False),        # kid_band_word at scale 6: YES! (6 letters)
    "listen": (232, False),     # .. at scale 5 (7 letters)
    "word": (232, False),       # .. at scale 4: TRY AGAIN, YOUR TURN; a top-row effect (9 letters)
    "mode": (178, False),       # ALGORITHM's mode at scale 3 beside its picture (10 letters)
    "meter": (232, False),      # a knob's word at scale 3, its dots under it (13 letters)
    "hint": (232, True),        # the band's other words at scale 3 (13 letters, or two lines)
    "drum": (232, False),       # a drum friend's drum, at scale 4 or 3 (13 letters)
    "write": (186, False),      # WRITE's words at scale 3 beside the friend (10 letters); the beats show there too
    "chord": (178, False),      # a chord's name at scale 3 after its root and a space ("C# " and 10 letters)
    "grown": (232, False),      # the grown-ups' words at scale 2 (19 letters)
    "hello": (232, False),      # the hello at scale 8 (HI!: 5 letters)
}
SCALE = {"big": 6, "listen": 5, "word": 4, "mode": 3, "meter": 3, "hint": 3, "drum": 3, "write": 3, "chord": 3, "grown": 2,
         "hello": 8}

WORDS = {
    "big": {"YES!": "JA!", "STAR!": "STER!", "YAY!": "HOERA!"},
    "listen": {"LISTEN": "LUISTER"},
    "word": {"TRY AGAIN": "NOG EENS", "YOUR TURN": "NU JIJ!",
             # the top row's effects
             "HICCUP": "HIK", "BACKWARDS": "ACHTERUIT", "SLEEPY": "SLAPERIG", "SQUEAKY": "PIEPSTEM", "GIANT": "REUS",
             "FREEZE": "BEVRIES"},
    "mode": {"1 FRIEND": "1 VRIEND", "3 FRIENDS": "3 VRIENDEN", "STRUM": "TOKKELEN", "ACCORDION": "ACCORDEON",
             "GUESS": "RADEN", "FOLLOW": "VOLGEN", "CHORDS": "AKKOORDEN", "COPY ME": "DOE MIJ NA"},
    "meter": {"BIG": "GROOT", "SMALL": "KLEIN", "MEDIUM": "MIDDEL", "DAY": "DAG", "SUNSET": "AVOND", "NIGHT": "NACHT",
              "WIGGLE": "WIEBEL", "SLOW": "LANGZAAM", "WALK": "WANDELEN", "FAST": "SNEL", "SPARKLE": "GLITTER",
              "SPARKLE TUNE": "GLITTER LIED", "SPARKLE ALL": "GLITTER ALLES", "STARS": "STERREN"},
    "hint": {"NEW HAT!": "NIEUWE HOED!", "NEW FRIEND!": "NIEUWE VRIEND!", "NEW SKY!": "NIEUWE LUCHT!",
             "NO HAT": "GEEN HOED",
             # FOLLOW's songs: the Dutch name where the tune is a Dutch song too
             "TWINKLE": "KORTJAKJE", "FRERE JACQUES": "VADER JACOB", "SILENT NIGHT": "STILLE NACHT",
             # CHORDS' lessons
             "FIRST CHORDS": "EERSTE AKKOORDEN", "POP FOUR": "POP VIER", "SEVENTHS": "SEPTIEMEN"},
    "drum": {"KICK": "BASDRUM", "SNARE": "SNAREDRUM", "CLAP": "KLAP", "OPEN HAT": "OPEN HI-HAT", "RIM": "RAND",
             "CLAVE": "CLAVES", "COWBELL": "KOEBEL", "CYMBAL": "BEKKEN"},
    "write": {"WRITE": "SCHRIJVEN", "LOOP": "AFSPELEN", "NEW SONG": "NIEUW LIED", "NO BEAT": "GEEN RITME",
              # the beats (SEQ)
              "DANCE": "DANS", "MARCH": "MARS", "SPOOKY": "GRIEZELIG", "TRAIN": "TREIN", "LULLABY": "WIEGELIED",
              "HOEDOWN": "BOERENDANS"},
    "chord": {"MAJOR": "GROOT", "MINOR": "KLEIN", "SEVEN": "ZEVEN", "NINE": "NEGEN"},
    "grown": {"LOOK-ALIKES ON": "TV-FIGUREN AAN", "LOOK-ALIKES OFF": "TV-FIGUREN UIT",
              # the grown-ups' NAME (the buttons keep their printed names)
              "YOUR NAME": "JOUW NAAM", "ALGORITHM  NEXT": "ALGORITHM  VOLGENDE", "SAVE  KEEP IT": "SAVE  BEWAAR",
              "HOME  LEAVE IT": "HOME  LAAT ZO",
              # the SMK-37's hello: RAINBOW under the name
              "RAINBOW": "REGENBOOG"},
    "hello": {"HI": "HOI", "HI!": "HOI!"},
}


def cut(s):
    """kid.c kid_band_setup's two lines: at the space or hyphen nearest the middle (a hyphen stays on the first)"""
    best = None
    for i, c in enumerate(s):
        if c in " -" and (best is None or abs(i - len(s) // 2) < abs(best - len(s) // 2)):
            best = i
    if best is None:
        return None
    return s[:best + (s[best] == "-")], s[best + 1:]


def fits(s, room, two, sc):
    if len(s) * 6 * sc - sc <= room:
        return True
    if not two or len(s) >= 20 or not cut(s):     # (kid.c: kf.l1, kf.l2 hold 19)
        return False
    return all(len(w) * 18 - 3 <= 232 for w in cut(s))


def name_fits(s):                                 # a friend's name: as "hint", at scale 3 or two lines
    return fits(s, 232, True, 3)


def check(kid_c):
    """every Dutch word in the font and in its room; every English one still in kid.c; no word with two Dutch ones"""
    seen = {}
    for name, nl in list(NAMES.items()) + list(HATS.items()):
        if not FONT.fullmatch(nl) or not name_fits(nl):
            raise SystemExit(f"kid nl: {nl!r} ({name}) is not in the band's font or does not fit, even on two lines")
    for place, words in WORDS.items():
        room, two = PLACES[place]
        for en, nl in words.items():
            if not FONT.fullmatch(nl) or not fits(nl, room, two, SCALE[place]):
                raise SystemExit(f"kid nl: {nl!r} ({en}) is not in the band's font or too wide for its place ({place})")
            if f'"{en}"' not in kid_c:
                raise SystemExit(f"kid nl: {en!r} is not a word of kid.c (renamed there?)")
            if seen.setdefault(en, nl) != nl:
                raise SystemExit(f"kid nl: {en!r} has two Dutch words ({seen[en]}, {nl})")
    return [(en, nl) for en, nl in seen.items() if en != nl]
