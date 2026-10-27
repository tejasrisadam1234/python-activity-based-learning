# Attendance Recovery Computation

total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
threshold = float(input("Enter required attendance percentage: "))

# Current attendance
current_percentage = (attended_classes / total_classes) * 100

print("\nCurrent Attendance:", round(current_percentage, 2), "%")

if current_percentage >= threshold:
    print("Status: Eligible")
    print("No recovery classes are required.")
else:
    print("Status: Not Eligible")

    # Find minimum consecutive classes required
    required_classes = 0

    while True:
        future_attended = attended_classes + required_classes
        future_total = total_classes + required_classes

        future_percentage = (future_attended / future_total) * 100

        if future_percentage >= threshold:
            break

        required_classes += 1

    print("Minimum consecutive classes required:",
          required_classes)

    print("Attendance after recovery:",
          round(future_percentage, 2), "%")

# Different future attendance scenarios
print("\n--- Future Attendance Scenarios ---")

scenarios = [5, 10, 15, 20]

for classes in scenarios:
    future_attended = attended_classes + classes
    future_total = total_classes + classes

    percentage = (future_attended / future_total) * 100

    print(
        classes,
        "future classes ->",
        round(percentage, 2),
        "%"
    )
