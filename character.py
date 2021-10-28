import requests

res = requests.get("https://randomuser.me/api/").json().get('results')[0]
def random_character():
    # res = requests.get("https://randomuser.me/api/").json().get('results')[0]
    result = res

    print(result)

def random_character_name():
    title = res.get('name').get('title')
    first = res.get('name').get('first')
    last = res.get('name').get('last')
    return title + '.' + ' ' + first + ' ' + last

def random_character_gender():
    gender = res.get('gender')
    return gender

def random_character_home():
    home = res.get('location').get('country')
    return home

def random_character_age():
    age = res.get('dob').get('age')
    return age

def random_character_picture():
    picture = res.get('picture').get('large')
    return picture
def random_character_paragraph():
    print( "{} is a {} year old {} from {}.".format(random_character_name(), random_character_age(),random_character_gender(),random_character_home()))


