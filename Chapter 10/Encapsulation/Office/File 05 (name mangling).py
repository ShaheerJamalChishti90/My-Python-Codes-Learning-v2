class Tree:
    def __init__(self, height: int):
        self.__height = height  # Private variable

tree = Tree(10)
# print(tree.__height)  # Raises AttributeError
print(tree._Tree__height)  # Can be accessed using name mangling
