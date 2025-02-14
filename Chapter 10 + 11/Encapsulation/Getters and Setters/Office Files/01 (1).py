class Person: #Base Class
    def __init__(self):
        self.__name = ''  #making a private attribute so that no one can access it directly

    def get_name(self):  #Returning(getting) the private attribute in this method 
        return self.__name

    def set_name(self, name): #Assigning(setting) the name to that private attribute in this method
        self.__name = name
        
shaheer = Person()   #Making an Instance/Object of the class   
shaheer.set_name('Shaheer Jamal Chishti')   #setting the name
print(shaheer.get_name())   #Getting the name