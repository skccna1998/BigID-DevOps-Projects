from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return jsonify({"ip": ip})

@app.route('/health')
def health():
    return "OK", 200

@app.route('/ready')
def ready():
    return "READY", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)