# Write a program that asks the user to enter a person's name.
# The program should indicate whether a person is an infant, child, teenager, or adult.
# 12 Jun 2017
# CTI-110 M3HW1 -- Age Classifier
# Calvin Gill

# If a person is 1 year old or less, then the person is an infant.
# If a person is between 1 year old and 12 years old, then the person is a child.
# If a person is 13 years old and 19 years old, then the person is a teenager.
# If a person is 20 years old or older, then the person is an adult.

infant = 1
teenager = 13
adult = 20

age = int(input('Enter the age of the person in years: '))

if age >= adult:
    print('The person is an adult')
elif age >= teenager:
    print('The person is a teenager')
elif age > infant:
    print('The person is a child')
else:
    print('The person is an infant')



