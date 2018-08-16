
# ================
# 12_while.py
# ================

# ==============================
# using while loop and random
# ==============================

# we will use this for loop as an example and then make a while loop
# code to do the same thing
# in for loop, if we don't initialize the initial i, python will
# give it the first number in the range

for i in range(10):
    print("i is now {}".format(i))

# now we will use a while loop to do same thing
# When using while, you must initialize the first i

print("="*20)
print("Using while loop")
i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1


# Using while to loop until a condition is met
# In this case, we want someone to choose the correct exit
# if they don't, they will be asked to choose until they get the
# correct answer.
# Note that you initialize chosenExit with "" so that it can ask
# the question when you start running the program

print("="*20)
availableExits = ["east", "north", "south"]
chosenExit = ""
while chosenExit not in availableExits:
    chosenExit = input("Please choose an exit: ")
print("Congrats. you choose available exit {}.".format(chosenExit))


# also note we have used else for the last print.
# NOTE: else is run when the while loop completes

print("="*20)
availableExits = ["east", "north", "south"]
chosenExit = ""
while chosenExit not in availableExits:
    chosenExit = input("Please choose and exit: ")
else:
    print("Congrats. you choose available exit {}.".format(chosenExit))


# an application for while loop like one above is when reading data
# from a file. The while loop can continue looping until there is
# no data in the file

# How to quit
# in above code, there is no way to get out of the loop unless you
# type the correct code.
# We can add some code to enable one to quit the code
# also note we have used else for the last print.
# NOTE: else is run when the while loop completes

print("="*20)
availableExits = ["east", "north", "south"]
chosenExit = ""
while chosenExit not in availableExits:
    chosenExit = input("Please choose and exit: ")
    if chosenExit == "quit":
        print("Game Over")
        break # This will break out of the game
else:
    print("Congrats. you choose available exit {}.".format(chosenExit))



# while loop challenge
# Modify the program below to use a while loop to allow as many
# guesses as necessary

# The program should let the player know whether to guess higher or
# lower and should print a message when the guess is correct.
# A correct guess will terminate the program

# For extra, allow the player to quit by entering 0 (zero) as their
# guess

# Original code using if/else/if
# This code gives you only two chances to guess
# import random to import built in program to generate random numbers

import random

print("="*20)
highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 0 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
        guess = int(input())
    else: # guess must be greater than number
        print("Please guess lower")
        guess = int(input())

    if guess == answer:
        print("Well done. {} is the correct answer".format(answer))
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("Got it first time. you're right. its {}".format(answer))




# Now we need to use while loop to give as many chances to guess
# as we like. Also if we type zero, it breaks out of loop
# Note: I did not initialize mine. so if you enter nothing
# we get an error


import random

print("="*20)
highest = 10
answer = random.randint(1, highest)
print("Please guess a number between 0 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:
        print("Game over. You typed {}".format(guess))
        break
    if guess < answer:
        guess = int(input("Please guess higher: "))
    else: # if the guess is higher
        guess = int(input("Please guess lower: "))


else:
    print("Got it. It is {}".format(answer))





# Trainers solution
# Even with initialization, this program crashes if you give it
# no input

import random
highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 0 and {}: ".format(highest))
guess = 0 # initialize to any number outside range 1 to 10

while guess != answer: # when starting, 0 is not answer
    guess = int(input()) # hence this will run first time
    if guess == 0:
        print("Game over. You typed {}".format(guess))
        break
    if guess < answer:
        print("Please guess higher: ")
    elif guess > answer: # if the guess is higher
        print("Please guess lower: ")
    else:
        print("Got it. It is {}".format(answer))


