class Product:

    def __init__(self, name, price, discountPercent):
        self.__name = name
        self.__price = price
        self.__discountPercent = discountPercent

    def get_DiscountAmount(self):
        return self.__price * self.__discountPercent /100
    
    def get_DiscountPrice(self):
        return self.__price - self.get_DiscountAmount()
    
    def get_Description(self):
        return self.__name
    
class Book(Product):

    def __init__(self, name, price, discountPercent, author):
        super().__init__(name, price, discountPercent)
        self.__author = author
    
    def get_Description(self):
        return (super().get_Description() + " by " + self.__author)

class Movie(Product):
     
     def __init__(self, name, price, discountPercent, year):
         super().__init__(name, price, discountPercent)
         self.__year = year

     def get_Description(self):
        return (super().get_Description() + " (" + self.__year + ")")