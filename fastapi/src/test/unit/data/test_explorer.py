import os
import pytest
from model.explorer import Explorer
from error import Missing, Duplicate

# 아래에서 data 모듈을 가져오기 전에 설정한다.
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"

from data import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Noah Weiser", country="DE",
                    description="눈이 나쁘고 벌목도를 가지고 다님")

def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)

def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample

def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("boxturtle")

def test_modify(sample):
    sample.country = "JP"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing(sample):
    thing: Explorer = Explorer(name="snurfle", country="RU",
                               description="some thing")
    with pytest.raises(Missing):
        _ = explorer.modify(thing.name, thing)

def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is True

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)