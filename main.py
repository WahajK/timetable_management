from tkinter import *
from subprocess import call
from Project import Admin
class Management_System:

    def __init__(self):
        self.name=""
        self.password=""
        self.root=Tk()
        self.root.title("FAST Management System")
        self.root.geometry("600x400")

        self.frame = Frame(self.root)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.52, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.username_label = Label(self.frame)
        self.username_label.place(relx=0.05, rely=0.03, height=47, width=289)
        self.username_label.configure(text="Username: ")

        self.username_entry=Entry(self.frame)
        self.username_entry.place(relx=0.47, rely=0.05,height=34, relwidth=0.43)

        self.pass_label = Label(self.frame)
        self.pass_label.place(relx=0.05, rely=0.29, height=47, width=289)
        self.pass_label.configure(text="Password: ")

        self.password_entry=Entry(self.frame,show="*")
        self.password_entry.place(relx=0.47, rely=0.31,height=34, relwidth=0.43)

        self.login_button=Button(self.frame,text="Login",font="Times 10",command=lambda:self.login_check(self.frame),height=5,width=10)
        self.login_button.place(relx=0.51, rely=0.55, height=50, width=100)
        self.root.mainloop()

    def login_check(self,frame):
        if self.username_entry.get()==self.name and self.password_entry.get()==self.password:
            Admin(self.root)
        else:
            self.message=Label(frame,text="Username or Passwrod is incorrect",fg="red")
            self.message.place(relx=0.48,rely=0.46)

if __name__ == '__main__':
    hotel=Management_System()

    