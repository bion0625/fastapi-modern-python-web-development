from model.explorer import Explorer
from error import Duplicate, Missing

# 가짜 데이터. 10장에서 실제 데이터베이스와 SQL로 바꾼다.
_explorers = [
    Explorer(name="Claude Hande",
             country="FR",
             description="보름달이 뜨면 만나기 힘듦"),
    Explorer(name="Noah Weiser",
             country="DE",
             description="눈이 나쁘고 벌목도를 가지고 다님")
]

def get_all() -> list[Explorer]:
    """탐험가 목록을 반환한다."""
    return _explorers

def get_one(name: str) -> Explorer:
    """검색한 탐험가를 반환한다."""
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    raise Missing(msg=f"Explorer {name} not fount")

def create(explorer: Explorer) -> Explorer:
    """탐험가를 추가한다."""
    if next((x for x in _explorers if x.name == explorer.name), None):
        raise Duplicate(msg=f"Explorer {explorer.name} already exists")
    _explorers.append(explorer)
    return explorer

def modify(name: str, explorer: Explorer) -> Explorer:
    """탐험가의 정보를 일부 수정한다."""
    _explorer = next((x for x in _explorers if x.name == explorer.name), None)
    if _explorer is not None:
        _explorer = explorer
        return _explorer
    else:
        raise Missing(msg=f"Explorer {name} not fount")

def replace(name: str, explorer: Explorer) -> Explorer:
    """탐험가를 완전히 교체한다."""
    _explorer = next((x for x in _explorers if x.name == explorer.name), None)
    if _explorer is None:
        raise Missing(msg=f"Explorer {name} not fount")

    _explorer = explorer
    return _explorer

def delete(name: str) -> bool:
    """탐험가를 삭제한다. 만약 대상이 없다면 False를 반환한다."""
    if not name:
        return False
    
    _explorer = next((x for x in _explorers if x.name == name), None)
    if _explorer is None:
        raise Missing(msg=f"Explorer {name} not fount")
    
    _explorers.remove(_explorer)
    return True