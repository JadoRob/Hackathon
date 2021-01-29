import os
from os import system
from mysql.connector import connect
import connect as c
import mysql
from vehicle import Vehicle


# *** not yet implemented ***
def createCustomer(customer):
    conn = c.returnConnection()
    selectedVehicle = Vehicle()
    try:
        cursor = conn.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS customers (customer_id INT PRIMARY KEY AUTO_INCREMENT, customer_name VARCHAR(15))')
        cursor.execute(f'INSERT INTO customers VALUES (customer_name)')
        cursor.close()
        conn.close()
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)

# connecting to the database to store purchsed vehicle as an order
def createOrder(customer, vehicle_id):
    conn = c.returnConnection()
    selectedVehicle = Vehicle()
    print(f'Vehicle ID from the createOrder function in database: {vehicle_id}')
    try:
        cursor = conn.cursor()
        cursor.execute(f'CREATE TABLE IF NOT EXISTS orders (order_id INT PRIMARY KEY AUTO_INCREMENT, customer_name VARCHAR(15), vehicle_id INT)')
        # Double quotes is needed when using single quotes for strings
        cursor.execute(f"INSERT INTO orders (customer_name, vehicle_id) VALUES ('{customer}', {vehicle_id})")
        # execute the commit() method to insert data into the table before 
        # closing the cursor
        conn.commit()
        cursor.close()
        conn.close()
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)

# Takes the selection that the customer chose (vehicle ID) and connects to the database to retrieves the vehicle
def getVehicle(selection):
    conn = c.returnConnection()
    selectedVehicle = Vehicle()
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM vehicles WHERE id = {selection}')
        for row in cursor:

            # using the object set methods to assign attributes to the object
            selectedVehicle.setId(row[0])
            selectedVehicle.setMake(row[1])
            selectedVehicle.setModel(row[2])
            selectedVehicle.setYear(row[3])
            selectedVehicle.setColor(row[4])
            selectedVehicle.setPrice(row[5])

        cursor.close()
        conn.close()
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)
    # using the get methods to show the object's attributes
    print(f'''
    
    Here is what you selected:
    {selectedVehicle.getYear()} {selectedVehicle.getMake()}, {selectedVehicle.getModel()}, {selectedVehicle.getColor()}, ${selectedVehicle.getPrice()}
    
    ''')
    
    

    return selectedVehicle
        

    

