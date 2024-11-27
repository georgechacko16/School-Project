import mysql.connector

conn = mysql.connector.connect(host='localhost', password='1234', user='root')


def booking_id():
    f = open("Storage1.txt", "r+")
    d = f.readlines()
    val = len(d) + 1
    f.write(f"Booking ID: {val} \n")
    f.close()

    return int(val)

def create():
    
    bkID = booking_id()
    rmNO = input("Enter Room no: ")
    name = input("Enter Name: ")
    dte = input("Enter Date(YYYY-MM-DD): ")
    stay = input("Enter Stay(Days): ")
    contact = input("Enter Contact: ")
    rmType = input("Enter Room Type: ")
    PymntStatus = input("Enter Payment Status: ")
    Pymnt = input("Enter Payment: ")

    c.execute(f'INSERT into hotel (book_id, room_no, name, date_booked, stay_for, contact, room_type, payment_status, payment) values ({bkID}, {rmNO}, "{name}", "{dte}", {stay}, "{contact}", "{rmType}", "{PymntStatus}", {Pymnt}); ')



def menu(user):
    print(f"Hello {user}")
    print("What would you like to do?")
    print("1.Create new booking")
    print("2.Delete existing booking")
    print("3.Check information")
    print("4.Search")
    print("5.Quit")

    choice = input("\n ------------------>>>  ")


    return choice

def delete():
    Id = input("\n\nEnter booking ID: ")
    c.execute(f"Delete from hotel where book_id={Id};")


def search():
    srch = input("Search via Booking ID: ")
    
    
    c.execute(f"SELECT * from hotel where book_id = {srch};")

def ShowAll():
    c.execute("SELECT * from hotel;")

def result(res):

    for bkID, rmNo, name, dte, stay, contact, rmType, paymntS, payment in res:
        print("Booking ID:", bkID)
        print("Room No: ", rmNo)
        print("Name: ", name)
        print("Date: ", dte)
        print("Stay: ",  stay)
        print("Contact: ", contact)
        print("Room Type: ", rmType)
        print("Payment Status: ", paymntS)
        print("Payment:", payment)

        print("~"*30)


if not conn.is_connected:
    print("MySQL not connected")
else:
    c = conn.cursor()
    
    c.execute("USE hoteldb;")
        
    
    while True:
        choice = menu("User")

        if choice == '1':
            #Create booking ID
            create()

        elif choice == '2':
            #Delete booking ID
            delete()
        elif choice == '3':
            #Show all data
            ShowAll()
        elif choice == '4':
            #Searches for row Based on desired key
            search()
        elif choice == '5':
            # Breaks the While Loop quiting the program
            print("Have a Nice Day")
            break
        else:
            print("Not an Option(Type 1-5 to select)")


        d = c.fetchall()

        result(d)
        

        
        print("\n\n\n\n ~~~~~~~~~~~~~~~~~~~~QUERY COMPLETE~~~~~~~~~~~~~~~~~~~~ \n\n\n\n")
        
        conn.commit()

    
    

