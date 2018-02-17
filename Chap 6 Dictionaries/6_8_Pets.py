# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'dog',
    'name': 'matilda', 
    'owner': 'sandra', 
    'weight': 20,
    'eats': 'everything', 
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'melinda', 
    'owner': 'fabiano', 
    'weight': 5,
    'eats': 'cat food', 
}
pets.append(pet)

pet = {
    'animal type': 'turtle',
    'name': 'Uga', 
    'owner': 'otávio', 
    'weight': 1,
    'eats': 'lettuce'
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
    
# Faça com nested lists + dictionaries para testar. 
