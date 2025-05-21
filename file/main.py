from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from typing import Generator

app = FastAPI()

@app.post("/small")
async def upload_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"

@app.post("/big")
async def upload_bog_file(big_file: UploadFile) -> str:
    return f"file size: {big_file.size}, name: {big_file.filename}"

@app.get("/small/{name}")
async def download_small_file(name):
    return FileResponse(name)

def gen_file(path: str) -> Generator:
    with open(file=path, mode="rb") as file:
        yield file.read()

@app.get("/download_big/{name}")
async def download_big_file(name: str):
    gen_expr = gen_file(path=name)
    response = StreamingResponse(
        content=gen_expr,
        status_code=200
    )
    return response