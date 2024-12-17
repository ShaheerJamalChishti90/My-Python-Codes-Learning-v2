# Using Properties:
# Create a Car class with a private attribute __speed.
# Use a property decorator (@property and @speed.setter) to manage access to the speed.

class Car:
    def __init__(self):
        self.__speed = 0  # Private attribute

    @property
    def speed(self):
        """Get the current speed of the car."""
        return self.__speed

    @speed.setter
    def speed(self, value):
        """Set the speed of the car, ensuring it is not negative."""
        if value < 0:
            raise ValueError("Speed cannot be negative.")
        self.__speed = value
    
 
# Example usage:
my_car = Car()
my_car.speed = int(input("Enter your car speed here: "))  # Set speed
print(my_car.speed)  # Get speed, should print 50

# my_car.speed = -10  # This would raise a ValueError