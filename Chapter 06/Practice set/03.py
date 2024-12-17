# # A spam comment is defined as a text containing following keywords:
# # “Make a lot of money”, “buy now”, “subscribe this”, “click this”.
# #  Write a program to detect these spams.

# spam_comments  = ['make a lot of money', ' buy now', 'subscribe this', 'click this']

# user_comment = input("Enter your comment here: ")

# if any (user_comment) in (spam_comments):
#     print('Its a spam comment, prevent using such kind of words')

# elif user_comment == "buy now" or "Buy now":
#     print('Its a spam comment, prevent using such kind of words')

# elif user_comment == "subscribe this" or "Subscribe this":
#     print('Its a spam comment, prevent using such kind of words')

# elif user_comment == "click this" or "Click this":
#     print('Its a spam comment, prevent using such kind of words')

# else:
#     print(f" This is your comment: {user_comment}")



# GPT CORRECTED CODE:

user_comment = input("Enter your comment here: ").lower()

if "make a lot of money" in user_comment:
    print('It\'s a spam comment, prevent using such kind of words')

elif "buy now" in user_comment:
    print('It\'s a spam comment, prevent using such kind of words')

elif "subscribe this" in user_comment:
    print('It\'s a spam comment, prevent using such kind of words')

elif "click this" in user_comment:
    print('It\'s a spam comment, prevent using such kind of words')

else:
    print(f"This is your comment: {user_comment}")



# COPILOT CORRECTED CODE:

# spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# user_comment = input("Enter your comment here: ").lower()

# if any(keyword in user_comment for keyword in spam_keywords):
#     print('It\'s a spam comment, prevent using such kind of words')
# else:
#     print(f"This is your comment: {user_comment}")
