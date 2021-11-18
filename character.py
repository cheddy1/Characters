import requests
from flask import request
import random
import re

# Date: 11/18/21
# Authors: EECS 448 Group 15
# Description: Functions to retrieve and evaluate random character information

# Define API keys and constants
UI_API_1 = '241E1EB8-FFA54369-A0851285-2C688163'
UI_API_2 = 'A3D1D37D-506D4D4B-B1C36F96-5FF139DB'
access_token = "?access_token=CWBwf6Bb0yL5QeJcefGLk9F2JLjnDt91Q9QNBHNC-gcKsW0kibHga6BuPz2No7wV"
API_Song = "https://api.genius.com/songs/"


# @post Uses randomuser api to get a random user
def random_character():
    return requests.get("https://randomuser.me/api/").json().get('results')[0]


# @param uses global variables: access_token, API_Song
# @post Generates a random song using the genius.com api
def random_song():
    song_id = str(random.randint(1, 2500000))
    res = requests.get(API_Song + song_id + access_token)
    if res.status_code != 200:
        while res.status_code != 200:
            song_id = str(random.randint(1, 2500000))
            res = requests.get(API_Song + song_id + access_token)
    song = res.json()['response']['song']
    return song['title'] + ' by ' + song['primary_artist']['name']


# @param age is the characters age
# @param gender is the characters gender
# @param key is the APIkey needed to use the API
# @post generates a random picture based on age and gender
def character_picture(age, gender, key):
    uiface = requests.get('https://uifaces.co/api', headers={
        'X-API-KEY': key,
        'Accept': 'application/json',
        'Cache-Control': 'no-cache'}, params={
        'limit': 1,
        'gender[]': gender,
        'from_age': age-10,
        'to_age': age+10
        }
    )
    return uiface.json()


# @post reads from a txt file of hobbies and returns 3 random ones
def character_hobbies_young():
    hobbies = open('static/hobbies.txt').read().splitlines()
    hobby1 = random.choice(hobbies)
    hobby2 = random.choice(hobbies)
    hobby3 = random.choice(hobbies)
    if hobby2 != hobby1 and hobby2 != hobby3 and hobby1 != hobby3:  # if hobbies are different
        hobbylistyoung = [hobby1, hobby2, hobby3]  # return array of 3 hobbies
        return hobbylistyoung
    else:
        return character_hobbies_young()


# @post reads from a txt file of hobbies for older people and returns 3 random ones
def character_hobbies_old():
    hobbiesold = open('static/hobbiesold.txt').read().splitlines()
    hobby1 = random.choice(hobbiesold)
    hobby2 = random.choice(hobbiesold)
    hobby3 = random.choice(hobbiesold)
    if hobby2 != hobby1 and hobby2 != hobby3 and hobby1 != hobby3:
        hobbylist = [hobby1, hobby2, hobby3]
        return hobbylist
    else:
        return character_hobbies_old()


# @post returns a random poem from the bean poems API
def character_poem():
    fav_poem = requests.get('https://www.beanpoems.com/api/poems/random').json().get('body')
    return fav_poem


# @param one sentence to start the deepai text generator
# @post returns ai generated text based on the characters name age and gender
def character_bio(text):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': text,
        },
        headers={'api-key': '9d321645-60cb-4d93-8e08-3583dd1c4ec9'}
    )
    return ' '.join(re.split(r'(?<=[.:;])\s', r.json()['output'])[:4])


# @param a character retrieved from random_character() using the randomuser API
# @post return a random character name
def random_character_name(character):
    first = character.get('name').get('first')
    last = character.get('name').get('last')
    return first + ' ' + last


# @param a character retrieved from random_character() using the randomuser API
# @post return a random character gender
def random_character_gender(character):
    gender = character.get('gender')
    return gender


# @param a character retrieved from random_character() using the randomuser API
# @post return a random character country of origin
def random_character_home(character):
    home = character.get('location').get('country')
    return home


# @param a character retrieved from random_character() using the randomuser API
# @post return a random character age
def random_character_age(character):
    age = character.get('dob').get('age')
    return age


# @param a character retrieved from random_character() using the randomuser API
# @post return a random character picture
def random_character_picture(character):
    picture = character[0]['photo']
    return picture


# @pre a form using the POST method collects user input in customization.html
# @post returns user provided name, country, age, and/or gender if input is valid
def customization_info():
    if request.method == "POST":
        output = request.form.to_dict()
        name = output["name"]
        country = output["CountryOfOrigin"]
        age = output["age"]
        gender = output["gender"]
        if gender != "Male" and gender != "male" and gender != "Female" and gender != "female" and gender != "":
            return "Invalid Field"

        if age != "":
            if all(x.isdigit() or x == " " for x in age):
                if int(age) > 120 or int(age) < 18:
                    return "Invalid Field"
            else:
                return "Invalid Field"

        if country != "":
            if not all(x.isalpha() or x == " " for x in country):
                return "Invalid Field"

        if name != "":
            if not all(x.isalpha() or x == " " for x in name):
                return "Invalid Field"

        return[name, country, age, gender]


# @post returns all information about the random character
def random_character_paragraph():
    character = random_character()
    if request.method == "POST":
        output = request.form.to_dict()
        if output["name"] != "":
            name = output["name"]
        else:
            name = random_character_name(character)
        if output["CountryOfOrigin"] != "":
            home = output["CountryOfOrigin"]
        else:
            home = random_character_home(character)

        if output["age"] != "/":
            age = int(output["age"])
        else:
            age = random_character_age(character)

        if output["gender"] != "/":
            gender = output["gender"]
        else:
            gender = random_character_gender(character)

    else:
        name = random_character_name(character)
        age = random_character_age(character)
        home = random_character_home(character)
        gender = random_character_gender(character)
    picture = random_character_picture(character_picture(age, gender, UI_API_1))
    if picture == "https://uifaces.co/images/cooldown-avatar.png":
        picture = random_character_picture(character_picture(random_character_age(character), random_character_gender(character), UI_API_2))
        if picture == "https://uifaces.co/images/cooldown-avatar.png":
            picture = character['picture']['large']
    if age >= 60:
        hobbies = character_hobbies_old()
    else:
        hobbies = character_hobbies_young()
    hobbiestext = "{}, {}, and {}.".format(hobbies[0], hobbies[1], hobbies[2])
    poem = character_poem()
    text = character_bio("{} is a {} year old {} from {}.".format(name, age, gender, home))
    song = random_song()
    return [text, picture, name, home, age, gender, poem, hobbiestext, song]


# @post returns a random character picture
def random_character_link():
    character = random_character()
    picture = random_character_picture(character)
    return picture
