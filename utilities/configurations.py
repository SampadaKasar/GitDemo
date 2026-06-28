import configparser
import mysql.connector
from mysql.connector import  Error
from mysql.connector.aio import cursor


def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

#dictionary for connecting configurations
connect_config = {
    "host" : get_config()["SQL"]["host"],
    "user" : get_config()["SQL"]["user"],
    "password" : get_config()["SQL"]["password"],
    "database" : get_config()["SQL"]["database"]
}



def getConnection():
    try:
       conn = mysql.connector.connect(**connect_config)  #two stars will show that it is dictionary
       if conn.is_connected():
           print("succesfully connected")
           return conn
    except Error as e:
        print(e)

def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    first_row = cursor.fetchone()
    conn.close()
    return first_row
