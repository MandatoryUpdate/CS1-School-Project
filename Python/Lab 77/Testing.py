class Students:
    #Constructor
    def __init__(self, n, g, s):
        self.name = n
        self.grade = g
        self.subject = s
        self.attendance = True

    #Getters or Accessors
    def getName(self):
        return self.name

    def getSubject(self):
        return self.subject

    def getGrade(self):
        return self.grade

    #Setters or modifiers
    def setName(self, newName):
        self.name = newName

    def setSubject(self, newSubject):
        self.subject = newSubject

    def setGrade(self, newGrade):
        self.grade = newGrade

    #String method to print
    def __str__(self):
        return "Studen name is : "+self.name+", grade is: "+str(self.grade)+" and subject is: "+self.subject
