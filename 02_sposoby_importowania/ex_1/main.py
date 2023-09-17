from shop.shopper import shopping
from shop.shopper import shopping_list

if __name__ ==  '__main__':
    while True:
        product_answere = input('Podaj nazwe produktu lub wybiesz "x" aby wyjść: ')
        if product_answere != 'x':
            quantity_answere = int(input('Podaj liczbe zamawianych produktów: '))
            shopping(product_answere, quantity_answere)
        else:
            print('\n',shopping_list)
            break


