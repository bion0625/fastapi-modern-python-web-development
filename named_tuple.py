from collections import namedtuple

creatureNamedTuple = namedtuple("CreatureNamedTuple", "name, country, area, description, aka")
namedtuple_ting = creatureNamedTuple("yeti", "CN", "Himalaya", "Hirsute Himalayan", "Abominable Snowman")
print("Name is", namedtuple_ting[0])
print("Name is", namedtuple_ting.name)