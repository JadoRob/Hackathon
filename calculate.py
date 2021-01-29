import os
from os import system
from decimal import Decimal

# calculates the total prices
# if car is black, discount 25%
# if car is white, bonus of $400 towards the down payment
# if customer is a veteran || disabled, they receive 25% off cost plust $500 bonus
# return total price and bonuses to the main file


def calculateTotal(color, price, veteran, disabled):
    print (f'Your base price is ............... ${price}')
    totalPrice = price
    if (color == 'black'):
        totalPrice = totalPrice * Decimal(.75)
    if (color == 'white'):
        totalPrice = totalPrice - 400
    if ((veteran == 'y') or (disabled == 'y')):
        totalPrice = (totalPrice * Decimal(.75)) - 500
    #tax       
    totalPrice *= Decimal(1.05)
    return round(totalPrice ,2)
    


