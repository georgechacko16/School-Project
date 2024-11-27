import mysql.connector
from datetime import date

conn = mysql.connector.connect(host='localhost', password='1234', user='root')


l = [
    {
        "Booking ID": "book_id",
        "type": int
    }, 
    {
        "Room Number": "room_no",
        "type": int
    }, 
    {
        "Name": "name",
        "type": str,
        "length": 50
    }, 
    { 
        "Date Booked(YYYY-MM-DD)": "date_booked",
        "type": str,
        "length": 50
    },
    { 
        "Stay for": "stay_for",
        "type": int
    }, 
    { 
        "Contact": "contact",
        "type": int,
        "length": 10
    },
    {
        "Room Type": "room_type",
        "type": str,
        "length": 6
    },
    { 
        "Payment Status": "payment_status",
        "type": str,
        "length": 40
    },
    { 
        "Payment": "payment",
        "type": int
    }
    ]


def booking_id():
    f = open("Storage.txt", "r+")
    d = f.readlines()
    val = len(d) + 1
    f.write(f"Booking ID: {val} \n")
    f.close()

    return int(val)

def create():
    print("\n\n")
    
    values = []
    
    x= 0
    
    #Loops the code till the values entered that WONT crash SQL
    while x<len(l):
        i = l[x]
        #This just means wheter they meet requirement or don't; Default is set to True meaning they don't meet requirements
        Not_req = True

        if x == 0:
            #Adds Booking ID to the Booking(THIS IS A PERMANENT THING AND WON"T CHANGE EVEN IF BOOKING IS DELETED)
            #   i.e Deleting older bookings won't lower booking ID
            values.append(booking_id())
            x += 1
            Not_req = False
        elif x == 3:
            #Adds currect date to the Booking
            values.append(date.today())
            x += 1
            Not_req = False
        else:
            #This is the first key from every dict in the list l
            ky = next(iter(i))

            p = input(f"Enter {ky}: ")

            #Logic check for any value of the Input that can cause conflicts with SQL
            if i["type"] == str:
                if len(p) <= i["length"]:
                    values.append(p)
                    x += 1
                    Not_req = False
            elif i["type"] == int:
                # If Type is in needs to contain digits only
                if p.isdigit():

                    #As contact is a type int but still requires a limit; this if statement it used
                    if i[ky] == "contact":
                        if len(p) == i["length"]:
                            values.append(p)
                            x += 1
                            Not_req = False
                    #Here it checks if the room no is the same as the previously entered data
                    elif i[ky] == "room_no":

                        c.execute("Select room_no from hotel;")
                        d = c.fetchall()
                        Not_req = False
                        for no in d:
                            if int(p) == no[0]:
                                Not_req = True
                        if Not_req:
                            print("ROOM TAKEN")
                        else:
                            values.append(p)
                            x += 1
                            

                    else:
                        values.append(p)
                        x += 1
                        Not_req = False

        #If they don't meet it, this is printed and the loop is repeated (Not_req == True)
        if Not_req:
            print("Didn't match requirements")
    

    c.execute(
        f'INSERT into hotel (book_id, room_no, name, date_booked, stay_for, contact, room_type, payment_status, payment) values ({values[0]}, {values[1]}, "{values[2]}", "{values[3]}", {values[4]}, "{values[5]}", "{values[6]}", "{values[7]}", {values[8]}); ')



def menu(user):
    #Creates Menu and returns Inputted value
    print(f"\n\n\nHello {user}")
    print("What would you like to do?")
    print("1.Create new booking")
    print("2.Delete existing booking")
    print("3.Check information")
    print("4.Search")
    print("5.Quit")

    choice = input("\n ------------------>>>  ")


    return choice


def search():
    #Search Booking ID
    print("\n\n\n")
    print("\n\nSearch via: (Copy Paste Values below for efficiency)")
    
    
    col = [next(iter(d.keys())) for d in l]

    #This just prints what I think is Important for the search
    for i in col: 
        print(i, end=", ")
    
    val = input("\n\n-->")
    
    try:
        # gets First key from all the dictionaries in l
        ky = l[col.index(val)][val]

        #Inputed value
        v = input(f"Search via {val}: ")

        #Runs a different version of the code based on type the value is
        if l[col.index(val)]["type"] != str:
            c.execute(f"SELECT * from hotel where {ky} = {v};")
        else:
            
            c.execute(f"SELECT * from hotel where {ky} = '{v}';")
        print("\n\n\n")
    except:
        #All of this is in a try except loop because there are many ways this could crash the program
        print("\n\nUnexpected Error \n\n Please enter values that are in the table or Are within Range")

# Displays Result from SQL
def result(res):

    col = [next(iter(d.keys())) for d in l]

    results = res

    # Define the column headers (matching your SQL schema)
    columns = col
    
    # Display the results in a structured way
    for row in results:
        print("Booking Details:")
        for col, value in zip(columns, row):
            print(f"  {col}: {value}")
        print("-" * 30)  # Separator for readability


if not conn.is_connected:
    print("MySQL not connected")
else:
    c = conn.cursor()
    
    c.execute("USE hoteldb;")
        
    
    while True:
        #Gets The choice value
        choice = menu("User")

        if choice == '1':
            #Create booking ID
            create()

        elif choice == '2':
            #Delete booking ID
            Id = input("\n\nEnter booking ID: ")
            c.execute(f"Delete from hotel where book_id={Id};")
        elif choice == '3':
            #Show all data
            c.execute("SELECT * from hotel;")
        elif choice == '4':
            #Searches for row Based on desired key
            search()
        elif choice == '5':
            # Breaks the While Loop quiting the program
            print("\n\n\n\n Have a Nice Day")
            break
        else:
            print("\n\n\n\nNot an Option(Type 1-5 to select)")


        d = c.fetchall()

        result(d)
        

        
        print("\n\n\n\n ~~~~~~~~~~~~~~~~~~~~QUERY COMPLETE~~~~~~~~~~~~~~~~~~~~ \n\n\n\n")
        
        conn.commit()

    
    

