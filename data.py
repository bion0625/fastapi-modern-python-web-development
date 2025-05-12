from model import Creature

_creatures: list[Creature] = [
    Creature(
        name = "yeti",
        country = "CN",
        area = "himalayas",
        description = "Hirsute Himalayan",
        aka = "Abominable Snowman"
    ),
    Creature(
        name = "sasquatch",
        country = "US",
        area = "*",
        description = "Yetti's cousin Eddie",
        aka = "BigFoot"
    ),
]

def get_creatures() -> list[Creature]:
    return _creatures