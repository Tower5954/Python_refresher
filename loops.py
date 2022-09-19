number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("Well done, you guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it was wrong!")

# running the program until a condition is met
user_input = input("Would you like to play? (Y/n) ")

while user_input != "n":
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("Well done, you guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it was wrong!")

# ^ this ^ becomes almost an infinite loop until you error out
# v this v introduces a break within the loop

while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == 'n':
        break

    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("Well done, you guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it was wrong!")


friends = ["Rolf", "Jen", "Bob", "Anne"]
