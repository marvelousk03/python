# favourite_books_series = ['the plated prisoner', 'the empyrean', 'throne of glass', 'ACOTAR']

# for book_series in favourite_books_series:
#     book_title = book_series.title()
#     print(f"This is one of my favourite books: {book_title}")
    
# for book_series in favourite_books_series:
#     print(f"This is one of my favourite books: {book_series.title()}")

# for number in range(1, 10):
#     print(number)
    
# numbers = range (2, 20)
# empty_list = []
# print(empty_list)

# for number in numbers: 
#     empty_list.append(number)  
#     # print(number) 
      
# print(empty_list)   
    
    
# my_list = ['item1', 'item2', 'item3', 'item4']
# my_tuple = ("one", "two", "three")

# my_list.reverse()
# print(my_list)


# # Creating a list of animals
# animals = ['Dog', 'Cat', 'Rabbit']

# # Printing each animal's name
# for animal in animals:
#     print(animal)

# # Printing a statement about each animal
# for animal in animals:
#     print(f"A {animal.lower()} would make a great pet.")

# # Printing what these animals have in common
# print("Any of these animals would make a great pet!")


# Creating a list of popular cities
cities = ['New York', 'Tokyo', 'Paris', 'Sydney', 'Berlin']

# # Printing each city
# print("Original cities:")
# for city in cities:
#     print(city)

# # # Modifying an item in the list
# cities[1] = 'London'

# # # Updating the list by changing some cities
# cities[3] = 'Dubai'

# # # Printing the updated list
# print("\nUpdated cities:")
# for city in cities:
#     print(city)

# # Using slices to print specific parts of the list
# print("\nThe first three cities in the list are:")
# print(cities[:3])

# print("\nThree cities from the middle of the list are:")
# print(cities[1:4])

# print("\nThe last three cities in the list are:")
# print(cities[-3:])



# # Creating a tuple of buffet foods
buffet_foods = ('Rice', 'Chicken', 'Salad', 'Soup', 'Bread')

# # Printing each food item
print("Original menu:")
for food in buffet_foods:
    print(food)

# # Trying to modify an item (this should cause an error)
# # buffet_foods[1] = 'Fish'  # Uncommenting this line will raise a TypeError

# # Updating the menu by redefining the tuple
buffet_foods = ('Rice', 'Fish', 'Salad', 'Pasta', 'Bread')

# # Printing the updated menu
print("\nUpdated menu:")
for food in buffet_foods:
    print(food)