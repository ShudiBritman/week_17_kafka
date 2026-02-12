from mysql_connection import get_connection


cnx = get_connection()


def init_db():
    cursor = cnx.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXIST users_orders;')
    cursor.execute('USE DATABASE users_orders;')
    query = '''CREATE TABLE IF NOT EXIST customers(
    `customerNumber` INT PRIMARY KEY,
    `customerName` varchar(50),
    `contactLastName` varchar(50),
    `contactFirstName` varchar(50),
    `phone` varchar(15),
    `addressLine1` varchar(50),
    `addressLine2` varchar(50),
    `city` varchar(50),
    `state` varchar(50),
    `postalCode` varchar(50),
    `country` varchar(50),
    `salesRepEmployeeNumber` INT,
    `creditLimit` FLOAT)'''
    cursor.execute(query)
    query = '''CREATE TABLE IF NOT EXIST orders(
    `orderNumber` INT PRIMARY KEY,
    `orderDate` DATETIME,
    `requiredDate` DATETIME,
    `shippedDate` DATETIME,
    `status` varchar(50),
    `comments` varchar(50),
    `customerNumber` INT FOREIGN KEY REFERENCES customers(customerNumber))'''
    cursor.execute(query)