# DooKluay 🍌

โปรเจ็คตรวจโรคใบกล้วยจากภาพถ่ายด้วย Machine Learning / Deep Learning  
อัปโหลดภาพ → ระบบทำนายโรคและให้คำแนะนำเบื้องต้น

---

## Features
- ตรวจโรคใบกล้วยจากภาพ
- API + เว็บอินเตอร์เฟซ
- รองรับ Docker

---

## Project Structure
```
DooKluay/
├── banana_api/      # API
├── DooKluayWeb/     # Configuration
├── docker-compose.dev.yml
├── requirements.txt
└── manage.py
```

## Installation
```bash
git clone https://github.com/Tannsxerd/DooKluay.git
cd DooKluay
cp .env.example .env # Edit .env and update configuration values
docker compose -f docker-compose.dev.yml up --build
```

---

## Tech Stack
- Backend: Python (Django)
- Model: TensorFlow 
- Deploy: Docker

---

## Development Notes

Whenever `requirements.txt` is modified (e.g. new dependencies added),
you need to rebuild and restart the containers to apply the changes:

```bash
# 1) Rebuild the image after updating requirements
docker compose -f docker-compose.dev.yml build

# 2) Restart containers in background
docker compose -f docker-compose.dev.yml up -d
```

---

## Running Tests

To run the unit tests inside the backend container:

```bash
docker compose -f docker-compose.dev.yml exec backend \
  python manage.py test banana_api -v 2
```
