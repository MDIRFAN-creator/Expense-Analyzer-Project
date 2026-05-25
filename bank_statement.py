import pandas as pd
import random
from datetime import datetime, timedelta

# Random names
names = [
    "RAMESH", "SURESH", "ARUN", "AKBAR", "PRIYA",
    "RAHUL", "NASEEM", "VIKRAM", "MOHAN", "KARTHIK"
]

# Random transaction keywords
keywords = [
    "UPI", "IMPS", "NEFT", "ATM", "SALARY",
    "SWIGGY", "ZOMATO", "AMAZON", "FLIPKART",
    "JIO", "AIRTEL", "OLA", "UBER",
    "NETFLIX", "SPOTIFY", "PETROL", "APOLLO"
]

data = []

balance = random.randint(50000, 200000)

start_date = datetime(2025, 1, 1)

for i in range(300):

    date = start_date + timedelta(days=random.randint(0, 120))

    txn_type = random.choice(keywords)

    amount = random.randint(50, 20000)

    ref_no = random.randint(100000000000, 999999999999)

    withdrawal = ""
    deposit = ""

    # Different transaction styles
    if txn_type == "SALARY":
        deposit = amount
        balance += amount

        description = f"SALARY CREDIT/{random.choice(['TCS','INFOSYS','WIPRO','ACCENTURE'])}"

    elif txn_type == "ATM":
        withdrawal = amount
        balance -= amount

        description = f"ATW/{random.randint(1000,9999)}/CASH WITHDRAWAL"

    elif txn_type in ["UPI", "IMPS", "NEFT"]:
        withdrawal = amount
        balance -= amount

        description = f"{txn_type}/{random.choice(names)}/{ref_no}/Payment"

    else:
        withdrawal = amount
        balance -= amount

        description = f"UPI/{txn_type}/{ref_no}/Payment"

    data.append([
        date.strftime("%d-%m-%Y"),
        description,
        ref_no,
        withdrawal,
        deposit,
        balance
    ])

# Create dataframe
df = pd.DataFrame(data, columns=[
    "Date",
    "Description",
    "Chq/Ref No",
    "Withdrawal (Dr.)",
    "Deposit (Cr.)",
    "Balance"
])

# Sort by date
df = df.sort_values(by="Date")

# Save CSV
df.to_csv("data/test_bank_statement.csv", index=False)

print("Test bank statement generated successfully!")