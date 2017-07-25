# Program creates a random number guessing game.
# 27 Jun 2017
# CTI-110 M5HW2
# Calvin Gill

import random

def main():
    number = random.randint (1, 100)
    print('The number is ',number)
    guess = int(input('Go ahead! Guess the number? ',))
    print('My guess is ',guess)
    attempts = 0
    while guess != number:
        attempts += 1
        if guess > number:
            print("It's too high. Try again")
        else:
            print("It's too low. Try again")
        guess = guess_again(number)
    good_guess()
    
def guess_again(another_guess):
   another_guess = int(input('Go ahead! Try guessing the number? ',))
   return another_guess
    
def good_guess():
    print('Congratulations! You guessed the right number!')
    print("Alright, let's try another number.")
    main()
  
# Run main()
main()

