Inheritance
Importing class
Person.py
#!/usr/bin/python
class Person:
    def __init__(self,name,address,dob):
        self.__name = name
        self.__address = address
        self.__dob = dob
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getDOB(self):
        return self.__dob
    def updateAddress(self, address):
        self.__address = address

Student_management_system.py
#!/usr/bin/python
from Person import Person
       
class Student(Person):
    auto_roll_no = 1
    def __init__(self, name, address, dob, course, division):
        Person.__init__(self,name, address, dob)
        self.__roll_no = Student.auto_roll_no
        Student.auto_roll_no += 1
        self.__name = name
        self.__address = address
        self.__dob = dob
        self.__course = course
        self.__division = division
        self.__marks = dict()
    def getRollNo(self):
        return self.__roll_no
    def getName(self):
        return Person.getName(self)
    def getAddress(self):
        return Person.getAddress(self)
    def getDOB(self):
        return Person.getDOB(self)
    def getCourse(self):
        return self.__course
    def getDivision(self):
        return self.__division
    def getMarks(self):
        return self.__marks
    
    def updateMarks(self, subject, marks):
        self.__marks[subject] = marks
    def updateCourse(self, course):
        self.__course = course
    def updateDivision(self, division):
        self.__division = division
    def __repr__(self):
        return "Name:"+self.getName()+"\nAddress:"+self.getAddress()+"\nDOB:"+self.getDOB()+"\nRoll No:"+str(self.__roll_no)

#Homework : Implement Library Management System

Multiple inheritance with 2.7 and 3.X
import inspect
class A():		#use in 3.x directly
#class A(object):    #USE in 2.7
    def mMethod(self):
        print("In m of A")
    def kMethod(self):
        print("In k of A")

class B(A):
    def lMethod(self):
        print("in l of B")

class C(A):
    def nMethod(self):
        print("in n of C")
    def mMethod(self):
        print("in m of C")

class D(B,C):
    def bMethod(self):
        print("in b of D")
    def cMethod(self):
        print("in c of D")

def main():
    d = D()
    d.mMethod()
    d.cMethod()
    print(inspect.getmro(D))

if __name__=="__main__":
    main()

To mke object callable use __Call__(self)
class Simple:
    def __call__(self):
        print("Object Invoked")
        
s = Simple()
s()
# Static method calling (using decorators (@))
class Demo:
    @staticmethod
    def InvokeStatic():
        print("In static method call")
    @classmethod
    def InvokeClassMethod(cls):
        print("In class method: ",type(cls),id(cls))
    def InvokeObjectMethod(self):
        print("In object method: ")

print(id(Demo))
Demo.InvokeClassMethod()
Demo.InvokeStatic()
d= Demo()

Demo.InvokeObjectMethod(d)
d.InvokeStatic()
