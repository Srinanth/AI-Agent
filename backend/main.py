from fastapi import FastAPI, UploadFile, Form, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from weasyprint import HTML
from starlette.responses import JSONResponse
import base64
import httpx
import json
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
@app.post("/api/upload")
async def upload_assignment(
    file: UploadFile,
    user_email: str = Form(...)
):
    try:
        files = {'file': (file.filename, file.file, file.content_type)}
        data = {
            'userEmail': user_email
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                N8N_WEBHOOK_URL,
                files=files,
                data=data,
                timeout=60.0
            )

        response.raise_for_status()
        return {"status": "success", "message": "Assignment submitted for processing"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
