import random

# Food class to store food item details
class Food:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

# Restaurant class to manage food items
class Restaurant:
    def __init__(self):
        self.food_items = []

    # Add new food item to the menu
    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = Food(name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully")

    # Edit existing food item using food id
    def edit_food_item(self, food_id, name=None, quantity=None, price=None, discount=None, stock=None):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                if name:
                    food_item.name = name
                if quantity:
                    food_item.quantity = quantity
                if price:
                    food_item.price = price
                if discount:
                    food_item.discount = discount
                if stock:
                    food_item.stock = stock
                print("Food item edited successfully")
                return
        print("Food item not found")

    # View list of all food items
    def view_food_items(self):
        print("Food ID\tName\tQuantity\tPrice\tDiscount\tStock")
        for food_item in self.food_items:
            print(f"{food_item.food_id}\t{food_item.name}\t{food_item.quantity}\t{food_item.price}\t{food_item.discount}\t{food_item.stock}")

    # Remove a food item from the menu using food id
    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully")
                return
        print("Food item not found")

# User class to manage user details and orders
class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    # Place a new order
    def place_order(self, restaurant):
        print("Menu:")
        restaurant.view_food_items()
        selected_items = input("Enter the numbers of the food items you want to order (separated by commas): ")
        selected_items = selected_items.split(",")
        selected_food_items = []
        for item in selected_items:
            selected_food_items.append(restaurant.food_items[int(item)-1])
        print("Selected Items:")
        for food_item in selected_food_items:
            print(f"{food_item.name} ({food_item.quantity}) [INR {food_item.price}]")
        place_order = input("Do you want to place the order? (y/n): ")
        if place_order == "y":
            order_total = 0
            for food_item in selected_food_items:
                order_total += food_item.price
            self.order_history.append(selected_food_items)
            print("Order placed successfully")
            print(f"Order Total: INR {order_total}")
        else:
            print("Order cancelled")

    # View order history
    def view_order_history(self):
        if len(self.order_history) == 0:
            print("No orders found")