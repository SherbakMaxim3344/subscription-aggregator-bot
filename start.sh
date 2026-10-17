#!/bin/bash
set -e
cd "$(dirname "$0")"

docker compose up -d --wait

cleanup() {
    docker compose down
}
trap cleanup EXIT INT TERM

venv/bin/python -m alembic upgrade head
venv/bin/python -m src.bot.run
