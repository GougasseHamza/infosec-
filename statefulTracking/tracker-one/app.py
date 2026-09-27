from flask import Flask, request, make_response, render_template, redirect
from datetime import datetime
import secrets
from urllib.parse import quote

app = Flask(__name__)
visits = []


@app.route("/track")
def track():
    tracker_id = request.cookies.get("tracker_id")
    new_id = tracker_id is None
    if new_id:
        tracker_id = "A-" + secrets.token_hex(4)

    publisher = request.args.get("publisher", "unknown")
    page = request.args.get("page", "unknown")
    visits.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "tracker_id": tracker_id,
        "publisher": publisher,
        "page": page,
        "cookie_header": request.headers.get("Cookie", "(none)")
    })

    print("TRACKER ONE:", visits[-1])
    response = make_response(render_template("tracker.html", tracker_id=tracker_id,
                                             publisher=publisher, page=page, new_id=new_id))
    if new_id:
        response.set_cookie("tracker_id", tracker_id, max_age=30 * 24 * 60 * 60,
                            samesite="None", secure=True, httponly=True)
    return response


@app.route("/profile")
def profile():
    return render_template("profile.html", visits=visits)


@app.route("/sync-now")
def sync_now():
    tracker_id = request.cookies.get("tracker_id", "missing")
    return redirect("http://tracker-two.localhost:9200/sync?a_id=" + quote(tracker_id))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)
