import requests
from fastapi import FastAPI
app = FastAPI()
N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/upload"

# Example text file content
file_content = "This is a test assignment content."

payload = {
    "file_name": "test.txt",
    "file_content": file_content,
    "assignment_type": "math"
}

response = requests.post(N8N_WEBHOOK_URL, json=payload)

print("Status code:", response.status_code)
print("Response:", response.text)
