from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        message = generate_prompt(prompt)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=message, # type: ignore
            temperature=1)
        
        return redirect(url_for("index", result=completion.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)

@app.route("/version", methods=["GET"])
def version():
    app = "0.1.0"
    http = request.environ.get('SERVER_PROTOCOL')
    return render_template("version.html", version=app, http=http)

def generate_prompt(prompt: str): 
    return [{"role": "user", "content": "Translate the following using only hiragana / katakana:{}".format(prompt.capitalize())}] 
