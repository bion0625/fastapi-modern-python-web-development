from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

top = Path(__file__).resolve().parent

template_obj = Jinja2Templates(directory=f"{top}/template")

# 미리 정의된 친구들 목록을 가져온다
from fake.creature import _creatures as fake_creatures
from fake.explorer import _explorers as fake_explorers

@app.get("/list")
def explorer_list(request: Request):
    return template_obj.TemplateResponse("list.html",
                                         {"request": request,
                                          "explorers": fake_explorers,
                                          "creatures": fake_creatures})