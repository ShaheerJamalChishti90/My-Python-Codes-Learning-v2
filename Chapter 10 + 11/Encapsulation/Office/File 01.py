class ToyBox:
    def __init__(self):
        self._toys = []  # Private list of toys

    def add_toy(self, toy):
        self._toys.append(toy)  # Public method to add a toy

    def show_toys(self):
        return self._toys  # Public method to show toys

# Using the ToyBox
my_toy_box = ToyBox()
my_toy_box.add_toy("Teddy Bear")
print(my_toy_box.show_toys())  # Output: ['Teddy Bear']