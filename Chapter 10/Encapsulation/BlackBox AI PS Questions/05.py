# Design a class User that has private attributes for username and password. Implement methods to change the password, ensuring that the new password meets certain criteria (e.g., minimum length).

#Did it all myself without the help of AI


#making a class and taking empty private attributes
class User:
    def __init__(self):
        self.__username = ""
        self.__password = ""
        
    #Using getter and setter decorators to change and get the new changed username
    @property
    def username(self):
        return self.__username
        
    @username.setter
    def username(self, name):
        # name = input("Enter your new username here: ")
        if len(name) < 3:
            raise ValueError("Username cant be under the 3 character!")
        else:
            self.__username = name
            
    #Defining a custom method to set a new username
    def change_password(self):
        while True:   
            pswd = input("Enter the new pswd here: ")
            if len(pswd) < 8:
                print("Password must be at least 8 characters long.")
            else:
                self.__password = pswd
                print("Changed Successfully!")
                break
            
    
    #Definig a custom method again this time to get the user credentials            
    def get_the_credentials(self, user_choice):
        while True:
            if user_choice == 1:
                print(f'User: {self.__username}\nPassword: {self.__password}')
                break
            if user_choice == 2:
                break


account = User()
account.username = name = input("Enter your new username here: ")
account.change_password()
print(f"=================================\n1. Show Credentials\n2. Exit")
uc = int(input("Enter your choice here: "))
account.get_the_credentials(uc)
                
        
    