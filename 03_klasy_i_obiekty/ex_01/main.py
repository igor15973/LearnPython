class Product:
    pass


class Order:
    pass


class Potato:
    pass


class Apple:
    pass


antonowka = Apple()
papierowka = Apple()
lobo = Apple()

frytki = Potato()
chipsy = Potato()

print(type(frytki))
print(type(chipsy))
print(type(antonowka))
print(type(papierowka))
print(type(lobo))


kebab = Order()
pizza = Order()
burger = Order()

orders = [
    kebab,
    pizza,
    burger
]

products = {
    'cola' : Product(),
    'fanta' : Product()
}

for order in orders:
    print(type(order))

for product in products.values():
    print(type(product))