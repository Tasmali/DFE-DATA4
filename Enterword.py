# Write a program that lets the user type words and when they press 'x', it prints how many words the user inputted then quits program.


count = 0
while True:
    word = input("Please enter a word. Then press x to quit: ")
    print (word)
    if word=="x":
        print ("You have entered %s words." %count)
        break
    else:
        count+=1
        

