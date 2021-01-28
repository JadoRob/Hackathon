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

#Functions -----------------------------------------
def readDatabase():
    conn = c.returnConnection()
    try:
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
        cursor.close() 
        conn.close() 
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)
#Functions -----------------------------------------


print('')
print('Welcome to the dealership!')
cart = []
counter = 1
# enter a while loop, exit if user chooses to stop purchasing
while (True):
    print("Here's our inventory: ")
    
    #open a connection and display each row of the table to show the inventory
    readDatabase()
    print("")
    #choose a vehicle by selecting id
    selection = input('What would you like to purchase? (please enter the id number) >> ')
    print('Thank you, searching through inventory... ')
    #time.sleep(3)
    #store the object that's returned from the database file, and use the get functions
    #to get the price and color
    vehicle = database.getVehicle(selection)
    price = vehicle.getPrice()
    color = vehicle.getColor()
    print('Lets see if you qualify for some discounts.')
    veteran = input('Are you a war veteran? [y/n] >> ')
    disabled = input('Do you have any disablilites? [y/n] >> ')
    print('Thank you for the information, calculating total... ')
    #time.sleep(3)
    #get the total from
    totalPrice = calculateTotal(color, price, veteran, disabled)
    print(f'The total price is: ${totalPrice}')
    buyNow = input(f'Would you like to make the purchase? [y/n] >> ')
    if (buyNow == 'y'):
        cart.append(Vehicle(counter))
        print('')
        if (counter == 5):
            break
        proceed = input(f'Thank you for your purchase! Would you like to purchase more? [y/n] >>')
        if (proceed == 'n'):
            break     
    counter += 1
for obj in cart:
    print(vehicle.getMake())

        
        



# print('''
# Lets take a look at what your looking for.

# 1. Make
# 2. Model
# 3. Year
# 4. Color

# ''')
# selection = input('Please choose a number [1-4]: >> ')

# make = input("What's the make? >> ")
# model = input("What's the model? >> ")
# year = input("What's the year? >> ")
# color = input("What color are you looking for? >> ")
# vehicle1 = Vehicle(make, model, year, color)
# print('')
# print('Here is what your looking for: ')
# print(f'''
# Make and model: {vehicle1.getMake()} {vehicle1.getModel()} 
# Year: {vehicle1.getYear()}
# Color: {vehicle1.getColor()}
# ''')