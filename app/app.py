from flask import Flask, render_template
from quotes import quote_list
import random

app = Flask(__name__)


@app.route("/")
def show_quote():
    quote = random.choice(quote_list)

    return render_template("index.html", quote=quote)
