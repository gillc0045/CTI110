 # Calvin Gill
# CTI 110
# M3LAB: Debugging

# Grade List
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Input the score
score = int(input('Enter the score: '))

if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
