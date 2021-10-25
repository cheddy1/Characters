import requests

def random_character():
    res = requests.get("https://randomuser.me/api/")
    print(res.json())
