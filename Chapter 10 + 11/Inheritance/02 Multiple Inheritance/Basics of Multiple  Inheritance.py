class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        
class Bike(Car):
    def __init__(self, model, color):
        super().__init__(model, color)
    
    def __str__(self):
        return f'I have a Bike, Its model is {self.model} and its in {self.color} color'
        
motorcycle = Bike("2025", "Red")
print(str(motorcycle))
