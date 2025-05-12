from pydantic import BaseModel, constr, Field

class Creature(BaseModel):
    # name: constr(min_length=2)
    name: str = Field(..., min_length=2)
    country: str
    area: str
    description: str
    aka: str

thing = Creature(
    name = "yeti",
    country = "CN",
    area = "himalayas",
    description = "Hirsute Himalayan",
    aka = "Abominable Snowman"
)

print("Name is", thing.name)

bad_creature = Creature(
    description="it's a raccoon",
    area="your attic"
)