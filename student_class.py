#In a new Python file, create a class of students.

#It should contain the following attributes: name, age, and class with default value "student".

#It should also contain a method which takes in 3 test scores and prints the students average test score.

class Student:

    def __init__(self, name, age, studentclass, test1, test2, test3): 
        self.name = name
        self.age = age
        self.studentclass = studentclass
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.student_avg = (test1+test2+test3)/3
       

student1 = Student("Jack", 10, 5, 20, 21, 22)
student2 = Student("Lucy", 11,5, 11, 14, 15)
print ("The average score for {student1} Jack is: {student1.student_avg}")
print ("The average score for {student2} is: {student2.student_avg}")






