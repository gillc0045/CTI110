# Calvin Gill
# CTI-110 M2HW2 - Tip Tax Total 
# M2HW2_TipTaxTotal_gillc0045.py
#

costOfMeal = float( input( "Please enter the charge of the food: " ) )

Tip = 0.18 * costOfMeal

salesTax = 0.07 * costOfMeal

Total = costOfMeal + Tip + salesTax

print( "Food Charge: $" + format( costOfMeal, ",.2f"), "Tip: $" + \
       format( Tip, ",.2f" ), "Sales Tax: $" + format( salesTax, ",.2f"), \
       "Total: $" + format( Total, ",.2f"), sep = "\n" )

