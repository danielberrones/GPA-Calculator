class Student:
    def __init__(self,name,qHours,qPoints):
        self.name = name
        self.qHours = qHours
        self.qPoints = qPoints
    def getName(self):
        return self.name
    def getQualityHours(self):
        return self.qHours
    def getQualityPoints(self):
        return self.qPoints
    def gpa(self):
        return self.qPoints/self.qHours
    def returnAll(self):
        return self.name + " " + str(self.qPoints) + " " + str(self.qHours) + " " + str(self.qPoints/self.qHours)
        # return self.qPoints
        # return self.qHours
        # return self.qPoints/self.qHours



aStudent = Student("John Doe", 125, 180)

# print(aStudent.gpa())
# userName, userHours, userPoints = input("Enter name, quality hours, quality points").split()
# myStudent = Student(userName,userName,userPoints)
print(aStudent.returnAll())

