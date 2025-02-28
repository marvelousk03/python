# from user import user_profile

# # logs the user in
# def my_login(user_profile):
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


def my_login(user_profile): 
    while True:
        print("\nPlease Login:")
        un = input("Username: ")
        pw = input("Password: ")

        if un == user_profile.get("username") and pw == user_profile.get("password"):
            print("\nLogin successful! Here is your profile:")
            for key, value in user_profile.items():
                print(f"{key.capitalize()}: {value}")
            break
        else:
            print("Incorrect username or password. Please try again.")
