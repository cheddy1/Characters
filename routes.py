from flask import render_template
from . import app
from .character import random_character, random_character_name, random_character_gender
from .character import random_character_home, random_character_age, random_character_link
from .character import random_character_paragraph, character_bio
import requests

# Default route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generator',methods = ['POST',"GET"])
def generator():
    print("in generator")
    character = random_character_paragraph()
    return render_template('generator.html', data1=character[1], data2=character[0], data3=character[2], data4=character[3], data5=character[4], data6=character[5])

@app.route('/information', methods = ['POST','GET'])
def information():
    print("in information")
    return render_template('information.html')
