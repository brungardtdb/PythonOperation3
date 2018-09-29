'''****************************
Operation3.py
Author: David Brungardt

This program has the user guess a randomly generated
number. If the user guesses lower, the program will tell
them that their guess was too low, if the guess is too
high, the user will be prompted to guess a lower number.
*******************************'''
class Operation3:

    #declare and initialize variables
    userGuess = 0
    counter = 1

    #import new instance of random class
    import random

    #assign random number variable
    randNumber = random.randint(1,101)

    #introduce game
    print("Welcome to the Higher / Lower game!!! \nTry to guess a number between 1 and 100.")

    #begin number guessing game
    while (userGuess != randNumber):

        #prompt user to guess a number
        userGuess = int(input("Enter your guess: "))

        #if user guesses correctly
        if userGuess == randNumber:
            print("\nThe number was {}! You guessed correctly!".format(userGuess))
            print("It took you  {} tries.".format(counter))

        #if the user guesses a number that's too low
        elif userGuess < randNumber and userGuess > 0:
            print("\nThe number {} was too low, try again.".format(userGuess))
            counter += 1

        #if the user guesses a number that's too high
        elif userGuess > randNumber and userGuess < 101:
            print("\nThe number {} was too high, try again.".format(userGuess))
            counter += 1

        #if the user guesses a number that's out of range
        else:
            print("\nThe number {} was out of range.".format(userGuess))
            print("Please enter a number between 1 and 100")
