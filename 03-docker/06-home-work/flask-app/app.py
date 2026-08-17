import os
print(f"Подключаюсь к Redis по адресу: {os.environ.get('REDIS_HOST')}")
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'OK from Flask'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
