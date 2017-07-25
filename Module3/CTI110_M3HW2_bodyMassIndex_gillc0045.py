# Write a program to calculate a person's body mass index (BMI).
# 12 Jun 2017
# CTI 110 - M3HW2 -- Body Mass Index
# Calvin Gill

weight = float(input("Enter the person's weight (pounds): "))
height = float(input("Enter the person's height (inches): "))
bmi = weight*(703/height**2)

print("The person's BMI value is ",bmi)

if bmi > 25:
    print('The person is overweight')
elif bmi < 18.5:
    print('The person is underweight')
else:
    print('The person is at optimal weight')
    
