# Smart Canteen Order and Stock Management

# Available inventory with prices
inventory = {
    "Idly": {"price": 30, "stock": 20},
    "Dosa": {"price": 40, "stock": 15},
    "Meals": {"price": 80, "stock": 10},
    "Tea": {"price": 15, "stock": 30},
    "Juice": {"price": 25, "stock": 20}
}

total_sales = 0
successful_orders = 0

n = int(input("Enter number of customer orders: "))

for order_no in range(1, n + 1):
    print("\nCustomer", order_no)
    print("Available items:", ", ".join(inventory.keys()))

    item = input("Enter item name: ").title()
    quantity = int(input("Enter quantity: "))

    # Validate item
    if item not in inventory:
        print("Item unavailable!")
        continue

    # Validate quantity
    if quantity <= 0:
        print("Invalid quantity!")
        continue

    # Check stock
    if quantity > inventory[item]["stock"]:
        print("Order rejected! Only",
              inventory[item]["stock"], item, "available.")
        continue

    # Calculate bill
    price = inventory[item]["price"]
    bill = price * quantity

    # Update stock
    inventory[item]["stock"] -= quantity

    total_sales += bill
    successful_orders += 1

    print("Order accepted!")
    print("Item:", item)
    print("Quantity:", quantity)
    print("Bill: ₹", bill)
    print("Remaining stock:", inventory[item]["stock"])

# Daily summary
print("\n========== DAILY SUMMARY ==========")
print("Successful orders:", successful_orders)
print("Total sales: ₹", total_sales)

print("\nRemaining Stock:")
for item, details in inventory.items():
    print(item, ":", details["stock"])

# Low-stock items
print("\nLow Stock Items:")
for item, details in inventory.items():
    if details["stock"] <= 5:
        print(item, "-", details["stock"], "remaining")
