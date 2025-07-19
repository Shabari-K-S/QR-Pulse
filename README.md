# ⚡ QR Pulse - Fast, Flexible QR Code API

[![FastAPI](https://img.shields.io/badge/Built%20with-FastAPI-009688?style=for-the-badge\&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge\&logo=python)](https://www.python.org/)

QR Pulse is a simple yet powerful QR Code Generator and Scanner API built with FastAPI. Effortlessly generate QR codes from text or URLs in PNG and Base64 formats, or decode QR codes from image URLs, base64 strings, or uploaded files.

> 🚀 Perfect for digital menus, payment systems, business cards, ticketing, contactless login, and more!

---

## ✨ Features

* 🔒 Generate high-quality QR codes from any string
* 🖼️ Output as PNG image or Base64 string
* 📷 Decode QR codes from:

  * Public **Image URLs**
  * **Base64**-encoded images
  * Uploaded **image files**
* ⚡ Built with FastAPI — blazing fast performance and async support
* 🌐 Full CORS support for easy web integration

---

## 📦 Installation

```bash
git clone https://github.com/Shabari-K-S/QR-Pulse.git
cd QR-Pulse
pip install -r requirements.txt
```

---

## 🚀 Running the Server

```bash
uvicorn main:app --reload
```

Visit the interactive API docs at:

* **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📡 API Endpoints

### ➕ Generate QR

| Endpoint           | Method | Description                         |
| ------------------ | ------ | ----------------------------------- |
| `/generate/image`  | POST   | Generate a PNG QR code from text    |
| `/generate/base64` | POST   | Generate a Base64 QR code from text |

**Request Body:**

```json
{
  "data": "https://example.com"
}
```

---

### 🔍 Scan QR

| Endpoint       | Method | Description                     |
| -------------- | ------ | ------------------------------- |
| `/scan/url`    | POST   | Scan QR code from image URL     |
| `/scan/base64` | POST   | Scan QR code from Base64 image  |
| `/scan/file`   | POST   | Scan QR code from uploaded file |

**/scan/url Example:**

```json
{
  "image_url": "https://example.com/qrcode.png"
}
```

---

## 📂 Project Structure

```
QR-Pulse/
├── main.py               # FastAPI app entrypoint
├── utils/
│   ├── generator.py      # QR generation logic
│   └── scanner.py        # QR scanning logic
├── requirements.txt
└── README.md
```

---

## 🛡️ Error Handling

All endpoints include built-in error handling for:

* Invalid image formats
* Missing/undetectable QR codes
* Malformed Base64 strings or URLs
* File upload errors

---

## 💡 Author

Made with ❤️ by [Shabari K S](https://github.com/Shabari-K-S)
