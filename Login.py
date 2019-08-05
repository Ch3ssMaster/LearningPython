class Login:
    system_users = {
        'admin': {
            'user': 'admin',
            'pass': 'admin'
        },
        'user': {
            'user': 'John',
            'pass': '1234'
        }
    }

    def __init__(self):
        self.role = None
        attempts = 3
        print('*' * 5 + ' Introduce username and password ' + '*' * 5)
        while attempts > 0:
            self.user = input('username: ')
            self.password = input('password: ')
            if self.validate_access():
                if self.role == 'admin':
                    pass
                else:
                    print(f'Welcome {self.user}')
                break
            else:
                attempts -= 1
                if attempts > 1:
                    print(f'username or password wrong, try again ({attempts} more attempts)')
                else:
                    print('username or password wrong, last attempt')

    def validate_access(self):
        user_found = False
        password_found = False
        for user_role, values in self.system_users.items():
            for key in values:
                if key == 'user' and self.user == values[key]:
                    user_found = True
                if key == 'pass' and self.password == values[key]:
                    password_found = True
            if user_found and password_found:
                self.role = user_role
                return user_found and password_found
            else:
                user_found = False
                password_found = False



test = Login()
