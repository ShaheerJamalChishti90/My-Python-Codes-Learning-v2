# Write a program to detect double space in a string

string = "This  is testing string written by Muhammad  Shaheer  Jamal  Chishti."
print(len(string), string.count("  "), string.count("Shaheer"))

#Q3: Replacing the double spaces from Q2 with single spaces.
print(string.replace("  ", " "))



#Q4: using escape sequence characters 
letter = "Dear Shaheer,\n this python course is nice.\n Thanks!"
print(letter)
