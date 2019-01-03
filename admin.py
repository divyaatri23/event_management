from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import  ImageTk,Image

yup=Tk()
yup.title("Add Admin")
yup.geometry("1366x768")
path="bg-main_mini.jpg"
img=ImageTk.PhotoImage(Image.open(path))
panel  = Label(yup,image=img)
panel.pack()

def insert():
    if aname.get() and apass.get() and adept.get() != "":
        name=aname.get()
        password=apass.get()
        department=adept.get()
        db=pymysql.connect("localhost","root","","myapp")
        cursor=db.cursor()
        sql="insert into admin(name,password,department)" "values('%s','%s','%s')" %(name,password,department)
        r=cursor.execute(sql)
        if r>0:
            messagebox.showinfo("Message","Admin Registered Successfully")
        else:
            messagebox.showerror("Error","No Admin Registered")


head=Label(yup,text="ADD MEMBER",font=('Arial',30),fg='white',bg='orange')
head.place(x=570,y=20)
aname=Label(yup,text="Name:",font=('Arial',20),fg='white',bg='orange')
aname.place(x=540,y=120)
aname=Entry(yup,text="",width=30)
aname.place(x=700,y=125)
apass=Label(yup,text="Password:",font=('Arial',20),fg='white',bg='orange')
apass.place(x=540,y=220)
apass=Entry(yup,text="",width=30)
apass.place(x=700,y=225)
adept=Label(yup,text="Department:",font=('Arial',20),fg='white',bg='orange')
adept.place(x=540,y=320)
adept=Entry(yup,text="",width=30)
adept.place(x=700,y=325)
btn1=Button(yup,text="ADD ADMIN",command=insert,font=('Arial',20),fg='white',bg='black')
btn1.place(x=530,y=420)
btn1=Button(yup,text="CANCEL",command=exit,font=('Arial',20),fg='white',bg='black')
btn1.place(x=750,y=420)

yup.mainloop()

