class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating three different instances of Restaurant
restaurant1 = Restaurant("The Gourmet Bistro", "French")
restaurant2 = Restaurant("Sushi Paradise", "Japanese")
restaurant3 = Restaurant("Pasta Heaven", "Italian")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()




class User:
    def __init__(self, first_name, last_name, location):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
    
    def describe_user(self):
        print(f"\tName: {self.first_name} {self.last_name}")
        print(f"\tLocation: {self.location}")
    
    def greet_user(self):
        print(f"\tHello, {self.first_name} {self.last_name}! Welcome back!")

# Creating several instances of User
user1 = User("Ethan", "Hurwitz", "Joburg")
user2 = User("Ronny", "Mputla", "Joburg")
user3 = User("Pierre", "Kahunda", "Joburg")

# Calling both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()