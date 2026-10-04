from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.before_request
def log_request():
    if request.path == "/":
        print("\n========== NEW VISIT ==========", flush=True)
        print("IP address:", request.remote_addr, flush=True)
        print("HTTP method:", request.method, flush=True)
        for name in ("User-Agent", "Accept-Language", "Accept", "Accept-Encoding", "Referer", "Sec-Fetch-Site", "Sec-Fetch-Mode", "Sec-Fetch-Dest", "Sec-Fetch-User", "Upgrade-Insecure-Requests", "Cookie"):
            print(f"{name}:", request.headers.get(name, "Not sent"), flush=True)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/typing")
def typing_page():
    return render_template("typing.html")

@app.post("/collect")
def collect():
    data = request.get_json(silent=True) or {}
    print("\n========== POST /collect ==========", flush=True)
    print(data, flush=True)
    print("===================================", flush=True)
    return jsonify(received=data, status="Received by Flask"), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
