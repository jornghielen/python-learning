"""A set of classes that can be used to represent electic cars."""

from car import Car

class Battery:
    """A simple attempt to model a battery for an electic car."""

    def __init__(self, battery_size=100):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315    
        elif self.battery_size == 130:
            range = 375

        print(f"This car can go about {range} kilometers on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """"
        Initialize attributes of the parent class.
        Then initialize attributes specific to an eletric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need gass in it's tank, bettery charge it!")

my_tesla = ElectricCar('tesla', 'cybertruck', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()