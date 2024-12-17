# Write a python program using function to convert Celsius to Fahrenheit.
# Method 01
# def converter(farenheit):
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C = {fahrenheit}°F")
# converter()

# def converter():
#     celsius = float(input("Enter temperature in Celsius: "))
#     kelvin = celsius + 273.15
#     print(f"{celsius}°C = {kelvin}K")
# converter()

# Method 02
# celsius = float(input("Enter temperature in Celsius: "))

# def converter(celcius):
#     fahrenheit = (celcius * 9/5) + 32
#     return fahrenheit
# print(f"{celsius}°C = {converter(celsius)}°F")  



# Making a converter which converts the temperature according to user command:
# My Code, worked perfectly fine in the FIRST GO!!
user_input = input("Convert Celcius to Kelvin or Farenheit: ").capitalize()

def converter_farenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
# converter_farenheit()


def converter_kelvin():
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = celsius + 273.15
    print(f"{celsius}°C = {kelvin}K")
# converter_kelvin()

if user_input == 'Kelvin':
    (converter_kelvin())
elif user_input == 'Farenheit':
    (converter_farenheit())
else:
    print("Invalid input")


# GPT CODE: simple and easy to understand

# def converter_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def converter_kelvin(celsius):
#     return celsius + 273.15

# def main():
#     user_input = input("Convert Celsius to Kelvin or Fahrenheit: ").capitalize()
#     celsius = float(input("Enter temperature in Celsius: "))

#     if user_input == 'Kelvin':
#         kelvin = converter_kelvin(celsius)
#         print(f"{celsius}°C = {kelvin}K")
#     elif user_input == 'Fahrenheit':
#         fahrenheit = converter_fahrenheit(celsius)
#         print(f"{celsius}°C = {fahrenheit}°F")
#     else:
#         print("Invalid input")

# main()
