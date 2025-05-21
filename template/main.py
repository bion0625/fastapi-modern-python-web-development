from fastapi import FastAPI, Form
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# main.py가 포함된 디렉터리:
top = Path(__file__).resolve().parent

app.mount("/static",
          StaticFiles(directory=f"{top}/static", html=True),
          name="free")

@app.post("/who2")
def greet2(name: str = Form()):
    return f"Hello, {name}?"