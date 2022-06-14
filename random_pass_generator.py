#!/usr/bin/env python3
# random_pass_generator.py generates a random password based on password requirements
# password ends in '!', starts with upper case letter, and contains numbers and lower case letters
# military phonetics for reading password are also printed.

import random, string

passLength = int(input('How many characters should the password be? '))

# define password characters
lcase = list(string.ascii_lowercase)
ucase = list(string.ascii_uppercase)
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(0, 10):
    lcase.append(str(i)) 

# generate password
def gen_password(passLength):
    password = ''
    password += random.choice(ucase)
    password += random.choice(num)
    
    for i in range(passLength - 3):
        randChoice = random.choice(lcase)
        password += randChoice
        
    password += '!'
    return password

#print password with military phoenetics
def gen_milp(password):
    # military phonetics
    mil_alph = {
        '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
        'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'I':'India', 'J':'Juliet', 
        'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 
        'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'
    }
    # empty string of military phonetics
    mil_ph = ''
    # First letter is capitalized
    for key, value in mil_alph.items():
        if password[0] == key:
            mil_ph += "Capital " + value + ", " 
    # Read the rest of password
    for c in password[1:]:
        for key, value in mil_alph.items():
            if c.upper() == key:
                mil_ph += value.lower() + ', '
    mil_ph += "!"
            
    return mil_ph
                
            
# call funtions

genpassword = gen_password(passLength)
phonetics = gen_milp(genpassword)

# print results

print(genpassword)
print(phonetics)

       