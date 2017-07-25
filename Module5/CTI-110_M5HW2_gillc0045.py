# Program creates a random number guessing game.
# 27 Jun 2017
# CTI-110 M5HW2
# Calvin Gill

import random

def main():
    secret_number = random.randint (1, 100)
    # Printing secret_number is for testing purposes only
    # print('The secret number is ',secret_number)
    guess = int(input('\nGo ahead! Try guessing the number? ',))
    print('\nYour guess is ',guess)
    attempts = 1
    while guess != secret_number:
        attempts += 1             # Keeps track of number of attempts
        if guess > secret_number: # Compares the guess to secret_number
            print("\nIt's too high. Try again")
        else:
            print("\nIt's too low. Try again")
        guess = guess_again(secret_number)
    print('\nWow! It only took you ',attempts,' times to get it.')
    good_guess()
    
# Restarts the guessing process
def guess_again(another_guess):
   another_guess = int(input('Come on! Guess again! ',))
   print('\nYour guess is ',another_guess)
   return another_guess
    
# Restarts the game
def good_guess():
    print('Congratulations! You guessed the right number!')
    print("Alright, let's try another number.")
    main()
  
# Run main()
main()

