class Person:
    def __init__(self):
        self.__name = ""

    @property  #This is a getter, basically from here we can get our value or our data, we can simply just access the getter like a method 
    def get_info(self):
        """From here we are basically getting the information of the Person"""
        return self.__name

    @get_info.setter #This is a setter, basically from here we can set the information of the Person
    def set_info(self, name):
        """Here we are basically setting the information of the Person"""
        self.__name = name
        
person = Person()
person.set_info = "John"
print(f"Hey Im {person.get_info}, Im 5 years old, Ty.")