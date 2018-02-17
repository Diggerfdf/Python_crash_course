bicycles = ['Trek', 'CanNonDale', 'redline', 'SPECIALIZED']

print(bicycles[0].title())

bicycles[1] = 'Cannondale'

print(bicycles)

bicycles.append('Giant')

print (bicycles)

motorcycles = []

motorcycles.append('Honda')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')

print (motorcycles)

motorcycles.insert(0, 'Ducati')

print(motorcycles)

del motorcycles[3]

print(motorcycles)

motorcycles = []

motorcycles.append('Honda')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')

print (motorcycles)

poped_motorcycle = motorcycles.pop(1)

print (motorcycles)
print (poped_motorcycle)

motorcycles.remove('Suzuki')

print (motorcycles)