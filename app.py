import os
import json

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":

        #Create our model 
        data = request.form["data"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(data),
            temperature=0,
        )
        #print(data)
        return redirect(url_for("index", result=response.choices[0].text))
   
    #Get result     
    result = request.args.get("result")
    if result is not None:
        print(result)

     #This line renders an HTML template named "index.html" and passes the value of result as a variable to the template. 
    return render_template("index.html", result=result)

def generate_prompt(data):
  return f"""Identify the following items from the prompt text: 
- Customer expressing anger? (true or false)
- Sentiment (negative or positive).

Format your response as an object with \
"Sentiment" and "Anger" as the keys.
If the information isn't present, use "unknown" \
as the value.
Format the Anger value as a boolean.

Result:""".format(data)
