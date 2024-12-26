class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @staticmethod
    def greet_student():
        print(f"Hello, Hope you are doing good!.")
        
    def student_info(self):
        print(f"Name: {self.name}, Score: {self.score}")


shaheer = Student('Shaheer', 90)
shaheer.greet_student()  
shaheer.student_info()