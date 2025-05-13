from fastapi import FastAPI, Header, Response, Body

app = FastAPI()

@app.get("/hi/{who}")
def greet(who: str):
    return f"Hello? {who}?"

@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello? {who}?"

@app.get("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)


import datetime
import pytest
from fastapi.encoders import jsonable_encoder
import json

@pytest.fixture
def data():
    return datetime.datetime.now()

def test_json_dump(data):
    with pytest.raises(Exception):
        _ = json.dumps(data)

def test_encoder(data):
    out = jsonable_encoder(data)
    assert out
    join_out = json.dumps(out)
    assert join_out