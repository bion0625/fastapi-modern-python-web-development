from fastapi import FastAPI, File

app = FastAPI()

@app.post("/small")
async def upload_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"