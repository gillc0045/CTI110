# Question M3Q2A-M
# Calvin Gill
# 13 Jun 2017
#
# Request for the temperature of the water
temp = float(input('What is the temperature of the sample? '))

# If the sample is greater than 212 degrees its state of matter is gas
# If the sample is greater than 32 degrees its state of matter is liquid
# If the sample is less than 32 degrees its state of matter is solid

if temp >= 212:
    print('The state of matter of the sample is gas (steam)')
elif temp >= 32:
    print('The state of matter of the sample is liquid')
else:
    print('The state of matter of the sample is solid (ice)')
