from db import *
from utils import box_message, message, transformDate

def showAllProducts():
    query = "SELECT * FROM Products"
    cursor.execute(query)
    keys = ("id", "title", "description", "base_price", "current_price", "bid_deadline", "customer_id","sold")
    for x in cursor:
        print(dict(zip(keys, x))) 

def showAllBidProducts():
    query = "SELECT id, title, description, base_price, current_price, bid_deadline FROM Products WHERE is_sold=0"
    cursor.execute(query)
    keys = ("id", "title", "description", "base_price", "current_price", "bid_deadline")
    for x in cursor:
        item = dict(zip(keys, x))
        print()
        box_message(f"  {item['title']}  ")
        if item['description']:
            print(item['description']) 
        print(f"Base Price: {item['base_price']}")
        print(f"Current Price: {item['current_price']}")
        print(f"Bid ends at: {item['bid_deadline']}")
        print(f"Product ID(use this while making a bid): {item['id']}")
        print()


def addProduct(): 
    title = input("Enter Product Title: ")
    if not title:
        message("Title can not be empty")
        return

    description = input("Enter Product Description(optional): ")

    base_price=float(input("Enter Base price: "))
    if not base_price:
        message("base_price can not be empty")
        return
    
    bid_deadline=input("Enter bid deadline(format:YYYY-MM-DD-HH-MM)\ne.g. 2021-10-31-23-58\n>>> ")
    if not bid_deadline:
        message("bid_deadline can not be empty")
        return    
    bid_deadline = transformDate(bid_deadline)
    if not bid_deadline:
        message("bid deadline not in correct format")
        return    
    query = f"""INSERT INTO Products 
            (title, description, base_price, current_price, bid_deadline)
            VALUES
            ('{title}', '{description}', {base_price}, {base_price}, '{bid_deadline}')"""

    cursor.execute(query)
    db.commit()
    box_message(f"Product {title} added!!")

def makeBid(customer_id):
    product_id = int(input('Enter Product Id: '))
    bid_amount = float(input('Enter Bid Amount: '))
    query = f"SELECT title, current_price from Products WHERE id={product_id} and is_sold=0"
    cursor.execute(query)
    products = list(cursor)
    if not len(products):
        message("The requested product is not for sale!!")
        return

    if bid_amount <= products[0][1]:
        message(f"The bid amount must be greater than the current bid({products[0][1]})")
        return
        
    query = f"UPDATE Products SET current_price = {bid_amount}, customer_id = {customer_id} WHERE (id = {product_id})"
    cursor.execute(query)
    db.commit()
    box_message(f"You raised the bid for {products[0][0]}!!")

def closeBid():
    product_id = int(input('Enter Product Id: '))
    query = f"SELECT title, current_price, customer_id from Products WHERE id={product_id} and is_sold=0"
    cursor.execute(query)
    products = list(cursor)
    if not len(products):
        message("The product is not for sale!!")
        return
    
    query = f"UPDATE Products SET is_sold = 1 WHERE (id = {product_id})"
    cursor.execute(query)
    db.commit() 
    title, current_price, customer_id = products[0]
    if not customer_id:
        box_message(f"{title} went unsold!!")
        return
    query = f"SELECT username, spent FROM Customers WHERE (id = {customer_id})"
    cursor.execute(query) 
    customers = list(cursor)
    username, spent = customers[0] 
    query = f"UPDATE Customers SET spent = {spent+current_price} WHERE (id = {customer_id})"
    cursor.execute(query)
    db.commit() 
    box_message(f"{title} is sold to {username} at {current_price}")
    
def deleteProduct():
    product_id = int(input('Enter Product Id: '))
    query = f"SELECT title, current_price, customer_id from Products WHERE id={product_id}  "
    cursor.execute(query)
    products = list(cursor)
    if not len(products):
        message(f"Unable to find the product with product id {product_id}")
        return

    query = f"DELETE FROM Products WHERE (id = {product_id})"
    cursor.execute(query)
    db.commit() 
    box_message(f"Deleted product {products[0][0]}")