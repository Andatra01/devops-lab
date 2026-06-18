from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Hello from Docker!",
        "hostname": socket.gethostname(),
        "version": os.environ.get("APP_VERSION", "1.0"),
        "port": os.environ.get("APP_PORT", "8000")
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get("APP_PORT", 8000))
    app.run(host='0.0.0.0', port=port)
