def make_sandwich(*items):
    """Make a Sandwich with the given items."""
    print("\nI'll make you a Great Sandwich:")
    for item in items:
        print(" ...adding {} to your sandwich.".format(item))
    print("Your sandwich is ready!")
    
make_sandwich('Roast beef', 'Cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('Roast beef', 'Prato', 'Salada', 'Picles', 'Molho Agridoce')
make_sandwich('Frango', 'Mussarela', 'Salada', 'Tomate', 'Maionese', 'Mostarda')
