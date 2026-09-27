from flask import Flask, render_template, request, make_response
import secrets

app = Flask(__name__)


@app.route("/")
def home():
    aid = request.cookies.get("aid")
    is_new = aid is None

    if is_new:
        aid = secrets.token_hex(8)

    response = make_response(render_template("index.html", aid=aid, is_new=is_new))
    response.headers["X-Lab-Message"] = "Hello from the Flask server"

    mode = request.args.get("mode", "session")

    if is_new:
        if mode == "persistent":
            response.set_cookie("aid", aid, max_age=30 * 24 * 60 * 60)
        elif mode == "secure":
            response.set_cookie("aid", aid, secure=True)
        elif mode == "httponly":
            response.set_cookie("aid", aid, httponly=True)
        elif mode == "strict":
            response.set_cookie("aid", aid, samesite="Strict")
        else:
            response.set_cookie("aid", aid)

    print("\n--- HTTP REQUEST HEADERS ---")
    print(request.headers)
    print("--- HTTP RESPONSE HEADERS ---")
    print(response.headers)
    print("aid =", aid, "new browser =", is_new, "mode =", mode)
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
