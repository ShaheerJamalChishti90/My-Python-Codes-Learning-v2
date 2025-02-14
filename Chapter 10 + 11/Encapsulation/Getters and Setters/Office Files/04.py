class Girl:  #Just another simple class of Encapsulation Topic
    def __init__(self): 
        self.__name = '' #just some casual private arguments
        self.__age = 0

    def get_info(self):  #Just an old school getter method
        print(f"{self.__name} is {self.__age} years old")
    
    def set_name(self, name): #Just an old school setter method
        self.__name = name

    def set_age(self, age): #Another old school setter method
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age
        
    girls_info = property(get_info, set_name, set_age) #our lovely old school way of using the property function
        

girl = Girl()   #assigning the Instance arguments here 
girl.set_age(19)
girl.set_name("Lily")
girl.girls_info  #calling the property function


