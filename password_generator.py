import random
import string

def generate_password(length, numbers=True, special_character=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters+= digits

    if special_character:
        characters+= special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd)<length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special

    print(pwd)

generate_password(10,False,False)
generate_password(10,True,False)
generate_password(10,False,True)



