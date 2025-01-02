class Student:
    grade = 12
    
    @classmethod
    def show_class(cls):
        print(f"This is the class of the student: {cls.grade}")

    @property
    def student_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @student_name.setter
    def student_name(self, name):
        self.first_name = name.split(" ")[0]
        self.last_name = name.split(" ")[1]


school_student = Student()
school_student.name = "John Doe"
school_student.show_class()  
print(f"The student name is {school_student.student_name}")

