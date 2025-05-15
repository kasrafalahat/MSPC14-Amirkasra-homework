class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product Name: {self.name}, Price: ${self.price:.2f}")

class ShoppingCart:
    def __init__(self):
        self.items = {}  # {product.name: {"product": product, "quantity": quantity}}

    def add_product(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]["quantity"] += quantity
        else:
            self.items[product.name] = {"product": product, "quantity": quantity}
        print(f"Added {quantity} x {product.name} to the cart.")

    def remove_product(self, product, quantity):
        if product.name in self.items:
            if self.items[product.name]["quantity"] <= quantity:
                del self.items[product.name]
                print(f"Removed {product.name} from the cart.")
            else:
                self.items[product.name]["quantity"] -= quantity
                print(f"Reduced {product.name} by {quantity}.")
        else:
            print(f"{product.name} is not in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["product"].price * item["quantity"]
        return total

    def display_cart(self):
        print("Cart contents:")
        for item in self.items.values():
            product = item["product"]
            quantity = item["quantity"]
            print(f"- {product.name}: {quantity} x ${product.price:.2f}")
        print(f"Total cost: ${self.calculate_total():.2f}")
