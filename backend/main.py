from fastapi import FastAPI,Request
from fastapi.responses import FileResponse

from backend.video_engine import generate_video
from backend.auth import check_login

app=FastAPI()

@app.post("/login")
async def login(req:Request):

    data=await req.json()

    if check_login(data["username"],data["password"]):
        return {"status":"ok"}

    return {"status":"error"}

@app.post("/generate")
async def generate(req:Request):

    data=await req.json()

    video=generate_video(
        data["script"],
        data["prompts"],
        data["speed"]
    )

    return {"video":video}

@app.get("/download")
def download():

    return FileResponse("output.mp4")
