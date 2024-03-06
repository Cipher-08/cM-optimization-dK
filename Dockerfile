FROM python:3.11.4-slim-bullseye AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

FROM python:3.11.4-slim-bullseye

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]
