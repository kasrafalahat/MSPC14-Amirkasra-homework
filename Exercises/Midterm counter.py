from .products import Burger

class Order:
    """Manages a single customer order, tracking items and calculating totals."""

    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        print(f"Order {self.order_id} started.")

    def add_item(self, burger: Burger):
        price = burger.get_price()
        if price <= 0:
            print("Item price must be positive.")
            return
        item_data = {'name': burger.get_name(), 'price': price}
        self.items.append(item_data)
        print(f'"{item_data["name"]}" added to order.')

    def get_total(self) -> float:
        return sum(item['price'] for item in self.items)

    def details(self):
        print(f"\nOrder ID: {self.order_id}\n")
        if not self.items:
            print("\n(No items in this order)")
        else:
            for item in self.items:
                print(f"- {item['name']}: ${item['price']}")
        total = self.get_total()
        print(f"\nTotal: ${total}\n")
