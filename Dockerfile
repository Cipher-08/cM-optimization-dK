FROM python:3.11.4-slim-bullseye
WORKDIR /app
COPY requirements.txt .

RUN apt-get update && apt-get install -y gcc

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask","run"]