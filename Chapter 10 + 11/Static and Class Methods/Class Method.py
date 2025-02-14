# class Student:
#     grade = 10 #Class Attribute
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
        
        
#     def student_info(self):
#         print(f"Grade: {self.grade}\nName: {self.name}\nScore: {self.score}")


# shaheer = Student('Shaheer', 90) 
# shaheer.grade = 12   #I can change the class attribute here which is also gonna mess up in the method above 
# shaheer.student_info()

#To prevent the above problem we can use class method

class Student:
    grade = 10 #Class Attribute
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    @classmethod
    def student_info(cls):
        print(f"Grade: {cls.grade}")

    def student_inf(self):
        print(f"Name: {self.name}\nScore: {self.score}")

shaheer = Student('Shaheer', 90) 
shaheer.grade = 12  
shaheer.student_info()
shaheer.student_inf()