# ✅ ใช้ Node 20 บน Alpine (เบาและเร็ว)
FROM node:20-alpine

# ตั้ง working directory
WORKDIR /app

# คัดลอก package.json / lockfile ก่อนเพื่อลด layer rebuild
COPY package*.json ./

# ติดตั้ง dependencies
RUN npm install

# ✅ คัดลอกไฟล์ .env เข้าไปใน image
# (ถ้ามี .env แล้ว — Vite จะ bake ตัวแปร VITE_* ตอน build)
COPY .env .env

# คัดลอก source code ทั้งหมด
COPY . .

# build โปรเจกต์
RUN npm run build