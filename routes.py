from flask import render_template
from . import app
from .character import random_character, random_character_name, random_character_gender
from .character import random_character_home, random_character_age, random_character_link
from .character import random_character_paragraph
import requests

# Default route
@app.route('/')
def index():
    return render_template('index.html', data=random_character_paragraph())

@app.route('/generator',methods = ['POST',"GET"])
def generator():
    print("in generator")
    return render_template('generator.html', data1=random_character_link(), data2=random_character_paragraph())

@app.route('/information', methods = ['POST','GET'])
def information():
    print("in information")
    return render_template('information.html')
