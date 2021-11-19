#In the following example, assume we have a file called "filename.txt" which has 10 lines in it.
#We only want to keep the even lines, so discard the odd ones.



file= open ("filename.txt" ,"r")
outfile = ""
for line in range(1,10):
    if line%2 ==0:
        outfile+= file.readline()
    else:
        file.readline()

file = open("filename.txt", "w")
file.write(outfile)
file.close()


#Create a Python file which does the following:

#Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
#Reads and displays the names of the 1st and 4th team in the file.

file1 = open("filename.txt")
chars = file1.readlines()
teamlist =["Swish Kebabs", "The Hot Shots", "Big Net Worth", " BasketBrawlers", "HotShots"]
for i in teamlist:
    newline= "/n"
    chars.append (teamlist)
print(teamlist)


#Create a new Py.thon file which does the following:
#Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
#Print out the edited file line by line

file2 = open ("filename.txt")
chars = file2.readlines()
chars.insert(1, "This is a new line." )
print(chars)