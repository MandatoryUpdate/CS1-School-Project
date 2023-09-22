# if you have a Runner and class in different files, include in runner:
from Students import *



student1 = Students("Sarah",12,"Math")
student2 = Students("Tom",9,"Comp Sci")
print(student1)
print(student2)
print()
print(student1.getName())
print()
student1.setName("Laura")
student2.setSubject("Biology")
print(student1)
print(student2)
