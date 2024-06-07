import random

# we anticipate if user does not enter an integer
try:
    top_range = int(input("Type a number: "))
except ValueError:
     print("type in a number next time :)")
     quit()

#we create a loop where we keep asking user an int greater than 0
while True:
    if top_range <= 0:
        print("Please type a number greater than 0")
        top_range = int(input("Type a number:"))
    else:
        break

# assign a value to random number
random_number = random.randint(1,top_range)

# we keep track of all guesses made
guesses = 0

# create the gameplay loop
while True:
    # guesses tracker
    guesses += 1

    # user makes a guess
    user_guess = int(input(f"Guess the number - between 1 and {top_range} :  "))

    # we check if guess is correct or not
    if user_guess == random_number:
        print("Got it")
        break 

    # we indicate if it's below or above
    elif user_guess < random_number:
        print("you were below")
    else: 
        print("you were above")

    # we congratulate the user when they find it
print("You guessed in",guesses,"guesses. Nice")
