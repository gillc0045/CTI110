# The program keeps a running tally of bugs collected daily and outputs a total
# 15 Jun 2017
# CTI-110 M4T1
# Calvin Gill
#
total = 0
for day in range (1, 6):
    bugs = int(input('How many bugs did you collect today?', ))
    print('You have collected ',bugs,' today')
    total = total + bugs

print('You have collected ',total,' bugs in five days')

