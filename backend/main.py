from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import json

from backend.video_engine import generate_video

app = FastAPI()

with open("backend/config.json") as f:
    users = json.load(f)["users"]

@app.post("/login")
async def login(req: Request):

    data = await req.json()

    for user in users:
        if user["username"] == data["username"] and user["password"] == data["password"]:
            return {"status":"ok"}

    return {"status":"error"}

@app.post("/generate")
async def generate(req: Request):

    data = await req.json()

    video_path = generate_video(
        data["script"],
        data["prompts"],
        data["speed"]
    )

    return {"video": video_path}

@app.get("/download")
def download():

    return FileResponse("output.mp4")
