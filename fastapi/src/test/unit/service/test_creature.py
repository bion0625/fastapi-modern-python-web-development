import os
os.environ["CRYPTID_UNIT_TEST"] = "true"
import pytest

from model.creature import Creature
from error import Missing, Duplicate
from service import creature as service

@pytest.fixture
def sample() -> Creature:
    return Creature(name="Yeti",
        country="CN",
        description="눈이 나쁘고 벌목도를 가지고 다님")

def test_create(sample):
    service.delete(sample.name)
    resp = service.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    service.delete(sample.name)
    resp = service.create(sample)
    assert resp == sample
    with pytest.raises(Duplicate):
        resp = service.create(sample)

def test_get_exist(sample):
    service.delete(sample.name)
    resp = service.create(sample)
    assert resp == sample
    resp = service.get_one(sample.name)
    assert resp == sample

def test_get_missing():
    with pytest.raises(Missing):
        _ = service.get_one("boxturtle")

def test_modify(sample):
    sample.country = "CA" # Canada!
    resp = service.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    bob: Creature = Creature(name="bob", country="US", area="*",
                             description="some guy", aka="??")
    with pytest.raises(Missing):
        _ = service.modify(bob.name, bob)