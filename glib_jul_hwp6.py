from dish import Dish
from menu_category import MenuCategory
from exceptions import InvalidPriceException
from event_logger import EventLogger

event_logger = EventLogger()

class Order:
    def __init__(self):
        self.items = []

    def add_dish(self, dish):
        if dish not in self.items:
            self.items.append(dish)
            event = f"Додано страву '{dish.name}' до замовлення"
            event_logger.log_event(event)
        else:
            event = f"Страва '{dish.name}' вже присутня в замовленні"
            event_logger.log_event(event)

    def __iadd__(self, dish):
        self.add_dish(dish)
        return self

    def remove_dish(self, dish):
        self.items.remove(dish)
        event = f"Видалено страву '{dish.name}' з замовлення"
        event_logger.log_event(event)

    def __str__(self):
        order_details = ""
        for dish in self.items:
            order_details += f"- {dish}\n"
        return order_details

try:
    dish1 = Dish("Броколі", "Дієтичний овочевий салат", 100)
    dish2 = Dish("Креветки темпура", "Ніжна японська закуска з хрусткою скоринкою", 250)
    dish3 = Dish("Вареники з вишнями", "Традиційна українська кухня", 300)
    dish4 = Dish("Шоколадний фондан", "Класичний французький десерт", 90)
    category1 = MenuCategory("Закуски", [dish1])
    category2 = MenuCategory("Основні страви", [dish2])
    category3 = MenuCategory("Десерти", [dish3, dish4])

    order = Order()
    order += dish1
    order += dish2
    order += dish3
    order += dish4
    order += dish4  # Додавання дубльованої страви

    print("Меню:")
    print(category1)
    print(category2)
    print(category3)

    print("Замовлення:")
    print(order)

    print("Лог подій:")
    event_logger.print_log()

except InvalidPriceException as e:
    event = f"InvalidPriceException: {str(e)}"
    event_logger.log_event(event)
    print(f"Помилка: {str(e)}")