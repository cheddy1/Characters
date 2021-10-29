from flask import render_template
from . import app
from .character import random_character, random_character_name, random_character_gender
from .character import random_character_home, random_character_age
from .character import random_character_paragraph
import requests

# Default route
@app.route('/')
def index():
    random_character_name()
    random_character_gender()
    random_character_home()
    random_character_age()
    random_character_paragraph()
    return render_template('index.html')

@app.route('/generator',methods = ['POST',"GET"])
def generator():
    print("in generator")
    return render_template('generator.html')

@app.route('/information', methods = ['POST','GET'])
def information():
    print("in information")
    return render_template('information.html')
