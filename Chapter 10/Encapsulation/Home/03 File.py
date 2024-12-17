class Toybox: #Base class
    def __init__(self):
        self.public_toy = 'Super Hero' #Public Key
        self.__private_toy = 'Sex Doll' #Private Key

class MyToys(Toybox):
    def __init__(self):
        super().__init__()
        print("Here Im calling my Private Toy:")
        print(self.__private_toy)

obj_01 = Toybox()
print(obj_01.public_toy)
print(obj_01.__private_toy)

