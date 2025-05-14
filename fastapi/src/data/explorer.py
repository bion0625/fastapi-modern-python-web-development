from data.init_db import conn, curs
from model.explorer import Explorer

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
    qry = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(explorer: Explorer):
    qry = """insert into explorer values
        (:name, :description, :country)"""
    params = model_to_dict(explorer)
    curs.execute(qry, params)
    conn.commit()
    return get_one(explorer.name)

def modify(name: str, explorer: Explorer):
    qry = """update explorer
                set country=:country,
                    name=:name,
                    description=:description
                where name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = name
    _ = curs.execute(qry, params)
    conn.commit()
    return get_one(explorer.name)

def replace(name: str, explorer: Explorer):
    qry = """update explorer
                set country=:country,
                    name=:name,
                    description=:description
                where name=:name_orig"""
    params = model_to_dict(explorer)
    params["name_orig"] = name
    _ = curs.execute(qry, params)
    conn.commit()
    return get_one(explorer.name)

def delete(name: str) -> bool:
    qry = "delete from explorer where name = :name"
    params = {"name": name}
    res = curs.execute(qry, params)
    conn.commit()
    return bool(res)