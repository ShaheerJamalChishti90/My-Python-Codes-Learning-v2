class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def person_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Student(Person):
    def __init__(self, name, age, gender, student_id, grade):
        self.student_id = student_id
        self.grade = grade
        super().__init__(name, age, gender)
        
    def student_info(self):
        return f"{super().person_info()}, SID: {self.student_id} , Gr: {self.grade}"

class Teacher(Person):
    def __init__(self, name, age, gender, employee_id, subject):
        self.employee_id = employee_id
        self.subject = subject
        super().__init__(name, age, gender)
        
    def employee_info(self):
        return f"{super().person_info()}, EID: {self.employee_id} , Subject: {self.subject}"

class ClassRoom:
    def __init__(self, classroom_name):
        self.classroom_name = classroom_name
        self.students = []
        self.teachers = []
        
    def add_student(self, student):
        self.students.append(student)   
        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        
    def student_info(self):
        student_info = ", ".join([student.student_info() for student in self.students])
        return f'Student Info: {student_info}, Classroom: {self.classroom_name}'
    
    def teacher_info(self):
        teacher_info = ", ".join([teacher.employee_info() for teacher in self.teachers])
        return f'Teacher Info: {teacher_info}, Classroom: {self.classroom_name}'

student01 = Student("Shaheer", 18, "Male", 2006, 12)
teacher = Teacher("Mr. Smith", 30, "Male", "T001", "Mathematics")
classroom = ClassRoom("8A")
classroom.add_student(student01)
classroom.add_teacher(teacher)
print(teacher.employee_info())
print(classroom.student_info())
print(classroom.teacher_info())