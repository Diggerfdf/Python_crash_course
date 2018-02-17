players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players)

# Selecione de 0 até 2 (michael)
print(players[0:3])


# Selecione de 2 até 3 (martina até florence)
print(players[1:4])

# Selecione do início até 4 (florence)

print(players[:4])

# Selecione do 3 até o fim (michael até eli)

print(players[2:])

# Selecione os 3 últimos da lista 

print(players[-3:])

players.append("fabiano")
players.append("otávio")
players.append("sandra")

print(players[-3:])
print()

# Looping through a Slice

print("Here are the first three players on my team: \n")

for player in players[:3]:
    print(player.title())
    
    
