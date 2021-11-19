class Dog:


    energy = "high" #defining variable

    def _init_(self,inputenergy):
        self.energy = inputenergy

    def speak(self): #function inside a class
        
        print (self.energy)
        print("Woof")

       

havoc = Dog("high")

havoc.speak()
print (havoc.energy)

clifford = Dog("large") #clifford is the object here

clifford.speak()
clifford.energy = "large"
print (clifford.energy)

scooby = Dog()
scooby.speak()
scooby.energy = "scared"

snoopy = Dog()
snoopy.speak()
snoopy.energy = "Fighting the red baron"

scooby.speak()
