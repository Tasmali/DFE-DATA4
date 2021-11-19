#In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. 
# In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.
#Write a program that reads the number of containers of each size from the user.
#Your program should continue by computing and displaying the refund that will be received for returning those containers. 
#Format the output so that it includes a dollar sign and always displays exactly two decimal places

oneltrcontainers = float(input("Please enter the number of 1 litre or lower than 1 litre drink containers that you have: "))
oneplusltrcontainers = float(input("Please enter the number of drink containers with more than 1 litre capacity that you have: "))
refund = (oneltrcontainers * 0.10) + (oneplusltrcontainers* 0.25)
limited_refund = round(refund,2)
print ("Your refund is $",limited_refund)