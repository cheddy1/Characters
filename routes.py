from flask import render_template
from . import app
from .character import random_character_paragraph, customization_info, random_song
from .tests import test1, test2, test3, test4, test5


# Default route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generator',methods = ['POST',"GET"])
def generator():
    character = random_character_paragraph()
    return render_template('generator.html', data1=character[1], data2=character[0],
                           data3=character[2], data4=character[3], data5=character[4],
                           data6=character[5], data7=character[6], data8=character[7], song=character[8])


@app.route('/information', methods = ['POST','GET'])
def information():
    return render_template('information.html')


@app.route('/customization', methods = ['POST','GET'])
def customization():
    return render_template('customization.html')

@app.route('/test', methods = ['POST','GET'])
def test():
    return render_template('test.html', test1=test1(), test2=test2(), test3=test3(), test4=test4(), test5=test5())

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
    return render_template('customization.html', name=name, country=country, age=age, gender=gender)

