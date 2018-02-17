my_pizzas = ['Mussarela', 'Portuguesa', 'Calabreza', 'Rúcula com tomate seco',
			    'Margherita']

friend_pizzas = my_pizzas[:]


my_pizzas.append("Romana")
friend_pizzas.append("California")

print("My favorite pizzas are:\n")

for pizza in my_pizzas:
    print(pizza)    
    
print()

print("My friend's favorite pizzas are:\n")

for pizza in friend_pizzas:
     print(pizza)
