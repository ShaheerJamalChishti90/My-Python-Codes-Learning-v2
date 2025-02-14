# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 

class A:
    a = 'shaheer'


object = A()
object.a = '0' #By doing this I can change the class attribute


print(object.a) #Output = 0, Ans: Yes it can change the Class Attribute