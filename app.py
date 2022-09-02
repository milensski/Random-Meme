import json

import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AaH1hIqIjkCk7fkBVAlmOwgVg4TGaNp7'


@app.route('/', methods=['GET', 'POST'])
def index():


    url = "https://meme-api.herokuapp.com/gimme/1"
    result = json.loads(requests.get(url).text)
    img_url = result['memes'][0]['preview'][2]

    if request.method == "POST":
        return redirect('/')


    return render_template('base.html', img_url=img_url)



if __name__ == "__main__":
    app.run(debug=True)