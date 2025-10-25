#!/usr/bin/env bash
set -e

# รอ DB ถ้าจำเป็น (ถ้ามี wait-for ก็ใช้ที่นี่)
# ./wait-for db:5432 -- echo "DB ready"

# migrate และรวบรวม static
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# (ทางเลือก) สร้าง superuser อัตโนมัติ ถ้า export ตัวแปรไว้
if [[ -n "$DJANGO_SUPERUSER_USERNAME" && -n "$DJANGO_SUPERUSER_EMAIL" && -n "$DJANGO_SUPERUSER_PASSWORD" ]]; then
  python manage.py createsuperuser --noinput || true
fi

# รัน gunicorn
exec gunicorn DooKluayWeb.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 4 \
  --timeout 120
