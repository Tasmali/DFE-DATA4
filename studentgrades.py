#Asks for the homework grade and returns it
def get_hmk_grade ():
    hmk= False
    while hmk == False:
        hmk = input ("Enter your HMK grade: ")
        if hmk.isdigit() == True:
            hmk = int(hmk)
            if hmk >=0 and hmk<=25:
                return hmk
            else:
                print ("Please enter a valid number: ")    
                hmk = False
        else:
            print ("Please enter a valid number")
            hmk = False

#Asks for the assessment grade and returns it
def get_assessment_grade():
    asess = False
    while asess == False:
        asess = input ("Enter your assessment grade: ")
        if asess.isdigit() == True:
            asess = int(asess)
            if asess >= 0 and asess <= 50:
                return asess
            else:
                print ("Please enter a valid number")
                asess = False
        else:
            print ("Please enter a valid number")
            asess = False



# Asks for the final exam grade and returns it     
def get_final_grade():
    final_grade = False
    while final_grade == False:
        final_grade = input ("Enter your final grade: ")
        if final_grade.isdigit() == True:
            final_grade = int (final_grade)
            if final_grade>=0 and final_grade <= 100:
                return final_grade
            else:
                print ("Please enter a valid number")
                final_grade = False
        else:
            print ("Please enter a valid number")
            final_grade = False



hmk_grade = get_hmk_grade()
assessment_grade = get_assessment_grade()
final_exam_grade = get_final_grade()



def return_grade_as_percentage (hmk_grade, assessment_grade, final_exam_grade):
    total_grade = int(hmk_grade) + int(assessment_grade) + int(final_exam_grade)
    print ("Total grade is: ", total_grade)
    percentage = (total_grade / 175) * 100
    print ("Total percentage is: ", "%.2f" %percentage)
    return percentage
 
 
def return_grade_as_letter(percentage):
    if percentage >= 90:
        print ("Grade is A")
    elif percentage >= 80:
        print ("Grade is B")
    elif percentage >= 70:
        print ("Grade is C")
    elif percentage >= 60:
        print ("Grade is D")
    elif percentage >= 50:
        print ("Grade is E")
    else:
        print ("Grade is F")
 
 
return_grade_as_letter(return_grade_as_percentage(hmk_grade, assessment_grade, final_exam_grade))