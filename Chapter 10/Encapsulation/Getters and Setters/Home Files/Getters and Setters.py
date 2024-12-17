#This is a very common and annoying way to access the attributes  

# class ToyBox:
#     def __init__(self):
#         self.toys = 0

#     def Get_Toys(self):
#         return f'I have {self.toys} in my Toy Box'

# shaheers_toybox = ToyBox()
# print(shaheers_toybox.Get_Toys()) #01: #The point comes here where I have to call the method by the help of Instance


#Instead of the above thing (#01) I can use a @Property (getter) to access the method like that
#So these are basically the getters and setters, lets see how they works
class ToyBox:
    def __init__(self):
        self.stoys = 0 #Basically setting the hardcoded value for this
         
    @property #Getter
    def toys(self):
        return f"I have {self.stoys} in my Box"
    
    @toys.setter #Setter
    def toys(self, value):
        if value > 100:
            return ("Woaa! Too many toys")
        else:
            self.stoys = value
            
shaheer = ToyBox()
shaheer.toys = 50
print(shaheer.toys) #as here i am just calling the Getter Method which is doing the same work for me!


        
        