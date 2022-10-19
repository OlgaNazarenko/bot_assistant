from input_parser import search_args,check_args
from utils import input_error

def main():
    while True:
        data = input('\nEnter command: ')

        args = search_args(data)

        if args:
            handler = args[0]
            args = args[1]

            result = handler(*args) if args else handler()

            if result:
                print('\n' + result)

            if result == 'Good bye!':
                break


if __name__ == '__main__':
    main()
