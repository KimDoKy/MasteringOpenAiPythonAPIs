import openai
import json
from dotenv import dotenv_values

from flask import Flask, render_template, request

config = dotenv_values("../../../.env")
openai.api_key = config["openai"]

app = Flask(__name__,
    template_folder="templates"
)

def get_colors(msg):
    prompt = f"""
    You are a color palette generating assistant that responds to text prompts for color palette
    Your should generate color palettes that fit the theme, mood, or instructions in the prompt.
    The palettes should be between 2 and 8 colors.

    Q: Convert the following verbal description or a color palette into a list of colors: The Mediterranean Sea
    A: ['#96b9ad', '#38465e', '#ebf2fa', '#fbd2ae', '#642029', '#ece8d2', '#4c4a4e']

    Q: Convert the following verbal description or a color palette into a list of colors: sage, nature, earth
    A: ['#767562','#98FF98','#7F4B4B','#F4FFA8','#BEACAE','#ADF9DE",'#FFDEAF']

    Desired Format: a JSON array of hexadecimal color codes

    Q: Convert the following verbal description or a color palette into a list of colors: {msg}
    A: 
    """

    res = openai.Completion.create(
        prompt=prompt,
        model="text-davinci-003",
        max_tokens=100,
    )
    colors = json.loads(res["choices"][0]["text"].strip())
    return colors

@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    app.logger.info(colors)
    return {"colors": colors}

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
