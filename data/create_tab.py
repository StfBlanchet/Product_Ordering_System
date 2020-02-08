#! /usr/bin/env python3
# coding: utf-8

"""
PizzaOrdering
creating schemas
"""

from data.mysql_connect import *

cursor.execute("CREATE SCHEMA IF NOT EXISTS Pizza DEFAULT CHARACTER SET utf8")

"""
Create tables
"""

customer = """
CREATE TABLE IF NOT EXISTS Pizza.Customer (
  id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  phone VARCHAR(45) NOT NULL,
  email VARCHAR(45) NOT NULL,
  username VARCHAR(45) NOT NULL,
  password VARCHAR(45) NOT NULL,
  billing_address INT NOT NULL,
  PRIMARY KEY (id)
  )
"""

address = """
CREATE TABLE IF NOT EXISTS Pizza.Address (
  id INT NOT NULL AUTO_INCREMENT,
  street VARCHAR(150) NOT NULL,
  street_number INT NOT NULL,
  city VARCHAR(150) NOT NULL,
  complements MEDIUMTEXT NULL,
  postal_code INT NOT NULL,
  PRIMARY KEY (id)
  )
"""

pos = """
CREATE TABLE IF NOT EXISTS Pizza.PoS (
  id INT NOT NULL,
  name VARCHAR(45) NOT NULL,
  address INT NOT NULL,
  catchment_area VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
  )
"""

employee = """
CREATE TABLE IF NOT EXISTS Pizza.Employee (
  id INT NOT NULL,
  job ENUM('Manager', 'Réceptionniste', 'Préparateur', 'Livreur') NOT NULL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  username VARCHAR(45) NOT NULL,
  password VARCHAR(45) NOT NULL,
  pos INT NOT NULL,
  PRIMARY KEY (id)
  )
"""

product = """
CREATE TABLE IF NOT EXISTS Pizza.Product (
  id INT NOT NULL,
  name VARCHAR(45) NOT NULL,
  description VARCHAR(255) NOT NULL,
  recipe VARCHAR(255) NOT NULL,
  image_path VARCHAR(255) NOT NULL,
  entry_price INT NOT NULL,
  PRIMARY KEY (id)
  )
"""

stock = """
CREATE TABLE IF NOT EXISTS Pizza.Stock (
  pos INT NOT NULL,
  pâte FLOAT NOT NULL,
  sauce_tomates FLOAT NOT NULL,
  mozzarella FLOAT NOT NULL,
  olives FLOAT NOT NULL,
  jambon FLOAT NOT NULL,
  champignons FLOAT NOT NULL,
  artichauds FLOAT NOT NULL,
  aubergines FLOAT NOT NULL,
  courgettes FLOAT NOT NULL,
  anchois FLOAT NOT NULL,
  câpres FLOAT NOT NULL,
  PRIMARY KEY (pos)
  )
"""

unit_stock = """
CREATE TABLE IF NOT EXISTS Pizza.UnitStock (
  pos INT NOT NULL,
  product INT NOT NULL,
  remaining_units FLOAT NOT NULL,
  PRIMARY KEY (pos, product)
  )
"""

basket = """
CREATE TABLE IF NOT EXISTS Pizza.Basket (
  line INT NOT NULL AUTO_INCREMENT,
  id INT NOT NULL,
  product INT NOT NULL,
  size ENUM('small', 'medium', 'large') NOT NULL,
  serving FLOAT NOT NULL,
  price INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (line)
  )
"""

ordering = """
CREATE TABLE IF NOT EXISTS Pizza.Ordering (
  id INT NOT NULL AUTO_INCREMENT,
  basket INT NOT NULL,
  pos INT NOT NULL,
  customer INT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  reception_mode ENUM('à emporter', 'à livrer') NOT NULL,
  reception_point INT NOT NULL,
  status ENUM('initialisée', 'abandonnée', 'enregistrée', 'en préparation', 'en cours de livraison', 'livrée') NOT NULL,
  PRIMARY KEY (id)
  )
"""

payment = """
CREATE TABLE IF NOT EXISTS Pizza.Payment (
  id INT NOT NULL,
  amount INT NOT NULL,
  mode ENUM('en ligne', 'à réception') NOT NULL,
  status ENUM('initialisé', 'abandonné', 'en attente', 'encaissé') NOT NULL,
  PRIMARY KEY (id)
  )
"""

tab_exec = [customer, address, employee, product, pos, ordering, payment, basket, stock, unit_stock]

for stmt in tab_exec:
    cursor.execute(stmt)

db.commit()
