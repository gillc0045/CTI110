# M6HW1 - Random Number File Writer
# A program to write random numbers into a file named "randomNumber.txt"
# gillc0045
# 7/5

import random
def main():
    # open a new file named "randomNumber.txt"
    randomNumber = open("randomNumber.txt","w")
    
    print ('\n','This program writes random numbers into randomNumber.txt')
    numberRange = int(input('How many random numbers do you want? ',))

    print ('\n','List of Random Numbers')
    print ('','----------------------')
    
    # randomNumber generator and writer
    for intervals in range (numberRange):
        number = random.randint (1, 500)
        randomNumber.write(str(number) + '\n')
        print('\t',number)
    randomNumber.close()

main()
