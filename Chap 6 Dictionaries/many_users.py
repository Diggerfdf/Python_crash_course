users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie', 
        'last': 'currie',
        'location': 'paris',
        },
    'fferreira': {
        'first': 'fabiano', 
        'last': 'ferreira', 
        'location': 'ribeirão pires',
        },
    }

for username, user_info in users.items(): 
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
