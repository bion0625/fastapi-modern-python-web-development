from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from web import creature, explorer, user

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

@app.get("/")
def top():
    return "top here"

@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)