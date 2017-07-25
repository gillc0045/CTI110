# Program prompts for a Km distance and converts it to miles.
# 26 Jun 2017
# CTI-110 M5T1
# Calvin Gill

def main():
    Km_to_miles()

def Km_to_miles():
    Km_to_miles = int(input('Enter distance in kilometers: ',))
    miles = Km_to_miles*0.6214
    print('The value of ',Km_to_miles,' kilometers converts to ',miles,' miles')
main()
