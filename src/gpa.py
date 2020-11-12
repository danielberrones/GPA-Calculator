class Student:
    "Returns Student name, quality hours, quality points, and GPA."
    def __init__(self,name,qhours,qpoints):
        self.name=name
        self.qhours=qhours
        self.qpoints=qpoints
    def getName(self):
        return self.name
    def getQualityHours(self):
        return self.qhours
    def getQualityPoints(self):
        return self.qpoints
    def gpa(self):
        return round(self.qpoints/self.qhours,2)


def main():
    aStudent = Student("Mark Williams",33,84)
    bStudent = Student("Jeb Doe",66,150)

    # student A
    print(f"Student's Name: {aStudent.getName()}")
    print(f"Quality Hours:{aStudent.getQualityHours()}")
    print(f"Quality Points:{aStudent.getQualityPoints()}")
    print(f"GPA:{aStudent.gpa()}")
    
    # student B
    print(f"Student's Name: {bStudent.getName()}")
    print(f"Quality Hours:{bStudent.getQualityHours()}")
    print(f"Quality Points:{bStudent.getQualityPoints()}")
    print(f"GPA:{bStudent.gpa()}")


main()
