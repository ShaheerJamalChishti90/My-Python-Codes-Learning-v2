class Institute:
    teacher = "Male"

    def __init__(self, name):
        self.name = name
        
#By using the format() method:
student = Institute('Harry')
print("Rodger is a {}".format(student.__class__.teacher))
print("Student's name is {}".format(student.name))


#By using the F-String:
print(f'Students names {student.name}')
print(f'{student.name} is a {Institute.teacher}')

