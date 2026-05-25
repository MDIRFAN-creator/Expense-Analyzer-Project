# AI-Based Personal Finance Analyzer

## Project Overview
This project is a machine learning-based personal finance analyzer that classifies bank transactions into categories (e.g., food, grocery, transfer, shopping) and provides interactive visualizations of spending behavior.

A Streamlit web application is built on top of the model to allow users to upload bank statements and instantly view insights about their financial activity.

## Features
- Transaction classification using Machine Learning (Naive Bayes)
- Synthetic bank statement dataset generation
- Automatic categorization of UPI and transaction descriptions
- Interactive dashboard using Streamlit
- Spending analysis with:
  - Category-wise breakdown
  - Income vs expenses comparison
  - Monthly spending trends
- Visualizations using bar charts and pie charts

## Machine Learning Model
- Algorithm: Multinomial Naive Bayes
- Feature Extraction: TF-IDF Vectorization
- Input: Transaction description text
- Output: Predicted spending category

## Dataset
- The dataset used is synthetically generated to simulate real-world bank statements.
- It includes:
  - Transaction descriptions (UPI, merchant names, personal transfers)
  - Labels (categories such as food, grocery, medical, etc.)
  - Credit and debit values

---

## Model Accuracy Note
The model achieved high accuracy on the available dataset due to the structured and synthetic nature of the data. However, real-world bank transaction data is more complex and unstructured (e.g., ambiguous UPI names, inconsistent merchant descriptions).

Therefore, further validation on larger and more diverse real-world datasets is recommended to confirm generalization performance.

## Streamlit App
Run the application locally:

streamlit run app.py
