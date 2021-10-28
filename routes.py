from flask import render_template
from . import app
from .character import random_character, random_character_name, random_character_gender
from .character import random_character_home, random_character_age


# Default route
@app.route('/')
def index():
    random_character()
    random_character_name()
    random_character_gender()
    random_character_home()
    random_character_age()
    return render_template('index.html')
