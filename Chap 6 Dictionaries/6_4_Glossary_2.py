glossary = {'string': 'A series of characters',
            'comment': 'A note in a program that the Python interpreter ignores.',
            'list': 'A collection of items in a particular order.', 
            'loop': 'Work through a collection of items, one at a time.',
            'dictionary': 'A collection of key-value pairs.',
            'iteration': 'An arbitrary variable to receive a value from each iteration\
                            through a list.',
            'tuple': 'An immutable list',
            'NumPy': 'A Python module to work with arrays, and numbers'                        
            }

for key, definition in glossary.items():
    print(key.title() + ": " + definition)
