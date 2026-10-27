# Progressive Electricity Billing

def calculate_bill(units):
    fixed_charge = 100

    # Calculate energy charge using slabs
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    subtotal = energy_charge + fixed_charge

    # Surcharge: 5% if units exceed 300
    surcharge = subtotal * 0.05 if units > 300 else 0

    # Rebate: 10% if units are 100 or less
    rebate = subtotal * 0.10 if units <= 100 else 0

    final_bill = subtotal + surcharge - rebate

    return final_bill


# Number of months
n = int(input("Enter number of months: "))

bills = []

for i in range(n):
    print("\nMonth", i + 1)
    units = float(input("Enter electricity units consumed: "))

    bill = calculate_bill(units)
    bills.append((units, bill))

    print("Electricity Bill: ₹", round(bill, 2))


# Compare bills
print("\n--- Monthly Bill Comparison ---")

for i, (units, bill) in enumerate(bills, 1):
    print(f"Month {i}: {units} units -> ₹{bill:.2f}")

# Find unusual increases
print("\n--- Unusual Increase Detection ---")

for i in range(1, n):
    previous_bill = bills[i - 1][1]
    current_bill = bills[i][1]

    increase = ((current_bill - previous_bill) / previous_bill) * 100

    if increase > 20:
        print(
            f"Month {i + 1}: Unusual increase of "
            f"{increase:.2f}%"
        )
    else:
        print(
            f"Month {i + 1}: Normal change "
            f"({increase:.2f}%)"
        )