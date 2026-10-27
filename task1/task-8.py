from datetime import datetime, timedelta

# Parking rates per hour
rates = {
    "car": 30,
    "bike": 15,
    "suv": 40,
    "truck": 50
}

DAILY_LIMIT = {
    "car": 200,
    "bike": 100,
    "suv": 250,
    "truck": 300
}

def get_time(prompt):
    while True:
        time_str = input(prompt)

        try:
            return datetime.strptime(time_str, "%H:%M")
        except ValueError:
            print("Invalid time! Please enter time in HH:MM format.")

def calculate_parking_fee(vehicle, entry, exit_time):
    # Handle overnight parking
    if exit_time < entry:
        exit_time += timedelta(days=1)

    duration = exit_time - entry
    minutes = duration.total_seconds() / 60
    hours = int(minutes // 60)

    # Charge for every started hour
    if minutes % 60 != 0:
        hours += 1

    # Maximum parking duration
    if hours > 24:
        penalty = 100
        print("Penalty: Parking exceeded 24 hours. ₹100 penalty added.")
    else:
        penalty = 0

    # Calculate normal fee
    fee = hours * rates[vehicle]

    # Apply daily limit
    if fee > DAILY_LIMIT[vehicle]:
        fee = DAILY_LIMIT[vehicle]

    total = fee + penalty

    return hours, fee, penalty, total


# Main program
print("===== SMART PARKING FEE MANAGEMENT =====")

# Vehicle validation
while True:
    vehicle = input("Enter vehicle category (car/bike/suv/truck): ").lower()

    if vehicle in rates:
        break
    else:
        print("Invalid vehicle category!")

entry_time = get_time("Enter entry time (HH:MM): ")
exit_time = get_time("Enter exit time (HH:MM): ")

# Calculate
hours, fee, penalty, total = calculate_parking_fee(
    vehicle, entry_time, exit_time
)

# Display bill
print("\n========== PARKING BILL ==========")
print("Vehicle Category :", vehicle.upper())
print("Parking Duration :", hours, "hour(s)")
print("Parking Fee      : ₹", fee)
print("Penalty          : ₹", penalty)
print("Total Amount     : ₹", total)
print("==================================")