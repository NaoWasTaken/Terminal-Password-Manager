import random
import string
import time
import sys
import hashlib

path = input('Sorry to ask for the folder path again... <: ')


def exiting():
    print('Exiting...')
    time.sleep(2)
    sys.exit()


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

while True:
    print('[PASSWORD GENERATOR]')
    go = input('Press Enter To Generate, Q to Quit <: ').upper()
    if go == 'Q':
        exiting()

    website = input('Enter website name (x.com) <: ')
    email = input('Enter the email used <: ')
    username = input('Enter the username used (if none, leave blank) <: ')
    min_length = int(input('Enter minimum length <: '))
    has_number = input('Do you want to have numbers? Y/N <: ').lower() == 'Y'
    has_special = input('Do you want to have special characters? Y/N <: ').upper() == 'Y'
    pwd = generate_password(min_length, has_number, has_special)

    file = open(path + '\\pass.txt', 'a')
    file.write(website + ' : ' + email + ' : ' + username + ' : ' + pwd + '\n')
    file.close()

    while True:

        while True:

            encode = input('Would you like to encrypt the password? Y/N <: ').upper()
            if encode == 'N':
                print('The generated password is <: ' + pwd)
                break

            elif encode == 'Y':
                hash_pass = hashlib.md5(pwd.encode('utf-8'))
                digested_pass = hash_pass.hexdigest()
                print('The encoded password is <:', digested_pass)
                file = open(path + '\\md5.txt', 'a')
                file.write(website + ' : ' + email + ' : ' + username + ' : ' + digested_pass + '\n')
                file.close()
                break

            else:
                print('Invalid Selection')
            
        new_pass = input('Would you like to create a new password? Y/N <: ').upper()
        if new_pass == 'Y':
            break

        elif new_pass =='N':
            exiting()
            
        else:
            print('Please enter a valid selection')
