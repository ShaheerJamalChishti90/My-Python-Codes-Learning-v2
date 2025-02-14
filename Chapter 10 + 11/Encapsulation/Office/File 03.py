class Student:  # Base Class

    def __init__(self, name="Rajaram", marks=50):  # Constructor with default values
        self.__name = name  # Private attribute for the student's name
        self.__marks = marks  # Private attribute for the student's marks

    def studentdata(self):  # Method to display student information
        print(f"Name: {self.__name}, Marks: {self.__marks}")

# Creating instances of the Student class
s1 = Student()  # First Instance with default values
s2 = Student("Bharat", 25)  # Second Instance with specified values

# Accessing the information of the students using the method
s1.studentdata()  # Output: Name: Rajaram, Marks: 50
s2.studentdata()  # Output: Name: Bharat, Marks: 25

# Attempting to access the private variables directly, which will throw an error
# The following lines will raise an AttributeError because __name and __marks are private
print(f"Name: {s1.__name}, Marks: {s1.__marks}")  # This will throw an error
print(f"Name: {s2.__name}, Marks: {s2.__marks}")  # This will throw an error