
FROM python:3.10-slim

# Instala o FFmpeg e o servidor de teste
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app
COPY . /app

# Inicia um servidor web simples na porta 10000 e roda o script da live
CMD python3 -m http.server 10000 & python3 main.py
