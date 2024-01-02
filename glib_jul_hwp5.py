from dish import Dish
from menu_category import MenuCategory
from exceptions import InvalidPriceException
from event_logger import EventLogger

event_logger = EventLogger()

try:
    dish1 = Dish("Броколі", "Дієтичний овочевий салат", 100)
    dish2 = Dish("Креветки темпура", "Ніжна японська закуска з хрусткою скоринкою", 250)
    dish3 = Dish("Вареники з вишнями", "Традиційна українська кухня", 300)
    dish4 = Dish("Шоколадний фондан", "Класичний французький десерт", 90)
    category1 = MenuCategory("Закуски", [dish1])
    category2 = MenuCategory("Основні страви", [dish2])
    category3 = MenuCategory("Десерти", [dish3, dish4])
    invalid_dish = Dish("Страва з недійсною ціною", "Опис страви", -50)
except InvalidPriceException as e:
    event = f"InvalidPriceException: {str(e)}"
    event_logger.log_event(event)
    print(f"Помилка: {str(e)}")

print("Меню:")
print(category1)
print(category2)
print(category3)

print("Лог подій:")
event_logger.print_log()