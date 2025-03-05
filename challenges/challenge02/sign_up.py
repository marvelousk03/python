# from roles import janitor, programmer, secretory

# class SignUp:

#     def __init__(self):
#         self.first_name = input("What is your first name: ")
#         self.second_name = input("What is your last name: ")
#         self.email = input("What is your email: ")
        
#         roles = {
#             "Janitor": janitor,
#             "Programmer": programmer,
#             "Secretory": secretory
#         }

#         print("\nAvailable Positions:")
#         for role_name in roles:
#             print(f"- {role_name}")

#         while True:
#             chosen_role = input("Select your position: ").strip().title()
#             if chosen_role in roles:
#                 self.position = roles[chosen_role]
#                 break
#             else:
#                 print("Invalid choice. Please select a valid position.")



# from roles import roles

# class SignUp:
#     def __init__(self):
#         self.first_name = input("What is your first name: ")
#         self.second_name = input("What is your last name: ")
#         self.email = input("What is your email: ")

#         print("\nAvailable Positions:")
#         for role_name in roles:
#             print(f"- {role_name}")

#         while True:
#             chosen_role = input("Select your position: ").strip().title()
#             if chosen_role in roles:
#                 self.position = roles[chosen_role]
#                 break
#             else:
#                 print("Invalid choice. Please select a valid position.")

# Importing role instances directly
from roles import janitor_role as janitor, programmer_role as programmer, secretary_role as secretary, manager_role as manager, designer_role as designer

class SignUp:
    def __init__(self):
        self.first_name = input("What is your first name: ").strip().title()
        self.second_name = input("What is your last name: ").strip().title()
        self.email = input("What is your email: ")

        roles = {
            "Janitor": janitor,
            "Programmer": programmer,
            "Secretary": secretary,
            "Manager": manager,
            "Designer": designer
        }

        print("\nAvailable Positions:")
        for role_name in roles:
            print(f"- {role_name}")

        while True:
            chosen_role = input("Select your position: ").strip().title()
            if chosen_role in roles:
                self.position = roles[chosen_role]
                break
            else:
                print("Invalid choice. Please select a valid position.")
