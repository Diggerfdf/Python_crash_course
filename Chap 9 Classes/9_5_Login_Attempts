class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information"""
        print("\n {} {}.".format(self.first_name, self.last_name))
        print("\t Username: {}".format(self.username))
        print("\t Email: {}".format(self.email))
        print("\t Location: {}".format(self.location))

    def greet_user(self):
        """Display a personalized greeting to the user"""
        print("\nWelcome Back, {}!".format(self.username))

    def increment_login_attempts(self):
        """Increment the value of login_attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset_login_attempts to 0"""
        self.login_attempts = 0


fabiano = User('fAbIano', 'feRReiRA', 'digger', 'diggerfdf@gmail.com', 'Sp')
fabiano.describe_user()
fabiano.greet_user()

print("\nMaking 3 login attempts...")
fabiano.increment_login_attempts()
fabiano.increment_login_attempts()
fabiano.increment_login_attempts()
print("  Login Attempts: " + str(fabiano.login_attempts))

print("Resetting login attempts...")
fabiano.reset_login_attempts()
print("  Login Attempts: " + str(fabiano.login_attempts))
