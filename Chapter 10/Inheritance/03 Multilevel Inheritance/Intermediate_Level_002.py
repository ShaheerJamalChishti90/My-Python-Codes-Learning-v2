# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Student Class
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def info(self):
        return f"{super().info()}, Student ID: {self.student_id}, Grade: {self.grade}"

# Teacher Class
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def info(self):
        return f"{super().info()}, Employee ID: {self.employee_id}, Subject: {self.subject}"

# Classroom Class
class Classroom(Student):
    def __init__(self, name, age, student_id, grade, classroom_name):
        super().__init__(name, age, student_id, grade)
        self.classroom_name = classroom_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def info(self):
        student_info = ', '.join([student.info() for student in self.students])
        return f"Classroom: {self.classroom_name}, Students: [{student_info}]"

# Example Usage
# Create some students
student1 = Student("Alice", 14, "S001", "8th Grade")
student2 = Student("Bob", 15, "S002", "9th Grade")

# Create a teacher
teacher = Teacher("Mr. Smith", 30, "T001", "Mathematics")

# Create a classroom and add students
classroom = Classroom("Alice", 14, "S001", "8th Grade", "8A")
classroom.add_student(student1)
classroom.add_student(student2)

# Print information
print(teacher.info())
print(classroom.info())