# This final example includes complex exception handling
# from the end of Chapter 6. Don't start here!
# However, this may be useful to you as an example of
# handling multiple types of exceptions
#
# No data file is included -- you will need to make your own.

def main():
    try:
        file = open("data.txt")
        for line in file:
            #print (line)
            value = line.rstrip("\n")
            value = int(value)
            print (value)
        print("END OF FILE")
        file.close()

    except FileNotFoundError as err:
        print("Error -- ",err)
        print("Please contact support.")

    except ValueError as err:
        print("Bad data!")
        print(err)


    # program continues from here







# start
main()
