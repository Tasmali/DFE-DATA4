#An online retailer sells two products: widgets and gizmos. 
# Each widget weighs 75 grams. 
# Each gizmo weighs 112 grams. 
# Write a program that reads the number of widgets and the number of gizmos in an order from the user.
#  Then your program should compute and display the total weight of the order

gizmos = int(input ("Please enter the number of gizmos: "))
widgets = int(input("Please enter the number of widgets: "))
gizmoweight = gizmos*0.075
widgetweight = widgets*0.112
t_weight = gizmoweight + widgetweight
print (t_weight, "kg")