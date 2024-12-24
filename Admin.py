from tkinter import *
import ast
from tkinter import messagebox
import os

class Admin:
    
    def __init__(self):
        self.teacher_dic=dict()
        self.teacher_dic={
            "Name":None,
            "Phone":None,
            "Qualification":None,
            "Email":None,
            "Address":None,
            "Consultation Hours":None,
            "Department":None,
            "Pass":None,
            "Room":None
        }
        self.room_dic=dict()
        self.room_dic={
            "Name":None,
            "Section":None,
            "Time":None,
            "Teacher":None,
            "Status":None,
            "Day":None
        }
        self.name="admin"
        self.password="admin"
        self.day=StringVar()
        self.room=StringVar()
        self.section=StringVar()
        self.status=StringVar()
        self.time=StringVar()
        root=Tk()
        root.geometry("600x400")
        self.login_screen(root)
    
    def data_val_teacher(self,root,name,phone,qualification,email,address,consultation,department,passw,room):
        self.flag=True

        if name.isalpha() and phone.isdigit() and qualification.isalpha() and address.isalpha() and department.isalpha():
            pass
        else:
            self.flag=False
        
        if "@nu.edu.pk" in email:
            pass
        else:
            self.flag=False
        
        if self.flag==True:
            self.__add_teacher_file(root,name,phone,qualification,email,address,consultation,department,passw,room)
        else:
            self.error_label=Label(self.frame1,text="Invalid Data !\n Kindly recheck the inputted data",fg="red")
            self.error_label.place(relx=0.35,rely=0.87)

    def login_screen(self,root):
        self.root=root
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

        self.login_button=Button(self.frame,text="Login",font="Times 10",command=lambda:self.__login_check(self.frame),height=5,width=10)
        self.login_button.place(relx=0.51, rely=0.55, height=50, width=100)
        self.root.mainloop()

    def __login_check(self,frame):
        if self.username_entry.get().upper()==self.name.upper() and self.password_entry.get().upper()==self.password.upper():
            self.__admin_screen(self.root)
        else:
            self.message=Label(frame,text="Username or Passwrod is incorrect",fg="red")
            self.message.place(relx=0.48,rely=0.46)

    def __admin_screen(self,root):  
        root.destroy()
        self.newroot=Tk()
        self.newroot.title("FAST Management System")
        self.newroot.geometry("600x400")

        self.frame = Frame(self.newroot)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.52, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.manage_class_button=Button(self.frame,text="Manage Rooms",font="Times 10",command=lambda:self.search_room(self.newroot))#Needs Work
        self.__manage_teachers_button=Button(self.frame,text="Manage Teacher's Data",font="Times 10",command=lambda:self.__manage_teacher(self.newroot)) #Needs Work
        self.manage_class_button.place(relx=0.3,rely=0.1,height=50,width=200)
        self.__manage_teachers_button.place(relx=0.3,rely=0.4,height=50,width=200)
        self.back_button=Button(self.frame,text="Signout",command=self.newroot.destroy,font="Times 10")
        self.back_button.place(relx=0.3,rely=0.7,height=50,width=200)
        self.newroot.mainloop()

    def search_room(self,root):
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

        self.view_room_button=Button(self.frame,font="Times 10",text="Check",height=2,width=15,command=lambda : self.check_room(self.newroot,self.room.get(),self.time.get(),self.day.get(),"Admin"))
        self.view_room_button.place(relx=0.1,rely=0.8,height=50,width=200)

        self.back_button=Button(self.frame,font="Times 10",text="Back",height=2,width=15,command=lambda: self.__admin_screen(self.newroot))
        self.back_button.place(relx=0.5,rely=0.8,height=50,width=200)

        self.newroot.mainloop()

    def check_room(self,root,class_name,time,day,user):
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
        
        self.name_label=Label(self.frame,font="Times 10",text="Name: "+str(class_name))#Put the damn name here somehow
        self.name_label.place(relx=0.25, rely=0.03, height=47, width=289)

        self.status_label=Label(self.frame,font="Times 10",text="Status: "+str(self.room_dic.get('Status')))#Put the damn status here somehow
        self.status_label.place(relx=0.25, rely=0.13, height=47, width=289)

        self.section_label=Label(self.frame,font="Times 10",text="Section: "+str(self.room_dic.get('Section')))#Put the damn status here somehow
        self.section_label.place(relx=0.25, rely=0.23, height=47, width=289)

        self.time_label=Label(self.frame,font="Times 10",text="Time: "+str(self.room_dic.get('Time')))#Put the damn status here somehow
        self.time_label.place(relx=0.25, rely=0.33, height=47, width=289)

        self.teacher_label=Label(self.frame,font="Times 10",text="Booked by: "+str(self.room_dic.get('Teacher')))#Put the damn status here somehow
        self.teacher_label.place(relx=0.25, rely=0.43, height=47, width=289)

        self.day_label=Label(self.frame,font="Times 10",text="Day: "+str(self.room_dic.get('Day')))#Put the damn status here somehow
        self.day_label.place(relx=0.25, rely=0.53, height=47, width=289)
        if user=="Admin":
            self.exit_button=Button(self.frame,font="Times 10",text="Exit",command=self.temproot.destroy,height=1,width=15)
            self.exit_button.place(relx=0.5, rely=0.8, height=47, width=189)

            self.Book_button=Button(self.frame,font="Times 10",text="Book",command=lambda : self.__book_room(self.temproot,str(class_name),str(self.room_dic.get('Time')),str(self.room_dic.get('Day'))),height=1,width=15) #Need Work
            self.Book_button.place(relx=0.15, rely=0.8, height=47, width=189)
        else:
            self.exit_button=Button(self.frame,font="Times 10",text="Exit",command=self.temproot.destroy,height=1,width=15)
            self.exit_button.place(relx=0.33, rely=0.8, height=47, width=189)
        
    def __book_room(self,root,room_name,time,day):
        root.destroy()
        self.temproot=Tk()
        self.temproot.geometry("600x400")

        self.frame = Frame(self.temproot)
        self.frame.place(relx=0.03, rely=0.2, relheight=0.62, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)
        
        

        self.status.set("Select a status")
        self.section.set("Select a section")

        self.name_label=Label(self.frame,font="Times 10",text="Name: ")
        self.name_label.place(relx=0.07, rely=0.03, height=47, width=289)

        self.name_entry=Entry(self.frame)
        self.name_entry.place(relx=0.5, rely=0.03, height=30, width=189)

        self.section_label=Label(self.frame,font="Times 10",text="Section: ")
        self.section_label.place(relx=0.07, rely=0.23, height=47, width=289)

        self.drop_section=OptionMenu(self.frame,self.section,'A','B','C','D','E','F','G','H','I','J')
        self.drop_section.place(relx=0.5, rely=0.23, height=37, width=189)

        self.status_label=Label(self.frame,font="Times 10",text="Status: ")
        self.status_label.place(relx=0.07, rely=0.43, height=47, width=289)

        self.drop_status=OptionMenu(self.frame,self.status,'Booked','Empty')
        self.drop_status.place(relx=0.5, rely=0.43, height=37, width=189)
        
        self.book_button=Button(self.frame,font="Times 10",text="Book",height=2,width=10,command=lambda : self.__room_booking_filing(room_name,time,day,self.name_entry.get(),self.status.get(),self.section.get(),self.temproot))
        self.book_button.place(relx=0.15, rely=0.65, height=47, width=189)

        self.cancel_button=Button(self.frame,font="Times 10",text="Cancel",command=self.temproot.destroy,height=2,width=10)
        self.cancel_button.place(relx=0.5, rely=0.65, height=47, width=189)

    def __room_booking_filing(self,room_name,time,day,name_entry,status,section,temproot):
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

    def __manage_teacher(self,root):
        root.destroy()
        self.newroot=Tk()
        self.newroot.geometry("600x400")

        self.frame = Frame(self.newroot)
        self.frame.place(relx=0.03, rely=0.15, relheight=0.82, relwidth=0.93)
        self.frame.configure(relief=GROOVE)
        self.frame.configure(borderwidth="2")
        self.frame.configure(width=995)

        self.add_button=Button(self.frame,font="Times 10",text="Add new Teachers",command=lambda :self.__add_teacher(),height=2,width=25) #Need Work
        self.add_button.place(relx=0.3,rely=0.15,height=50,width=200)

        self.check_button=Button(self.frame,font="Times 10",text="Check a Teacher's Data",command=lambda :self.view_teacher(self.newroot,None),height=2,width=25) #Need Work
        self.check_button.place(relx=0.3,rely=0.35,height=50,width=200)

        self.back_button=Button(self.frame,font="Times 10",text="Delete/Edit a Teacher",height=2,width=25,command=lambda: self.view_teacher(self.newroot,"Delete"))
        self.back_button.place(relx=0.3,rely=0.55,height=50,width=200)

        self.back_button=Button(self.frame,font="Times 10",text="Back",height=2,width=25,command=lambda: self.__admin_screen(self.newroot))
        self.back_button.place(relx=0.3,rely=0.75,height=50,width=200)

    def __add_teacher(self):
        self.temproot=Tk()
        self.temproot.geometry("1000x800")

        self.frame1 = Frame(self.temproot)
        self.frame1.place(relx=0.03, rely=0.03, relheight=0.92, relwidth=0.93)
        self.frame1.configure(relief=GROOVE)
        self.frame1.configure(borderwidth="2")
        self.frame1.configure(width=995)

        
        self.time.set("Select a time")
        self.Entry_Label = Label(self.frame1,font="Times 10",text="Enter the teacher's Data")
        self.Entry_Label.place(relx=0.3,rely=0.03,height=18,width=200)

        self.name_label=Label(self.frame1,font="Times 10",text="Name: ")
        self.name_label.place(relx=0.2,rely=0.07,height=38,width=200)

        self.name_entry=Entry(self.frame1)
        self.name_entry.place(relx=0.5,rely=0.07,height=38,width=200)

        self.phone_label=Label(self.frame1,font="Times 10",text="Phone #: ")
        self.phone_label.place(relx=0.2,rely=0.17,height=38,width=200)

        self.phone_entry=Entry(self.frame1)
        self.phone_entry.place(relx=0.5,rely=0.17,height=38,width=200)
        
        self.qualification_label=Label(self.frame1,font="Times 10",text="Qualification: ")
        self.qualification_label.place(relx=0.2,rely=0.27,height=38,width=200)

        self.qualification_entry=Entry(self.frame1)
        self.qualification_entry.place(relx=0.5,rely=0.27,height=38,width=200)

        self.email_label=Label(self.frame1,font="Times 10",text="Email: ")
        self.email_label.place(relx=0.2,rely=0.37,height=38,width=200)

        self.email_entry=Entry(self.frame1)
        self.email_entry.place(relx=0.5,rely=0.37,height=38,width=200)

        self.address_label=Label(self.frame1,font="Times 10",text="Address: ")
        self.address_label.place(relx=0.2,rely=0.47,height=38,width=200)

        self.address_entry=Entry(self.frame1)
        self.address_entry.place(relx=0.5,rely=0.47,height=38,width=200)

        self.consultation_label=Label(self.frame1,font="Times 10",text="Consultation Time: ")
        self.consultation_label.place(relx=0.2,rely=0.57,height=38,width=200)

        self.drop_time=OptionMenu(self.frame1,self.time,"8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","12:00-1:00","1:00-2:00","2:00-3:00","3:00-4:00")
        self.drop_time.place(relx=0.5,rely=0.57,height=38,width=200)

        self.deparment_label=Label(self.frame1,font="Times 10",text="Department: ")
        self.deparment_label.place(relx=0.2,rely=0.67,height=38,width=200)

        self.deparment_entry=Entry(self.frame1)
        self.deparment_entry.place(relx=0.5,rely=0.67,height=38,width=200)

        self.deparment_label=Label(self.frame1,font="Times 10",text="Staff Room: ")
        self.deparment_label.place(relx=0.2,rely=0.75,height=38,width=200)

        self.drop_room=OptionMenu(self.frame1,self.room,"SR1","SR2","SR3","SR4","SR5")
        self.drop_room.place(relx=0.5, rely=0.75,height=38,width=200)
        
        self.pass_label=Label(self.frame1,font="Times 10",text="Login Password: ")
        self.pass_label.place(relx=0.2,rely=0.83,height=38,width=200)

        self.password_entry=Entry(self.frame1,show="*")
        self.password_entry.place(relx=0.5,rely=0.83,height=38,width=200)

        self.add_teacher_button=Button(self.frame1,font="Times 10",text="Add",height=1,width=15,command=lambda : self.data_val_teacher(self.temproot,self.name_entry.get(),self.phone_entry.get(),self.qualification_entry.get(),self.email_entry.get(),self.address_entry.get(),self.time.get(),self.deparment_entry.get(),self.password_entry.get(),self.room.get()))
        self.add_teacher_button.place(relx=0.2,rely=0.91,height=38,width=200)

        self.cancel_button=Button(self.frame1,font="Times 10",text="Cancel",height=1,width=15,command=self.temproot.destroy)
        self.cancel_button.place(relx=0.5,rely=0.9,height=38,width=200)
    
    def __add_teacher_file(self,root,name,phone,qualification,email,address,consultation,department,passw,room):
        self.teacher_dic={
            "Name":name,
            "Phone":phone,
            "Qualification":qualification,
            "Email":email,
            "Address":address,
            "Consultation Hours":consultation,
            "Department":department,
            "Pass":passw,
            "Room":room
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
    
    def __del_teacher(self,name,overload):
        self.flag=False
        fh=open("Teacher.txt","r")
        ft=open("Temp.txt","w")
        while True:
            test=fh.readline()
            if not test:
                break
            self.teacher_dic = ast.literal_eval(test)
            if name.upper()==self.teacher_dic.get("Name").upper():
                self.flag=True
                ans=messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
                if ans=="yes":
                    continue

            ft.write(str(self.teacher_dic))
            ft.write("\n")
        fh.close()
        ft.close()
        os.remove("Teacher.txt")
        os.rename("Temp.txt","Teacher.txt")
        if self.flag==False:
            self.message=Label(self.frame,font="Times 10",text="Teacher not found!",fg="red")
            self.message.place(relx=0.48,rely=0.46)

    def cancel(self,dic):
        ft=open("Teacher.txt","a")
        ft.write(str(dic))
        ft.write("\n")
        ft.close()
        
    def __edit_teacher(self,name):
        self.flag=False
        try:
            fh=open("Teacher.txt","r")
            ft=open("Temp.txt","w")
            while True:
                test=fh.readline()
                if not test:
                    break
                self.teacher_dic = ast.literal_eval(test)
                if name.upper()==self.teacher_dic.get("Name").upper():
                    self.flag=True
                    temp=self.teacher_dic
                    continue
                ft.write(str(self.teacher_dic))
                ft.write("\n")
            fh.close()
            ft.close()
            os.remove("Teacher.txt")
            os.rename("Temp.txt","Teacher.txt")
            if self.flag==False:
                self.message=Label(self.frame,font="Times 10",text="Teacher not found!",fg="red")
                self.message.place(relx=0.48,rely=0.46)
        except:
            print("Error opening file")
        if self.flag==True:
            self.frame1 = Frame(self.temproot)
            self.frame1.place(relx=0.03, rely=0.03, relheight=0.92, relwidth=0.93)
            self.frame1.configure(relief=GROOVE)
            self.frame1.configure(borderwidth="2")
            self.frame1.configure(width=995)

            self.time.set("Select a time")
            self.Entry_Label = Label(self.frame1,font="Times 10",text="Enter the teacher's Data")
            self.Entry_Label.place(relx=0.3,rely=0.03,height=18,width=200)

            self.name_label=Label(self.frame1,font="Times 10",text="Name: ")
            self.name_label.place(relx=0.2,rely=0.07,height=38,width=200)

            self.name_entry=Entry(self.frame1)
            self.name_entry.place(relx=0.5,rely=0.07,height=38,width=200)

            self.phone_label=Label(self.frame1,font="Times 10",text="Phone #: ")
            self.phone_label.place(relx=0.2,rely=0.17,height=38,width=200)

            self.phone_entry=Entry(self.frame1)
            self.phone_entry.place(relx=0.5,rely=0.17,height=38,width=200)
            
            self.qualification_label=Label(self.frame1,font="Times 10",text="Qualification: ")
            self.qualification_label.place(relx=0.2,rely=0.27,height=38,width=200)

            self.qualification_entry=Entry(self.frame1)
            self.qualification_entry.place(relx=0.5,rely=0.27,height=38,width=200)

            self.email_label=Label(self.frame1,font="Times 10",text="Email: ")
            self.email_label.place(relx=0.2,rely=0.37,height=38,width=200)

            self.email_entry=Entry(self.frame1)
            self.email_entry.place(relx=0.5,rely=0.37,height=38,width=200)

            self.address_label=Label(self.frame1,font="Times 10",text="Address: ")
            self.address_label.place(relx=0.2,rely=0.47,height=38,width=200)

            self.address_entry=Entry(self.frame1)
            self.address_entry.place(relx=0.5,rely=0.47,height=38,width=200)

            self.consultation_label=Label(self.frame1,font="Times 10",text="Consultation Time: ")
            self.consultation_label.place(relx=0.2,rely=0.57,height=38,width=200)

            self.drop_time=OptionMenu(self.frame1,self.time,"8:00-9:00","9:00-10:00","10:00-11:00","11:00-12:00","12:00-1:00","1:00-2:00","2:00-3:00","3:00-4:00")
            self.drop_time.place(relx=0.5,rely=0.57,height=38,width=200)

            self.deparment_label=Label(self.frame1,font="Times 10",text="Department: ")
            self.deparment_label.place(relx=0.2,rely=0.67,height=38,width=200)

            self.deparment_entry=Entry(self.frame1)
            self.deparment_entry.place(relx=0.5,rely=0.67,height=38,width=200)

            self.deparment_label=Label(self.frame1,font="Times 10",text="Staff Room: ")
            self.deparment_label.place(relx=0.2,rely=0.75,height=38,width=200)

            self.drop_room=OptionMenu(self.frame1,self.room,"SR1","SR2","SR3","SR4","SR5")
            self.drop_room.place(relx=0.5, rely=0.75,height=38,width=200)
            
            self.pass_label=Label(self.frame1,font="Times 10",text="Login Password: ")
            self.pass_label.place(relx=0.2,rely=0.83,height=38,width=200)

            self.password_entry=Entry(self.frame1,show="*")
            self.password_entry.place(relx=0.5,rely=0.83,height=38,width=200)
            
            self.add_teacher_button=Button(self.frame,font="Times 10",text="Update",height=1,width=15,command=lambda : self.data_val_teacher(self.temproot,self.name_entry.get(),self.phone_entry.get(),self.qualification_entry.get(),self.email_entry.get(),self.address_entry.get(),self.time.get(),self.deparment_entry.get(),self.password_entry.get(),self.room.get()))
            self.add_teacher_button.place(relx=0.2,rely=0.9,height=38,width=200)

            self.cancel_button=Button(self.frame,font="Times 10",text="Cancel",height=1,width=15,command=lambda:[self.temproot.destroy(),self.cancel(temp)])
            self.cancel_button.place(relx=0.5,rely=0.9,height=38,width=200)

        else:
            self.message=Label(self.frame,font="Times 10",text="Teacher not found!",fg="red")
            self.message.place(relx=0.48,rely=0.46)

    def search_teacher_file(self,name):
        self.flag=False
        try:
            fh=open("Teacher.txt","r")
            while True:
                test=fh.readline()
                if not test:
                    break
                self.teacher_dic = ast.literal_eval(test)
                if name.upper()==self.teacher_dic.get("Name").upper():
                    self.flag=True
                    break
            fh.close()
        except:
            print("File Missing/Error opening file")

    def search_teacher_ui(self,name):
        self.flag=False
        self.search_teacher_file(name)
        if self.flag==True: 
            self.temproot=Tk()
            self.temproot.geometry("700x500")
            self.frame = Frame(self.temproot)
            self.frame.place(relx=0.03, rely=0.2, relheight=0.72, relwidth=0.93)
            self.frame.configure(relief=GROOVE)
            self.frame.configure(borderwidth="2")
            self.frame.configure(width=995)
            
            self.name_label=Label(self.frame,font="Times 10",text="Name: "+str(name))#Put the damn name here somehow
            self.name_label.place(relx=0.25, rely=0.03, height=47, width=289)

            self.status_label=Label(self.frame,font="Times 10",text="Phone: "+str(self.teacher_dic.get('Phone')))#Put the damn status here somehow
            self.status_label.place(relx=0.25, rely=0.13, height=47, width=289)

            self.section_label=Label(self.frame,font="Times 10",text="Qualification: "+str(self.teacher_dic.get('Qualification')))#Put the damn status here somehow
            self.section_label.place(relx=0.25, rely=0.23, height=47, width=289)

            self.time_label=Label(self.frame,font="Times 10",text="Address: "+str(self.teacher_dic.get('Address')))#Put the damn status here somehow
            self.time_label.place(relx=0.25, rely=0.33, height=47, width=289)

            self.teacher_label=Label(self.frame,font="Times 10",text="Email: "+str(self.teacher_dic.get('Email')))#Put the damn status here somehow
            self.teacher_label.place(relx=0.25, rely=0.43, height=47, width=289)

            self.day_label=Label(self.frame,font="Times 10",text="Consultation Hours: "+str(self.teacher_dic.get('Consultation Hours')))#Put the damn status here somehow
            self.day_label.place(relx=0.25, rely=0.53, height=47, width=289)
            
            self.day_label=Label(self.frame,font="Times 10",text="Department: "+str(self.teacher_dic.get('Department')))#Put the damn status here somehow
            self.day_label.place(relx=0.25, rely=0.63, height=47, width=289)

            self.day_label=Label(self.frame,font="Times 10",text="Staff Room: "+str(self.teacher_dic.get('Room')))#Put the damn status here somehow
            self.day_label.place(relx=0.25, rely=0.73, height=47, width=289)

            self.exit_button=Button(self.frame,font="Times 10",text="Exit",command=self.temproot.destroy,height=1,width=15)
            self.exit_button.place(relx=0.35, rely=0.85, height=47, width=189)

        else:
            self.message=Label(self.frame,font="Times 10",text="Teacher not found!",fg="red")
            self.message.place(relx=0.48,rely=0.46)

    def view_teacher(self,root,overload1):
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

        if overload1==None:
            self.search_button=Button(self.frame,font="Times 10",text="Search",command=lambda : self.search_teacher_ui(self.teacher_entry.get()))
            self.search_button.place(relx=0.15,rely=0.55,height=38,width=180)

            self.Back_button=Button(self.frame,font="Times 10",text="Back",command=lambda : self.__manage_teacher(self.newroot))
            self.Back_button.place(relx=0.65,rely=0.55,height=38,width=180)

        else:
            self.search_button=Button(self.frame,font="Times 10",text="Edit",command=lambda : self.__edit_teacher(self.teacher_entry.get()))
            self.search_button.place(relx=0.35,rely=0.55,height=38,width=150)

            self.search_button=Button(self.frame,font="Times 10",text="Delete",command=lambda : self.__del_teacher(self.teacher_entry.get(),None))
            self.search_button.place(relx=0.03,rely=0.55,height=38,width=150)

            self.Back_button=Button(self.frame,font="Times 10",text="Back",command=lambda : self.__manage_teacher(self.newroot))
            self.Back_button.place(relx=0.65,rely=0.55,height=38,width=150)
