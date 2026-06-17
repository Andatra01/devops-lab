from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database='appdb',
        user='appuser',
        password=os.environ.get('DB_PASSWORD', '')
    )
    cur = conn.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    cur.close()
    conn.close()
    return f'Hello from app! DB version: {ver[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
