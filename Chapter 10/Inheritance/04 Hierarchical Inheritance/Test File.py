class Vehicle:
    def starts(self):
        print("Vehicle is staring!")

    def stop(self):
        print('Vehicle is stopping')

class Car(Vehicle):
    def honk(self):
        print("Car is honking!")

class Bike(Vehicle):
    def ring_bell(self):
        print("Bike bells ring!")

Toyota = Car()
Honda = Bike()

Toyota.starts()
Toyota.honk()
Toyota.stop()

Honda.ring_bell()



