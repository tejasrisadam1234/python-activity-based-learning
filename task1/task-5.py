# Retail Billing with Multiple Discount Rules

products = [
    {"name": "Laptop", "category": "Electronics", "price": 50000, "qty": 1},
    {"name": "Shirt", "category": "Clothing", "price": 1500, "qty": 2},
    {"name": "Rice Bag", "category": "Grocery", "price": 1200, "qty": 3},
    {"name": "Headphones", "category": "Electronics", "price": 2500, "qty": 1}
]

# Category-wise tax rates
tax_rates = {
    "Electronics": 18,
    "Clothing": 12,
    "Grocery": 5
}

# Discount rules
# If subtotal >= 50000 -> 10%
# If subtotal >= 25000 -> 7%
# If subtotal >= 10000 -> 5%
def calculate_discount(subtotal):
    if subtotal >= 50000:
        discount = subtotal * 0.10
    elif subtotal >= 25000:
        discount = subtotal * 0.07
    elif subtotal >= 10000:
        discount = subtotal * 0.05
    else:
        discount = 0

    # Maximum concession limit
    max_concession = 5000

    if discount > max_concession:
        discount = max_concession

    return discount


subtotal = 0
invoice = []

# Calculate item totals
for product in products:
    item_total = product["price"] * product["qty"]
    tax_rate = tax_rates[product["category"]]
    tax = item_total * tax_rate / 100

    invoice.append({
        "name": product["name"],
        "category": product["category"],
        "qty": product["qty"],
        "price": product["price"],
        "item_total": item_total,
        "tax_rate": tax_rate,
        "tax": tax
    })

    subtotal += item_total


# Calculate discount
discount = calculate_discount(subtotal)

# Total tax
total_tax = sum(item["tax"] for item in invoice)

# Final amount
final_amount = subtotal - discount + total_tax


# Print invoice
print("=" * 70)
print("                    RETAIL INVOICE")
print("=" * 70)

print(f"{'Product':<15}{'Category':<15}{'Qty':<5}{'Price':<10}{'Amount':<12}")
print("-" * 70)

for item in invoice:
    print(f"{item['name']:<15}"
          f"{item['category']:<15}"
          f"{item['qty']:<5}"
          f"{item['price']:<10.2f}"
          f"{item['item_total']:<12.2f}")

print("-" * 70)

print(f"Subtotal              : ₹{subtotal:.2f}")
print(f"Discount              : ₹{discount:.2f}")
print(f"Total Tax             : ₹{total_tax:.2f}")
print(f"Final Amount          : ₹{final_amount:.2f}")

print("=" * 70)
print("                 Thank You! Visit Again")
print("=" * 70)