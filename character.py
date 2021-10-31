import requests

def random_character():
    return requests.get("https://randomuser.me/api/").json().get('results')[0]

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
    picture = character.get('picture').get('large')
    return picture

def random_character_paragraph():
    character = random_character()
    picture = random_character_picture(character)
    return ["{} is a {} year old {} from {}.".format(random_character_name(character), random_character_age(character), random_character_gender(character), random_character_home(character)),picture]


def random_character_link():
    character = random_character()
    picture = random_character_picture(character)
    return picture
