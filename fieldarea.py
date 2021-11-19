#Create a program that reads the length and width of a farmer’s field from the user in feet.
# Display the area of the field in acres.

length = float(input("Please enter the length of your field in feet: "))
width = float(input("Please enter the width of your field in feet: "))
areainacres = (length * width)/43560
print("The area of your field in acres is: ",areainacres)
