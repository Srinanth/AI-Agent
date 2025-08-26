from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use your n8n production webhook URL here
N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/upload"

@app.post("/api/upload")
async def upload_assignment(
    file: UploadFile,
    assignment_type: str = Form(...),
    user_email: str = Form(...)
):
    try:
        # We don't parse the file here. We send it directly.
        files = {'file': (file.filename, file.file, file.content_type)}
        data = {
            'assignmentType': assignment_type,
            'userEmail': user_email
        }
        
        async with httpx.AsyncClient() as client:
            # Send as multipart/form-data
            response = await client.post(
                N8N_WEBHOOK_URL,
                files=files,
                data=data,
                timeout=60.0  # Increased timeout for file uploads
            )
        
        response.raise_for_status() # Raises an exception for 4xx/5xx responses
            
        return {"status": "success", "message": "Assignment submitted for processing"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))