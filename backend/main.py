from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

STORAGE_PATH = "backend/storage"
os.makedirs(STORAGE_PATH, exist_ok=True)

@app.post("/upload")
async def upload_file(username: str, file: UploadFile = File(...)):
    user_path = os.path.join(STORAGE_PATH, username)
    os.makedirs(user_path, exist_ok=True)

    file_path = os.path.join(user_path, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {"status": "uploaded", "user": username, "filename": file.filename}

