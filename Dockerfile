FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONPATH=/app/src

COPY pyproject.toml .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -e .

COPY src/app/backend /app/src/app/backend

EXPOSE 8001

CMD ["uvicorn", "app.backend.main:app", "--host", "0.0.0.0", "--port", "8001"]