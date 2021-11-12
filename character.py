import requests

UI_API_1 = '241E1EB8-FFA54369-A0851285-2C688163'
UI_API_2 = 'A3D1D37D-506D4D4B-B1C36F96-5FF139DB'

def random_character():
    return requests.get("https://randomuser.me/api/").json().get('results')[0]

def character_picture(age, gender, key):
    uiface = requests.get(
        'https://uifaces.co/api',
        headers={
        'X-API-KEY': key,
        'Accept': 'application/json',
	    'Cache-Control': 'no-cache'
        },
        params={
        'limit': 1,
        'gender[]': gender,
        'from_age': age-10,
        'to_age': age+10
        }
    )
    return uiface.json()

def character_bio(text):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': text,
        },
        headers={'api-key': '9d321645-60cb-4d93-8e08-3583dd1c4ec9'}
    )
    groups = r.json()['output'].split('\n')
    return '\n'.join(groups[:3])

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

def random_character_paragraph():
    character = random_character()
    picture = random_character_picture(character_picture(random_character_age(character), random_character_gender(character), UI_API_1))
    if picture == "https://uifaces.co/images/cooldown-avatar.png":
        picture = random_character_picture(character_picture(random_character_age(character), random_character_gender(character), UI_API_2))
        if picture == "https://uifaces.co/images/cooldown-avatar.png":
            picture = character['picture']['large']
    name = random_character_name(character)
    age = random_character_age(character)
    home = random_character_home(character)
    gender = random_character_gender(character)
    text = character_bio("{} is a {} year old {} from {}.".format(name, age, gender, home))
    return [text,picture,name,home,age,gender]


def random_character_link():
    character = random_character()
    picture = random_character_picture(character)
    return picture
