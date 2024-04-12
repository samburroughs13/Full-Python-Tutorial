def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")

greet_user("John", "Smith") # these are positional arguments
greet_user(last_name="Smith", first_name="John") # these are keyword arguments where you call out the parameter by name
#calc_cost(total=50, shipping=5, discount=0.1) #in a situation like this where you're passing numbers, keyword arguments might help
# keyword arguments must always come after positional arguments