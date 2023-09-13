product = {
    'chleb': {
        'price': 2.50,
        'quantity': 100
    },
    'jajka': {
        'price': 8.30,
        'quantity': 70
    }
}

def new_quantity(product_name, order_quantity):
    product[product_name]['quantity'] -= order_quantity