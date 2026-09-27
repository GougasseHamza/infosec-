from flask import Flask, request, make_response
import secrets

app = Flask(__name__)
sync_table = []


@app.route("/sync")
def sync():
    b_id = request.cookies.get("tracker_two_id")
    if b_id is None:
        b_id = "B-" + secrets.token_hex(4)

    a_id = request.args.get("a_id", "missing")
    sync_table.append((a_id, b_id))
    print("COOKIE SYNC: tracker-one", a_id, "= tracker-two", b_id)

    response = make_response("Synced: %s belongs to the same browser as %s" % (a_id, b_id))
    response.set_cookie("tracker_two_id", b_id, max_age=30 * 24 * 60 * 60,
                        samesite="None", secure=True, httponly=True)
    return response


@app.route("/profile")
def profile():
    result = "<h1>Cookie sync pairs</h1>"
    for pair in sync_table:
        result += "<p>%s = %s</p>" % pair
    return result


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9200, debug=True)
