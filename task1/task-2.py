

applicants = [
    {"name": "Ravi", "marks": 85, "maths": 80, "physics": 75,
     "attendance": 90, "income": 150000},

    {"name": "Sita", "marks": 92, "maths": 88, "physics": 85,
     "attendance": 95, "income": 120000},

    {"name": "Kiran", "marks": 78, "maths": 70, "physics": 65,
     "attendance": 85, "income": 180000},

    {"name": "Anu", "marks": 92, "maths": 88, "physics": 85,
     "attendance": 95, "income": 120000},

    {"name": "Priya", "marks": 88, "maths": 82, "physics": 80,
     "attendance": 92, "income": 100000}
]


MIN_MARKS = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 200000

eligible = []


for student in applicants:
    if (student["marks"] >= MIN_MARKS and
        student["maths"] >= MIN_SUBJECT_MARKS and
        student["physics"] >= MIN_SUBJECT_MARKS and
        student["attendance"] >= MIN_ATTENDANCE and
        student["income"] <= MAX_INCOME):

        eligible.append(student)


# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
# 4. Alphabetical name if still tied

eligible.sort(
    key=lambda x: (-x["marks"], -x["attendance"], x["income"], x["name"])
)


print("UNIVERSITY SCHOLARSHIP ALLOCATION")
print("----------------------------------")

print("\nEligible Students and Ranking:")

for rank, student in enumerate(eligible, start=1):
    print(
        f"{rank}. {student['name']} | "
        f"Marks: {student['marks']} | "
        f"Attendance: {student['attendance']}% | "
        f"Income: ₹{student['income']}"
    )


print("\nNot Eligible Students:")

for student in applicants:
    if student not in eligible:
        print(student["name"])