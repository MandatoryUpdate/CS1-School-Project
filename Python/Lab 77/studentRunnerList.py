#If you have a Runner and class in different files, include in Runner:
from Students import *

def createData():
    name = ["Sarah","Tim","David"]
    grades = [12,9,11]
    subjects = ["Math", "Comp Sci I", "Biology"]

    students = []
    for i in range(3):
        students.append(Students(name[i], grades[i], subjects[i]))
    return students

def printAllStudents(students):
    for s in students:
        print(s)

def addNewStudents(students):
    students.append(Students("Ryan",11,"English III"))
    
#Main Program
studentData = []
studentData = createData() #Method to create the lists of objects
printAllStudents(studentData)
print()
addNewStudents(studentData)
studentData[1].setName("Thomas")
printAllStudents(studentData)
