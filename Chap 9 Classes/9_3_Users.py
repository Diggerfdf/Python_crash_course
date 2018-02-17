class User():
    """Represent a simple user profile."""
    
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.email = email
        self.location = location.title()
        
    def describe_user(self): 
        """Display a summary of the user's information"""
        print("\n {} {}.".format(self.first_name, self.last_name))
        print("\t Username: {}".format(self.username))
        print("\t Email: {}".format(self.email))
        print("\t Location: {}".format(self.location))
    
    def greet_user(self):
        """Display a personalized greeting to the user"""
        print("\nWelcome Back, {}!".format(self.username))
        
        
        
        
fabiano = User('fAbIano', 'feRReiRA', 'digger', 'diggerfdf@gmail.com', 'RIbeirÃO PIRes')
fabiano.describe_user()
fabiano.greet_user()

otavio = User('otAvio', 'aSSis', 'oTacOn', 'otavio.marquesassis@gmail.com', 'Ribeirão Pires')
otavio.describe_user()
otavio.greet_user()
