from tkinter import *
from subprocess import call
from Admin import Admin

class Management_System:

    def __init__(self):
        self.root=Tk()
        self.root.title("FAST Management System")
        self.root.geometry("600x400")

        self.frame = Frame(self.root)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.52, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.Admin_Button = Button(self.frame,font="Times 10",text="Admin Login",command=self.Admin_obj)
        self.Admin_Button.place(relx=0.25, rely=0.1, height=47, width=289)

        self.Teacher_Button = Button(self.frame,font="Times 10",text="Teacher Login ",command=lambda:call(["python","Teacher.py"]))
        self.Teacher_Button.place(relx=0.25, rely=0.39, height=47, width=289)

        self.Student_button=Button(self.frame,text="Student Login",font="Times 10",command=lambda:call(["python","Student.py"]))
        self.Student_button.place(relx=0.25, rely=0.65, height=50, width=289)
        self.root.mainloop()

    def Admin_obj(self):
        obj=Admin()
        
if __name__ == '__main__':
    obj=Management_System()