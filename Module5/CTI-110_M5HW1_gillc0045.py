# Program prompts for test scores; displays letter grades and average test score.
# 27 Jun 2017
# CTI-110 M5HW1
# Calvin Gill

def main():
    # The user must enter five test scores
    score1 = int(input('Enter first test score: ',))
    score2 = int(input('Enter second test score: ',))
    score3 = int(input('Enter third test score: ',))
    score4 = int(input('Enter fourth test score: ',))
    score5 = int(input('Enter fifth test score: ',))

    # Call a function to determine a letter grade for each test score
    grade1 = determine_grade(score1)
    grade2 = determine_grade(score2)
    grade3 = determine_grade(score3)
    grade4 = determine_grade(score4)
    grade5 = determine_grade(score5)
    
    # Print a table of the test scores and letter grades
    print('\n')
    print('Test Score',' ','Letter Grade')
    print('-------------------------')
    print('   ',score1,'\t','\t',grade1)
    print('   ',score2,'\t','\t',grade2)
    print('   ',score3,'\t','\t',grade3)
    print('   ',score4,'\t','\t',grade4)
    print('   ',score5,'\t','\t',grade5)

    # Call functions to: calculate average test score; & determine average grade
    avg_score = calc_average(score1,score2,score3,score4,score5)
    avg_grade = determine_grade(avg_score)
    print('-------------------------')
    print('Avg Score','   ','Avg Grade')
    print('   ',avg_score,'\t',avg_grade)
    print('-------------------------')

# Function to determine the letter grade of a score
def determine_grade(score):
    if score > 89:
        letter_grade = 'A'
    elif score > 79:
        letter_grade = 'B'
    elif score > 69:
        letter_grade = 'C'
    elif score > 59:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return(letter_grade)

# Function to calculate the average of test scores
def calc_average(s1,s2,s3,s4,s5): 
   average = (s1+s2+s3+s4+s5)/5
   return (average)

# Run main()
main()
