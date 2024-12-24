from tkinter import *
from Admin import Admin
import ast
import os
from tkinter import messagebox

class Teacher(Admin):

    def __init__(self):
        self.root=Tk()
        self.root.title("FAST Management System")
        self.root.geometry("600x400")
        self.day=StringVar()
        self.time=StringVar()
        self.room=StringVar()
        Label(self.root,text="Teacher Login").place(relx=0.48,rely=0.03)

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

        self.login_button=Button(self.frame,text="Login",font="Times 10",command=lambda:self.__login_check(),height=5,width=10)
        self.login_button.place(relx=0.51, rely=0.55, height=50, width=100)
        self.root.mainloop()

    def __login_check(self):
        self.flag=False
        try:
            fh=open("Teacher.txt","r")
            while True:
                test=fh.readline()
                if not test:
                    break
                self.teacher_dic = ast.literal_eval(test)
                if self.username_entry.get().upper()==self.teacher_dic.get("Name").upper() and self.password_entry.get().upper()==self.teacher_dic.get("Pass"):
                    self.flag=True
                    fh.close()
                    self.tempvar=self.teacher_dic
                    self.root.destroy()
                    self.teacher_screen()
                    break
            fh.close()
            if self.flag==False:
                self.message=Label(self.frame,text="Username or Passwrod is incorrect",fg="red")
                self.message.place(relx=0.48,rely=0.46)
        except:
            print("Error opening file")

    def teacher_screen(self):
        self.root=Tk()
        self.root.geometry("600x400")

        self.frame = Frame(self.root)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.62, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.add_button=Button(self.frame,font="Times 10",text="Check Room Data",command=lambda :self.search_room(self.root,"Student"),height=2,width=25) #Need Work
        self.add_button.place(relx=0.23,rely=0.1,height=50,width=289)

        self.check_button=Button(self.frame,font="Times 10",text="Update your Consultation Time",command=lambda :self.update_consultation(),height=2,width=25) #Need Work
        self.check_button.place(relx=0.23,rely=0.35,height=50,width=289)

        self.back_button=Button(self.frame,font="Times 10",text="Signout",command=self.root.destroy)
        self.back_button.place(relx=0.23,rely=0.6,height=50,width=289)

    def update_consultation(self):
        self.root.destroy()
        self.root=Tk()
        self.root.geometry("600x400")

        self.frame = Frame(self.root)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.62, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.time.set("Select a time")

        self.consultation_label=Label(self.frame,font="Times 10",text="Consultation Time: ")
        self.consultation_label.place(relx=0.2,rely=0.35,height=38,width=200)

        self.drop_time=OptionMenu(self.frame,self.time,"8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","12:00-1:00","1:00-2:00","2:00-3:00","3:00-4:00")
        self.drop_time.place(relx=0.5,rely=0.35,height=38,width=200)

        self.update_button=Button(self.frame,text="Update",font="Times 10",command=lambda : [self.root.destroy(),self.consult_update_file(self.time.get()),self.teacher_screen()])
        self.update_button.place(relx=0.2,rely=0.6,height=50,width=189)

        self.update_button=Button(self.frame,text="Cancel",font="Times 10",command=lambda : [self.root.destroy(),self.teacher_screen()])
        self.update_button.place(relx=0.6,rely=0.6,height=50,width=189)

    def consult_update_file(self,consult):
        fh=open("Teacher.txt","r")
        ft=open("Temp.txt","w+")
        while True:
            test=fh.readline()
            if not test:
                break
            self.teacher_dic = ast.literal_eval(test)
            if self.tempvar.get("Name").upper()==self.teacher_dic.get("Name").upper():
                self.teacher_dic["Consultation Hours"]=consult
            ft.write(str(self.teacher_dic))
            ft.write("\n")
        fh.close()
        ft.close()
        os.remove("Teacher.txt")
        os.rename("Temp.txt","Teacher.txt")
        messagebox.showinfo("Info", "Data Successfully Written!")

    def search_room(self,root,user):
        root.destroy()
        self.newroot=Tk()
        self.newroot.geometry("600x400")

        self.frame = Frame(self.newroot)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.72, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.day.set("Select a Day")
        self.time.set("Select a Time")
        self.room.set("Select a Room")
        self.day_select=Label(self.frame,font="Times 10",text="Select the details!",fg="red")
        self.day_select.place(relx=0.3, rely=0.03, height=47, width=289)

        self.day_label=Label(self.frame,font="Times 10",text="Day")
        self.day_label.place(relx=0.03, rely=0.25, height=47, width=200)

        self.time_label=Label(self.frame,font="Times 10",text="Time")
        self.time_label.place(relx=0.03, rely=0.4, height=47, width=200)

        self.room_label=Label(self.frame,font="Times 10",text="Room")
        self.room_label.place(relx=0.03, rely=0.55, height=47, width=200)

        self.drop_day=OptionMenu(self.frame,self.day,"Monday","Tuesday","Wednesday","Thursday","Friday")
        self.drop_day.place(relx=0.47, rely=0.25,height=34, relwidth=0.43)

        self.drop_time=OptionMenu(self.frame,self.time,"8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","12:00-1:00","1:00-2:00","2:00-3:00","3:00-4:00")
        self.drop_time.place(relx=0.47, rely=0.4,height=34, relwidth=0.43)

        self.drop_room=OptionMenu(self.frame,self.room,"CR1","CR2","CR3","CR4","CR5","Lab 1","Lab 2","Lab 3","Lab 4","Lab 5")
        self.drop_room.place(relx=0.47, rely=0.55,height=34, relwidth=0.43)

        self.view_room_button=Button(self.frame,font="Times 10",text="Check",height=2,width=15,command=lambda : self.check_room(self.newroot,self.room.get(),self.time.get(),self.day.get(),"Student"))
        self.view_room_button.place(relx=0.1,rely=0.8,height=50,width=200)

        self.back_button=Button(self.frame,font="Times 10",text="Back",height=2,width=15,command=lambda: [self.newroot.destroy(),self.teacher_screen()])
        self.back_button.place(relx=0.5,rely=0.8,height=50,width=200)

        self.newroot.mainloop()

obj=Teacher()