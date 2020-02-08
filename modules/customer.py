from data.mysql_connect import *


class Customer:

    def __init__(self):
        self.login_info = []
        self.id = []

    def authenticate(self):
        email = input("\n\tEntrez votre email : ")
        self.login_info.append(email)
        pw = input('\tSaisissez votre mot de passe : ')
        self.login_info.insert(1, pw)
        cursor.execute('SELECT id FROM Customer WHERE email = "{}" and password = "{}"'.format(
            self.login_info[0], self.login_info[1]))
        self.id.append(cursor.fetchone()[0])
