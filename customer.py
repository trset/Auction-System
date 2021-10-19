from db import *
from utils import box_message, message
from product import showAllBidProducts, makeBid

def loggedInCustomer(id, name):
    while True:
        choice = int(input(f"Logged in as {name}:\n1. Show All Products\n2. Make a Bid\n3. Exit\n>>> "))
        if(choice==1) :
            showAllBidProducts()
        
        elif(choice==2):
            makeBid(id)
        
        elif(choice==3):
            break

        else:
            message("Invalid Choice")

def registerCustomer():
    name = input("Enter Username: ")
    
    if not name:
        message("username can not be empty")
        return

    passwd = input("Enter New Password: ")
    if not passwd:
        message("password can not be empty")
        return

    query = f"INSERT INTO Customers (username, password) VALUES ('{name}', '{passwd}')"
    cursor.execute(query)
    db.commit()
    box_message(f"New Customer {name} Registered!!")

def loginCustomer():
    name = input("Enter Username: ")
    
    if not name:
        message("username can not be empty")
        return

    passwd = input("Enter Password: ")
    if not passwd:
        message("password can not be empty")
        return

    query = f"SELECT id, username, password FROM Customers"
    cursor.execute(query) 
    for customer in cursor: 
        id, username, password = customer
        if name == username and passwd == password:
            loggedInCustomer(id, name)
            return
    else:
        message("user credentials did not matched") 
