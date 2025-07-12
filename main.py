from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

# ========== Pydantic Models ==========
class QRData(BaseModel):
    data: str

class ImageURL(BaseModel):
    image_url: str

class Base64Image(BaseModel):
    image_base64: str

# ========== QR Generator ==========
@app.post("/generate/image")
async def generate_qr_image(body: QRData):
    try:
        img = generate_qr(body.data)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to generate QR code image. {str(e)}"})

@app.post("/generate/base64")
async def generate_qr_base64(body: QRData):
    try:
        img = generate_qr(body.data)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        b64_data = base64.b64encode(buffer.getvalue()).decode()
        return {"image_base64": f"data:image/png;base64,{b64_data}"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to generate QR code as base64. {str(e)}"})

# ========== QR Scanner ==========
@app.post("/scan/url")
async def scan_from_url(body: ImageURL):
    try:
        result = scan_qr_from_url(body.image_url)
        return {"data": result} if result else JSONResponse(status_code=400, content={"error": "QR Code not found or image URL invalid."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to scan QR code from URL. {str(e)}"})

@app.post("/scan/base64")
async def scan_from_base64(body: Base64Image):
    try:
        result = scan_qr_from_base64(body.image_base64)
        return {"data": result} if result else JSONResponse(status_code=400, content={"error": "QR Code not found or invalid base64 image."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to scan QR code from base64. {str(e)}"})

@app.post("/scan/file")
async def scan_from_file(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        result = scan_qr_from_file(file_bytes)
        return {"data": result} if result else JSONResponse(status_code=400, content={"error": "QR Code not found in uploaded file."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to scan QR code from file. {str(e)}"})

@app.get("/ping")
async def ping():
    return {"message": "pong"}
