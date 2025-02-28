# MAIN CHALLENGE (all that is needed to solve the problem):
# Separate the following program into atleast 2 separate modules

# TIPS:
# A third module is possible in order to neaten your code even further.
# The more Python practices you utilize, the more points you get.
# You can neaten up one of the functions to make your code even more easy to manage.

# THE ZEN OF PYTHON:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# # stores user's details
# user_profile = {}

# # creates user's profile (remember the "double asterix Arbitrary parameter" purpose (think about keys value pairings))
# def create_account(**profile):
    
#     # this is just making a relation to the above variable.
#     global user_profile
#     user_profile = profile

# # logs the user in
# def my_login():
#     logged_in = False

#     while logged_in != True:
#         print("Please Login:")

#         un = input("What is your Username: ")
#         pw = input("What is your Password: ")

#         if un == user_profile["username"] and pw == user_profile["password"]:
#             logged_in = True
#             print(f"Here is your profile:\n{user_profile}")
#         else:
#             print("False entry")

from user import create_account
from login import my_login

user_profile = create_account(
    username = input("What would you like your username to be: "),
    password = input("What would you like your password to be: "), 
    firstname = input("What is your first name: "),
    lastname = input("What is your last name: "),
    location = input("Where do you stay: ")
)

my_login(user_profile)