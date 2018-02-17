# 4.10 slices: Using one of the programs you wrote, add several lines
# at the end that do the following: "

# First three items

twenty_num = [ value for value in range(1, 21)]
print(twenty_num)

print("\n\nThe first three items in the list are: {}.".format(twenty_num[:3]))

# Three itens from te middle of the list

print("\n\nThe itens from the middle of the list are: {}.".format(twenty_num[7:-8]))

# Last three items

print("\n\nThe last 3 itens are: {}.".format(twenty_num[-3:]))
