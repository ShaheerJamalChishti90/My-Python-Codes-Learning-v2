class Father:
    def __init__(self):
        self.a = "Shaheer Jamal Chishti"
        self.__c = "ShaheerJamalChishti"

class Son(Father):
    def __init__(self):
        # super().__init__()
        Father.__init__(self)
        print('Lets call the private membre of the Fathers Class')
        print(self.__c)


David = Father()
print(David.a)






        