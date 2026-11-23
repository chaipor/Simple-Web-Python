# syntax=docker/dockerfile:1
FROM python:3.12-slim

WORKDIR /app

COPY server.py ./
COPY public ./public

ENV HOST=0.0.0.0
ENV PORT=8000
ENV MESSAGE="เว็บเริ่มทำงานแล้ว"
EXPOSE 8000

CMD ["python", "server.py"]
