# M6T1 - program displaying all the numbers in numbers.txt
# gillc0045
# 7/5

# open a file, read the contents one line at a time, close it
# uses a while loop

def main():
    # read the contents of "numbers.txt" from the same directory
    myFile = open("numbers.txt","r")

    line = myFile.readline()
    while line != '':
        line = line.rstrip()
        print(line)
        line = myFile.readline()
    myFile.close()

main()
