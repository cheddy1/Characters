from flask import render_template
from . import app
from .character import random_character
# Default route
@app.route('/')
def index():
    random_character()
    return render_template('index.html')