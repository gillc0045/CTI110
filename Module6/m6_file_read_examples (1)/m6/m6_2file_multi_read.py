# m6 - file i/o
# norrisa
# 7/5

# open a file, read the contents one line at a time, close it

def main():


    # read the contents of "data1.txt" from the same directory
    myFile = open("data1.txt","r")

    for line in myFile:
        print(line)

    myFile.close()





main()
