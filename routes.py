from flask import render_template
from . import app
from .character import random_character_paragraph, customization_info
from .tests import test1, test2, test3, test4, test5,check_string_in_file,age_check

# Date: 11/18/21
# Authors: EECS 448 Group 15
# Description: All of the routes of the web application


# Default route
@app.route('/')
def index():
    return render_template('index.html')


# Random Character Generation Route
@app.route('/generator', methods=['POST', "GET"])
def generator():
    character = random_character_paragraph()
    return render_template('generator.html', data1=character[1], data2=character[0],
                           data3=character[2], data4=character[3], data5=character[4],
                           data6=character[5], data7=character[6], data8=character[7], song=character[8])


# Information Page Route
@app.route('/information', methods=['POST', "GET"])
def information():
    return render_template('information.html')


# Customization Page Route
@app.route('/customization', methods=['POST', "GET"])
def customization():
    return render_template('customization.html')


# Test page Route
@app.route('/test', methods=['POST', "GET"])
def test():
    character = random_character_paragraph()
    testone = test1(character)
    print(testone)
    testtwo = test2(character)
    print(testtwo)
    testthree = test3(character)
    print(testthree)
    testfour = test4(character)
    print(testfour)
    testfive = test5(character)
    print(testfive)

    return render_template('test.html', test1=testone, test2=testtwo, test3=testthree, test4=testfour, test5=testfive)


# Post user input Customization page route
# (goes to this route after entering custom user information, before character generation)
@app.route('/custom_process_test', methods=['POST', "GET"])
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
