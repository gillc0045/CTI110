# M6HW2 - Random Number File Reader
# A program to read the numbers from the file "randomNumber.txt"
# gillc0045
# 7/5

def main():
    # read the contents of "randomNumber.txt"
    randomNumber = open("randomNumber.txt","r")

    # initialize an accumulator to get the sum of the numerals in the file
    numeralTotal = 0

    # initialize an accumulator to count the number of numerals in the file
    numeralCount = 0

    print ('\n','This program totals the numbers in randomNumber.txt.')
    print ('\n','List of Random Numbers')
    print ('','----------------------')

    #read each line of numerals in the file and print them out
    for line in randomNumber:
        numeral = int(line)
        print ('\t',numeral)
        numeralTotal += numeral
        numeralCount += 1
    randomNumber.close()
    
    print ('','----------------------')
    print ('','Total =',numeralTotal)
    print ('\n','The randomNumber.txt file has',numeralCount,'numerals within it.')
    
main()
