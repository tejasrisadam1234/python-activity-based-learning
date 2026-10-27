
venue = float(input("Enter venue cost: ₹"))
equipment = float(input("Enter equipment cost: ₹"))
catering_per_person = float(input("Enter catering cost per participant: ₹"))
transport = float(input("Enter transport cost: ₹"))
certificate_per_person = float(input("Enter certificate cost per participant: ₹"))

participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant: ₹"))
sponsorship = float(input("Enter sponsorship amount: ₹"))

fixed_cost = venue + equipment + transport

variable_cost = (catering_per_person + certificate_per_person) * partic
total_cost = fixed_cost + variable_cost
participant_contribution = participants * registration_fee


total_funds = participant_contribution + sponsorship


shortfall = total_cost - total_funds

cost_per_participant = catering_per_person + certificate_per_person
amount_available_per_registration = registration_fee - cost_per_participant

if amount_available_per_registration > 0:
    minimum_registrations = (fixed_cost - sponsorship) / amount_available_per_registration

    if minimum_registrations < 0:
        minimum_registrations = 0

    minimum_registrations = int(minimum_registrations) + (
        1 if minimum_registrations % 1 != 0 else 0
    )
else:
    minimum_registrations = "Not possible with the given registration fee"

# Display results
print("\n----- CAMPUS EVENT FINANCIAL PLAN -----")
print(f"Fixed Cost: ₹{fixed_cost:.2f}")
print(f"Variable Cost: ₹{variable_cost:.2f}")
print(f"Total Event Cost: ₹{total_cost:.2f}")
print(f"Participant Contribution: ₹{participant_contribution:.2f}")
print(f"Sponsorship: ₹{sponsorship:.2f}")
print(f"Sponsorship Shortfall: ₹{max(0, shortfall):.2f}")

if isinstance(minimum_registrations, int):
    print(f"Minimum Registrations to Break Even: {minimum_registrations}")
else:
    print(f"Minimum Registrations: {minimum_registrations}")

if total_funds >= total_cost:
    print("Event Status: BREAK EVEN / PROFIT")
else:
    print("Event Status: FUNDING SHORTFALL")