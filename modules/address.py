from data.mysql_connect import *


class Address:

    def __init__(self, customer):
        self.id = int()
        self.customer = customer.id
        self.delivery = []

    def delivery_loc(self):
        cursor.execute("SELECT GROUP_CONCAT(a.street_number, ' ', a.street, ', ', a.postal_code, ' ', a.city) "
                       "FROM Address AS a JOIN Customer AS c ON a.id = c.billing_address "
                       "WHERE c.id = {}".format(self.customer[0]))
        billing_address = cursor.fetchall()[0][0]
        print("\n\tSouhaitez-vous être livré à : {} ?".format(billing_address))
        delivery_point = input("\tOUI=1 / NON=2 \n\t")
        if int(delivery_point) == 1:
            cursor.execute("SELECT a.id FROM Address AS a JOIN Customer AS c "
                           "ON a.id = c.billing_address WHERE c.id = {}".format(self.customer[0]))
            self.delivery.append(cursor.fetchone()[0])
        elif int(delivery_point) == 2:
            self.add_new()

    def add_new(self):
        print("\n\tVeuillez renseigner l'adresse de livraison :\n")
        street = input("\true / avenue / boulevard : ")
        street_number = input("\tnuméro : ")
        postal_code = input("\tcode postal : ")
        city = input("\tville : ")
        complements = input("\tcompléments : ")
        cursor.execute("SELECT id FROM Address "
                       "WHERE street = '{}' AND street_number = {} AND city = '{}' "
                       "AND postal_code = {}".format(street, street_number, city, postal_code))
        if cursor.fetchone() is not None:
            self.delivery.append(cursor.fetchone()[0])
        else:
            cursor.execute("INSERT INTO Address (street, street_number, city, complements, postal_code) "
                           "VALUES ('{}', {}, '{}', '{}', {})".format(street, int(street_number), city, complements,
                            int(postal_code)))
            db.commit()
            cursor.execute("SELECT id FROM Address "
                           "WHERE street = '{}' AND street_number = {} AND city = '{}' "
                           "AND postal_code = {}".format(street, street_number, city, postal_code))
            self.delivery.append(cursor.fetchone()[0])
