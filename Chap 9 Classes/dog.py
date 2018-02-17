class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('maTilda', 8)
your_dog = Dog('wiLlie', 6)

print("My dog's name is {}.".format(my_dog.name.title()))
print("My dog is {} years old.".format(str(my_dog.age)))
my_dog.sit()

print("\nYour dog's name is {}.".format(your_dog.name.title()))
print("Your dog is {} years old.".format(str(your_dog.age)))
your_dog.sit()


some_dog = Dog('bIllie', 10)
print("Some dog's name is {}.".format(some_dog.name.title()))
print("Some dog is {} years old.".format(str(some_dog.age)))
my_dog.sit()
