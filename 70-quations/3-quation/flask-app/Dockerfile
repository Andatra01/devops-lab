FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install python3 && apt-get install python3-pip
RUN pip install -r /app/requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "/app/app.py"]