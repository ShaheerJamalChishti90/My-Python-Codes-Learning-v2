# Create a Person class with private attributes __name and __age.
# Add methods to set and get the values of these attributes.

class Person:
    def __init__(self):
        self.__name = ''
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_info(self):
        print(f"Im the private kid: My name is {self.__name} and my age is {self.__age}")

Child = Person()
Child.set_name('Shaheer')
Child.set_age(18)
Child.get_info()
