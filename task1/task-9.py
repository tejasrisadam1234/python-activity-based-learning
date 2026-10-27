# Progressive Water Tariff Analysis

def calculate_bill(units):
    fixed_fee = 100
    penalty = 0

    # Progressive tariff slabs
    if units <= 10:
        bill = units * 5
    elif units <= 20:
        bill = (10 * 5) + ((units - 10) * 8)
    elif units <= 30:
        bill = (10 * 5) + (10 * 8) + ((units - 20) * 12)
    else:
        bill = (10 * 5) + (10 * 8) + (10 * 12) + ((units - 30) * 18)

    # Excessive usage penalty
    if units > 40:
        penalty = 200
    elif units > 30:
        penalty = 100

    total = bill + fixed_fee + penalty
    return bill, penalty, total


# Number of households
n = int(input("Enter number of households: "))

households = []

for i in range(n):
    print(f"\nHousehold {i + 1}")
    name = input("Enter household name: ")
    units = float(input("Enter water consumption (KL): "))

    if units < 0:
        print("Invalid consumption!")
        continue

    bill, penalty, total = calculate_bill(units)

    households.append({
        "name": name,
        "units": units,
        "bill": bill,
        "penalty": penalty,
        "total": total
    })


# Display results
print("\n========== WATER BILL REPORT ==========")
print(f"{'Household':<15}{'Usage':<10}{'Bill':<10}{'Penalty':<10}{'Total':<10}")

for h in households:
    print(f"{h['name']:<15}{h['units']:<10.1f}"
          f"{h['bill']:<10.2f}{h['penalty']:<10.2f}"
          f"{h['total']:<10.2f}")


# Compare consumption
if households:
    highest = max(households, key=lambda x: x["units"])
    lowest = min(households, key=lambda x: x["units"])

    print("\n========== CONSUMPTION ANALYSIS ==========")
    print("Highest Consumption :", highest["name"],
          "-", highest["units"], "KL")
    print("Lowest Consumption  :", lowest["name"],
          "-", lowest["units"], "KL")

    print("\nExcessive Usage Households (>30 KL):")

    found = False
    for h in households:
        if h["units"] > 30:
            print(h["name"], "-", h["units"], "KL")
            found = True

    if not found:
        print("No household has excessive usage.")
