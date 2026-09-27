from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", page="technology-home")


@app.route("/ai")
def ai_article():
    return render_template("index.html", page="ai-article")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8011, debug=True)
