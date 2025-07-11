from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from utils.generator import generate_qr
from utils.scanner import scan_qr_from_url, scan_qr_from_base64, scan_qr_from_file
import io
import base64

app = FastAPI(title="QR Pulse API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# =========================
# QR GENERATION ENDPOINTS
# =========================

@app.post("/generate/image")
async def generate_qr_image(data: str = Form(...)):
    img = generate_qr(data)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")

@app.post("/generate/base64")
async def generate_qr_base64(data: str = Form(...)):
    img = generate_qr(data)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    b64_data = base64.b64encode(buffer.getvalue()).decode()
    return {"image_base64": f"data:image/png;base64,{b64_data}"}

# =========================
# QR SCANNER ENDPOINTS
# =========================

@app.post("/scan/url")
async def scan_from_url(image_url: str = Form(...)):
    result = scan_qr_from_url(image_url)
    return {"data": result} if result else {"error": "QR Code not found."}

@app.post("/scan/base64")
async def scan_from_base64(image_base64: str = Form(...)):
    result = scan_qr_from_base64(image_base64)
    return {"data": result} if result else {"error": "QR Code not found."}

@app.post("/scan/file")
async def scan_from_file(file: UploadFile = File(...)):
    file_bytes = await file.read()
    result = scan_qr_from_file(file_bytes)
    return {"data": result} if result else {"error": "QR Code not found."}
