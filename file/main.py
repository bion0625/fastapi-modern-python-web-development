from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/small")
async def upload_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"

@app.post("/big")
async def upload_bog_file(big_file: UploadFile) -> str:
    return f"file size: {big_file.size}, name: {big_file.filename}"