# Write a program to find out whether a given post is talking about "Shaheer" or not

post = '''
With a calm demeanor and a thoughtful approach to life,
Shaheer effortlessly balances ambition with kindness,
making an impact on everyone around him. 
His ability to listen and understand others sets him apart, 
as he navigates challenges with a sense of purpose and empathy. 
A true leader in every sense, 
he inspires those around him not just through words 
but through actions that reflect integrity and dedication.'''.lower()

if  "shaheer" in post:
    print("This post is talking about shaheer")
else:
    print("This post is not talking about shaheer")


