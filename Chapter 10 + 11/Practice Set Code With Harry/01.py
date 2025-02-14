# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
    def __init__(self, name, age, experience, language):
        self.name = name
        self.age = age
        self.experience = experience
        self.language = language
        
    def Programmer_Info(self):
        print(f"Name: {self.name}, Age: {self.age}, Experience: {self.experience}, Programming Language: {self.language}")


David = Programmer('David Larry', 30, '5 YoE', "Python")
David.Programmer_Info()
