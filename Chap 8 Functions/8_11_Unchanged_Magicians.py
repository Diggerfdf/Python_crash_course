def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Add 'The Great!' to each magicians's name."""
    # Build a new list to hold the great magicians.
    great_magicians = []
    
    # make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    
    # Add the great Magicians back into magicians:
    for great_magician in great_magicians:
        magicians.append(great_magician)        
        
magicians = ['HaRry Houdini', 'DavID Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)
