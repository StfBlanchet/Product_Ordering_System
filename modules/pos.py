from features import *
from data.mysql_connect import *


class PoS:

    def __init__(self):
        self.ref = int()
        self.id = []
        self.address = []
        self.name = str()

    def identify(self):
        code = input("\n\tEntrez le code postal : ")
        if code in pos1:
            self.ref = 1
        if code in pos2:
            self.ref = 2
        if code in pos3:
            self.ref = 3
        if code in pos4:
            self.ref = 4
        if code in pos5:
            self.ref = 5
        self.id.append(self.ref)

    def location(self):
        cursor.execute("SELECT GROUP_CONCAT(street_number, ' ', street, ', ', postal_code, ' ', city)"
                       " FROM Address WHERE id = {}".format(self.ref))
        self.address = cursor.fetchall()[0][0]
        cursor.execute("SELECT name FROM PoS WHERE id = {}".format(self.ref))
        self.name = cursor.fetchone()[0]
        print('\n\tVotre point de vente "{}" se trouve {}.\n'.format(self.name, self.address))

