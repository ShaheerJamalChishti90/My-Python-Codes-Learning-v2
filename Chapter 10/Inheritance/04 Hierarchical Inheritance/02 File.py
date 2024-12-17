class Grandfather:
    def Books(self):
        print ("Books at Grandfather's time")

class Father(Grandfather):
    def Books(self):
        print ("Books at Father's time")

    def Phone(self):
        print ("Phone at Father's time")
        
        
        
class Kid1(Father):
    def Phone(self):
        print ("Phone at Son's time")

    def Gaming_Console(self):
        print ("Gaming Console at Son's time")    


class Kid2(Father):
    def Phone(self):
        print ("Phone at daughter's time")        

    def Smart_Tv(self):
        print ("Smart Tvs at daughter's time")
    
class Step_Mother(Grandfather):
    def Books(self):
        print ("Books at Mother's time")

    def Phone(self):
        print ("Phone at Mother's time")



David_Michell = Grandfather()
Larry_Michell = Father()
Sarah_Larry_Michell = Step_Mother()
Sean_Michell = Kid1()
Jenny_Michell = Kid2()

David_Michell.Books()

Larry_Michell.Books()
Larry_Michell.Phone()

Sean_Michell.Gaming_Console()
Sean_Michell.Books()
Sean_Michell.Phone()

Jenny_Michell.Phone()
Jenny_Michell.Books()
Jenny_Michell.Smart_Tv()