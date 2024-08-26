import time
import sys

path = input('Sorry to ask for the folder path again... <: ')


def add():
    while True:
        type_file = input('[1] Add To MD5 List\n[2] Add to TXT List\n[3] Go Back\n ')
        if type_file == '1':
            website = input('Enter Website Name (x.com) <: ')
            hash_pass = input('Enter MD5 Hash <: ')

            file = open(path + '\\md5.txt', 'a')
            file.write(website + ' : ' + hash_pass + '\n')
            file.close()
            break

        elif type_file == '2':
            website = input('Enter Website Name (x.com) <: ')
            pwd = input('Enter Password <: ')

            file = open(path + '\\pass.txt', 'a')
            file.write(website + ' : ' + pwd + '\n')
            file.close()
            break

        elif type_file == '3':
            break
        
        else:
            print('Enter a valid input')


def view_md5():
    file = open(path + '\\md5.txt', 'r')
    txt = file.read()
    print(txt)


def view_txt():
    file = open(path + '\\pass.txt', 'r')
    txt = file.read()
    print(txt)


def exiting():
    print('Exiting...')
    time.sleep(2)
    sys.exit()


def what_to_do():
    print('[PASSWORD STORAGE]')

    while True:

        action = input('\n[1] Add\n[2] Retrieve\n[3] Exit\n ')

        if action == '1':
            print('')
            add()

        elif action == '2':

            while True:

                pass_type = input('\n[1] MD5 HASH\n[2] TXT LIST\n[3] GO BACK ')

                if pass_type == '1':
                    print('\n\n')
                    view_md5()
                    print('\n\n')
                    break

                elif pass_type =='2':
                    print('\n\n')
                    view_txt()
                    print('\n\n')
                    break

                elif pass_type == '3':
                    break

                else:
                    print('Enter a valid input')

        elif action == '3':
            exiting()

        else:
            print('\nEnter a valid input\n')


def main():
    while True:
        what_to_do()


if __name__ == '__main__':
    main()
