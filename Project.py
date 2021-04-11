from tkinter import *
import ast
from tkinter import messagebox
import os
class Admin:
    
    def __init__(self,root):
        self.teacher_dic=dict()
        self.teacher_dic={
            "Name":None,
            "Phone":None,
            "Qualification":None,
            "Email":None,
            "Address":None,
            "Consultion Hours":None,
            "Department":None
        }
        self.name=""
        self.password=""
        self.room_dic=dict()
        self.room_dic={
            "Name":None,
            "Section":None,
            "Time":None,
            "Teacher":None,
            "Status":None,
            "Day":None
        }
        self.admin_screen(root)

    def admin_screen(self,root):  
        root.destroy()
        self.newroot=Tk()
        self.newroot.title("FAST Management System")
        self.newroot.geometry("600x400")

        self.frame = Frame(self.newroot)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.52, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.manage_class_button=Button(self.frame,text="Manage Rooms",font="Times 10",command=lambda:self.manage_room(self.newroot))#Needs Work
        self.manage_teachers_button=Button(self.frame,text="Manage Teacher's Data",font="Times 10",command=lambda:self.manage_teacher(self.newroot)) #Needs Work
        self.manage_class_button.place(relx=0.3,rely=0.2,height=50,width=200)
        self.manage_teachers_button.place(relx=0.3,rely=0.5,height=50,width=200)
        self.newroot.mainloop()

    def manage_room(self,root):
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
        self.day_select=Label(self.frame,text="Select the details!",fg="red")
        self.day_select.place(relx=0.3, rely=0.03, height=47, width=289)

        self.day_label=Label(self.frame,text="Day")
        self.day_label.place(relx=0.03, rely=0.25, height=47, width=200)

        self.time_label=Label(self.frame,text="Time")
        self.time_label.place(relx=0.03, rely=0.4, height=47, width=200)

        self.room_label=Label(self.frame,text="Room")
        self.room_label.place(relx=0.03, rely=0.55, height=47, width=200)

        self.drop_day=OptionMenu(self.frame,self.day,"Monday","Tuesday","Wednesday","Thursday","Friday")
        self.drop_day.place(relx=0.47, rely=0.25,height=34, relwidth=0.43)

        self.drop_time=OptionMenu(self.frame,self.time,"8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","12:00-1:00","1:00-2:00","2:00-3:00","3:00-4:00")
        self.drop_time.place(relx=0.47, rely=0.4,height=34, relwidth=0.43)

        self.drop_room=OptionMenu(self.frame,self.room,"CR1","CR2","CR3","CR4","CR5","Lab 1","Lab 2","Lab 3","Lab 4","Lab 5")
        self.drop_room.place(relx=0.47, rely=0.55,height=34, relwidth=0.43)

        self.view_room_button=Button(self.frame,text="Check",height=2,width=15,command=lambda : self.update_room(self.newroot,self.room.get(),self.time.get(),self.day.get()))
        self.view_room_button.place(relx=0.1,rely=0.8,height=50,width=200)

        self.back_button=Button(self.frame,text="Back",height=2,width=15,command=lambda: self.admin_screen(self.newroot))
        self.back_button.place(relx=0.5,rely=0.8,height=50,width=200)

        self.newroot.mainloop()

    def update_room(self,root,class_name,time,day):
        self.temproot=Tk()
        self.temproot.geometry("600x400")
        try:
            fh=open("Rooms.txt","r")
            while True:
                test=fh.readline()
                if not test:
                    break
                self.room_dic = ast.literal_eval(test)
                if self.room_dic.get('Name')==class_name and self.room_dic.get('Time')==time and self.room_dic.get('Day')==day:
                    break
            fh.close()
        except:
            print("File Missing/Error opening file")

        self.frame = Frame(self.temproot)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.72, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)
        
        self.name_label=Label(self.frame,text="Name: "+str(class_name))#Put the damn name here somehow
        self.name_label.place(relx=0.25, rely=0.03, height=47, width=289)

        self.status_label=Label(self.frame,text="Status: "+str(self.room_dic.get('Status')))#Put the damn status here somehow
        self.status_label.place(relx=0.25, rely=0.13, height=47, width=289)

        self.section_label=Label(self.frame,text="Section: "+str(self.room_dic.get('Section')))#Put the damn status here somehow
        self.section_label.place(relx=0.25, rely=0.23, height=47, width=289)

        self.time_label=Label(self.frame,text="Time: "+str(self.room_dic.get('Time')))#Put the damn status here somehow
        self.time_label.place(relx=0.25, rely=0.33, height=47, width=289)

        self.teacher_label=Label(self.frame,text="Booked by: "+str(self.room_dic.get('Teacher')))#Put the damn status here somehow
        self.teacher_label.place(relx=0.25, rely=0.43, height=47, width=289)

        self.day_label=Label(self.frame,text="Day: "+str(self.room_dic.get('Day')))#Put the damn status here somehow
        self.day_label.place(relx=0.25, rely=0.53, height=47, width=289)

        self.exit_button=Button(self.frame,text="Exit",command=self.temproot.destroy,height=1,width=15)
        self.exit_button.place(relx=0.5, rely=0.8, height=47, width=189)

        self.Book_button=Button(self.frame,text="Book",command=lambda : self.book_room(self.temproot,str(class_name),str(self.room_dic.get('Time')),str(self.room_dic.get('Day'))),height=1,width=15) #Need Work
        self.Book_button.place(relx=0.15, rely=0.8, height=47, width=189)
        
    def book_room(self,root,room_name,time,day):
        root.destroy()
        self.temproot=Tk()
        self.temproot.geometry("600x400")

        self.frame = Frame(self.temproot)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.62, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)
        
        self.section=StringVar()
        self.status=StringVar()

        self.status.set("Select a status")
        self.section.set("Select a section")

        self.name_label=Label(self.frame,text="Name: ")
        self.name_label.place(relx=0.07, rely=0.03, height=47, width=289)

        self.name_entry=Entry(self.frame)
        self.name_entry.place(relx=0.5, rely=0.03, height=30, width=189)

        self.section_label=Label(self.frame,text="Section: ")
        self.section_label.place(relx=0.07, rely=0.23, height=47, width=289)

        self.drop_section=OptionMenu(self.frame,self.section,'A','B','C','D','E','E','F','G','H','I','J')
        self.drop_section.place(relx=0.5, rely=0.23, height=37, width=189)

        self.status_label=Label(self.frame,text="Status: ")
        self.status_label.place(relx=0.07, rely=0.43, height=47, width=289)

        self.drop_status=OptionMenu(self.frame,self.status,'Booked','Empty')
        self.drop_status.place(relx=0.5, rely=0.43, height=37, width=189)
        
        self.book_button=Button(self.frame,text="Book",height=2,width=10,command=lambda : self.booking(room_name,time,day,self.name_entry.get(),self.status.get(),self.section.get(),self.temproot))
        self.book_button.place(relx=0.15, rely=0.65, height=47, width=189)

        self.cancel_button=Button(self.frame,text="Cancel",command=self.temproot.destroy,height=2,width=10)
        self.cancel_button.place(relx=0.5, rely=0.65, height=47, width=189)

    def booking(self,room_name,time,day,name_entry,status,section,temproot):
        try:
            fh=open("Rooms.txt","r")
            ft=open("Temp.txt","w")
            while True:
                test=fh.readline()
                if not test:
                    break
                self.room_dic = ast.literal_eval(test)
                if self.room_dic.get('Name')==room_name and self.room_dic.get('Time')==time and self.room_dic.get('Day')==day:
                    self.room_dic["Section"]=section
                    self.room_dic["Status"]=status
                    self.room_dic["Teacher"]=name_entry
                ft.write(str(self.room_dic))
                ft.write("\n")
            fh.close()
            ft.close()
            os.remove("Rooms.txt")
            os.rename("Temp.txt","Rooms.txt")
            messagebox.showinfo("Info", "Data Successfully Written!")
            self.temproot.destroy()
        except:
            print("File Missing/Error opening file")

    def manage_teacher(self,root):
        root.destroy()
        self.newroot=Tk()
        self.newroot.geometry("600x400")

        self.frame = Frame(self.newroot)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.62, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.add_button=Button(self.frame,text="Add new Teachers",command=lambda :self.add_teacher(),height=2,width=25) #Need Work
        self.add_button.place(relx=0.3,rely=0.1,height=50,width=200)

        self.check_button=Button(self.frame,text="Check a Teacher's Data",command=lambda :self.view_teacher(self.newroot),height=2,width=25) #Need Work
        self.check_button.place(relx=0.3,rely=0.35,height=50,width=200)

        self.back_button=Button(self.frame,text="Back",height=2,width=25,command=lambda: self.admin_screen(self.newroot))
        self.back_button.place(relx=0.3,rely=0.6,height=50,width=200)

    def add_teacher(self):
        self.temproot=Tk()
        self.temproot.geometry("800x600")

        self.frame = Frame(self.temproot)
        self.frame.place(relx=0.03, rely=0.03, relheight=0.92, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.time=StringVar()
        self.time.set("Select a time")
        self.Entry_Label = Label(self.frame,text="Enter the teacher's Data")
        self.Entry_Label.place(relx=0.3,rely=0.03,height=38,width=200)

        self.name_label=Label(self.frame,text="Name: ",font="Times 10")
        self.name_label.place(relx=0.2,rely=0.13,height=38,width=200)

        self.name_entry=Entry(self.frame)
        self.name_entry.place(relx=0.5,rely=0.13,height=38,width=200)

        self.phone_label=Label(self.frame,text="Phone #: ",font="Times 10")
        self.phone_label.place(relx=0.2,rely=0.23,height=38,width=200)

        self.phone_entry=Entry(self.frame)
        self.phone_entry.place(relx=0.5,rely=0.23,height=38,width=200)
        
        self.qualification_label=Label(self.frame,text="Qualification: ",font="Times 10")
        self.qualification_label.place(relx=0.2,rely=0.33,height=38,width=200)

        self.qualification_entry=Entry(self.frame)
        self.qualification_entry.place(relx=0.5,rely=0.33,height=38,width=200)

        self.email_label=Label(self.frame,text="Email: ",font="Times 10")
        self.email_label.place(relx=0.2,rely=0.43,height=38,width=200)

        self.email_entry=Entry(self.frame)
        self.email_entry.place(relx=0.5,rely=0.43,height=38,width=200)

        self.address_label=Label(self.frame,text="Address: ",font="Times 10")
        self.address_label.place(relx=0.2,rely=0.53,height=38,width=200)

        self.address_entry=Entry(self.frame)
        self.address_entry.place(relx=0.5,rely=0.53,height=38,width=200)

        self.consultation_label=Label(self.frame,text="Consultation Time: ",font="Times 10")
        self.consultation_label.place(relx=0.2,rely=0.63,height=38,width=200)

        self.drop_time=OptionMenu(self.frame,self.time,"8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","12:00-1:00","1:00-2:00","2:00-3:00","3:00-4:00")
        self.drop_time.place(relx=0.5,rely=0.63,height=38,width=200)

        self.deparment_label=Label(self.frame,text="Department: ",font="Times 10")
        self.deparment_label.place(relx=0.2,rely=0.73,height=38,width=200)

        self.deparment_entry=Entry(self.frame)
        self.deparment_entry.place(relx=0.5,rely=0.73,height=38,width=200)

        self.add_teacher_button=Button(self.frame,text="Add",height=1,width=15,command=lambda : self.add_teacher_file(self.temproot,self.name_entry.get(),self.phone_entry.get(),self.qualification_entry.get(),self.email_entry.get(),self.address_entry.get(),self.time.get(),self.deparment_entry.get()))
        self.add_teacher_button.place(relx=0.2,rely=0.85,height=38,width=200)

        self.cancel_button=Button(self.frame,text="Cancel",height=1,width=15,command=self.temproot.destroy)
        self.cancel_button.place(relx=0.5,rely=0.85,height=38,width=200)
    
    def add_teacher_file(self,root,name,phone,qualification,email,address,consultation,department):
        self.teacher_dic={
            "Name":name,
            "Phone":phone,
            "Qualification":qualification,
            "Email":email,
            "Address":address,
            "Consultion Hours":consultation,
            "Department":department
        }
        try:
            fh=open("Teacher.txt","a+")
            fh.write(str(self.teacher_dic))
            fh.write("\n")
            fh.close()
            messagebox.showinfo("Info", "Data Successfully Written!")
            root.destroy()
        except:
            print("Error Opening File!")
        
    def search_teacher(self,name):
        flag=False
        try:
            fh=open("Teacher.txt","r")
            while True:
                test=fh.readline()
                if not test:
                    break
                self.teacher_dic = ast.literal_eval(test)
                if name.upper()==self.teacher_dic.get("Name").upper():
                    self.temproot=Tk()
                    self.temproot.geometry("600x400")
                    flag=True
                    self.frame = Frame(self.temproot)
                    self.frame.place(relx=0.03, rely=0.2, relheight=0.72, relwidth=0.93)
                    self.frame.configure(relief=GROOVE)
                    self.frame.configure(borderwidth="2")
                    self.frame.configure(width=995)
                    
                    self.name_label=Label(self.frame,text="Name: "+str(name))#Put the damn name here somehow
                    self.name_label.place(relx=0.25, rely=0.03, height=47, width=289)

                    self.status_label=Label(self.frame,text="Phone: "+str(self.teacher_dic.get('Phone')))#Put the damn status here somehow
                    self.status_label.place(relx=0.25, rely=0.13, height=47, width=289)

                    self.section_label=Label(self.frame,text="Qualification: "+str(self.teacher_dic.get('Qualification')))#Put the damn status here somehow
                    self.section_label.place(relx=0.25, rely=0.23, height=47, width=289)

                    self.time_label=Label(self.frame,text="Address: "+str(self.teacher_dic.get('Address')))#Put the damn status here somehow
                    self.time_label.place(relx=0.25, rely=0.33, height=47, width=289)

                    self.teacher_label=Label(self.frame,text="Email: "+str(self.teacher_dic.get('Email')))#Put the damn status here somehow
                    self.teacher_label.place(relx=0.25, rely=0.43, height=47, width=289)

                    self.day_label=Label(self.frame,text="Consultation Hours: "+str(self.teacher_dic.get('Consultion Hours')))#Put the damn status here somehow
                    self.day_label.place(relx=0.25, rely=0.53, height=47, width=289)
                    
                    self.day_label=Label(self.frame,text="Department: "+str(self.teacher_dic.get('Department')))#Put the damn status here somehow
                    self.day_label.place(relx=0.25, rely=0.63, height=47, width=289)

                    self.exit_button=Button(self.frame,text="Exit",command=self.temproot.destroy,height=1,width=15)
                    self.exit_button.place(relx=0.35, rely=0.8, height=47, width=189)

            fh.close()
            if flag==False:
                self.message=Label(self.frame,text="Teacher not found!",fg="red")
                self.message.place(relx=0.48,rely=0.46)
        except:
            print("File Missing/Error opening file")

    def view_teacher(self,root):
        root.destroy()
        self.newroot=Tk()
        self.newroot.geometry("600x400")

        self.frame = Frame(self.newroot)
        self.frame.place(relx=0.03, rely=0.3, relheight=0.52, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.teacher_label=Label(self.frame,text="Teacher's Name: ")
        self.teacher_label.place(relx=0.13,rely=0.3,height=18,width=200)

        self.teacher_entry=Entry(self.frame)
        self.teacher_entry.place(relx=0.5,rely=0.3,height=28,width=200)

        self.search_button=Button(self.frame,text="Search",command=lambda : self.search_teacher(self.teacher_entry.get()))
        self.search_button.place(relx=0.15,rely=0.55,height=38,width=180)

        self.Back_button=Button(self.frame,text="Back",command=lambda : self.manage_teacher(self.newroot))
        self.Back_button.place(relx=0.5,rely=0.55,height=38,width=180)

root=Tk()
root.geometry("600x400")
apps=Admin(root)
root.mainloop()