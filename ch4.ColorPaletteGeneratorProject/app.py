from flask import Flask, render_template, request

app = Flask(__name__,
    template_folder="templates"
)

@app.route("/ping")
def ping():
    return "pong!"

@app.route("/")
def index():
    return "Hello There from flask!"

if __name__ == "__main__":
    app.run(debug=True)
