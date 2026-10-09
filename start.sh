#!/bin/bash
docker compose up -d --build

cleanup() {
    docker compose down
}
trap cleanup EXIT INT TERM

python -m src.bot.run
