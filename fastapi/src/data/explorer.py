from data.init_db import conn, curs
from model.explorer import Explorer
from error import Missing, Duplicate
from sqlite3 import IntegrityError

from sqlalchemy import MetaData, Table, Column, Text
from sqlalchemy import create_engine, select, Row

from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "cryptid.db"

print(f"DB 경로 확인: {DB_PATH}")

engine = create_engine(f"sqlite:///{DB_PATH}")
connn = engine.connect()
meta = MetaData()
explorer_table = Table(
    "explorer",
    meta,
    Column("name", Text, primary_key=True),
    Column("country", Text),
    Column("description", Text),
)

curs.execute("""create table if not exists explorer(
                    name text primary key, 
                    description text,
                    country text)""")

def row_to_model(row: tuple) -> Explorer:
    name, description, country = row
    return Explorer(name=name, description=description, country=country)

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump()

def get_one(name: str) -> Explorer:
    # qry = "select * from explorer where name=:name"
    # params = {"name": name}
    # curs.execute(qry, params)
    # row = curs.fetchone()
    # if row:
    #     return row_to_model(row)
    # else:
    #     raise Missing(msg=f"Explorer {name} not found")
    stmt = select(explorer_table).where(explorer_table.c.name == name)
    result = connn.execute(stmt)
    return result.fetchone()

def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(explorer: Explorer):
    if not explorer:
        return None
    qry = """insert into explorer values
        (:name, :description, :country)"""
    params = model_to_dict(explorer)
    try:
        curs.execute(qry, params)
        conn.commit()
    except IntegrityError:
        raise Duplicate(msg=
                        f"Explorer {explorer.name} already exists")
    return get_one(explorer.name)

def update(name: str, explorer: Explorer):
    if not (name and explorer):
        return None
    qry = """update explorer
                set country=:country,
                    name=:name,
                    description=:description
                where name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = name
    _ = curs.execute(qry, params)
    conn.commit()
    if curs.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(msg=f"Explorer {name} not fount")


def modify(name: str, explorer: Explorer):
    return update(name, explorer)

def replace(name: str, explorer: Explorer):
    return update(name, explorer)

def delete(name: str) -> bool:
    if not name:
        return False
    qry = "delete from explorer where name = :name"
    params = {"name": name}
    res = curs.execute(qry, params)
    conn.commit()
    if curs.rowcount != 1:
        raise Missing(msg=f"Explorer {name} not found")
    return bool(res)