from utils import *
from product import *
from customer import *

def loggedInAdmin():
    while True:
        choice = int(input("Logged in as Admin:\n1. Show All Products\n2. Show Products available for biding\n3. Close Bid\n4. Add Product\n5. Delete Product\n6. Exit\n>>> "))
        if(choice==1) :
            showAllProducts()
        
        elif(choice==2) :
            showAllBidProducts()

        elif(choice==3) :
            closeBid()
        
        elif(choice==4):
            addProduct()
        
        elif(choice==5):
            deleteProduct()
        
        elif(choice==6):
            break
        
        else:
            message("Invalid Choice")
         
def customerMenu():
    while True:
        choice = int(input("Welcome Customer:\n1. Register\n2. Login\n3. Exit\n>>> "))
        if(choice==1) :
            registerCustomer()
        
        elif(choice==2):
            loginCustomer()
        
        elif(choice==3):
            break
        
        else:
            message("Invalid Choice")
          
while True:
    choice = int(input("Welcome To PyAuction:\n1. Admin Login\n2. Customer Menu\n3. Exit\n>>> "))
    
    if(choice==1) :
        secret = int(input("Enter Secret Code: "))
        if secret != ADMIN_SECRET:
            message("Wrong secret code!")
        else:
            loggedInAdmin()
    
    elif(choice==2):
        customerMenu() 

    elif(choice==3):
        break

    else:
        message("Invalid Choice")
    
