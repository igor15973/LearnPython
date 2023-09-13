from .products import product
shopping_list = []

def shopping(product_name, how_much):
    if product_name in product:
        if how_much <= product[product_name]['quantity']:
            order_price = how_much * product[product_name]['price']
            order = product_name, str(how_much), str(order_price)
            shopping_list.append(order)
            return shopping_list
        else:
            print('Niewystarczająca ilość produktu w magazynie')
    else:
        print('Nie ma takiego produktu')
