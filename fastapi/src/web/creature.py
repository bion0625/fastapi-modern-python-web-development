import os
from fastapi import APIRouter, HTTPException
from model.creature import Creature

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as service
else:
    import service.creature as service
from error import Missing, Duplicate

router = APIRouter(prefix="/creature")

@router.get("")
@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
@router.get("/{name}/")
def get_one(name) -> Creature | None:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

# 나머지 엔드포인트, 현재는 아무 일도 하지 않는다.
@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.patch("/{name}")
@router.patch("/{name}/")
def modify(name, creature: Creature) -> Creature:
    try:
        return service.modify(name, creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.put("/{name}")
@router.put("/{name}/")
def replace(name, creature: Creature) -> Creature:
    try:
        return service.modify(name, creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{name}", status_code=204)
@router.delete("/{name}/", status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

from fastapi import Response
import plotly.express as px

# @router.get("/test/")
@router.get("/chart/test")
@router.get("/chart/test/")
def test():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    # fig_bytes = fig.to_image(format="png")
    fig_bytes = fig.to_html(full_html=True)
    # return Response(content=fig_bytes, media_type="image/png")
    return Response(content=fig_bytes, media_type="text/html")

from collections import Counter

@router.get("/chart/plot")
@router.get("/chart/plot/")
def plot():
    cretures = service.get_all()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counts = Counter(creature.name[0] for creature in cretures if len(creature.name) > 0)
    y = {letter: counts.get(letter, 0) for letter in letters}
    fig = px.histogram(x=list(letters), y=y, title="Creature Names", labels={"x": "Initial", "y": "Initial"})
    fig_bytes = fig.to_html(full_html=True)
    return Response(content=fig_bytes, media_type="text/html")

import country_converter as coco

@router.get("/map/sample")
@router.get("/map/sample/")
def map():
    creatures = service.get_all()
    iso2_codes = set(creature.country for creature in creatures)
    iso3_codes = coco.convert(names=iso2_codes, to="ISO3")
    fig = px.choropleth(
        locationmode="ISO-3",
        locations=iso3_codes)
    fig_bytes = fig.to_html(full_html=True)
    return Response(content=fig_bytes, media_type="text/html")

@router.get("/map/sample2")
@router.get("/map/sample2/")
def map():
    creatures = service.get_all()
    areas = [creature.country for creature in creatures]
    fig = px.choropleth(
        locationmode="USA-states",
        locations=areas
    )
    fig_bytes = fig.to_html(full_html=True)
    return Response(content=fig_bytes, media_type="text/html")