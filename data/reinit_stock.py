#! /usr/bin/env python3
# coding: utf-8

"""
PizzaOrdering
reinitializing values
"""

from data.mysql_connect import *

cursor.execute("UPDATE Stock SET pâte = 500, sauce_tomates = 500, mozzarella = 500, olives = 500, jambon = 200, champignons = 300, artichauds = 200, aubergines = 100, courgettes = 100, anchois = 100, câpres = 100 ;")
cursor.execute("UPDATE UnitStock SET remaining_units = 500 where product = 1;")
cursor.execute("UPDATE UnitStock SET remaining_units = 200 where product = 2;")
cursor.execute("UPDATE UnitStock SET remaining_units = 100 where product = 3;")
cursor.execute("UPDATE UnitStock SET remaining_units = 200 where product = 4;")
cursor.execute("UPDATE UnitStock SET remaining_units = 100 where product = 5;")
cursor.execute("UPDATE Ordering SET status = 'livrée'")
cursor.execute("UPDATE Payment SET status = 'encaissé'")
db.commit()

