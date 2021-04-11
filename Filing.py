# import ast
# dic=dict()
# dic1={
#     "Name": "Wahaj Khan",
#     "Age": 18,
#     "CGPA": 3.06
# }
# dic2={
#     "Name": "Fizza Khan",
#     "Age": 19,
#     "CGPA": 3.6
# }
# file1=open("filing_test.txt","r+")
# # file1.write(str(dic1))
# # file1.write("\n")
# # file1.write(str(dic2))
# # file1.write("\n")

# while True:
#     test=file1.readline()
#     if not test:
#         break
#     print(test)
#     print("New Line")
#     dictionary = ast.literal_eval(test)
#     print(dictionary.get('Name'))

# file1.close()
from tkinter import *
root=Tk()

frame=LabelFrame(root,text="Test",padx=5,pady=5,borderwidth=1)
frame.pack(padx=10,pady=10)
message=Message(frame,text="Username: ",width=100)
message.grid(row=1,column=1)
button=Button(frame,text="TEST")
button.grid(row=0,column=0,pady=10,padx=10)

frame1=LabelFrame(root,text="Test",padx=5,pady=5)
frame1.pack(side=LEFT,padx=10,pady=10)
button1=Button(frame1,text="TEST1")
button1.grid()
root.mainloop()