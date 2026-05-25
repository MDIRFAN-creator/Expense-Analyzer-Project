import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="AI Finance Analyzer", layout="wide")

st.title("AI-Based Personal Finance Analyzer")

uploaded_file = st.file_uploader("Upload Bank Statement (CSV)", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    data.columns = data.columns.str.strip()
    if "Description" not in data.columns:
        st.error("CSV must contain a 'Description' column")
    else:
        X = vectorizer.transform(data["Description"])
        data["Predicted Category"] = model.predict(X)

        st.success("Transactions categorized successfully!")

        st.subheader("Categorized Transactions")
        st.dataframe(data)

        if "Withdrawal (Dr.)" in data.columns:
            data["Withdrawal (Dr.)"] = pd.to_numeric(
                data["Withdrawal (Dr.)"], errors="coerce"
            ).fillna(0)

        if "Deposit (Cr.)" in data.columns:
            data["Deposit (Cr.)"] = pd.to_numeric(
                data["Deposit (Cr.)"], errors="coerce"
            ).fillna(0)
        
        total_spent = data["Withdrawal (Dr.)"].sum()
        total_income = data["Deposit (Cr.)"].sum()
        net_savings = total_income - total_spent

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Expenses", f"₹ {total_spent:,.2f}")
        col2.metric("Total Income", f"₹ {total_income:,.2f}")
        col3.metric("Net Savings", f"₹ {net_savings:,.2f}")

        # bar chart
        st.subheader("Spending by Category")
        category_summary = (
            data.groupby("Predicted Category")["Withdrawal (Dr.)"]
            .sum()
        )
        st.bar_chart(category_summary)

        # income vs expense Bar chart
        st.subheader("Income vs Expenses")

        comparison_df = pd.DataFrame({
            "Type": ["Income", "Expenses"],
            "Amount": [total_income, total_spent]
        })

        st.bar_chart(comparison_df.set_index("Type"))

        # PIE CHART
        expense_data = data[data["Withdrawal (Dr.)"] > 0]

        category_summary = (    
        expense_data.groupby("Predicted Category")["Withdrawal (Dr.)"]
        .sum()
        )

        st.subheader("Category Distribution")
        st.pyplot(
            category_summary.plot.pie(
                autopct="%1.1f%%", figsize=(3, 3)
            ).figure
        )

        # monthly expemses
        if "Date" in data.columns:
            data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
            data["Month"] = data["Date"].dt.to_period("M")

            monthly = (
                data.groupby("Month")["Withdrawal (Dr.)"]
                .sum()
            )
            st.subheader("Monthly Spending Trend")
            st.line_chart(monthly)

        # savings rate
        if total_income > 0:
            savings_rate = (net_savings / total_income) * 100
        else:
            savings_rate = 0

        st.metric(" Savings Rate", f"{savings_rate:.2f}%")