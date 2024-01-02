from dish import Dish
from event_logger import EventLogger

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes
        self.event_logger = EventLogger()

    def add_dish(self, dish):
        self.dishes.append(dish)
        event = f"Додано страву '{dish.name}' до категорії '{self.name}'"
        self.event_logger.log_event(event)

    def remove_dish(self, dish):
        self.dishes.remove(dish)
        event = f"Видалено страву '{dish.name}' з категорії '{self.name}'"
        self.event_logger.log_event(event)

    def __str__(self):
        category_menu = f"{self.name}:\n"
        for dish in self.dishes:
            category_menu += f"- {dish}\n"
        return category_menu