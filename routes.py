from flask import render_template
from . import app
from .character import random_character, random_character_name, random_character_gender
from .character import random_character_home, random_character_age
from .character import random_character_paragraph


# Default route
@app.route('/')
def index():
    random_character_name()
    random_character_gender()
    random_character_home()
    random_character_age()
    random_character_paragraph()
    return render_template('index.html')
