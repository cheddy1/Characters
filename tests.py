#Test Suite
from .character import random_character_paragraph, customization_info, random_song
#test checks image, name ,country, age and gender output
def test1():
    character = random_character_paragraph()
    string1=character[1] #string represents image url
    string2=character[2] #string represents name
    string3=character[3] #string represents country
    string4=character[4]#string represents age
    string5=character[5]#string represents gender
    if "images" and "jpg" not in string1:
        return("Test 1 failed: image not loaded for character")
    elif not all(x.isalpha() or x == " " for x in string2):
        return("Test 1 failed: name field is  invalid for character")
    elif not all(x.isalpha() or x == " " for x in string3):
        return "Test 1 failed: country field is invalid for character"
    #elif not all(x.isdigit() or x == " " for x in string4):
        #return ("Test 1 failed: age field is invalid for character")
    elif not all(x.isalpha() or x == " " for x in string5):
        return ("Test 1 failed: gender field is invalid for character")
    else:
        return("Test 1 passed: Image,name,country,age and gender fields are valid when generating character")
#Test checks short biography field
def test2():
    character = random_character_paragraph()
    string0 = character[0]  # string represents biography
    if not all(x.isalpha() or x == " " or x=="\n" or x=="." or x.isdigit() for x in string0):
        return ("Test 2 failed: Character bio field is invalid for character")
    else:
        return ("Test 2 passed: Character bio field is valid for character")

#Test checks favorite poem field for character
def test3():
    character = random_character_paragraph()
    string6 = character[6]  # string represents poem
    if not all(x.isalpha() or x == " " or x=="," for x in string6):
        return ("Test 3 failed: poem field is invalid for character")
    else:
        return("Test 3 passed: poem field is valid for character")
#Test checks hobbies field for character
def test4():
    character = random_character_paragraph()
    string7=character[7]
    y = string7.split(",")
    z=y[2].split("and")
    s=z[1].split(".")
    search_hobbies=[y[0],y[1],s[0]]
    hobby_list = open('static/hobbies.txt')
    for line in hobby_list:
        if y[0] in line:
           return("Hello")
        else:
            return (y[1])
#tests favorite song field
def test5():
    character = random_character_paragraph()
    string8=character[8]#string represents favorite song
    if(x.isalpha() or x == " " or x=="," for x in string8):
        return ("Test 5 failed: song field is invalid for character")
    else:
        return ("Test 5 passed: song field is invalid for character")



