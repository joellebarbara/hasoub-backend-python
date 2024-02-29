class Item:
    def __init__(self, weight):
        self.weight = weight

class UniversalCharger(Item):
    def __init__(self, color, price, size, brand, weight):
        super().__init__(weight)
        self.color = color
        self.price = price
        self.size = size
        self.brand = brand

class Passport(Item):
    def __init__(self, color, weight, cost, bought_from):
        super().__init__(weight)
        self.color = color
        self.cost = cost
        self.bought_from = bought_from

class Sunglasses(Item):
    def __init__(self, have_case, color, origin, weight):
        super().__init__(weight)
        self.have_case = have_case
        self.color = color
        self.origin = origin

class Sneakers(Item):
    def __init__(self, brand, is_new, bought_from, weight):
        super().__init__(weight)
        self.brand = brand
        self.is_new = is_new
        self.bought_from = bought_from

class Smartphone(Item):
    def __init__(self, brand, os, storage, display, camera, materials, weight):
        super().__init__(weight)
        self.brand = brand
        self.os = os
        self.storage = storage
        self.display = display
        self.camera = camera
        self.materials = materials

class Laptop(Item):
    def __init__(self, brand, processor, ram, storage, graphics, weight):
        super().__init__(weight)
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.graphics = graphics

class Smartwatch(Item):
    def __init__(self, brand, display, battery_life, fitness_features, connectivity, weight):
        super().__init__(weight)
        self.brand = brand
        self.display = display
        self.battery_life = battery_life
        self.fitness_features = fitness_features
        self.connectivity = connectivity

class Campus(Item):
    def __init__(self, brand, accuracy, price, materials, weight):
        super().__init__(weight)
        self.brand = brand
        self.accuracy = accuracy
        self.price = price
        self.materials = materials

class Bag:
    def __init__(self, max_weight=80, max_items=6):
        self.max_weight = max_weight
        self.max_items = max_items
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.max_items and sum(item.weight for item in self.items) + item.weight <= self.max_weight:
            self.items.append(item)
            print(f"{type(item).__name__} added to the bag.")
        else:
            print("Cannot add item. Weight or item limit exceeded.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{type(item).__name__} removed from the bag.")
        else:
            print(f"{type(item).__name__} not found in the bag.")

    def print_all_items(self):
        for item in self.items:
            print(type(item).__name__)

    def print_items_by_category(self):
        categories = set(type(item).__name__ for item in self.items)
        for category in categories:
            items_in_category = [item for item in self.items if type(item).__name__ == category]
            print(f"{category}s: {', '.join(type(item).__name__ for item in items_in_category)}")

    def print_items_by_category_x(self, category_x):
        items_in_category_x = [item for item in self.items if type(item).__name__ == category_x]
        if items_in_category_x:
            print(f"{category_x}s: {', '.join(type(item).__name__ for item in items_in_category_x)}")
        else:
            print(f"No {category_x}s in the bag.")


bag = Bag()

charger = UniversalCharger("black", 50, "Medium", "Lenovo", 12)
passport = Passport("blue", 1, 50, "USA")
sunglasses = Sunglasses("yes", "black", "Italy", 10)

bag.add_item(charger)
bag.add_item(passport)
bag.add_item(sunglasses)

bag.print_all_items()
bag.print_items_by_category()
bag.print_items_by_category_x("Passport")

bag.remove_item(passport)
bag.print_all_items()
