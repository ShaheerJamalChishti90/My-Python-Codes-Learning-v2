class Living_Being():
    def __init__(self, breath, eat):
        self.breath = breath
        self.eat = eat
    def info_LB(self):
        print(f"Living being can {self.breath} and {self.eat}")

class Human(Living_Being):
    def __init__(self, breath, eat, walk):
        self.walk = walk
        super().__init__(breath, eat)
    def info_H(self): 
        print(f"Human can {self.breath} {self.eat} and can {self.walk}")

class Boy(Human):
    def __init__(self, breath, eat, walk, play):
        self.play = play
        super().__init__(breath, eat, walk)
    def Info_Boy(self):
        return (f"Boy can {self.breath}, He can {self.eat}, He can {self.walk} and he can also have fun {self.play} with his friends")

little_boy = Boy("Breath fresh air", 'eat healthy food', "walk on two legs", "play Football" )
print(little_boy.Info_Boy())


#Black Box Ai Code: 

# Grandparent Class
class LivingBeing:
    def breathe(self):
        print("I can breathe!")

# Parent Class
class Human(LivingBeing):  # Human inherits from LivingBeing
    def speak(self):
        print("I can speak!")

# Child Class
class Kid(Human):  # Kid inherits from Human
    def play(self):
        print("I can play!")

# Now let's create a Kid object
my_kid = Kid()
my_kid.breathe()  # Inherited from LivingBeing
my_kid.speak()    # Inherited from Human
my_kid.play()     # Own method