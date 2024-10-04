from DA_OOP_Product import *

def display_products(product_tuple: tuple):

    for product in product_tuple:
        print(product.get_Description())

def main():

    product_tuple = (Product("Bury My Heart at Wounded Knee", 1, 1), 
                     Book("Find Your People", 1, 1, "Jennie Allen"), 
                     Movie("Pretty Woman", 1, 1, "DVD (1990)"))
    
    display_products(product_tuple)
    
if __name__ == "__main__":
    main()