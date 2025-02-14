# Using Properties:
# Create a Car class with a private attribute __speed.
# Use a property decorator (@property and @speed.setter) to manage access to the speed.

class Car:
    def __init__(self):
        self.__speed = 0
        
    @property
    def speed_of_Car(self):
        return f"Your Car speed is: {self.__speed}"

    @speed_of_Car.setter
    def speed_of_Car(self, value):
        # value = int(input("Enter the speed of your car: "))
        if value > 100:
            print("Speed is too high")
        else:
            self.__speed = value
            
tesla = Car()
tesla.speed_of_Car = int(input("Enter the speed of your Tesla: "))
        
        
        