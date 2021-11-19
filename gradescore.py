def gradescore (input1, input2, input3):
    totalscorepercentage= (input1 + input2 +input3)/175 *100
    return totalscorepercentage


stu = input("NAME")
hws = int (input("Homework: "))
ass = int (input ("Assessment"))
fin = int(input("FINAL EXAM: "))


returnpercentscore = gradescore(hws, ass, fin)
print(stu,returnpercentscore)