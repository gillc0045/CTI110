# Program prompts for a distance in feet and converts it to inches.
# 26 Jun 2017
# CTI-110 M5T2
# Calvin Gill

def main():
    feet_to_inches()

def feet_to_inches():
    feet_to_inches = int(input('Enter distance in feet: ',))
    inches = feet_to_inches*12
    print('The value of ',feet_to_inches,' feet converts to ',inches,' inches')
main()
