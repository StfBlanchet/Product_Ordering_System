from data.mysql_connect import *
from features import *


class Payment:

    def __init__(self, order):
        self.id = order.id
        self.amount = order.amount
        self.mode = str()

    def get_details(self):
        set = int(input(set_payment))
        if set == 1:
            self.mode = "en ligne"
        if set == 2:
            self.mode = "à réception"
        cursor.execute('INSERT INTO Payment (id, amount, mode, status) '
                       'VALUES ({}, {}, "{}", "initialisé")'.format(self.id[0], self.amount[0], self.mode))
        db.commit()
