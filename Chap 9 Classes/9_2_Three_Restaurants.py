class Restaurant():
    """A class representing a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
        
    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)
        
    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)
        
mean_queen = Restaurant('the Mean QUEEN', 'PizZa')
mean_queen.describe_restaurant()

jotas = Restaurant('Jotas', 'sandwichs')
jotas.describe_restaurant()

grease_spoon = Restaurant('Grease SPOon', 'Bad food')
grease_spoon.describe_restaurant()
