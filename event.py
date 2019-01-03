import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import  ImageTk,Image
import pymysql
from tkinter import messagebox
db = pymysql.connect("localhost","root","","event")
cursor=db.cursor()
def new_window ():
    def registration():
        def login():
            id = int(identry.get())
            name = nameentry.get()
            addr = str(addressentry.get("0.0", END))
            mob = mobileentry.get()
            email = emailentry.get()
            password = passentry.get()
            if id and  name and addr and mob and email and password != "":
                try:
                    sql = "insert into registration(userid,name,address,mobile,email,password) values ('%d','%s','%s','%s','%s','%s')" % (id, name, addr, mob, email, password)
                    sql2 = "Insert into login (cid,password)  values('%d','%s')" % (id, password)
                    r = cursor.execute(sql)
                    r2 = cursor.execute(sql2)
                    if r > 0 and r2 > 0:
                        messagebox.showinfo('Success', 'Coustmer successfully addedd')
                    else:
                        messagebox.showinfo("Error", "No Coustmer added")
                except:
                   db.rollback()
                   messagebox.showwarning("Warning", " fill the appropirate details")
            else:
                messagebox.showinfo("Warning", "Fill all the fields")
            db.commit()
            new_window()
        def up():
            def update():
                id = int(identry.get())
                name = nameentry.get()
                addr = str(addressentry.get("0.0", END))
                mob = mobileentry.get()
                email = emailentry.get()
                password = passentry.get()
                if id and name and addr and mob and email and password != "":
                    try:
                        sql = "update registration set name='%s', address='%s' , mobile='%s' ,email='%s', password='%s' where userid='%d'" % (name, addr, mob, email, password, id)
                        r = cursor.execute(sql)
                        if r > 0:
                            messagebox.showinfo('Success', 'Information successfully Updated')
                        else:
                            messagebox.showinfo("Error", "No Inforamtion updated , Enter the correct Id")
                            up()
                    except:

                        db.rollback()
                        messagebox.showwarning("Warning", " fill the appropirate details")


                else:
                    messagebox.showinfo("Warning", "Fill all the fields")
                db.commit()
                up()
            def delete():
                id = int(identry.get())

                if id != "":
                    try:
                        sql = "delete from registration where  userid='%d'" % (id)
                        r = cursor.execute(sql)
                        if r > 0:
                            messagebox.showinfo('Success', 'Coustmer successfully Deleted')
                        else:
                            messagebox.showinfo("Error", "No coustmer deleted, Enter the Correct ID")
                    except:

                        db.rollback()
                        messagebox.showwarning("Warning", " fill a valid id")


                else:
                    messagebox.showinfo("Warning", "Fill a valid id")
                db.commit()
                up()
            def back():
                registration()
            ab = Toplevel(a)
            ab.title("Event Management")
            ab.geometry("2160x1080")
            ab.configure(background='grey')
            path = "53b0150c46fd23eb14d2c025b09e579d.jpg"
            img = ImageTk.PhotoImage(Image.open(path))
            path2="coustmer registration.jpg"
            img2=ImageTk.PhotoImage(Image.open(path2))
            panel = Label(ab, image=img)
            # panel.place(x=600,y=100)
            lab = Label(ab, text="Coustmer Registration", font=("times new roman", 20), width=25)
            lab.place(x=350, y=50)
            idlab = Label(ab, text="User ID", width=10)
            idlab.place(x=350, y=150)
            identry = Entry(ab, text="", width=46)
            identry.place(x=450, y=150)
            namelab = Label(ab, text="Name", width=10)
            namelab.place(x=350, y=190)
            nameentry = Entry(ab, text="", width=46)
            nameentry.place(x=450, y=190)
            addlab = Label(ab, text="Address", width=10)
            addlab.place(x=350, y=240)
            addressentry = Text(ab, height=2, width=34)
            addressentry.place(x=450, y=230)
            mobilelab = Label(ab, text="Mobile", width=10)
            mobilelab.place(x=350, y=290)
            mobileentry = Entry(ab, text="", width=46)
            mobileentry.place(x=450, y=290)
            emaillab = Label(ab, text="Email", width=10)
            emaillab.place(x=350, y=330)
            emailentry = Entry(ab, text="", width=46)
            emailentry.place(x=450, y=330)
            passwordlab = Label(ab, text="Password", width=10)
            passwordlab.place(x=350, y=370)
            passentry = Entry(ab, text="", show="*", width=46)
            passentry.place(x=450, y=370)
            lab = Label(ab,text=" ",width=200,height=150,image=img2).place(x=970,y=250)
            Update = Button(ab, text="Update", command=update, font=('Arial', 13)).place(x=400, y=440)
            Delete = Button(ab, text="Delete", font=('Arial', 13), command=delete).place(x=480, y=440)
            back = Button(ab, text="Back", font=('Arial', 13),command=back).place(x=550, y=440)
            panel.pack(side="top")
            ab.mainloop()
        def bck():
            new_window()
        a = Toplevel(top)
        a.title("Event Management")
        a.geometry("2160x1080")
        a.configure(background='black')
        path = "53b0150c46fd23eb14d2c025b09e579d.jpg"
        img = ImageTk.PhotoImage(Image.open(path))


        panel = Label(a, image=img)
        # panel.place(x=600,y=100)
        lab = Label(a, text="Coustmer Registration", font=("Monotype Corsiva", 25), width=25,fg="white",bg="orange")
        lab.place(x=480, y=30)
        idlab = Label(a, text="User ID", font=('Arial', 14) ,  width=10 , fg="white",bg="black")
        idlab.place(x=470, y=110)
        identry = Entry(a, text="",font=('Arial', 14), width=30)
        identry.place(x=600, y=110)
        namelab = Label(a, text="Name",font=('Arial', 14) , width=10,fg="white",bg="black")
        namelab.place(x=470, y=170)
        nameentry = Entry(a, text="", width=30,font=('Arial', 14))
        nameentry.place(x=600, y=170)
        addlab = Label(a, text="Address",font=('Arial', 14) , width=10,fg="white",bg="black")
        addlab.place(x=470, y=230)
        addressentry = Text(a, height=2, width=31,font=('Arial', 14))
        addressentry.place(x=600, y=230)
        mobilelab = Label(a, text="Mobile",font=('Arial', 14) , width=10,fg="white",bg="black")
        mobilelab.place(x=470, y=290)
        mobileentry = Entry(a, text="",font=('Arial', 14), width=30)
        mobileentry.place(x=600, y=290)
        emaillab = Label(a, text="Email", font=('Arial', 14) , width=10,fg="white",bg="black")
        emaillab.place(x=470, y=350)
        emailentry = Entry(a, text="",font=('Arial', 14), width=30)
        emailentry.place(x=600, y=350)
        passwordlab = Label(a, text="Password",font=('Arial', 14) ,  width=10,fg="white",bg="black")
        passwordlab.place(x=470, y=410)
        passentry = Entry(a, text="",  width=30,show="*",fg="black",bg="white",font=('Arial', 14))
        passentry.place(x=600, y=410)
        menubar = Menu(a)
        d = Menu(menubar, tearoff=0)

        d.add_command(label=" Update/Delete", command=up)
        d.add_separator()
        menubar.add_cascade(label="Edit Details", menu=d)
        path6="coustmer registration.jpg"
        img8=ImageTk.PhotoImage(Image.open(path6))
        lab = Label(a,image=img8).place(x=990,y=150)

        a.config(menu=menubar)
        submit = Button(a, text="Submit", command=login, font=('Arial', 16),fg="white",bg="black").place(x=600, y=500)
        cancel = Button(a, text="Cancel", font=('Arial', 16),fg="white",bg="black",command=bck).place(x=695, y= 500)
        panel.pack(side="top")
        a.mainloop()

    def con():
        messagebox.showinfo("Contact Details", "mail :- evetfusion@gmail.com Phone : 1234567890")

    def abt():

        messagebox.showinfo("About Us", "Manage Bussiness/Parties/Weddings/Social Events")
    def book():
        def next():
            def calculate():
                total = 0
                str1 = ""
                if cb1.get() == 1:
                    total = total + 25000
                    str1 = str1 + "DJ-                         25000"
                    #print(str)
                    #print(total)
                if cb2.get() == 1:
                    total = total + 70000
                    str1 = str1 + "\nstage-                    70000"
                    #print(str)
                    #print(total)
                if cb3.get() == 1:
                    total = total + 50000
                    str1 = str1 + "\nmike and speakers-        50000"
                    print(total)
                if cb4.get() == 1:
                    total = total + 100000
                    str1 = str1 + "\nBreakfast-               100000"
                    #print(total)
                if cb5.get() == 1:
                    total = total + 200000
                    str1 = str1 + "\nLunch-                   200000"

                    #print(total)
                if cb6.get() == 1:
                    total = total + 50000
                    str1 = str1 + "\nTea and snacks-           50000"
                    #print(total)
                if cb7.get() == 1:
                    total = total + 500000
                    str1 = str1 + "\nDinner-                  500000"
                    #print(total)
                if num1.get()== "normal":
                    total= total+50000
                    str1 = str1 + "\nNormal Lunch-             50000"
                   # print(total)
                if num1.get() == "delux":
                    total = total + 100000
                    str1 = str1 + "\nDelux Lunch-             100000"
                   # print(total)
                if num1.get() == "Royal":
                    total = total + 200000
                    str1 = str1 + "\nRoyal Lunch-             200000"
                    #print(total)
                if num2.get()== "normal":
                    total= total+50000
                    str1 = str1 + "\nNormal Dinner-            50000"
                    #print(total)
                if num2.get() == "delux":
                    total = total + 100000
                    str1 = str1 + "\nDelux Dinner-            100000"
                    #print(total)
                if num2.get() == "Royal":
                    total = total + 200000
                    str1 = str1 + "\nRoyal Dinner-            200000"
                    #print(total)
                if cb8.get == 1:
                    total = total + 40000
                    str1 = str1 + "\nLightning-                40000"
                   # print(total)
                if cb9.get == 1:
                    total = total + 30000
                    str1 = str1 + "\nFlowers-                  30000"

                    #print(total)
                if cb0.get == 1:
                    total = total + 100000
                    str1 = str1 + "\nSeating-                 100000"

                if number2.get()=="Star Resort":
                    total = total+600000
                    str1 = str1 + "\nVenue-                   600000"
                if number2.get() == "Friends Garden":
                    total = total + 700000
                    str1 = str1 + "\nVenue-                   700000"

                if number2.get() == "Ritumbara Resort" :
                    total = total + 800000
                    str1 = str1 + "\nVenue-                   800000"

                if number2.get() == "Park Classic" :
                    total = total + 1000000
                    str1 = str1 + "\nVenue-                  1000000"

                def submit():
                    #print("Heloo")
                    evt_type = str(number1.get())
                    ven = str(number2.get())
                    date = dateentry.get()
                    userid = int(dateentry2.get())
                    toatl = int(labt.get())
                    def pay():
                        def printval():
                            id = int(uid1.get())
                            if var.get() == "cheque":
                               # messagebox.showinfo("value", "Payment is done by cheque successfully")
                                a = "cheque"
                                st = "paid"
                                sql = "insert into payment(uid,paymenttype,status)" "values('%d','%s','%s')" % (id, a, st)
                                r1 = cursor.execute(sql)
                                if r1 > 0:
                                    messagebox.showinfo("Info", "Payment successfully done")
                                else:
                                    messagebox.showerror("Error", "No payment is done")
                                submit()
                            if var.get() == "cash":
                               # messagebox.showinfo("value", "Payment is done by cash successfully")
                                a = "cash"
                                st = "paid"
                                sql = "insert into payment(uid,paymenttype,status)" "values('%d','%s','%s')" % (id, a, st)
                                r1 = cursor.execute(sql)
                                if r1 > 0:
                                    messagebox.showinfo("Info", "Payment successfully done through Cash")
                                else:
                                    messagebox.showerror("Error", "No payment is done")
                                submit()
                            elif var.get()=="nopay":
                                a = "--"
                                st = "Not Paid"
                                sql = "insert into payment(uid,paymenttype,status) values ('%d','%s','%s')"%(id , a ,st)
                                r = cursor.execute(sql)
                                if r>0 :
                                     messagebox.showwarning("Warning", "No payment is done")
                            else :
                                    messagebox.showwarning("Warning","no Such user exist reenter the user id")
                            db.commit()
                            submit()
                        def bck():
                            new_window()
                        hel = Toplevel(f)
                        hel.title("pay")
                        hel.geometry("2160x1080")
                        head = Label(hel, text="Payment", font=("Monotype Corsiva", 25), width=25)
                        head.place(x=500, y=50)
                        uid = Label(hel, text="User ID", font=('Arial', 20), fg='white', bg='orange')
                        uid.place(x=550, y=150)
                        uid1 = Entry(hel, text="", width=30,font=('Arial', 20))
                        uid1.place(x=660, y=155)
                        hel.configure(background="pink")
                        #path="bg-main_mini.jpg"
                        #img = ImageTk.PhotoImage(Image.open(path))
                        var = StringVar()
                        var.set(0)
                        cheque = Radiobutton(hel, text="By Cheque", value="cheque", variable=var, font=('Arial', 14))
                        cheque.place(x=550, y=250)
                        cash = Radiobutton(hel, text="By Cash", value="cash", variable=var, font=('Arial', 14))
                        cash.place(x=700, y=250)
                        nopay= Radiobutton(hel, text="No Payment", value="nopay", variable=var, font=('Arial', 14))
                        nopay.place(x=850, y=250)

                        butn = Button(hel, text="PAY", font=('Arial', 20), width=5, command=printval)
                        butn.place(x=550, y=350)
                        #panel = Label(hel, image=img)
                        # panel.pack(side="top")


                        butn = Button(hel, text="BACK", font=('Arial', 20), width=5,command=bck)
                        butn.place(x=700, y=350)
                        hel.mainloop()


                    if evt_type and ven and date and userid != "":
                        try:
                            sql2 = "select * from registration where userid='%d'"%(userid)
                            sql = "insert into booking(event_type , event_place,date, userid ,total) values ('%s' , '%s' , '%s' , '%d' ,'%d')" % (evt_type, ven, date, userid, toatl)
                            r = cursor.execute(sql)
                            r1 = cursor.execute(sql2)
                            if r > 0 and r1>0 :
                                messagebox.showinfo('Successful', "Booking Successful")
                                pay()
                            else:
                                messagebox.showerror('Unsuccessfful ', "Booking not Successful, Enter a registered user id")
                                book()

                        except:
                            db.rollback()
                            messagebox.showerror('Error', "Fill the Correct Data")

                    else:
                              messagebox.showwarning('Warning', "Fill all the fields")
                    db.commit()
                def bck():
                    next()
                f = Toplevel(top)
                #ent.insert('0', total)
                f.geometry('2160x1080')
                f.title('Bill')
                entry = Text(f)
                f.configure(background="pink")
                lab = Label(f,text="Invoice").place(x=250,y=10)
                entry.insert("0.0", str1)
                entry.place(x=10, y=45)
               # lab = Label(f,text="_________________________________________________________________________________________________________________________________").place(x=0, y=25)
                labt1 = Label(f,text="total",font=('Arial',12)).place(x=0,y=500)
                labt= Entry(f,text="",font=('Arial',12))
                labt.place(x=80,y=500)
                labt.insert("0",total)
                but = Button(f, text="Confirm Booking", command=submit, font=('Arial', 18), fg="white", bg="black",width=13)
                but.place(x=200, y=600)
                but = Button(f, text="Back", command=bck, font=('Arial', 18), fg="white", bg="black",width=13)
                but.place(x=420, y=600)
                print(total)
                f.mainloop()
            def bck():
                book()
            top = Toplevel(add)
            top.title("Book An Event")
            top.geometry("1366x768")
            top.configure(background="black")
            path="bg-main_mini.jpg"
            img = ImageTk.PhotoImage(Image.open(path))
            panel = Label(top, image=img)
            cb1 = IntVar()
            cb2 = IntVar()
            cb3 = IntVar()
            lab1 = Label(top, text="Equipments", font=('Monotype Corsiva', 30), width=10,fg="white",bg="orange")
            lab1.place(x=100, y=50)
            cbdj = Checkbutton(top, text="DJ", variable=cb1, onvalue=1, offvalue=0,font=('Arial',18))
            cbdj.place(x=400, y=150)
            cbstage = Checkbutton(top, text="STAGE", variable=cb2, onvalue=1, offvalue=0,font=('Arial',18))
            cbstage.place(x=550, y=150)
            cbms = Checkbutton(top, text="MIKE and SPEAKERS", variable=cb3, onvalue=1, offvalue=0,font=('Arial',18))
            cbms.place(x=750, y=150)

            cb4 = IntVar()
            cb5 = IntVar()
            cb6 = IntVar()
            cb7 = IntVar()
            lab1 = Label(top, text="Food", font=('Monotype Corsiva', 30), width=10,fg="white",bg="orange")
            lab1.place(x=100, y=200)
            cbb = Checkbutton(top, text="BREAKFAST", variable=cb4, onvalue=1, offvalue=0,font=('Arial',18))
            cbb.place(x=350, y=320)
            cbl = Checkbutton(top, text="LUNCH", variable=cb5, onvalue=1, offvalue=0,font=('Arial',18))
            cbl.place(x=550, y=320)
            cbts = Checkbutton(top, text="TEA and SNACKS", variable=cb6, onvalue=1, offvalue=0,font=('Arial',18))
            cbts.place(x=690, y=320)
            cbd = Checkbutton(top, text="DINNER", variable=cb7, onvalue=1, offvalue=0,font=('Arial',18))
            cbd.place(x=970, y=320)

            num1 = StringVar()
            lbll = Label(top, text="Lunch Type",font = ("arial",18))
            lbll.place(x=400, y=400)
            cb = Combobox(top, textvariable=num1, state="readonly", width=30,font = ("arial",10))
            cb["values"] = ("Normal", "Delux", "Royal")
            cb.place(x=610, y=400)
            cb.current(0)

            lbld = Label(top, text="Dinner Type",font = ("arial",18))
            lbld.place(x=400, y=450)
            num2 = StringVar()
            cb = Combobox(top, textvariable=num2, state="readonly", width=30,font = ("arial",10))
            cb["values"] = ("Normal", "Delux", "Royal")
            cb.place(x=610, y=450)
            cb.current(0)

            cb8 = IntVar()
            cb9 = IntVar()
            cb0 = IntVar()
            lbld = Label(top, text="Decoration", font=('Monotype Corsiva', 30),fg="white",bg="orange",width=10)
            lbld.place(x=100, y=500)
            cbl = Checkbutton(top, text="Lightings", variable=cb8, onvalue=1, offvalue=0,font=('Arial',18))
            cbl.place(x=450, y=600)
            cbts = Checkbutton(top, text="Flowers", variable=cb9, onvalue=1, offvalue=0,font=('Arial',18))
            cbts.place(x=600, y=600)
            cbd = Checkbutton(top, text="Seating", variable=cb0, onvalue=1, offvalue=0,font=('Arial',18))
            cbd.place(x=750, y=600)
            but = Button(top, text="Calculate", command=calculate,font=('Arial',18),bg="black",fg="white",width=8)
            but.place(x=890, y=520)
          #  ent = Entry(top,text="",font=('Arial',20))
          #  ent.place(x=1030,y=520)
            but2 = Button(top, text="Back", command=bck, font=('Arial', 18), bg="black", fg="white", width=8)
            but2.place(x=890, y=570)
            panel.pack(side="top")
            top.mainloop()
        def bck():
            new_window()
        add = Toplevel(top)
        add.title("Book an Event")
        add.geometry("2160x1080")
        path = "53b0150c46fd23eb14d2c025b09e579d.jpg"
        path1 = "pic.jpg"
        img2 = ImageTk.PhotoImage(Image.open(path1))
        lab = Label(add,image=img2).place(x=500,y=100)
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(add, image=img)
        lbl1 = Label(add, text="BOOK VENUE", font=('Monotype Corsiva', 20), width=20,fg="white",bg="orange")
        lbl1.place(x=590, y=20)
        #lbl2 = Label(add, text="Booking ID", font=('Arial', 15), width=9,fg="white",bg="orange")
        #lbl2.place(x=500, y=140)
        #identry = Entry(add, text="", width=30,fg="black",bg="white",font=('Arial', 15))
        #identry.place(x=630, y=140)

        lblevent = Label(add, text="Event Type", font=('Arial', 15), width=9,fg="white",bg="orange")
        lblevent.place(x=500, y=240)
        number1 = StringVar()
        cb1 = Combobox(add, textvariable=number1, state="readonly", width=28,font=('Arial', 15))
        cb1["values"] = ("--EVENT TYPE--", "Marrige", "Party", "Social Event ", "Business meeting")
        cb1.place(x=630, y=240)
        cb1.current(0)

        lblvenue = Label(add, text="Venue ", font=('Arial', 15), width=9,fg="white",bg="orange")
        lblvenue.place(x=500, y=320)
        number2 = StringVar()
        def combo_input():
            cursor.execute("select venue from venue")
            data = []
            for row in cursor.fetchall():
                data.append(row[0])
            return data
        cb2 = Combobox(add,font=('Arial',15),width=28,textvariable=number2)
        cb2["values"] = combo_input()
        cb2.place(x=630, y=320)
        cb2.current(0)

        lbl4 = Label(add, text="Date", font=('Arial', 15), width=9,fg="white",bg="orange")
        lbl4.place(x=500, y=400)
        dateentry = Entry(add, text="", width=30,fg="black",bg="white",font=('Arial', 15))
        dateentry.place(x=630, y=400)
        lbl5 = Label(add, text="User Id", font=('Arial', 15), width=9, fg="white", bg="orange")
        lbl5.place(x=500, y=480)
        dateentry2 = Entry(add, text="", width=30, fg="black", bg="white", font=('Arial', 15))
        dateentry2.place(x=630, y=480)

        but = Button(add, text="Next", command=next, width=5, font=('Arial', 15),fg="white",bg="black")
        but.place(x=600, y=530)
        back = Button(add, text="Back", width=5, font=('Arial', 15),fg="white",bg="black",command=bck)
        back.place(x=700, y=530)
        panel.pack(side="top")
        add.mainloop()
    def admin():
        def window():
            def venue():
                def add_venue():
                    txt=str(number.get())
                    ven = entry1.get()
                    cst = int(entry.get())
                    if txt and ven and cst !="":
                        sql = "Insert into venue(venue , amount) values('%s','%d')"%(ven , cst)
                        r = cursor.execute(sql)
                        if r>0:
                            messagebox.showinfo('Success',"Venue Successfully added")
                        else:
                            messagebox.showinfo('Unsuccessful','No venue added')
                    else:
                        messagebox.showwarning('Warning',"Fill all the fields")
                    window()
                tool = Toplevel(q)
                tool.title("Add Venus")
                tool.geometry("2160x1080")
                path = "bg-main_mini.jpg"
                ime = ImageTk.PhotoImage(Image.open(path))
                panel = Label(tool, image=ime)
                lblh = Label(tool, text="Add Venues", font=('Monotype Corsiva', 25),fg="white",bg="orange",width=20)
                lblh.place(x=500, y=50)
                lblevent = Label(tool, text="Event Type ", font=('Monotype Corsiva', 15),fg="white",bg="orange",width=10)
                lblevent.place(x=450, y=170)
                number = StringVar()
                lbleven = Combobox(tool, textvariable=number, state="readonly", width=30,font=('Monotype Corsiva', 15))
                lbleven["values"] = ("--Event Type--", "Marrige", "Party", "Social Event ", "Business meeting")
                lbleven.place(x=600, y=170)
                lbleven.current(0)

                lblvenue = Label(tool, text="Venue ", font=('Monotype Corsiva', 15),fg="white",bg="orange",width=10)
                lblvenue.place(x=450, y=270)
                entry1 = Entry(tool, text="",font=('Monotype Corsiva', 15),fg="black",bg="white",width=33)
                entry1.place(x=600, y=270)
                path1 = "index2.jpg"
                pane = ImageTk.PhotoImage(Image.open(path1))
                lab = Label(tool, image=pane, width=300,height=180)
                lab.place(x=520, y=470)
                panel.pack(side="top")
                btn = Label(tool, text="Cost",font=('Monotype Corsiva', 15),fg="white",bg="orange",width=10)
                btn.place(x=450, y=350)
                entry = Entry(tool, text="", width=33,font=('Monotype Corsiva', 15),fg="black",bg="white")
                entry.place(x=600, y=350)
                But = Button(tool,text="ADD VENUE",fg="white",bg="black",font=('Arial', 13),command=add_venue).place(x=600,y=400)
                tool.mainloop()
            def adm():
                def bck():
                    window()
                yup = Toplevel(q)
                yup.title("Add Admin")
                yup.geometry("1366x768")
                path = "bg-main_mini.jpg"
                img = ImageTk.PhotoImage(Image.open(path))
                panel = Label(yup, image=img)
                panel.pack()

                def insert():
                    if aname.get() and apass.get() and adept.get() != "":
                        name = aname.get()
                        password = apass.get()
                        department = adept.get()
                        sql = "insert into admin(name,password,department)values('%s','%s','%s')" % (name, password, department)
                        r = cursor.execute(sql)
                        if r > 0:
                            messagebox.showinfo("Message", "Admin Registered Successfully")
                        else:
                            messagebox.showerror("Error", "No Admin Registered")
                    else :
                        messagebox.showerror('Unsuccessful'," Fill all the details")
                    db.commit()
                    window()
                head = Label(yup, text="ADD MEMBER", font=('Monotype Corsiva', 25), fg='white', bg='orange')
                head.place(x=580, y=20)
                aname = Label(yup, text="Name", font=('Monotype Corsiva', 20),width=8, fg='white', bg='orange')
                aname.place(x=500, y=120)
                aname = Entry(yup, text="", width=30, font=('Monotype Corsiva', 20))
                aname.place(x=650, y=120)
                apass = Label(yup, text="Password", font=('Monotype Corsiva', 20),width=8, fg='white', bg='orange')
                apass.place(x=500, y=220)
                apass = Entry(yup, text="", width=30,show="*",font=('Monotype Corsiva', 20))
                apass.place(x=650, y=220)
                adept = Label(yup, text="Department:", font=('Monotype Corsiva', 20), fg='white', bg='orange')
                adept.place(x=500, y=320)
                adept = Entry(yup, text="", width=30,font=('Monotype Corsiva', 20))
                adept.place(x=650, y=325)
                btn1 = Button(yup, text="ADD ADMIN", command=insert, font=('Arial', 15), fg='white', bg='black')
                btn1.place(x=550, y=430)
                btn1 = Button(yup, text="CANCEL", command=bck, font=('Arial', 15), fg='white', bg='black')
                btn1.place(x=750, y=430)
                yup.mainloop()
                #new_window()
            def rc():
                    r = Toplevel(q)
                    r.title('Coustmers Details')
                    r.geometry('2180x1080')
                    tree = Treeview(r)
                    tree["column"] = ("userid", "name", "address", "mobile", "email")

                    tree.column("userid", width=40)
                    tree.column("name", width=100)
                    tree.column("address", width=100)
                    tree.column("mobile", width=50)
                    tree.column("email", width=120)
                    # tree.column("password", width=100)
                    tree.heading("userid", text="User Id")
                    tree.heading("name", text="Name")
                    tree.heading("address", text="Address")
                    tree.heading("mobile", text="Mobile")
                    tree.heading("email", text="Email")
                    sql = "select * from registration"
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for i in rows:
                        userid = i[0]
                        name = i[1]
                        address = i[2]
                        mobile = i[3]
                        email = i[4]
                        tree.insert("",0,text="", values=(userid, name, address, mobile, email))
                    tree.pack()
                    r.mainloop()
                    #new_window()
            def ad():
                r = Toplevel(q)
                r.title('Coustmers Details')
                r.geometry('2180x1080')
                tree = Treeview(r)
                tree["column"] = ("aid", "name", "department")

                tree.column("aid", width=40)
                tree.column("name", width=100)
                tree.column("department", width=100)
                tree.heading("aid", text="Admin Id")
                tree.heading("name", text="Name")
                tree.heading("department", text="Department")

                sql = "select * from admin"
                cursor.execute(sql)
                rows = cursor.fetchall()
                for i in rows:
                    aid = i[0]
                    name = i[1]
                    department = i[3]
                    tree.insert("", 0, text="", values=(aid, name, department))
                tree.pack()
                r.mainloop()
            def de():
                tool = Toplevel(q)
                tool.title("price of items")
                tool.geometry("1366x768")
                tree = Treeview(tool)
                tree["column"] = ("itemname", "price")
                tree.column("itemname", width=150)
                tree.column("price", width=70)
                tree.heading("itemname", text="Itemname")
                tree.heading("price", text="Price")
                sql = "select * from eitems"
                cursor.execute(sql)
                rows = cursor.fetchall()
                for i in rows:
                    itemname = i[0]
                    price = i[1]
                    tree.insert("", 0, values=(itemname, price))
                tree.place(x=430, y=150)

                tool.mainloop()
            def lg():
                new_window()
            q = Toplevel(w)
            q.geometry("2160x1080")
            q.title('Admin Block')

            path1 = "index.jpg"
            path2 = "index2.jpg"
            path3 = "index3.jpg"
            path4="SocialPro16-1920x1080-OG-1.png"
            img6 = ImageTk.PhotoImage(Image.open(path1))
            img7 = ImageTk.PhotoImage(Image.open(path2))
            img8 = ImageTk.PhotoImage(Image.open(path3))
            img9= ImageTk.PhotoImage(Image.open(path4))
            path = "53b0150c46fd23eb14d2c025b09e579d.jpg"
            img = ImageTk.PhotoImage(Image.open(path))
            lab10 = Label(q, image=img6, width=300, height=170).place(x=200, y=100)
            lab10 = Label(q, text="Party", fg="white", bg="black", width=5, font=('Arial', 14)).place(x=300, y=280)
            lab9 = Label(q, image=img7, width=300, height=170).place(x=600, y=100)
            lab9 = Label(q, text="Wedding", fg="white", bg="black", width=8, font=('Arial', 14)).place(x=700, y=280)
            lab8 = Label(q, image=img8, width=280, height=150).place(x=400, y=400)
            lab8 = Label(q, text="Bussiness", fg="white", bg="black", width=8, font=('Arial', 14)).place(x=500, y=580)
            lab11 = Label(q, image=img9, width=300, height=170).place(x=850, y=400)
            lab11 = Label(q, text="Social", fg="white", bg="black", width=8, font=('Arial', 14)).place(x=940, y=580)
            q.configure(background="pink")
            menubar = Menu(q)
            a = Menu(menubar, tearoff=0)
            b = Menu(menubar, tearoff=0)
            c = Menu(menubar, tearoff=0)
            d = Menu(menubar,tearoff=0)
            a.add_command(label="Add Admin",command=adm)
            a.add_separator()
            menubar.add_cascade(label="Add Admin",menu=a)
            q.configure(menu=menubar)
            b.add_command(label="Add Venue",command=venue)
            b.add_separator()
            menubar.add_cascade(label="Add venue", menu=b)
            c.add_command(label="Registered Coustmers",command=rc)
            c.add_command(label="Admin Details",command=ad)
            c.add_separator()
            c.add_command(label="Prices of events",command=de)
            c.add_separator()
            menubar.add_cascade(label="Report", menu=c)
            d.add_command(label="logout",command=lg)
            d.add_separator()
            menubar.add_cascade(label="Logout",menu=d)

            #panel = Label(q,image=img)
            #panel.pack(side="top")
            q.mainloop()
            #new_window()
        def log():
            user= ent1.get()
            pas = ent2.get()
            if user and pas != "" :
                  sql = "select * from admin where name='%s' and password='%s'" %(user,pas)
                  r = cursor.execute(sql)
                  if r>0:
                      window()
                  else:
                      messagebox.showerror('Error',"Enter the correct username or password")
                      new_window()
            else :
                messagebox.showwarning('Warning',"Fill all the fields")

            db.commit()
            #new_window()
        def bck():
            new_window()
        '''def fog():
            def update():
                password = ent2.get()
                cpassword = ent3.get()
                id = ent1.get()
                if password == cpassword:
                    sql = "update admin set password = %s where user aid = %d " % (password, id)
                    r = cursor.execute(sql)
                    if r > 0:
                        messagebox.showinfo('Info', "Password changed successfully")
                    else:
                        messagebox.showerror("Error", "Enter the correct user id ")
                else :
                    messagebox.showerror("Error", "Password doesnt matched")
                    new_window()
                db.commit()
            def bck():
                new_window()
            k = Toplevel(w)
            k.geometry('2160x1080')
            k.title('Forgot password')
            k.configure(background='black')
            path = "bg-main_mini.jpg"
            img = ImageTk.PhotoImage(Image.open(path))
            panel = Label(k, image= img)
            lab = Label(k, text="Forgot Password", font=('Monotype Corsiva', 30), width=20, fg="white", bg="orange").place(
                x=450, y=60)
            lab = Label(k, text="User id", font=('Monotype Corsiva', 15), width=13, fg="white", bg="orange").place(
                x=370, y=210)
            ent1 = Entry(k, text="", font=('Monotype Corsiva', 15), width=40, fg="black")
            ent1.place(x=540, y=210)
            lab = Label(k, text="New Password", font=('Monotype Corsiva', 15), width=13, fg="white", bg="orange").place(
                x=380, y=280)
            ent2 = Entry(k, text="", font=('Monotype Corsiva', 15), width=40, fg="black")
            ent2.place(x=540, y=280)
            lab = Label(k, text="Confirm password", font=('Monotype Corsiva', 15), width=13, fg="white", bg="orange").place(
                x=380, y=340)
            ent3 = Entry(k, text="", font=('Monotype Corsiva', 15), width=40, fg="black", show="*")
            ent3.place(x=540, y=340)
            but1 = Button(k, text="Update", font=('Arial', 15), fg="white", bg="black", width=15, command=update).place(
                x=500, y=400)
            but2 = Button(k, text="Back", font=('Arial', 15), fg="white", bg="black", width=15, command=bck).place(
                x=700, y=400)

            panel.pack(side="top")
            k.mainloop()'''

        w = Toplevel(top)
        w.geometry('2160x1080')
        w.title('Admin')
        w.configure(background="black")
        path="bg-main_mini.jpg"
        img=ImageTk.PhotoImage(Image.open(path))
        panel = Label(w, image=img)
        lab = Label(w,text="Admin Login",font=('Monotype Corsiva',30),width=20,fg="white",bg="orange").place(x=450,y=60)
        lab = Label(w,text="Username",font=('Monotype Corsiva',15),width=13,fg="white",bg="orange").place(x=370,y=210)
        ent1= Entry(w,text="",font=('Monotype Corsiva',15),width=40,fg="black")
        ent1.place(x=540,y=210)
        lab = Label(w, text="Password", font=('Monotype Corsiva', 15), width=13, fg="white", bg="orange").place(x=370,y=310)
        ent2 = Entry(w, text="", font=('Monotype Corsiva', 15), width=40, fg="black",show="*")
        ent2.place(x=540, y=310)
        but1 = Button(w,text="Login",font=('Arial',15),fg="white",bg="black",width=15,command=log).place(x=450,y=400)
        but2 = Button(w, text="Cancel", font=('Arial', 15), fg="white", bg="black", width=15,command=bck).place(x=650, y=400)
       # but3 = Button(w,text="Forgot Password",font=('Arial',15),fg = "white",bg="Black",width=15,command=fog).place(x=770,y=400)
        panel.pack(side="top")
        w.mainloop()
    def cusdetail():
        def de():

            tree = Treeview(c)
            tree["column"] = ( "userid", "event_type","event_place","date","total")

            tree.column("userid")
            tree.column("event_type", width=100)
            tree.column("event_place", width=100)
            tree.column("date",width=100)
            tree.column("total",width=100)

            tree.heading("userid",text="User Id")
            tree.heading("event_type",text="Event_type")
            tree.heading("event_place",text="Event_place")
            tree.heading("date",text="Date")
            tree.heading("total",text="Total")
            id = int(ent1.get())
            name = ent2.get()
            if id and name !="":

                sql = "select * from booking where userid='%d' "%(id)

                cursor.execute(sql)
                rows = cursor.fetchall()
                for i in rows:
                   event_type = i[1]
                   event_place = i[2]
                   date = i[3]
                   userid = i[4]
                   total = i[5]
                   tree.insert("", 0, text="", values=(userid, event_type, event_place,date,total))
            else :
                  messagebox.showwarning('Warning ',"Fill all The fields")
            tree.place(x=200,y=500)
        def bck():
            new_window()
        def t():
            def u():
                def print():

                    id = int(uid1.get())
                    if id != " ":
                        if var.get() == "cheque":
                            messagebox.showinfo("value", "Payment is done by cheque successfully")
                            a = "cheque"
                            st = "paid"
                            sql = "update  payment set paymenttype='%s',status='%s' where uid='%d' " % (a, st, id)
                            r1 = cursor.execute(sql)
                            if r1 > 0:
                                messagebox.showinfo("Info", "Payment successfully done by cheque")
                            else:
                                messagebox.showerror("Error", "No payment is done")

                        if var.get() == "cash":
                            # messagebox.showinfo("value", "Payment is done by cash successfully")
                            a = "cash"
                            st = "paid"
                            sql = "update  payment set paymenttype='%s',status='%s' where uid='%d'" % (a, st, id)
                            r1 = cursor.execute(sql)
                            if r1 > 0:
                                messagebox.showinfo("Info", "update Payment successfully done through Cash")
                            else:
                                messagebox.showerror("Error", "No update of payment is done")

                    else:
                        messagebox.showerror('Error', "Fill all the fields")
                    new_window()
                r = Toplevel(y)
                r.geometry('2160x1080')
                r.title('Status Change')
                lab = Label(r, text=" Status Update", font=('Monotype Corsiva', 20), bg="orange", fg="white").place(x=500, y=30)
                uid = Label(r, text="User ID", font=('Arial', 15), fg='white', bg='orange')
                uid.place(x=550, y=150)
                uid1 = Entry(r, text="", width=30, font=('Arial', 15))
                uid1.place(x=660, y=155)
                var = StringVar()
                r.configure(background="pink")
                var.set(0)
                cheque = Radiobutton(r, text="By Cheque", value="cheque", variable=var, font=('Arial', 14))
                cheque.place(x=550, y=250)
                cash = Radiobutton(r, text="By Cash", value="cash", variable=var, font=('Arial', 14))
                cash.place(x=700, y=250)
                butn = Button(r  , text="Update", font=('Monotype Corsiva', 15), width=6, command=print,fg="white",bg="black")
                butn.place(x=550, y=350)
            y = Toplevel(c)
            y.title('Payment Info')
            y.geometry('2160x1080')
            tree = Treeview(y)
            tree["column"] = ("paymentid", "Userid", "paymenttype", "status")
            tree.column("paymentid", width=100)
            tree.column("Userid",width=100)
            tree.column("paymenttype", width=100)
            tree.column("status", width=100)

            tree.heading("paymentid", text="Payment_id")

            tree.heading("Userid", text="User Id")
            tree.heading("paymenttype", text="Payment_type")
            tree.heading("status", text="Status")
            id = int(ent1.get())
            name = ent2.get()
            if id and name != "":

                sql = "select * from payment where uid='%d' " % (id)

                cursor.execute(sql)
                rows = cursor.fetchall()
                for i in rows:
                    paymentid = i[0]
                    userid = i[1]
                    paymenttype = i[2]
                    status = i[3]
                    #total = i[5]
                    tree.insert("", 0, text="", values=(paymentid, userid, paymenttype, status))
            else:
                messagebox.showwarning('Warning ', "Fill all The fields")
            db.commit()
            tree.place(x=200, y=50)
            menubar = Menu(y)
            d = Menu(menubar, tearoff=0)
            d.add_command(label="Update", command=u)
            d.add_separator()
            menubar.add_cascade(label="Update Status", menu=d)
            y.configure(menu=menubar)
            y.mainloop()
        c = Toplevel(top)
        c.title('Customer Details')
        c.geometry('2160x1080')
        path="bg-main_mini.jpg"
        img= ImageTk.PhotoImage(Image.open(path))
        panel = Label(c,image=img)
        lab = Label(c,text="Coustmer Details",font=('monotype corsiva',20),bg="orange",fg="white").place(x=600,y=30)
        lab = Label(c,text="User Id",font=('Monotype Corsiva',17),bg="orange",fg="white",width=8).place(x=400,y=150)
        ent1 = Entry(c,text="",font=('Monotype Corsiva',17),width=30)
        ent1.place(x=600,y=150)
        lab = Label(c, text="User Name", font=('Monotype Corsiva', 17), bg="orange", fg="white",width=8).place(x=400, y=250)
        ent2 = Entry(c, text="", font=('Monotype Corsiva', 17), width=30)
        ent2.place(x=600, y=250)
        but = Button(c,text="Submit",fg="white",bg="black",font=('Monotype Corsiva',15),width=9,command=de).place(x=500,y=400)
        but2 = Button(c, text="Back", fg="white", bg="black", font=('Monotype Corsiva', 15), width=9,command=bck).place(x=650, y=400)
        but3 = Button(c, text="Payment Info", fg="white", bg="black", font=('Monotype Corsiva', 15), width=10,command=t).place(x=770, y=400)
        panel.pack(side="top")
        c.mainloop()
    def ex():
        sys.exit()
    top = Toplevel(root)
    top.geometry('2160x1080')
    top.title('Home')
    path = "admin.png"
    path2 = "53b0150c46fd23eb14d2c025b09e579d.jpg"
    path3 = "coustmer.png"
    path4 = "coustmer registration.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    img2 = ImageTk.PhotoImage(Image.open(path2))
    img3 = ImageTk.PhotoImage(Image.open(path3))
    img4 = ImageTk.PhotoImage(Image.open(path4))
    path5 = "images.jpg"
    img5= ImageTk.PhotoImage(Image.open(path5))
    panel = Label(top, image=img2)
    menubar = Menu(top)
    Home = Menu(menubar, tearoff=0)
    Contact = Menu(menubar, tearoff=0)
    about = Menu(menubar, tearoff=0)
    Login = Menu(menubar, tearoff=0)
    # Home.add_command(label=" Back to Home",command=call)
    # Home.add_separator()
    # menubar.add_cascade(label=" Home", menu=Home)
    Contact.add_command(label=" Contact Details", command=con)
    Contact.add_separator()
    menubar.add_cascade(label=" Contact", menu=Contact)
    about.add_command(label=" About Us", command=abt)
    about.add_separator()
    menubar.add_cascade(label=" About", menu=about)
    # Login.add_command(label="Login",command=login)
    # Login.add_separator()
    # menubar.add_cascade(label="Login",menu =Login)
    top.config(menu=menubar)
   # adminlab = Label(top, text="Admin", font=('Times new roman', 15), fg="green", bg="Black").place(x=200, y=200)
    label = Label(top, text="Event Fusion", font=('times new roman', 30), fg="white", bg="black", width=20).place(x=450, y=50)

    label3 = Label(top, text="Admin Login", font=('Times new roman', 25), fg="white", bg="black", width=17).place(x=180,y=250)
    admin = Button(top, text="Admin", width=120, image=img, height=100,command=admin).place(x=500, y=210)
    label2 = Label(top, text="Customer Details", font=('Times new roman', 25), fg="white", bg="black", width=17).place(x=180, y=470)
    coustmer = Button(top, text="Customer Details", width=120, height=100, image=img3,command=cusdetail).place(x=500, y=450)
    label = Label(top, text="Customer ", font=('times new roman', 25), fg="white", bg="black",width=17).place(x=660, y=250)
    coustmer_reg = Button(top, text="Customer", width=120, height=100, image=img4, command=registration).place(x=980,y=210)
    label4 = Label(top, text="Book an Event", font=('times new roman', 25), fg="white", bg="black",width=17).place(x=660, y=470)
    coustmer_reg = Button(top, text="Customer", width=120, height=100, image=img5, command=book).place(x=980,y=450)
    exit1 = Button(top, text="Exit",font=('arial',20),bg="black",fg="white", command=ex).place(x=600,y=600)

    panel.pack(side="top")
    # root.destroy()
    top.mainloop()

root = Tk()
root.title("Event Management")
root.geometry("2860x1080")
root.configure(background='grey')
path = "Beautiful-candle-lights-at-night-wishes - Copy.jpg"
img = ImageTk.PhotoImage(Image.open(path))
label2 = Label(root, text="Event Fusion", font=('times new roman', 30), fg="white", bg="black").place(x=10, y=70)
# lab = Label(root,text="contact no:- 9182772389 , 7845536298",font=('Arial',14),fg="white",bg="black",width=31).place(x=5,y=20)
panel = Button(root, image=img,command=new_window)
lab = Label(root, text="email:-eventfusion@gmail.com", font=('Arial', 14), fg="white", bg="black", width=31).place(x=50,y=630)
lab = Label(root, text="contact no:- 9182772389 , 7845536298", font=('Arial', 14), fg="white", bg="black",width=31).place(x=50, y=658)
panel.pack(side="top")
root.mainloop()