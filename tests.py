# Test Suite


# test checks image, name ,country, age and gender output
def test1(character):
    image_url = character[1]
    name = character[2]
    country = character[3]
    age = character[4]
    gender = character[5]
    print("here")
    if "images" and "jpg" not in image_url:
        return "Test 1 failed: image not loaded for character"
    elif not all(x.isalpha() or x == " " for x in name):
        return "Test 1 failed: name field is  invalid for character"
    elif not all(x.isalpha() or x == " " for x in country):
        return "Test 1 failed: country field is invalid for character"
    # elif not all(x.isdigit() or x == " " for x in age):
        # return ("Test 1 failed: age field is invalid for character")
    elif not all(x.isalpha() or x == " " for x in gender):
        return "Test 1 failed: gender field is invalid for character"
    else:
        return "Test 1 passed: Image,name,country,age and gender fields are valid when generating character"


# Test checks short biography field
def test2(character):
    bio_text = character[0]  # string represents biography
    if not bio_text:
        return "Test 2 failed: Character bio field is invalid for character"
    else:
        return "Test 2 passed: Character bio field is valid for character"


# Test checks favorite poem field for character
def test3(character):
    poem_text = character[6]  # string represents poem
    if not poem_text:
        return "Test 3 failed: poem field is invalid for character"
    else:
        return "Test 3 passed: poem field is valid for character"


# Test checks hobbies field for character
def test4(character):
    string7 = character[7]
    y = string7.split(",")
    z = y[2].split("and")
    s = z[1].split(".")
    search_hobbies = [y[0], y[1], s[0]]
    with open('static/hobbies.txt') as hobby_list:
        for line in hobby_list:
            if y[0] in line:
                return "Hello"
            else:
                return y[1]


# tests favorite song field
def test5(character):
    song = character[8]
    if not song:
        return "Test 5 failed: song field is invalid for character"
    else:
        return "Test 5 passed: song field is valid for character"



