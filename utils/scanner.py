from PIL import Image
from pyzbar.pyzbar import decode
import requests
import base64
import io

def _decode_qr(image):
    decoded = decode(image)
    return decoded[0].data.decode() if decoded else None

def scan_qr_from_url(url: str):
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    return _decode_qr(image)

def scan_qr_from_base64(b64_image: str):
    header, encoded = b64_image.split(",", 1)
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    return _decode_qr(image)

def scan_qr_from_file(file_bytes: bytes):
    image = Image.open(io.BytesIO(file_bytes))
    return _decode_qr(image)
