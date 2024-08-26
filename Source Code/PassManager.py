import hashlib
import getpass
import sys
import subprocess
import time



def exiting():

    print('Exiting...')
    time.sleep(2)
    sys.exit()


def exiting2():
    print('Redirecting...')
    time.sleep(3)


def creating_initial():

    while True:
        print('Welcome to Nao\'s password manager!\n')

        account = input('Have you already set up a password? Y/N <: ').upper()
        if account == 'Y':
            break

        elif account == 'N':
            try:
                pwd_path = input('Copy and Paste the path this application is found in <: ')
                pwd_file = open(pwd_path + '\\app_password.txt', 'x')

            except FileExistsError:
                print('You have already made a password!')
                exiting2()
                break

            pwd = input('Carefully enter password for this application\n>>>>> WARNING <<<<<\nTHIS PASSWORD CANNOT BE CHANGED! MAKE SURE TO REMEMBER AND ENTER IT CORRECTLY\n>>> ')

            app_pass = open(pwd_path + '\\app_password.txt', 'a')
            app_pass.write(pwd + '')
            app_pass.close

            print('You have successfully created your password!')
            while True:
                like_to_see = input('Would you like to see your password? Y/N <: ').upper()

                if like_to_see == 'Y':
                    print('Your application password is <: ' + pwd)
                    exiting2()
                    break

                elif like_to_see == 'N':
                    exiting2()
                    break

                else:
                    print('Enter Y or N')
            break
        
        else:
            print('Enter Y or N')


def login():

    path = input('\nHi! From here on out (because I\'m not very good at coding) I need the path where this zip installed lol\nPlease enter it here (starting with disk i.e., c:) <: ')

    passwurdo = open((path + '\\app_password.txt'), 'r').read()

    login_password = getpass.getpass('\nEnter password <: ')

    if login_password == passwurdo:
        print('\nSuccessfully Logged In\n')
        print('>>>>> PASSWORD MANAGER <<<<<')
        print('v1.01')
        print('@NaoWasTaken\n')

        get_file()

        while True:
            project = input('\n[MAIN MENU]\n[1] Password Generator\n[2] Stored Passwords\n[3] Exit\n ')

            if project == '1':
                confirm = input('\n[PASS GENERATOR]\nAre you sure you want to open Password Generator?\n[1] Yes\n[2] Go Back\n ')
                if confirm == '1':
                    exe_path = path + '\\pass_generator'
                    try:
                        subprocess.run([exe_path])
                    except subprocess.CalledProcessError as e:
                        print(f'An error occured: {e}')

            elif project == '2':
                confirm = input('\n[STORED PASS]\nAre you sure you want to open Stored Passwords?\n[1] Yes\n[2] Go Back\n ')
                if confirm == '1':
                    exe_path = path + '\\stored_passwords'
                    try:
                        subprocess.run([exe_path])
                    except subprocess.CalledProcessError as e:
                        print(f'An error occured: {e}')

            elif project == '3':
                exiting()
               
            else:
                print('Please enter a valid input\n')

    else:
        print('\nIncorrect Password\n')
    


def account_login():
    while True:
        choice = input('[1] Login\n[2] Exit\n ')

        if choice == '1':
            login()

        elif choice == '2':
            break

        else:
            print('\nInvalid Selection\n')


def get_file():
    
    while True:

        try:
            create_file = input('Do you need to generate pass.txt and md5.txt? (If this is your first time using, enter 1)\n[1] Yes\n[2] No\n ')
            if create_file == '1':
                pwd_path = input('Copy and Paste the path this application is found in (again) <: ')
                pwd_file = open(pwd_path + '\\pass.txt', 'x')
                md5_file = open(pwd_path + '\\md5.txt', 'x')
                print('\nCreating files...')
                time.sleep(3)
                print('\nFiles successfully created!')
                break

            elif create_file == '2':
                break

            else:
                print('\nEnter a valid input\n')

        except FileExistsError:
            print('\nYou already have these files!')
            break


def main():
    creating_initial()
    account_login()


if __name__ == '__main__':
    main()
