current_users = ['fabiano', 'otávio', 'sandra', 'lucas', 'genevieve']

new_users = ['fabIAno', 'LUcas', 'margarida', 'mickey', 'pateta']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("{} is already taken. Please choose a different name".format(new_user))         
    else:
        print("{} is availabe.".format(new_user))
