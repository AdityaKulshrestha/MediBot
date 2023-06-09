from flask import Flask, render_template
from flask import request
from utils import response_from_gpt
import os

app = Flask(__name__)
app.static_folder = 'static'


def declare_env(key):
    os.environ['OPENAI_API_KEY'] = key


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/chat")
def about():
    return "Ask your questions"


@app.route("/get")
def get_bot_response():
    if request.args.get('api_key'):
        apikey = request.args.get('api_key')
        print(apikey)
        try:
            declare_env(apikey)
        except:
            return "Enter a valid api key first"
    userText = request.args.get('msg')
    return response_from_gpt(userText)


if __name__ == "__main__":
    app.run(debug=True)
