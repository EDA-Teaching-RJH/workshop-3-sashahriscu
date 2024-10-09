import random

# generates a random number
secret_number = random.randint(1, 10)
# ask user for integer input
guessed_number = int(input("Guess a number between 1 and 10 "))

# assure the number guessing game only works when numbers between 1 and 10 are chosen
if guessed_number < 1 or guessed_number > 10:
    print("Invalid: number must be between the range of 1 to 10.")
# when generated number is higher than user's guess
elif secret_number > guessed_number:
    print("Too high")
# when generated number is lower than user's guess
elif secret_number < guessed_number:
    print("Too low")
# when generated number is equal to user's guess
elif secret_number==guessed_number:
    print("Correct")