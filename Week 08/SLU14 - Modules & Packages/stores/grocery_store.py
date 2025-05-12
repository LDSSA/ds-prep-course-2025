class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

class GroceryStore:
    def __init__(self, name, address, items):
        self.name = name
        self.address = address
        self.items = items

    def get_total_sales(self):
        total_sales = 0
        for item in self.items:
            total_sales += item.get_total_price()
        return total_sales

description = "This is a module named grocery_store."

if __name__ == "__main__":
    items = [
        Item("Bananas", 0.50, 10),
        Item("Apples", 0.75, 5),
        Item("Oranges", 1.00, 3),
    ]

    grocery_store = GroceryStore("My Grocery Store", "123 Main St", items)

    print(f"Total sales: ${grocery_store.get_total_sales():.2f}")
