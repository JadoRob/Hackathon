import os
from os import system
from mysql.connector import connect
import connect as c
import mysql
from vehicle import Vehicle


def getVehicle(selection):
    conn = c.returnConnection()
    make = 'null'
    model = 'null'
    year = 0
    color = 'null'
    price = 0
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM vehicles WHERE id = {selection}')
        for row in cursor:
            make = row[1] 
            model = row[2] 
            year = row[3] 
            color = row[4] 
            price = row[5]

        cursor.close()
        conn.close()
    except(Exception, mysql.connector.Error) as error:
        print('Error while fetching data from MySQL', error)
    selectedVehicle = Vehicle(make, model, year, color, price)
    return selectedVehicle
        

    

