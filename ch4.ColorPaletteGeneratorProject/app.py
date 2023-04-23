import openai
from dotenv import dotenv_values

from flask import Flask, render_template, request

config = dotenv_values("../../../.env")
openai.api_key = config["openai"]

app = Flask(__name__,
    template_folder="templates"
)

@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    # OpneAi Completion Call

    # Return List of Color
    return "pong!"

@app.route("/")
def index():
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt="Give me a funny word: "
    )
    print('ai test: ', res["choices"][0]["text"])
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
