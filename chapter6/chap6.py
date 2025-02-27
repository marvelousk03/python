# my_person = {
#     "name": "Marvelous",
#     "age": 19,
#     "language": "English"
# }
# print(my_person)

# my_person["gender"] = "Female"
# print(my_person)

# my_person["age"] = "20"
# print(my_person)
# print(my_person["language"])


# favourite_foods = {
#     "Ethan": "Pizza",
#     "Ronny": "Italian Bread",
#     "Pierre": "Chicken Nuggets",
#     "Marvelous": "Noddles"
# }
# favourite_foods["David"] = "Carrot Cake"

# for names, food in favourite_foods.items():
#     print (f"\t{names}'s favourite food is {food}")
    
# if "Sandra" not in favourite_foods.keys():
#     print("\tSorry cant take it now that list has been sent.")
    

# avengers_404 = {
#     "Ethan": "Mac",
#     "Marvelous": "Asus",
#     "Pierre": 'Lenovo',
#     "Ronny": "Asus"
# }

# for class_mate, brand in avengers_404.items():
#     if brand == "Mac":
#         print(f"{class_mate} uses {brand} the apple guy.")
#     elif brand == "Asus":
#         print(f"{class_mate} uses {brand}, I heard it's a good brand.")
#     elif brand == 'Lenovo':
#         print(f"{class_mate} uses {brand}, you got something unique.")
#     elif brand == "Asus":
#         print(f"{class_mate} uses {brand}, is a copy cat.")  
        
dad = {
    "name": "Moses",
    "age": 45,
    "passtime": "Sports"
}         

mom = {
    "name": "Jeanne",
    "age": 43,
    "passtime": "sewing"
}

sibling = {
    "name": "Pierre",
    "age": 18,
    "passtime": "Watching Anime"
}

family = [dad, mom, sibling]

best_friend = {
    "name": "Kelly",
    "age": 20,
    "passtime": "Content Creation"
}

family.append(best_friend)
print(family)



