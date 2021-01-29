import os
from os import system
from vehicle import Vehicle
from mysql.connector import connect
import connect as c
import mysql
import calculate
import time
from calculate import calculateTotal
import database
from database import createCustomer

# HACKATHON Python project 
# by Jane, Jeff, Terrell, and Rob
# assisted by Professor Dunieski Otano

#Functions -----------------------------------------
def readDatabase():
    # creates connection
    conn = c.returnConnection()
    try:
        # cursor goes through the vehicles table display information
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM vehicles')
        # go through each row of the table
        for row in cursor:
            print('')
            #print the attributes of the vehicle
            print(f'''
            -------------------------------------------------------
            [{row[0]}] Vehicle: {row[3]} {row[1]} {row[2]} 
            Color: {row[4]} 
            Price: ${row[5]}
            -------------------------------------------------------
            ''')
        #closes the connection
        cursor.close() 
        conn.close() 
    # if unable to connect or read the database, shows the errorr
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)
#Functions -----------------------------------------


print('')
print('Welcome to the dealership!')
customer = input('May we have your name please? >> ')
# createCustomer(customer)

cart = []
counter = 1
# enter a while loop, exit if user chooses to stop purchasing
while (True):
    vehicle = Vehicle()
    print("Here's our inventory: ")
    
    # open a connection and display each row of the table to show the inventory
    readDatabase()
    print("")

    # choose a vehicle by selecting id
    selection = input('What would you like to purchase? (please enter the id number) >> ')
    print('Thank you, searching through inventory... ')
    #time.sleep(3)
    
    #store the object that's returned from the database file, and use the get functions
    # to get the price and color
    vehicle = database.getVehicle(selection)
    price = vehicle.getPrice()
    color = vehicle.getColor()
    print('Lets see if you qualify for some discounts.')
    veteran = input('Are you a war veteran? [y/n] >> ')
    disabled = input('Do you have any disablilites? [y/n] >> ')
    print('Thank you for the information, calculating total... ')
    # time.sleep(3)
   
    # get the total from calculate.py file using the calculateTotal method
    totalPrice = calculateTotal(color, price, veteran, disabled)

    print(f'The total price is: ${totalPrice}')
    buyNow = input(f'Would you like to make the purchase? [y/n] >> ')
    if (buyNow == 'y'):
        # create the customer order for the purchase
        database.createOrder(customer, vehicle.getId()) 
        print('')
        # adds 1 to counter as each car is purchased, max is 5 purchases
        if (counter == 5):
            # exits out of the while loop and ends program
            break
        proceed = input(f'Thank you for your business! Would you like to look around some more? [y/n] >>')
        if (proceed == 'n'):
            break     
    counter += 1
#for obj in cart:
    # print(vehicle.getMake())
print('Thank you for your business! Have a great day and safe driving.')
        
        