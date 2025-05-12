from dataclasses import dataclass

@dataclass
class CreatureDataClass():
    name: str
    country: str
    area: str
    description: str
    aka: str

dataclass_thing = CreatureDataClass("yeti",
    "CN",
    "Himalaya",
    "Hirsute Himalayan",
    "Abominable Snowman")

print("Name is", dataclass_thing.name)