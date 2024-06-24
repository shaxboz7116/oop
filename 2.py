class Phone:
    def __init__(self, model, ram, price, color):
        self.model = model
        self.ram = ram
        self.price = price
        self.color = color

phone1 = Phone("Samsung Galaxy S21", "8GB", 10000000, "Black")

print("Model:", phone1.model)
print("RAM:", phone1.ram)
print("Price:", phone1.price)
print("Color:", phone1.color)
