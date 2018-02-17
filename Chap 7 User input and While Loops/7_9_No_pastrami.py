sandwich_orders = ['veggie', 'pastrami', 'grilled cheese', 'pastrami', 'turkey', 'roast beef', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []

print("\nSorry, our Deli is out of Pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:    
    current_sanduiche = sandwich_orders.pop()
    print("I'm working on you {} sandwich.".format(current_sanduiche))
    finished_sandwiches.append(current_sanduiche)
    
print("\n")
for sandwich in finished_sandwiches: 
    print("I made a {} sandwich.".format(sandwich))
