# common_errors_in_python

# 1. SyntaxError: yeh error tab aata hai jab code ka structure ghalat ho
# eg: colon (:) na lagana function ya loop ke end pe

# Ghalat code:
# def my_func()
#     print("Hello")

# Theek code:
def my_func():
    print("Hello")  # sahi tariqa se function define kiya gaya hai

# 2. IndentationError: jab aap code ki proper indentation (space/tab) follow nahi karte
# Python whitespace pe depend karta hai
# Ghalat code:
# if 5 > 3:
# print("5 is greater")

# Theek code:
if 5 > 3:
    print("5 is greater")  # ye block properly indented hai

# 3. NameError: jab koi variable use karein jo pehly define nahi hua ho
# Ghalat code:
# print(x)

# Theek code:
x = 10
print(x)  # ab koi error nahi aayega kyun ke x define ho chuka hai

# 4. TypeError: jab data types ghalat mix ho jaayein
# eg: integer + string
# Ghalat code:
# num = 5 + "5"

# Theek code:
num = 5 + int("5")  # string ko pehle int mein convert kiya hai

# 5. ValueError: jab conversion valid data pe na ho
# Ghalat code:
# int("abc")  # yeh integer mein convert nahi ho sakta

# Theek code:
a = "123"
print(int(a))  # yeh sahi hai kyunki "123" valid integer hai

# 6. ZeroDivisionError: jab kisi number ko 0 se divide karein
# Ghalat code:
result = 10 / 0
print(result)  # yeh error dega

# 7. IndexError: jab list ke valid range se bahar index access karein
my_list = [1, 2, 3]
# print(my_list[5])  # yeh galti karega

# Theek code:
if len(my_list) > 2:
    print(my_list[2])  # valid index access ho raha hai

# 8. AttributeError: jab object mein wo attribute nahi hota jo aap call kar rahe ho
# Ghalat code:
# x = 5
# x.append(3)  # int mein append nahi hota

# Theek code:
y = [1, 2]
y.append(3)  # list mein append method hota hai

# 9. ImportError: jab module exist nahi karta ya naam ghalat likha ho
# Ghalat code:
# import maths

# Theek code:
import math  # sahi module ka naam

# 10. KeyboardInterrupt: jab user program ko manually rokta hai (Ctrl+C)
# Isay usually handle nahi karte beginners, lekin handle karna acha practice hai
try:
    while True:
        pass  # infinite loop
except KeyboardInterrupt:
    print("User ne program stop kiya")

# Note:
# Har error ko samajhna zaroori hai, taki aap debugging mein expert ban sakein.
# Yeh basic examples hain, lekin real code mein inka asar kaafi zyada hota hai.

