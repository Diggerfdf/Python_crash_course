people = [
    {'first_name': 'otávio', 'last_name': 'assis', 
     'age': '15', 'city': 'ribeirão pires'},
    {'first_name': 'fabiano', 'last_name': 'ferreira',
     'age': '42', 'city': 'ribeirão pires'},
    {'first_name': 'sandra', 'last_name': 'marques',
     'age': '62', 'city': 'ribeirão pires'},
     ]

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].capitalize()
    
    print(name + ", of " + city + ", is " + age + " years old.")
