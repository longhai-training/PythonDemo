def greet_user(uname):
    print("Hello "+uname)

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

greet_user("young man")
describe_pet('hamster', 'harry')

def make_pizza(size, toppings): #概述要制作的比萨
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
for topping in toppings:
    print("- " + topping)


