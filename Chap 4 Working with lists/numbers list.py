# numbers list
# For range to generate this rang from 2 up to 7

for value in range (2,8):
    print(value)
    
# You can generate a range and a list at the same time    
numbers = list(range(1, 6))

print(numbers)

# Even numbers. The 2 at the end of the argument is a "leap"
even_numbers = list(range(2, 11, 2))

print(even_numbers)

# Odd numbers. 
odd_numbers = list(range(1, 12, 2))

print(odd_numbers)

# squares list... 

squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    
#   linhas 27 & 28 podem ser simplificadas = squares.append(value ** 2)
    
print()    
print(squares)

# Simple statistics

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

x = min(digits)

y = max(digits)

z = sum(digits)

print('min is {}, max is {} and sum is {}'.format(x, y, z))

# LIST COMPREHENSIONS!!!!

squares = [ value ** 2 for value in range(1, 11)]
print()
print(squares)

