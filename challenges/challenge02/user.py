# MAIN CHALLENGES:
# Create 2 more job positions to select from.
# Make a method that prints out the user instances' details.

# TIPS:
# Extra points if you show team synergy (get as many members to demo different sections)

# from sign_up import SignUp

# class User:

#     def __init__(self):
#         signup = SignUp()  
#         self.user_first_name = signup.first_name
#         self.user_second_name = signup.second_name
#         self.user_email = signup.email
#         self.user_position = signup.position 


from sign_up import SignUp as RegisterUser

class User:
    def __init__(self):
        signup = RegisterUser()
        self.user_first_name = signup.first_name
        self.user_second_name = signup.second_name
        self.user_email = signup.email
        self.user_position = signup.position

    def display_user_info(self):
        print("\nUser Details:")
        print(f"Name: {self.user_first_name} {self.user_second_name}")
        print(f"Email: {self.user_email}")
        print(f"Position: {self.user_position.position_name}")


user = User()
user.display_user_info()
