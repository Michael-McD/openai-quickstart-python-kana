import os

from openai import OpenAI
from flask import Flask, redirect, render_template, request, url_for, json

app = Flask(__name__)
client = OpenAI()

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        message = generate_prompt(prompt)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=message)
        
        return redirect(url_for("index", result=completion.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = '0'
    response.headers["Pragma"] = "no-cache"
    return response

# completion = await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

def generate_prompt(prompt):
    return [{"role": "user", "content": "Translate the following using only hiragana / katakana:{}".format(prompt.capitalize())}]