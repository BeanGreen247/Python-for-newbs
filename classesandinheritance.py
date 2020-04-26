class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def samplefunc(self):
        print("My name is "+ self.name + " and i am "+ str(self.age) + " years old.")

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.gratuationyear = year
    
    def studentfunc(self):
        print("I am going to gratuate in the year "+str(self.gratuationyear))
   
p1 = Person("John",36)
p2 = Person("Jack",25)
std = Student("Peter",20,2025)

p1.age = 45
p2.age = 50

p1.samplefunc()
p2.samplefunc()
std.samplefunc()
std.studentfunc()