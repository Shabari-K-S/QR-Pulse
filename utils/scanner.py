from PIL import Image, UnidentifiedImageError
from pyzbar.pyzbar import decode
import requests
import base64
import io

def _decode_qr(image):
    decoded = decode(image)
    return decoded[0].data.decode() if decoded else None

def scan_qr_from_url(url: str):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        if 'image' not in response.headers.get("Content-Type", ""):
            print("Invalid content type:", response.headers.get("Content-Type"))
            return None

        image = Image.open(io.BytesIO(response.content))
        return _decode_qr(image)

    except (requests.RequestException, UnidentifiedImageError, IOError) as e:
        print(f"Error in scan_qr_from_url: {e}")
        return None

def scan_qr_from_base64(b64_image: str):
    try:
        header, encoded = b64_image.split(",", 1)
        decoded = base64.b64decode(encoded)
        image = Image.open(io.BytesIO(decoded))
        return _decode_qr(image)

    except (ValueError, UnidentifiedImageError, IOError, base64.binascii.Error) as e:
        print(f"Error in scan_qr_from_base64: {e}")
        return None

def scan_qr_from_file(file_bytes: bytes):
    try:
        image = Image.open(io.BytesIO(file_bytes))
        return _decode_qr(image)

    except (UnidentifiedImageError, IOError) as e:
        print(f"Error in scan_qr_from_file: {e}")
        return None
