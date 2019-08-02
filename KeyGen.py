import random


class KeyGen:
    key = []
    lower = []
    numbers = []
    symbols = []
    upper = []

    '''
    constructor that generates 4 lists, 
    for lowercase, uppercase, numbers and symbols,
    from ASCII characters
    '''

    def __init__(self):
        i = 0
        for number in range(33, 127):
            i += 1
            # print(number , ' - ', chr(number))
            if 48 <= number <= 57:
                self.numbers.append(chr(number))
            elif 65 <= number <= 90:
                # print(number)
                self.upper.append(chr(number))
            elif 97 <= number <= 122:
                self.lower.append(chr(number))
            else:
                self.symbols.append(chr(number))
        self.create_menu()

    '''
    creates a 2 options menu, which allows you to choose 
    between closing the program or generating a new password
    '''

    def create_menu(self):
        print('Welcome to KeyGen program')
        option = ''
        while option != 'q':
            print('*' * 5, 'press c for create a new password')
            print('*' * 5, 'press q for exit')
            option = input('select your choice:').lower()
            if option == 'c':
                self.define_key_parameters()

    '''
    Interact with the user to define the password parameters.
    The outputs of the method itself explain its operation
    '''

    def define_key_parameters(self):
        print('Introduce the parameters for the new password: ')
        ch_number = input('*' * 5 + 'select key\'s characters number: (between 8 and 12)')
        while not ch_number.isnumeric() or int(ch_number) not in range(8, 13):
            print('please enter a valid option:')
            ch_number = input('*' * 5 + 'select key\'s characters number: (between 8 and 12)')
        values = ('y', 'n')
        option = ''
        characters = ('lowercase', 'uppercase', 'numbers', 'symbols')
        ch_included = []
        for ch_type in characters:
            while option not in values:
                print('enter y (yes) or n (no)')
                option = input('*' * 5 + f'Would you like include {ch_type}?').lower()
                if option == 'y':
                    if ch_type == 'lowercase':
                        ch_included.extend(self.lower)
                    elif ch_type == 'uppercase':
                        ch_included.extend(self.upper)
                    elif ch_type == 'numbers':
                        ch_included.extend(self.numbers)
                    else:
                        ch_included.extend(self.symbols)
                    print(f'ok, {ch_type} included')

            option = None

        if not ch_included:
            print('no characters have been selected, at least the lower case will be included in the password')
            ch_included.extend(self.lower)
        self.key_generator(ch_number, ch_included)

    '''
    create a password with user-defined parameters, and send it to standard output
    '''

    def key_generator(self, ch_number, ch_included):
        for i in range(0, int(ch_number)):
            self.key.append(ch_included[random.randint(0, (len(ch_included)-1))])

        print('A new password has been created: ' + ''.join(self.key))
        self.key.clear()


test = KeyGen()
# print(test.symbols)
