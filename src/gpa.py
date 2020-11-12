import tkinter as tk


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
    aStudent = Student("Nayeli Fernandez",69,184)
    bStudent = Student("Paula Gomez",96,152)

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

    root = tk.Tk()
    root.title("GPA Calculator")

    data = ['Student Name','Student Quality Hours', 'Student Quality Points', 'GPA']
    for i,j in enumerate(data):
        tk.Label(root,text=f'{j}',bg="navy",fg="whitesmoke",font=('Verdana 17')).grid(row=i+1,column=0,sticky=tk.W)


    # myFunctionsA = ['aStudent.getName()','aStudent.getQualityHours()','aStudent.getQualityPoints()','aStudent.gpa()']
    # myFunctionsB = ['bStudent.getName()','bStudent.getQualityHours()','bStudent.getQualityPoints()','bStudent.gpa()']

    myDicta = {0:aStudent.getName(),1:aStudent.getQualityHours(),2:aStudent.getQualityPoints(),3:aStudent.gpa()}
    myDictb = {0:bStudent.getName(),1:bStudent.getQualityHours(),2:bStudent.getQualityPoints(),3:bStudent.gpa()}

    for i,j in  enumerate(myDicta.values()):
        tk.Label(root,text=f'{j}',bg="whitesmoke",fg="navy",font=('Helvetica 20')).grid(row=i+1,column=1,sticky=tk.W)

    # for i,j in  enumerate(myDictb.values()):
    #     tk.Label(root,text=f'{j}',bg="whitesmoke",fg="navy",font=('Helvetica 20')).grid(row=i+1,column=1,sticky=tk.W)
    
    root.mainloop()

main()
