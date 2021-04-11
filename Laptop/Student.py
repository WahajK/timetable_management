from tkinter import *
from Admin import Admin

class Student(Admin):

    def __init__(self):
        self.student_screen()

    def student_screen(self):
        self.root=Tk()
        self.root.geometry("600x400")

        self.frame = Frame(self.root)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.62, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.add_button=Button(self.frame,font="Times 10",text="Check Room Data",command=lambda :self.search_room(self.root,"Student"),height=2,width=25) #Need Work
        self.add_button.place(relx=0.23,rely=0.1,height=50,width=289)

        self.check_button=Button(self.frame,font="Times 10",text="Check a Teacher's Data",command=lambda :self.view_teacher(self.root,"Student"),height=2,width=25) #Need Work
        self.check_button.place(relx=0.23,rely=0.35,height=50,width=289)

        self.back_button=Button(self.frame,font="Times 10",text="Signout",height=2,width=25,command=self.root.destroy)
        self.back_button.place(relx=0.23,rely=0.6,height=50,width=289)
        self.root.mainloop()
        
    def search_room(self,root,user):
        root.destroy()
        self.newroot=Tk()
        self.day=StringVar()
        self.time=StringVar()
        self.room=StringVar()
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

        self.back_button=Button(self.frame,font="Times 10",text="Back",height=2,width=15,command=lambda: [self.newroot.destroy(),self.student_screen()])
        self.back_button.place(relx=0.5,rely=0.8,height=50,width=200)

        self.newroot.mainloop()

    def view_teacher(self,root,user):
        root.destroy()
        self.newroot=Tk()
        self.newroot.geometry("600x400")

        self.frame = Frame(self.newroot)
        self.frame.place(relx=0.03, rely=0.3, relheight=0.52, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.teacher_label=Label(self.frame,font="Times 10",text="Teacher's Name: ")
        self.teacher_label.place(relx=0.13,rely=0.3,height=18,width=200)

        self.teacher_entry=Entry(self.frame)
        self.teacher_entry.place(relx=0.5,rely=0.3,height=28,width=200)

        self.search_button=Button(self.frame,font="Times 10",text="Search",command=lambda : self.search_teacher_ui(self.teacher_entry.get()))
        self.search_button.place(relx=0.15,rely=0.55,height=38,width=180)

        self.Back_button=Button(self.frame,font="Times 10",text="Back",command=lambda: [self.newroot.destroy(),self.student_screen()])
        self.Back_button.place(relx=0.5,rely=0.55,height=38,width=180)

obj=Student()