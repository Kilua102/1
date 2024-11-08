class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price * self.quantity


    def display_info(self):
        total_price = self.calculate_total_price()
        print(f"Назва товару")
        print(f"Ціна за одиницю грн")
        print(f"Кількість одиниць")
        print(f"Загальна вартість грн")


product1 = Product("Ноутбук", 15000, 2)
product1.display_info()
