# 4. Add a static method in problem 2, to greet the user with hello. 


class WelcomeMessage:
    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def welcome():
        print(f"Hello, welcome to ShaheerTechGroup!")

employee = WelcomeMessage('David')
employee.welcome()
print(employee.name, 'You will be assigned with a Job role shortly!')

