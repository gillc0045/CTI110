# m6 - file i/o
# norrisa
# 7/5

# open a file, read one line, print that line, close the file

def main():


    # read the contents of "data1.txt" from the same directory
    myFile = open("data1.txt","r")

    line = myFile.readline()
    print(line)

    myFile.close()





main()
