from exceptions import InvalidPriceException

class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.set_price(price)

    def set_price(self, price):
        if price <= 0:
            raise InvalidPriceException("Недійсна ціна страви")
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.description} - Ціна: {self.price}"
