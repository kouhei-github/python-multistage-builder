# syntax=docker/dockerfile:1.3-labs

FROM python:3.11-slim AS prebuild

ENV TZ=Asia/Tokyo
ENV LANG=en_US.UTF-8

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN adduser --disabled-password -gecos "" --home /home/app app

USER app
WORKDIR /home/app

COPY --chown=app ./python/requirements.txt .

RUN <<EOF
PATH="${PATH}:/home/app/.local/bin"
pip install --no-cache-dir --user --upgrade pip
pip install --no-cache-dir --user pipenv==2023.8.25
pipenv install -r ./requirements.txt
python -m pipenv requirements > requirements.txt
EOF

FROM python:3.11-slim AS build

ENV TZ=Asia/Tokyo
ENV LANG=en_US.UTF-8

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN <<EOF
apt-get update --yes
apt-get upgrade --yes
apt-get install --yes build-essential default-libmysqlclient-dev
adduser --disabled-password -gecos "" --home /home/app app
EOF

USER app
WORKDIR /home/app

COPY --from=prebuild --chown=app /home/app/requirements.txt .

RUN <<EOF
PATH="${PATH}:/home/app/.local/bin"
pip install --no-cache-dir --user --upgrade pip
pip install --no-cache-dir --user --requirement requirements.txt
pip install --no-cache-dir --user pipenv==2023.8.25
EOF

FROM python:3.11-slim AS main

ENV TZ=Asia/Tokyo
ENV LANG=en_US.UTF-8

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN <<EOF
apt-get update --yes
apt-get upgrade --yes
apt-get install --yes default-libmysqlclient-dev
apt-get clean
rm -rf /var/lib/apt/lists/*
adduser --uid 5678 --disabled-password -gecos "" --home /home/app app
EOF

USER app
WORKDIR /home/app

COPY --from=prebuild --chown=app /home/app/Pipfile .
COPY --from=prebuild --chown=app /home/app/Pipfile.lock .
COPY --from=build --chown=app /home/app/.local /home/app/.local
COPY --chown=app ./python/bin ./bin
COPY --chown=app ./python/src ./src

RUN chmod u+x ./bin/start.sh

#CMD [ "bin/start.sh" ]
