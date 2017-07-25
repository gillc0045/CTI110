# m5 Module Use
# norrisa
# 7/5

# this file shows how you can import and use a function from
# a module you write yourself.
# Remember, any .py file is a module

# import the file (should be foo.py in the same directory)
import foo

def main():
    # call the method from the other module
    foo.hello()

    print('Done')





main()
