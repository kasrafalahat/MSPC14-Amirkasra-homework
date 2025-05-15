from .constants import CONSTANTS

class Burger:
    """Represents a single burger item with customizable toppings."""

    def __init__(self):
        """Initializes a basic burger with no patty or cheese added yet."""
        self.patty = False
        self.cheese = False
        self.base_price = CONSTANTS['BURGER_BASE_PRICE']

    def add_patty(self):
        """Adds a patty to the burger."""
        self.patty = True
        print("Patty added...")

    def add_cheese(self):
        """Adds cheese to the burger."""
        self.cheese = True
        print("Cheese added...")

    def get_price(self) -> float:
        """Calculates the total price of the burger based on added toppings."""
        price = self.base_price
        if self.patty:
            price += CONSTANTS['ADDITIONAL_PATTY_PRICE']
        if self.cheese:
            price += CONSTANTS['ADDITIONAL_CHEESE_PRICE']
        return price

    def get_name(self) -> str:
        """Generates the display name for the burger based on added toppings."""
        if self.patty and self.cheese:
            return "Cheese Burger"
        elif not self.patty and self.cheese:
            return "Veggie Cheese Burger"
        else:
            return "Burger"
