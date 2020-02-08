from data.mysql_connect import *
from modules.queries import *


class Stock:

    def __init__(self, order, pos):
        self.order = order.basket
        self.pos = pos.id
        self.product_list = order.product_list

    def update(self):
        # Update ingredient stock
        for i in range(len(self.product_list)):
            spec_pos = "WHERE b.id = {} AND b.product = {} " \
                       "AND s.pos = {}".format(self.order[0], self.product_list[i], self.pos[0])
            cursor.execute(prod_q[self.product_list[i] - 1] + spec_pos)
        # Update unit stock
        for i in range(len(update_q)):
            spec_line = 'AND u.pos = {}'.format(self.pos[0])
            cursor.execute(update_q[i] + spec_line)
        # Update basic product
        cursor.execute(update_q[0] + 'AND u.pos = {}'.format(self.pos[0]))
        db.commit()
