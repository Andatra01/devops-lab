FROM python:3.11-slim
WORKDIR /app
RUN pip install --upgrade pip
COPY app.py .
ENV PORT=8000
EXPOSE 8000
RUN echo "Building image..."
CMD ["python3", "app.py"]
