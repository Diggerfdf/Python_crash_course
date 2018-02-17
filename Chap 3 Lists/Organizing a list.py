# Organising a list

'''cars = ['BmW', 'auDI', 'ToyTa', 'SUBARU']

# You can use a "parser" small program to sort it out Upper, lower or Title cases 
# in a list. Like below.

cars = [i.lower() for i in cars] 

cars.sort()

print(cars)'''


cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort(reverse=True)

print(cars)

print("here is the original list: {}".format(cars))

print("\nHere is the sorted list: {}".format(sorted(cars)))

print("\nHere is the original list again: {}".format(cars))

print(len(cars))