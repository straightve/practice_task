class FoodItems:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_name(self):
        """Getter function - returns the name"""
        return self.__name

    def get_price(self):
        """Getter function - returns the price"""
        return self.__price

    def get_stock(self):
        return self.__stock

    def set_price(self, new_price):
        """Setter function - sets a new price for the comic.

        Args:
            new_price (int): the new price for the comic
        """
        # catches any invalid values being passed from the UI
        if new_price is None or type(new_price) is not int:
            print("Price must be an integer")
            return
            # simple boundary test - is the price positive?
        if new_price <= 0:
            print("price must be positive")
            return
        self.__price = new_price
