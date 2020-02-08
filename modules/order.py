from data.mysql_connect import *
from features import *
from datetime import datetime
from tabulate import tabulate


class Order:

    def __init__(self, basket, customer, address):
        self.id = []
        #self.created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.basket = basket.id
        self.pos = basket.pos
        self.customer = customer.id
        self.amount = basket.total
        self.reception_mode = basket.reception_mode
        self.delivery = address.delivery
        self.reception_point = []
        self.validation = int()
        self.product_list = []

    def initialize(self):
        if self.reception_mode[0] == "à emporter":
            self.reception_point.append(self.pos.id[0])
        if self.reception_mode[0] == "à livrer":
            self.reception_point.append(self.delivery[0])
        cursor.execute('INSERT INTO Ordering'
                       ' (basket, customer, pos, reception_mode, reception_point, status)'
                       ' VALUES ({}, {}, {}, "{}", {}, "initialisée")'.format(self.basket[0], self.customer[0],
                       self.pos.id[0], self.reception_mode[0], self.reception_point[0]))
        db.commit()
        cursor.execute('SELECT id FROM Ordering WHERE basket = {}'.format(self.basket[0]))
        self.id.append(cursor.fetchone()[0])
        cursor.execute('SELECT product FROM Basket WHERE id = {}'.format(self.basket[0]))
        for item in cursor.fetchall():
            self.product_list.append(item[0])

    def edit_invoice(self):
        cursor.execute('SELECT first_name, last_name FROM Customer WHERE id = {}'.format(self.customer[0]))
        identity = cursor.fetchall()[0]
        cursor.execute('SELECT GROUP_CONCAT(a.street_number, " ", a.street, ", ", a.postal_code, " ", a.city)'
                       ' FROM Address AS a JOIN Customer AS c ON a.id = c.billing_address'
                       ' WHERE c.id = {}'.format(self.customer[0]))
        billing_address = cursor.fetchall()[0][0]
        cursor.execute('SELECT GROUP_CONCAT(street_number, " ", street, ", ", postal_code, " ", city)'
                       ' FROM Address WHERE id = {}'.format(self.reception_point[0]))
        address = cursor.fetchall()[0][0]
        cursor.execute('SELECT p.name, b.size, b.price, b.quantity FROM Basket b JOIN Product p ON b.product = p.id'
                       ' WHERE b.id = {}'.format(self.basket[0]))
        order_content = cursor.fetchall()
        cursor.execute('SELECT mode FROM Payment WHERE id = {}'.format(self.id[0]))
        payment = cursor.fetchone()[0]
        print(edit)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Commande n°{} enregistrée le {}\n".format(self.id[0], time))
        print("Client : ", identity[0], identity[1])
        print("Adresse de facturation : ", billing_address)
        print("\n", tabulate(order_content, headers=order_labels, tablefmt='grid'))
        print("\nTotal de {} euros payables {}.".format(self.amount[0], payment))
        print("Commande {} à l'adresse : {}.".format(self.reception_mode[0], address))
        self.validate()

    def validate(self):
        self.validation = int(input(validate_order))
        if self.validation == 1:
            cursor.execute('UPDATE Ordering SET status = "enregistrée" WHERE id = {}'.format(self.id[0]))
            cursor.execute('UPDATE Payment SET status = "en attente" WHERE id = {}'.format(self.id[0]))
            db.commit()
            print(thanks)
        else:
            cursor.execute('UPDATE Ordering SET status = "abandonnée" WHERE id = {}'.format(self.id[0]))
            cursor.execute('UPDATE Payment SET status = "abandonné" WHERE id = {}'.format(self.id[0]))
            cursor.execute('DELETE FROM Basket WHERE id = {}'.format(self.basket[0]))
            db.commit()
