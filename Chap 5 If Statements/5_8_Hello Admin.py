user_names = ['Lucas', 'Otávio', 'Fabiano', 'admin', 'Sandra']

for name in user_names:
    if name == 'admin':
        print('Hello, Admin! Do you want to see a status report?')
    
    else:
        print('Hello {}, thank you for logging in again'.format(name))
