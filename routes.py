from flask import render_template
from . import app
from .character import random_character, random_character_name, random_character_gender
from .character import random_character_home, random_character_age, random_character_link, character_hobbies_old
from .character import random_character_paragraph, character_bio, customization_info

# Default route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generator',methods = ['POST',"GET"])
def generator():
    print("in generator")
    character = random_character_paragraph()
    return render_template('generator.html', data1=character[1], data2=character[0],
                           data3=character[2], data4=character[3], data5=character[4],
                           data6=character[5], data7=character[6],data8=character[7])

@app.route('/information', methods = ['POST','GET'])
def information():
    print("in information")
    return render_template('information.html')

@app.route('/customization', methods = ['POST','GET'])
def customization():
    print("in customization")
    return render_template('customization.html')

@app.route('/custom_process_test', methods=["POST","GET"])
def custom_process_test():
    custom_info = customization_info()
    name = 0
    country = 0
    age = 0
    gender = 0
    if custom_info != "Invalid Field":
        name = custom_info[0]
        country = custom_info[1]
        age = custom_info[2]
        gender = custom_info[3]
    return render_template('customization.html', name = name, country = country, age = age, gender = gender)

