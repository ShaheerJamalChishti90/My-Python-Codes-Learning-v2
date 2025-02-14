# Create a class Temperature that encapsulates a temperature value in Celsius. Implement methods to convert the temperature to Fahrenheit and Kelvin, ensuring that the internal representation remains private.

class Temprature:
    def __init__(self, celcius):
        self.__celcius = celcius
        
    def celcius_to_farenhite(self):
        return (self.__celcius * 9/5) + 32
    
    def celcius_to_kelvin(self):
        return self.__celcius + 273.15
    
thermometer = Temprature(10)
print(thermometer.celcius_to_farenhite())  
print(thermometer.celcius_to_kelvin())  