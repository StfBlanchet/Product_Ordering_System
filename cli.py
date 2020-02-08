from modules.pos import *
from modules.basket import *
from modules.customer import *
from modules.address import *
from modules.order import *
from modules.payment import *
from modules.stock import *


pos = PoS()
basket = Basket(pos)
customer = Customer()
address = Address(customer)
order = Order(basket, customer, address)
payment = Payment(order)
stock = Stock(order, pos)


def shopping_process():
    basket.create_line()
    add_line()

def ordering_process():
    order.initialize()
    payment.get_details()
    order.edit_invoice()
    if int(order.validation) == 1:
        stock.update()
    else:
        pass

def add_line():
    more = input(add_product)
    if int(more) == 1:
        basket.line.clear()
        shopping_process()
    if int(more) == 2:
        customer.authenticate()

def user_path():
    print(welcome_user)
    basket.initialize()
    # take_away choice
    if basket.mode == 1:
        shopping_process()
        ordering_process()
    # delivery choice
    if basket.mode == 2:
        shopping_process()
        address.delivery_loc()
        ordering_process()

user_path()
