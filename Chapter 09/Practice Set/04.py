# 4. A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file. 

para = '''
The donkey is a remarkable animal. 
Donkeys have been used for centuries as working animals. 
Unlike horses, donkeys are known for their strength and endurance. 
A donkey can carry heavy loads over long distances. 
Many people love their donkeys for their gentle nature. 
Donkeys also communicate with each other using braying sounds. 
If you take care of a donkey, it can become a loyal companion. 
The donkey has a unique place in many cultures, 
often symbolizing hard work and perseverance.


'''

with open("D:\\Visual Studio Codes\\Learning Python 2024 v2\\Chapter 09\\Practice Set\\Donkey.txt", "w") as file:
    updated_para = para.replace("Donkeys", "####").replace("donkey", '####')
    file.write(updated_para)


