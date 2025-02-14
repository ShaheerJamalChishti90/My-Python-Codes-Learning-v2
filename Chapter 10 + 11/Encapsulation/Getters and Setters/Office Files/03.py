class Product:
    def __init__(self):
        self.__products = [] 

    @property
    def get_products(self):
        return self.__products

    @get_products.setter
    def buy_products(self, product):
        self.__products.append(product)

imtiaz = Product()
imtiaz.buy_products = input("Enter the product you buy want to buy, eg:(apple mango vegetables meat bakery items): ")
print(f"This is the list of products you buy: {imtiaz.get_products}")