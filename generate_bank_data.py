import pandas as pd
import random
from datetime import datetime, timedelta

# Categories & keywords
transaction_types = {
    "Food": ["ZOMATO", "SWIGGY", "RESTAURANT", "CAFE"],
    "Travel": ["UBER", "OLA", "IRCTC", "PETROL"],
    "Shopping": ["AMAZON", "FLIPKART", "MYNTRA"],
    "Bills": ["ELECTRICITY BILL", "WATER BILL", "JIO RECHARGE"],
    "Entertainment": ["NETFLIX", "BOOKMYSHOW", "SPOTIFY"],
    "Salary": ["SALARY CREDIT"],
    "Transfer": ["UPI TRANSFER", "IMPS TRANSFER"],
    "Bank Charges": ["ATM WITHDRAWAL", "BALANCE ALERT CHARGES"]
}

names = ["RAMESH", "SURESH", "ARUN", "KRUTHIVA", "AKBAR", 
         "NASEEM", "SHAIK", "MOHAMMED", "PRIYA", "RAHUL"]

data = []
balance = 150000
start_date = datetime(2025, 1, 1)

for i in range(800):
    date = start_date + timedelta(days=random.randint(0, 120))
    category = random.choice(list(transaction_types.keys()))
    keyword = random.choice(transaction_types[category])

    # Random reference number
    ref_no = f"UPI-{random.randint(1000000000,9999999999)}"

    withdrawal = ""
    deposit = ""

    if category == "Salary":
        amount = random.randint(30000, 80000)
        deposit = amount
        balance += amount
        description = f"{keyword}/COMPANY PVT LTD"

    elif category == "Bank Charges":
        amount = random.randint(10, 5000)
        withdrawal = amount
        balance -= amount
        description = f"Chrg: {keyword}"

    elif category == "Transfer":
        amount = random.randint(500, 20000)
        withdrawal = amount
        balance -= amount
        description = f"UPI/{random.choice(names)}/{random.randint(1000000000,9999999999)}/Payment"

    else:
        amount = random.randint(100, 10000)
        withdrawal = amount
        balance -= amount
        description = f"UPI/{keyword}/{random.randint(1000000000,9999999999)}/Payment"

    data.append([
        i+1,
        date.strftime("%d-%m-%Y"),
        description,
        ref_no,
        withdrawal,
        deposit,
        balance,
        category
    ])

df = pd.DataFrame(data, columns=[
    "#",
    "Date",
    "Description",
    "Chq/Ref No",
    "Withdrawal (Dr.)",
    "Deposit (Cr.)",
    "Balance",
    "Category"
])

df = df.sort_values(by="Date")
df.to_csv("data/expenses.csv", index=False)

print("Advanced realistic bank dataset generated successfully!")