#! /usr/bin/env python3
# coding: utf-8

"""
PizzaOrdering
manager
"""

from data.mysql_connect import *
from tabulate import tabulate
from features import *


class Manager:

    def __init__(self):
        self.pos = int()

    def launch(self):
        print(welcome_manager)
        self.pos = int(input("\n\tEntrez le numéro de votre point de vente : "))
        # Check orders
        cursor.execute('SELECT o.created, o.reception_mode, o.status, p.amount, p.mode, p.status'
                       ' FROM Ordering o JOIN Payment p ON o.id = p.id'
                       ' WHERE o.pos = {}'.format(self.pos))
        orders = cursor.fetchall()
        o_header = order_follow
        print("\n\n\tCommandes pour le point de vente n° {} :\n".format(self.pos))
        print(tabulate(orders, headers=o_header, tablefmt='grid'))
        cursor.execute('SELECT SUM(p.amount) FROM Payment p JOIN Ordering o ON p.id = o.id'
                       ' WHERE o.pos = {} and p.status = "encaissé"'.format(self.pos))
        turnover = cursor.fetchone()[0]
        print("\n\n\tTotal encaissé = {} EUR".format(turnover))
        cursor.execute('SELECT SUM(p.amount) FROM Payment p JOIN Ordering o ON p.id = o.id'
                       ' WHERE o.pos = {} and p.status = "en attente"'.format(self.pos))
        pending = cursor.fetchone()[0]
        if not pending:
            print("\n\tTotal en attente = 0 EUR")
        else:
            print("\n\tTotal en attente = {} EUR".format(pending))
        # Check stock
        print("\n\n\tStock d'ingrédients pour le point de vente n°{} :\n".format(self.pos))
        cursor.execute('SELECT * FROM Stock WHERE pos = {}'.format(self.pos))
        stock = cursor.fetchall()
        s_header = ingredient_list
        print(tabulate(stock, headers=s_header, tablefmt='grid'))
        print(
            '\n\tStock de produits pour le point de vente n°{} :\n'.format(
                self.pos))
        cursor.execute('SELECT p.name, u.remaining_units'
                       ' FROM UnitStock u JOIN Product p'
                       ' ON p.id = u.product WHERE u.pos = {}'.format(self.pos))
        prod_stock = cursor.fetchall()
        print(tabulate(prod_stock, tablefmt='grid'))


manager = Manager()
manager.launch()
