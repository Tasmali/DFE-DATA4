#The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. 
#Then your program will compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing.
#Compute the tip as 18 percent of the meal amount (without the tax). 
#The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. 
#Format the output so that all of the values are displayed using two decimal places.

cost= float(input ("Enter the cost of your meal: "))

tax = round((cost * 0.20),2)
tip = round((cost * 0.18),2)
total = round((cost + tax + tip),2)
print ("Your tax amount is: ", "$", tax)
print ("Your tip amount is:", "$", tip)
print ("Your total is: ", "$", total)

