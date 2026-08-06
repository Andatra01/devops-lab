FROM python:3.11-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -m appuser
COPY --chown=appuser:appuser . .
USER appuser


EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
	CMD curl -f http://localhost:5000/health || exit 1
CMD ["python3", "app.py"]
