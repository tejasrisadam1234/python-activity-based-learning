from datetime import datetime

# Parking rates per hour
rates = {
    "car": 30,
    "bike": 15,
    "suv": 50,
    "truck": 60
}

# Maximum daily charges
daily_limits = {
    "car": 200,
    "bike": 100,
    "suv": 300,
    "truck": 350
}

PENALTY = 100


def get_time(prompt):
    while True:
        value = input(prompt)

        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M")

        except ValueError:
            print("Invalid time! Use format: YYYY-MM-DD HH:MM")


print("===== SMART PARKING FEE MANAGEMENT =====")

vehicle = input("Enter vehicle category (car/bike/suv/truck): ").lower()

if vehicle not in rates:
    print("Invalid vehicle category!")
    exit()

entry = get_time("Enter entry time (YYYY-MM-DD HH:MM): ")
exit_time = get_time("Enter exit time (YYYY-MM-DD HH:MM): ")

# Validate exit time
if exit_time <= entry:
    print("Invalid input: Exit time must be after entry time.")
    exit()

# Calculate parking duration
duration_seconds = (exit_time - entry).total_seconds()
hours = duration_seconds / 3600

# Charge partial hours as a full hour
charged_hours = int(hours)

if hours > charged_hours:
    charged_hours += 1

# Check overnight parking
overnight = entry.date() != exit_time.date()

# Calculate basic fee
fee = charged_hours * rates[vehicle]

# Apply daily limit
number_of_days = (exit_time.date() - entry.date()).days + 1
maximum_fee = number_of_days * daily_limits[vehicle]

if fee > maximum_fee:
    fee = maximum_fee

# Penalty conditions
penalty = 0

# Penalty for parking longer than 24 hours
if duration_seconds > 24 * 60 * 60:
    penalty += PENALTY

# Penalty for very long parking
if charged_hours > 72:
    penalty += PENALTY

total = fee + penalty

# Display bill
print("\n========== PARKING BILL ==========")
print("Vehicle Category :", vehicle.upper())
print("Entry Time       :", entry.strftime("%Y-%m-%d %H:%M"))
print("Exit Time        :", exit_time.strftime("%Y-%m-%d %H:%M"))
print("Parking Hours    :", round(hours, 2))
print("Charged Hours    :", charged_hours)
print("Overnight        :", "Yes" if overnight else "No")
print("Parking Fee      : ₹", fee)
print("Penalty          : ₹", penalty)
print("----------------------------------")
print("TOTAL AMOUNT     : ₹", total)
print("==================================")