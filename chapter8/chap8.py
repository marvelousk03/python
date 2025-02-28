# my_name = input("May I have your name please:")

# def my_function():
#     print(my_name)
    
# my_function()




# def my_name(user, age):
#     print(f"Welcome back {user}! It must be nice to be {age} years old...")
    
# my_name("Marvelous", 19)
# my_name(input("May I please have your name please: "), input("How old are you: "))
# my_name(input("May I please have your name please: "), input("How old are you: "))  


# def values(a, b):
#     return a, b 

# result = values(10, 20)
# print(result)  

# val1, val2 = values(30, 40)
# print(val1, val2)


# def user(first_name, last_name="Doe", age=None):
    
#     full_name = (f"{first_name} {last_name}")
    
    # if age:
    #     return (f"Name: {full_name}, Age: {age}")
    # else:
    #     return (f"Name: {full_name}, Age: Not provided")

# print(user.input())               
# print(user("Alice", "Smith", 25)) 
# print(user("Bob", {(age)})) 

# my_list = [1, 2, 3, 4, 5]
# copied_list = None

# def my_test(list):
#     copied_list = list.reverse()
#     return copied_list
#     print(list)
    
# my_test(my_list[:])

# print(my_list)
# print(copied_list)



# def my_pizza(*toppings):
#     print(f"Here is your {toppings} pizza.")
    
# my_pizza("Ham", "Cheese", "Pepperoni", "Pepper", "Pineapple")

# def test(*first, second):
#     print(f"these are my first arguments: {first}")
#     print(f"this aisre my other argument: {second}")

# test(1, 2, 3, 4, second = 5)


# def my_pizza(*toppings):
#     print("Making a pizza with:")
#     for topping in toppings:
#         print(f"- {topping}")

# my_pizza("pepperoni", "cheese", "olives")
# my_pizza("mushrooms", "onions")
# my_pizza("chesse")

# def build_profile(first, last, **user_info):

#   user_info['first_name'] = first



# def make_sandwich(*items):
#     print("\nMaking a sandwich with the following ingredients:")
#     for item in items:
#         print(f"- {item}")
#     print("Enjoy your sandwich!\n")

# make_sandwich("Turkey", "Lettuce", "Tomato", "Mayonnaise")
# make_sandwich("Ham", "Cheese")
# make_sandwich("Peanut Butter", "Jelly", "Banana", "Honey", "Cinnamon")



# def describe_pet(*animals):
#     for animal in animals:
#         print(f"I have a {animal}.")
# describe_pet("dog", "cat", "rabbit")

# def show(name, age):
#     print(name, age)

# data = {"name": "Alice", "age": 25}
# show(**data)

  
# def square():
#       return number ** 3
# result = square(6)
# print(result)

def greet(name):
    print(f"Hello, {name}!")
