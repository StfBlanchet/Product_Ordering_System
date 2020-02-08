#! /usr/bin/env python3
# coding: utf-8

"""
PizzaOrdering
filling database
"""

from data.mysql_connect import *

# allow local infile
cursor.execute("SET GLOBAL local_infile = 1")
db.commit()


"""
Fill tables
"""

customer = """
    LOAD DATA LOCAL INFILE 'Customer.csv'
    INTO TABLE Customer
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'   
    IGNORE 1 ROWS
    """

address = """
    LOAD DATA LOCAL INFILE 'Address.csv'
    INTO TABLE Address
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'    
    LINES TERMINATED BY '\n'  
    IGNORE 1 ROWS
    """

employee = """
    LOAD DATA LOCAL INFILE 'Employee.csv'
    INTO TABLE Employee
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'    
    LINES TERMINATED BY '\n'   
    IGNORE 1 ROWS
    """

pos = """
    LOAD DATA LOCAL INFILE 'PoS.csv'
    INTO TABLE PoS
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'    
    LINES TERMINATED BY '\n'   
    IGNORE 1 ROWS
    """

product = """
    LOAD DATA LOCAL INFILE 'Product.csv'
    INTO TABLE Product
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'    
    LINES TERMINATED BY '\n'   
    IGNORE 1 ROWS
    """

stock = """
    LOAD DATA LOCAL INFILE 'Stock.csv'
    INTO TABLE Stock
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'    
    LINES TERMINATED BY '\n'   
    IGNORE 1 ROWS
    """

unit_stock = """
    LOAD DATA LOCAL INFILE 'UnitStock.csv'
    INTO TABLE UnitStock
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'    
    LINES TERMINATED BY '\n'   
    IGNORE 1 ROWS
    """

tab_exec = [customer, address, employee, product, pos, stock, unit_stock]

for stmt in tab_exec:
    cursor.execute(stmt)
    db.commit()
