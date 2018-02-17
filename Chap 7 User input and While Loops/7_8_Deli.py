sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sanduiche = sandwich_orders.pop()
    print("I'm working on you {} sandwich.".format(current_sanduiche))
    finished_sandwiches.append(current_sanduiche)
    
print("\n")
for sandwich in finished_sandwiches: 
    print("I made a {} sandwich.".format(sandwich))
