

from funcion import *

if __name__ == '__main__':

    while True:

        str1 = input('Input: ')

        if str1 == 'exit':
            print("Exiting the program!!!")
            break

        str2 = clear(str1)
        print(parse(str2))
