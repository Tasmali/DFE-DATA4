
#precise temperature conversion
f = input ("Please enter the temperature in Fahrenheit: ")
f = (float(f)-32) * 5/9
print ("Your temperature in Celsius is: " , f)

#rounded off temperature conversion
f = input ("Please enter the temperature in Fahrenheit: ")
f = (round(float(f)-32) * 5/9,0)
print ("Your temperature in Celsius is: ", f )

#This program lets the user decide whether to convert from Celsius scale to Fahrenheit or vice versa

choice = ("Please enter 1 to convert Fahrenheit to Celsius or press 2 to convert Celsius to Fahrenheit")
temp = ("Please enter the temperature number that you would like to convert: ")

if float(choice) == 1:
    temp= float(temp)-32 * 5/9
    print ("Your temperature in Celsius is: %s." %temp)
elif float(choice) ==2:
    temp = float (temp)* 9/5 + 32
    print ("Your temperature in Fahrenheit is: %s." %temp)
else:
     print ("Please enter either 1 or 2")
    

