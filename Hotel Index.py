from tkinter import ttk
from Hotel_backend import *


class MainWindow:
    def __init__(self, main):
        self.main = main
        self.main.geometry('1530x770+0+0')
        self.main.title("Hotel Management System")
        self.main.config(bg='powder blue')

        # ======================================Frames============================================================

        frame = Frame(self.main, height=770, width=1530)
        frame.pack()

        mainframe = Frame(frame, height=765, width=1200)
        mainframe.pack(side=LEFT)
        mainframe.pack_propagate(0)

        sideframe = Frame(frame, height=765, width=330)
        sideframe.pack(side=RIGHT)
        sideframe.pack_propagate(0)

        topframe = Frame(mainframe, bd=14, bg='cadet blue', relief='ridge', height=100, width=1200)
        topframe.pack(side=TOP)
        topframe.pack_propagate(0)

        midframe = Frame(mainframe, bd=14, bg='cadet blue', relief='ridge', height=665, width=1200, padx=20, pady=20)
        midframe.pack(side=BOTTOM)
        midframe.pack_propagate(0)

        leftframe = Frame(midframe, bd=14, bg='powder blue', relief='ridge', height=597, width=766, pady=106, padx=94)
        leftframe.pack(side=LEFT)
        leftframe.grid_propagate(0)

        rightframe = Frame(midframe, bg='powder blue', height=597, width=366)
        rightframe.pack(side=RIGHT)
        rightframe.pack_propagate(0)

        rightcancel = Frame(rightframe, bd=14, bg='powder blue', relief='ridge', height=299, width=366, pady=50)
        rightcancel.pack(side=TOP)
        rightcancel.pack_propagate(0)

        rightbill = Frame(rightframe, bd=14, bg='powder blue', relief='ridge', height=298, width=366, pady=50)
        rightbill.pack(side=BOTTOM)
        rightbill.pack_propagate(0)

        buttonframe = Frame(sideframe, bd=14, bg='powder blue', relief='ridge', height=765, width=330, padx=58.4,
                            pady=100)
        buttonframe.pack()
        buttonframe.grid_propagate(0)

        Name = StringVar()
        Surname = StringVar()
        Email = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        Room = StringVar()
        Meal = StringVar()
        Chin = StringVar()
        Chout = StringVar()
        Cid = StringVar()
        billid = StringVar()

        # =======================================Functions=========================================================

        def exit():
            iexit = tkinter.messagebox.askyesno('Hotel System', 'Confirm, If you Want to exit?')
            if iexit > 0:
                root.destroy()
                return

        def reset():
            Name.set('')
            Surname.set('')
            Email.set('')
            Address.set('')
            Mobile.set('')
            Room.set('')
            Meal.set('')
            Chin.set('')
            Chout.set('')
            Cid.set('')
            billid.set('')

        def submit():
            a = Name.get()
            b = Surname.get()
            c = Email.get()
            d = Address.get()
            e = Mobile.get()
            f = Room.get()
            g = Meal.get()
            h = Chin.get()
            i = Chout.get()
            addnew(a, b, c, d, e, f, g, h, i)

        def delete():
            a = str(Cid.get())
            cancel(a)

        def bill():
            generate_bill(billid.get())

        # =======================================Widgits============================================================

        self.lblwelcome = Label(topframe, text='WELCOME To Hotel TAJ', bg='powder blue', font='times 36 bold').pack(
            pady=5)

        self.lblnew = Label(midframe, text='  New Bookings  ', bg='cadet blue', font='times 25 bold',
                            relief='solid').place(x=263, y=40)

        self.lblname = Label(leftframe, text='Name: ', bg='powder blue', font='times 16 bold').grid(row=0, column=0,
                                                                                                    pady=5)
        self.txtname = Entry(leftframe, font='times 16 bold', textvariable=Name, width=35).grid(row=0, column=1)

        self.lblsurname = Label(leftframe, text='Surname: ', bg='powder blue', font='times 16 bold').grid(row=1,
                                                                                                          column=0,
                                                                                                          pady=5)
        self.txtsurn = Entry(leftframe, font='times 16 bold', textvariable=Surname, width=35).grid(row=1, column=1)

        self.lblemail = Label(leftframe, text='Email: ', bg='powder blue', font='times 16 bold').grid(row=2, column=0,
                                                                                                      pady=5)
        self.txtemail = Entry(leftframe, font='times 16 bold', textvariable=Email, width=35).grid(row=2, column=1)

        self.lbladdress = Label(leftframe, text='Address: ', bg='powder blue', font='times 16 bold').grid(row=3,
                                                                                                          column=0,
                                                                                                          pady=5)
        self.txtaddress = Entry(leftframe, font='times 16 bold', textvariable=Address, width=35).grid(row=3, column=1)

        self.lblmobile = Label(leftframe, text='Mobile No.', bg='powder blue', font='times 16 bold').grid(row=4,
                                                                                                          column=0,
                                                                                                          pady=5)
        self.txtmobile = Entry(leftframe, font='times 16 bold', textvariable=Mobile, width=35).grid(row=4, column=1)

        self.lblroom = Label(leftframe, text='Room Type: ', bg='powder blue', font='times 16 bold').grid(row=5,
                                                                                                         column=0,
                                                                                                         pady=5)
        self.cboroom = ttk.Combobox(leftframe, textvariable=Room, state='readonly', font='times 15', width=35,
                                    value=('Single Deluxe', 'Double Deluxe', 'Executive', 'Suit')).grid(row=5, column=1)

        self.lblmeal = Label(leftframe, text='Meal Type: ', bg='powder blue', font='times 16 bold').grid(row=6,
                                                                                                         column=0,
                                                                                                         pady=5)
        self.cbomeal = ttk.Combobox(leftframe, textvariable=Meal, state='readonly', font='times 15', width=35,
                                    value=('Breakfast', 'Dinner', 'Combo', 'All three')).grid(row=6, column=1)

        self.lblcheckin = Label(leftframe, text='Check In Date: ', bg='powder blue', font='times 16 bold').grid(row=7,
                                                                                                                column=0,
                                                                                                                pady=5)
        self.txtchecin = Entry(leftframe, font='times 16 bold', textvariable=Chin, width=25).grid(row=7, column=1)

        self.lblcheckout = Label(leftframe, text='Check Out Date: ', bg='powder blue', font='times 16 bold').grid(row=8,
                                                                                                                  column=0,
                                                                                                                  pady=5)
        self.txtcheckout = Entry(leftframe, font='times 16 bold', textvariable=Chout, width=25).grid(row=8, column=1)

        self.lblcancel = Label(rightcancel, text='  Cancel Bookings  ', bg='cadet blue', font='times 25 bold',
                               relief='solid').pack()
        self.lblid = Label(rightcancel, text='Booking ID ', bg='powder blue', font='times 16 bold').pack(pady=20)
        self.txtid = Entry(rightcancel, font='times 16 bold', textvariable=Cid, width=25).pack()

        self.lblmakebill = Label(rightbill, text='  Generate Bill  ', bg='cadet blue', font='times 25 bold',
                                 relief='solid').pack()
        self.lblid = Label(rightbill, text='Booking ID ', bg='powder blue', font='times 16 bold').pack(pady=20)
        self.txtid = Entry(rightbill, font='times 16 bold', textvariable=billid, width=25).pack()

        # ======================================Buttons============================================================

        self.btn1 = Button(buttonframe, bd=4, text='Show Bookings', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=showbookings).grid(row=0,
                                                                                                             column=0,
                                                                                                             pady=8)

        self.btn2 = Button(buttonframe, bd=4, text='Submit', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=submit).grid(row=1, column=0,
                                                                                                       pady=8)

        self.btn3 = Button(buttonframe, bd=4, text='Clear', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=reset).grid(row=2, column=0,
                                                                                                      pady=8)

        self.btn4 = Button(buttonframe, bd=4, text='Cancel', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=delete).grid(row=3, column=0,
                                                                                                       pady=8)
        self.btn5 = Button(buttonframe, bd=4, text='Generate Bill', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=bill).grid(row=4, column=0,
                                                                                                     pady=8)

        self.btn6 = Button(buttonframe, bd=4, text='Exit', height=2, width=13, font='arial 16 bold',
                           activebackground="pink", activeforeground="dark blue", command=exit).grid(row=5, column=0,
                                                                                                     pady=8)


if __name__ == '__main__':
    root = Tk()
    root.iconbitmap('favicon.ico')
    application = MainWindow(root)
    root.mainloop()
