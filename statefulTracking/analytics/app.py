from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
events = []


@app.route("/collect")
def collect():
    event = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "analytics_id": request.args.get("aid", "missing"),
        "publisher": request.args.get("publisher", "unknown"),
        "page": request.args.get("page", "unknown"),
        "cookie_header": request.headers.get("Cookie", "(none)"),
        "referer": request.headers.get("Referer", "(none)")
    }
    events.append(event)
    print("ANALYTICS EVENT:", event)
    return "", 204


@app.route("/profile")
def profile():
    return render_template("profile.html", events=events)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9100, debug=True)
