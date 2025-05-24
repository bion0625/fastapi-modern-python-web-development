from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from web import creature, explorer, user, game
from fastapi.openapi.utils import get_openapi

# 서버 기동 명령어
# gunicorn src.main:app --worker 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# 윈도우에서 서버 기동 명령어
# uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
# 하지만 main.py 소스에 적용했으니 아래와 같이 기동
# python ./src/main.py

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ui.cryptids.com"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)
app.include_router(game.router)
  
@app.get("/")
def top():
    return "top here"

@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="3.0.2",
        openapi_version="3.0.2",
        description="커스텀 OpenApi 스키마",
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000, workers=4)