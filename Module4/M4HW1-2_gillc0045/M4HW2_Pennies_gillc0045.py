# Program calculating the amount of pay a person earns over a period of time
# 15 Jun 2017
# CTI-110 M4HW2
# Calvin Gill

# Program prompts for a period of time in numbers of WorkDays.
WorkDays = int(input('How many days will you work? ', ))

# A table displays Pay earned per Day.
print(' ')
print('\t','Day\tPay')
print('\t','-----\t--------------')

# The table also displays TotalPay earned during WorkDays.
TotalPay = 0

# Pay begins with 1 penny on Day 1.
Day = 0

# Pay increases by double on each successive Day.
for Pay in range(Day,WorkDays): 
    Pay = 2**Day                # Pay is in cents value.
    DollarValue = Pay/100       # Pay converted to DollarValue.
    Day = Day + 1
    TotalPay = TotalPay + DollarValue
    print('\t',Day,'\t$',DollarValue)
    
# TotalPay is the sum of Pay earned per Day.
print('\t\t','_______________')
print('\t\t',' Total Pay')
print('\t\t$',TotalPay)
