from features import *
from data.mysql_connect import *


class Basket:

    def __init__(self, pos):
        self.id = []
        self.mode = int()
        self.reception_mode = []
        self.pos = pos
        self.ref = []
        self.line = []
        self.total = []

    def initialize(self):
        cursor.execute('SELECT CONNECTION_ID()')
        self.id.append(cursor.fetchone()[0])
        self.mode = int(input(set_reception))
        self.pos.identify()
        if self.mode == 1:
            self.reception_mode.append("à emporter")
            self.pos.location()
        if self.mode == 2:
            self.reception_mode.append("à livrer")

    def create_line(self):
        product_id = int(input(choose_product))
        self.line.append(product_id)
        cursor.execute('SELECT entry_price FROM Product WHERE id = {}'.format(self.line[0]))
        self.line.extend(cursor.fetchall()[0])
        entry_price = self.line[1]
        get_size = int(input(choose_size))
        size = str()
        serving = float()
        price = int()
        if get_size == 1:
            size = "small"
            serving = small_serving
            price = entry_price
        if get_size == 2:
            size = "medium"
            serving = medium_serving
            price = entry_price + medium_pricing
        elif get_size == 3:
            size = "large"
            serving = large_serving
            price = entry_price + large_pricing
        quantity = int(input("\n\tEntrez la quantité souhaitée : "))
        self.line.extend((size, serving, price, quantity))
        self.check_units()
        cursor.execute('INSERT INTO Basket (id, product, size, serving, price, quantity)'
                       ' VALUES ({}, {}, "{}", {}, {}, {})'.format(self.id[0], self.line[0], self.line[2],
                       self.line[3], self.line[4], self.line[5]))
        db.commit()
        self.total.clear()
        self.calculate_total()

    def check_units(self):
        cursor.execute('SELECT remaining_units FROM UnitStock'
                       ' WHERE product = {} AND pos = {}'.format(self.line[0], self.pos.id[0]))
        availability = cursor.fetchone()[0]
        if availability >= self.line[3] * self.line[5]:
            pass
        else:
            print(no_stock)
            self.line.clear()
            self.create_line()

    def calculate_total(self):
        cursor.execute('SELECT SUM(price * quantity) FROM Basket WHERE id = {}'.format(self.id[0]))
        self.total.append(cursor.fetchone()[0])
        print("\n\tVotre commande s'élève à {} euros.\n".format(self.total[0]))
