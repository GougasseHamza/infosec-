from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", page="travel-home")


@app.route("/morocco")
def morocco():
    return render_template("index.html", page="morocco-guide")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002, debug=True)
