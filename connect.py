import mysql.connector
from mysql.connector import connect 
from colorama import Fore, Back, Style
from os import getenv, system, environ
from dotenv import load_dotenv


load_dotenv()

def returnConnection():
    conn = connect(
        host=getenv('DB_URL'),
        user=getenv('DB_USER'),
        password=getenv('DB_PASSWORD'),
        database=getenv('DB_NAME')
    )
    return conn