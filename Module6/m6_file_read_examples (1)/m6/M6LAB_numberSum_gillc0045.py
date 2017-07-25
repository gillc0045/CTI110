# M6LAB: Sum of Numbers
""" Requirements: 
      - program reads numbers from "numbers.txt"
      - and outputs a sum of the numbers."""
# Username: gillc0045
# Date: 7/5

def main():
    # read the contents of "number.txt"
    numbers = open("numbers.txt","r")
    
    # initialize an accumulator to get the sum of numbers
    numSum = 0

    print ('\n','This program adds the numbers in numbers.txt.')
    print ('\n','List of Numbers')
    print ('','---------------')

    #read and print out each number of numbers.txt
    for line in numbers:
        numerals = int(line)
        print ('\t',numerals)
        numSum += numerals
    numbers.close()
    
    print ('','---------------')
    print ('','Sum =','\t',numSum)
    
main()
