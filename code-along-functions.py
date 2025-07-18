# functions are reusable pieces of code !

print("hello!")
print("My name is python")


# have functions do one thing, helps modularity and troubleshooting. KISS
def greet(name):
    name = name.capitalize()
    print(f"Howdy, {name}! Hows it hanging, Good Buddy?")

def user_input(prompt):
    input_value = input(prompt)

greet("scoot")

def main_menu():
    print("Welcome to the main menu!")
    print("1. Start")
    print("2. Exit")
    choice = input("please choose an option: ")
    print(f"you chose option {choice}")

main_menu_choice = main_menu()

if main_menu_choice == 1:
    print("starting the program good buddy...")
else:
    print("exiting the program. goodbye suite prints")
