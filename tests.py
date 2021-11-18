# Test Suite
#helper function to check if age input is an int
def age_check(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False

# test checks image, name ,country, age and gender output
def test1(character):
    image_url = character[1] #string represents image url
    name = character[2] #string represents name
    country = character[3] #string represents country
    age = character[4]#string represents age
    gender = character[5]#string represents gender
    print("here")
    if "images" and "jpg" not in image_url:
        return("Test 1 failed: image not loaded for character")
    elif not all(x.isalpha() or x == " " for x in name):
        return("Test 1 failed: name field is  invalid for character")
    elif not all(x.isalpha() or x == " " for x in country):
        return "Test 1 failed: country field is invalid for character"
    elif age_check(age)==False:
        return ("Test 1 failed: age field is invalid for character")
    elif not all(x.isalpha() or x == " " for x in gender):
        return ("Test 1 failed: gender field is invalid for character")
    else:
        return("Test 1 passed: Image,name,country,age and gender fields are valid when generating character")


# Test checks short biography field
def test2(character):
    bio_text = character[0]  # string represents biography
    if not bio_text:
        return ("Test 2 failed: Character bio field is invalid for character")
    else:
        return ("Test 2 passed: Character bio field is valid for character")


# Test checks favorite poem field for character
def test3(character):
    poem_text = character[6]  # string represents poem
    if not poem_text:
        return ("Test 3 failed: Poem field is invalid for character")
    else:
        return("Test 3 passed: Poem field is valid for character")

#checks to see if string is in line helper function for hobbies test
def check_string_in_file(file_name, string):
    # Open the file in read only mode and check lines for string
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string in line:
                return True
    return False

# Test checks hobbies field for character
def test4(character):
    string7 = character[7]
    y = string7.split(",") #splits hobby y[0]
    if check_string_in_file('static/hobbies.txt', str(y[0]))==True or check_string_in_file('static/hobbiesold.txt', str(y[0]))==True:
        return("Test 4 passed: Hobbies field is valid for character")
    else:
        return("Test 4 failed: Hobbies field is invalid for character")

# tests favorite song field
def test5(character):
    song = character[8]#string represents favorite song
    if not song:
        return ("Test 5 failed: Song field is invalid for character")
    else:
        return ("Test 5 passed: Song field is valid for character")



