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

    root = tk.Tk()
    root.title("GPA Calculator")

    tkLabel = tk.Label(root, text='Student Name',bg="navy",fg="whitesmoke",font=('Helvetica 22'))
    tkLabel.grid(row=0,column=0, sticky=tk.W)

    tkLabel1 = tk.Label(root, text='Student Quality Hours',bg="navy",fg="whitesmoke",font=('Helvetica 22'))
    tkLabel1.grid(row=1,column=0, sticky=tk.W)

    tkLabel2 = tk.Label(root, text='Student Quality Points',bg="navy",fg="whitesmoke",font=('Helvetica 22'))
    tkLabel2.grid(row=2,column=0, sticky=tk.W)
    
    tkLabel3 = tk.Label(root, text='GPA',bg="navy",fg="whitesmoke",font=('Helvetica 22'))
    tkLabel3.grid(row=3,column=0, sticky=tk.W)

    tkLabel4 = tk.Label(root, text=f"{bStudent.getName()}",bg="whitesmoke",fg="navy",font=('Arial 22'))
    tkLabel4.grid(row=0,column=1, sticky=tk.W)
    
    tkLabel5 = tk.Label(root, text=f"{bStudent.getQualityHours()}",bg="whitesmoke",fg="navy",font=('Arial 22'))
    tkLabel5.grid(row=1,column=1, sticky=tk.W)

    tkLabel6 = tk.Label(root, text=f"{bStudent.getQualityPoints()}",bg="whitesmoke",fg="navy",font=('Arial 22'))
    tkLabel6.grid(row=2,column=1, sticky=tk.W)

    tkLabel7 = tk.Label(root, text=f"{bStudent.gpa()}",bg="whitesmoke",fg="navy",font=('Arial 22'))
    tkLabel7.grid(row=3,column=1, sticky=tk.W)

    
    root.mainloop()

main()
