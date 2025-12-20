# ---- Base Node ----
FROM python:3.11-slim AS base

WORKDIR /elherafeen-api
COPY requirements.txt .

FROM base AS dependencies
RUN pip install --no-cache-dir -r requirements.txt

FROM dependencies AS main
COPY . .
