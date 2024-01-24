FROM python:3.11
WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --upgrade pip &&  pip3 install -r requirements.txt --no-cache-dir

COPY . .