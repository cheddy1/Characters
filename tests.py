#Test Suite
from .character import random_character_paragraph, customization_info, random_song
#checks to see if all fields are generated properly once user clicks generate character
def test1():
    character = random_character_paragraph()
    string1=character[1]
    if ".jpg" not in string1:
        return("Test 1 failed image not loaded for character")
    else:
        return("Test 1 passed image loaded properly")

def testsuite():
    return(test1())
