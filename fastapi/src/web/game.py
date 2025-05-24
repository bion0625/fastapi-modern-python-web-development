from pathlib import Path

from fastapi import APIRouter, Body, Request
from fastapi.templating import Jinja2Templates

from service import game as service

router = APIRouter(prefix = "/game")

# 게임 초기화
@router.get("")
@router.get("/")
def game_start(request: Request):
    name = service.get_word()
    top = Path(__file__).resolve().parents[1] # 2단계 상위 디렉터리
    templates = Jinja2Templates(directory=f"{top}/template")
    return templates.TemplateResponse("game.html", {"request": request, "word": name})

# 다음 단계 요청
@router.post("")
@router.post("/")
async def game_step(word: str = Body(), guess: str = Body()):
    score = service.get_score(word, guess)
    return score