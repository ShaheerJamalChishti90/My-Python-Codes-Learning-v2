class ToyBox:
    def __init__(self):
        self.public_toy = "Teddy Bear"
        self.__private_toy = "Sex Doll"

    def Show_Toys(self):
        print(f'I have a {self.public_toy} in my Toy Treasure Box')
        print(f'I also have a {self.__private_toy} in my Toy Treasure Box, but its only for my use! (Private Product)')


Treasure_Box = ToyBox()
Treasure_Box.Show_Toys()


# print(Treasure_Box.__private_toy) #Its gonna raise an error