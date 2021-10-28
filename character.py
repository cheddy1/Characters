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
    print(title + ' ' + first + ' ' + last)

def random_character_gender():
    gender = res.get('gender')
    print(gender)

def random_character_home():
    home = res.get('location').get('country')
    print(home)

def random_character_age():
    age = res.get('dob').get('age')
    print(age)

def random_character_picture():
    picture = res.get('picture').get('large')
    return picture


