from restaurant_system.products import Burger
from restaurant_system.counter import Order

def test_1():
    order1 = Order("ORD101")

    burger_1 = Burger()
    burger_1.add_patty()
    burger_1.add_cheese()
    order1.add_item(burger_1)

    burger_2 = Burger()
    burger_2.add_patty()
    order1.add_item(burger_2)

    order1.details()

def test_2():
    order2 = Order("ORD102")

    burger_3 = Burger()
    burger_3.add_patty()
    burger_3.add_cheese()
    order2.add_item(burger_3)

    burger_4 = Burger()
    burger_4.add_cheese()
    order2.add_item(burger_4)

    order2.details()

if __name__ == '__main__':
    test_1()
    test_2()
