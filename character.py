import requests
from flask import request
import random

UI_API_1 = '241E1EB8-FFA54369-A0851285-2C688163'
UI_API_2 = 'A3D1D37D-506D4D4B-B1C36F96-5FF139DB'


def random_character():
    return requests.get("https://randomuser.me/api/").json().get('results')[0]


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


def character_hobbies_old():
    hobbiesold = open('static/hobbiesold.txt').read().splitlines()
    hobby1 = random.choice(hobbiesold)
    hobby2 = random.choice(hobbiesold)
    hobby3 = random.choice(hobbiesold)
    if hobby2 != hobby1 and hobby2 != hobby3 and hobby1 != hobby3: #if hobbies are different
        hobbylist = [hobby1, hobby2, hobby3] #return array of 3 hobbies
        return hobbylist
    else:
        return character_hobbies_old()


def character_poem():
    fav_poem = requests.get('https://www.beanpoems.com/api/poems/random').json().get('body')
    return fav_poem


def character_bio(text):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': text,
        },
        headers={'api-key': '9d321645-60cb-4d93-8e08-3583dd1c4ec9'}
    )
    groups = r.json()['output'].split('\n')
    return '\n'.join(groups[:2])


def random_character_name(character):
    title = character.get('name').get('title')
    first = character.get('name').get('first')
    last = character.get('name').get('last')
    return title + '.' + ' ' + first + ' ' + last


def random_character_gender(character):
    gender = character.get('gender')
    return gender


def random_character_home(character):
    home = character.get('location').get('country')
    return home


def random_character_age(character):
    age = character.get('dob').get('age')
    return age


def random_character_picture(character):
    picture = character[0]['photo']
    return picture

def customization_info():
    if request.method == "POST":
        output = request.form.to_dict()
        name = output["name"]
        country = output["CountryOfOrigin"]
        age = output["age"]
        gender = output["gender"]
        print(name, country, age, gender)

        if gender == "Male" or gender == "male" or gender == "Female" or gender == "female" or gender == "":
            if age != "":
                if 18 < int(age) < 120:
                    return[name, country, age, gender]
                else:
                    return("Invalid Field")
            else:
                return [name, country, age, gender]
        else:
            return("Invalid Field")



def random_character_paragraph():
    character = random_character()
    if request.method == "POST":
        output = request.form.to_dict()
        if output["name"] != "/":
            name = output["name"]
        else:
            name = random_character_name(character)

        if output["CountryOfOrigin"] != "/":
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

        print(name, age, home, gender)
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
    return [text, picture, name, home, age, gender, poem, hobbiestext]


def random_character_link():
    character = random_character()
    picture = random_character_picture(character)
    return picture
