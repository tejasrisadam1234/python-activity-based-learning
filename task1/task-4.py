# Hospital Billing and Patient Classification

# Input patient details
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
payment_type = input("Enter payment type (Insurance/Self-Pay): ").lower()

consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

# Calculate total
total = consultation + diagnostic + treatment

# Apply conditional concessions
concession = 0

if age >= 60:
    concession = total * 0.20       # 20% senior citizen concession
elif payment_type == "insurance":
    concession = total * 0.10       # 10% insurance concession
elif total >= 10000:
    concession = total * 0.05       # 5% high-bill concession

final_bill = total - concession

# Billing validation
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid billing: Charges cannot be negative.")
elif total == 0:
    print("Invalid billing: Total charge cannot be zero.")
else:
    # Patient classification
    if final_bill < 5000:
        category = "Basic Patient"
    elif final_bill < 15000:
        category = "Standard Patient"
    else:
        category = "Premium Patient"

    # Display bill
    print("\n----- HOSPITAL BILL -----")
    print("Patient Name:", name)
    print("Age:", age)
    print("Payment Type:", payment_type.title())
    print("Consultation Charge: ₹", consultation)
    print("Diagnostic Charge: ₹", diagnostic)
    print("Treatment Charge: ₹", treatment)
    print("Total Amount: ₹", total)
    print("Concession: ₹", concession)
    print("Final Bill: ₹", final_bill)
    print("Patient Classification:", category)