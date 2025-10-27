# This is an academic project for the Master's program at TUS Midlands.
# Academic Project - TUS Midlands 2025
# Student: Weverton de Souza Castanho

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py /app

EXPOSE 8000

CMD ["python", "server.py"]
