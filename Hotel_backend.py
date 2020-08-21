from tkinter import *
import mysql.connector
import tkinter.messagebox


def daily_taasks():
    """Removes bookings that have ended and set room status unoccupied which aren't booked currently"""

    MyDb = mysql.connector.connect(user="root", password="12345", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    cursor.execute("DELETE FROM hotelbookings WHERE cout <(SELECT curdate())")
    cursor.execute("UPDATE rooms SET status=0 WHERE roomn NOT IN (SELECT hotelbookings.roomno FROM hotelbookings);")
    MyDb.commit()
    MyDb.close()


def showbookings():
    """Function to show the bookings currently active in a tabular form"""

    MyDb = mysql.connector.connect(user="root", password="12345", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    cursor.execute('SELECT * FROM hotelbookings')
    Data = cursor.fetchall()
    MyDb.close()

    # ===================================================================================================================
    Show = Tk()
    Show.state('zoomed')
    Show.title("Hotel Management System")

    def quitwin():
        Show.destroy()

    # ===================================================================================================================

    mainframe = Frame(Show, bg='powder blue', padx=10, pady=10)
    mainframe.pack(fill='both', expand=1)

    topframe = Frame(mainframe, bd=14, relief='ridge', bg='ghost white', height=100, width=750, padx=70, pady=5)
    topframe.pack(pady=10)

    heading = Frame(topframe, bg='ghost white')
    heading.pack(side=LEFT)

    content = Frame(mainframe, bd=8, relief='ridge', bg='powder blue', height=600, width=750, padx=80, pady=30)
    content.pack(pady=10, fill='both', expand=1)

    # ===================================================================================================================

    lblheading = Label(heading, text='CURRENT BOOKINGS', font='times 36 bold', bg='ghost white')
    lblheading.pack(padx=50)

    btnquit = Button(topframe, bd=4, text='Quit', height=1, width=13, font='arial 16', bg='cadet blue',
                     activeforeground="dark blue", command=quitwin)
    btnquit.pack(side=RIGHT)

    h1 = Label(content, padx=10, text="Booking ID", font='times 16')
    h1.grid(row=0, column=0)
    h2 = Label(content, padx=20, text="Name", font='times 16')
    h2.grid(row=0, column=1)
    h3 = Label(content, padx=20, text="Surname", font='times 16')
    h3.grid(row=0, column=2)
    h4 = Label(content, padx=50, text="Email", font='times 16')
    h4.grid(row=0, column=3)
    h5 = Label(content, padx=50, text="Address", font='times 16')
    h5.grid(row=0, column=4)
    h6 = Label(content, padx=60, text="Mobile", font='times 16')
    h6.grid(row=0, column=5)
    h7 = Label(content, padx=15, text="Room No", font='times 16')
    h7.grid(row=0, column=6)
    h8 = Label(content, padx=15, text="Meal", font='times 16')
    h8.grid(row=0, column=7)
    h9 = Label(content, padx=15, text="Checkin Date", font='times 16')
    h9.grid(row=0, column=8)
    h10 = Label(content, padx=15, text="Checkout Date", font='times 16')
    h10.grid(row=0, column=9)

    row = 1
    for i in Data:
        column = 0
        for j in i:
            lbldata = Label(content, bg="powder blue", padx=15, text=j, pady=8)
            lbldata.grid(row=row, column=column)
            column += 1
        row += 1


def addnew(name, surname, email, address, mobile, rtype, meal, cin, cout):
    """The add new function used to insert records of data in bookings table"""

    global roomno
    MyDb = mysql.connector.connect(user="root", password="12345", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    cursor.execute("SELECT roomn FROM rooms WHERE status=0 and type = %s", (rtype,))
    nolist = cursor.fetchall()

    if len(nolist) == 0:
        tkinter.messagebox.showerror("Error", "No Rooms Available")
        # Shows error if room of the selected type is not available
    else:
        roomno = nolist[0][0]
        sql = "INSERT INTO hotelbookings (name, surname, email, address, mobile, roomno ,meal, cin, cout) VALUES \
              (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, surname, email, address, mobile, roomno, meal, cin, cout)
        cursor.execute(sql, val)

    cursor.execute("SELECT bookingid,roomno FROM hotelbookings WHERE roomno=%s", (roomno,))
    showdata = cursor.fetchall()
    tkinter.messagebox.showinfo("ID & Room No.", "Your Booking ID is: " + str(showdata[0][0]) + " and Room No is: "
                                + str(showdata[0][1]))
    cursor.execute("UPDATE rooms SET status=1 WHERE roomn=%s", (roomno,))

    MyDb.commit()
    MyDb.close()


def cancel(id):
    """Cancel function to delete a currently active booking"""

    MyDb = mysql.connector.connect(user="root", password="12345", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    response = tkinter.messagebox.askquestion("Confirm", "Are you sure?")
    if response == 'yes':
        cursor.execute("SELECT bookingid FROM hotelbookings WHERE bookingid=%s", (id,))
        if len(cursor.fetchall()) == 0:
            tkinter.messagebox.showerror("Error",
                                         "No Such Booking")  # shows error if no booking is there with the given ID
        else:
            cursor.execute("DELETE FROM hotelbookings WHERE bookingid=%s", (id,))
            tkinter.messagebox.showinfo("Message", "Booking Has been Canceled")
            MyDb.commit()
    MyDb.close()


def generate_bill(bill_id):
    """Generates bill for the given booking ID by fetching details from the database"""

    meal = {'Breakfast': 250, 'Dinner': 230, 'Combo': 450, 'All three': 550}
    room = {'single deluxe': 2000, 'double deluxe': 2500, 'executive': 3000, 'suit': 5000}

    MyDb = mysql.connector.connect(user="root", password="12345", host="localhost", database="coder01")
    cursor = MyDb.cursor()
    cursor.execute("SELECT bookingid FROM hotelbookings WHERE bookingid=%s", (bill_id,))
    if len(cursor.fetchall()) == 0:
        tkinter.messagebox.showerror("Error", "No Such Booking / Booking is over")
    else:
        cursor.execute("SELECT meal,cin,cout,roomno FROM hotelbookings WHERE bookingid=%s", (bill_id,))
        data = cursor.fetchone()
        cursor.execute("SELECT type FROM rooms where roomn=%s", (data[3],))
        data += cursor.fetchone()  # gets the details of booking from the database to genarae bill
        days = (data[2] - data[1]).days
        rcost = (room[data[4]]) * days
        mcost = (meal[data[0]]) * days

        bill = open('Bill_ID_' + str(bill_id), 'w+')  # Creates a new file and generates a bill in default formatting

        bill.write('    HOTEL TAJ    \n')
        bill.write('\n    Bill Memo     \n')
        bill.write('\n Room Type:  ')
        bill.write(data[4])
        bill.write('\n Days:  ')
        bill.write(str(days))
        bill.write('\n Meal:  ')
        bill.write(data[0])

        bill.write('\n\n Room Cost:  ')
        bill.write(str(rcost))

        bill.write('\n Meal Cost:  ')
        bill.write(str(mcost))

        bill.write('\n\n Grand Total:  ')
        bill.write(str(rcost + mcost))
        bill.close()

        tkinter.messagebox.showinfo("Message", "Bill Has Been Saved Locally")
    MyDb.close()


if __name__ == 'Hotel_backend':
    daily_taasks()
