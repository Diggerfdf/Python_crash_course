"""trying to emulate an Electric Car."""


class Car():
    """A Simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize the basic car info."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Descriptive name of the car."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Reading the Odometer."""
        print("this car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Updatind the Odometer."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll bak an odometer!")

    def increment_odometer(self, miles):
        """Incrementing the Odometer."""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an ellectric car."""

    def __init__(self, battery_size=60):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-KWh Battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 KWh.")
        else:
            print("The Battery is already upgraded.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the batttery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
