# Personal Expense Analyzer

A Python-based personal expense analysis application that helps analyze, summarize, and visualize expense data using Pandas and Matplotlib.

## Project Overview

The Personal Expense Analyzer is a command-line application developed using Python.

The project takes expense data stored in CSV files, performs data cleaning and exploratory data analysis, and provides different ways to understand spending patterns.

The application can analyze expenses by category, payment method, and month. It also provides budget analysis, financial summaries, filtering, and visualizations.

## Objectives

- Practice Python programming and modular programming
- Perform data cleaning using Pandas
- Analyze expense data using Pandas
- Understand spending patterns
- Create useful data visualizations
- Build a command-line application
- Practice exception handling and input validation
- Use Git and GitHub for version control

## Features

### Expense Analysis

- View all expenses
- Calculate total expense
- Calculate average expense
- Find highest expense
- Find lowest expense
- Analyze expenses by category
- Analyze expenses by payment method
- Analyze monthly expenses

### Expense Filtering

- Filter expenses by category
- Find expenses above a specified amount

### Budget Analysis

- Perform overall budget analysis
- Perform category-wise budget analysis
- Check remaining budget
- Detect when spending exceeds the budget

### Financial Summary

The application provides a financial summary containing:

- Total expense
- Average expense
- Highest expense
- Lowest expense
- Number of transactions
- Highest spending category
- Highest spending month

### Data Visualization

The project generates:

- Category-wise expense bar chart
- Monthly expense trend line chart
- Category spending distribution pie chart

## Technologies Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Git
- GitHub

## Python Concepts Used

- Variables
- Data types
- Lists and dictionaries
- Conditional statements
- Loops
- Functions
- Modules
- Exception handling
- File handling
- String methods
- Input validation

## Data Analysis Techniques

The project uses Pandas for:

- Data loading
- Data inspection
- Missing value handling
- Duplicate removal
- Data type conversion
- GroupBy operations
- Aggregation
- Sorting
- Filtering
- Percentage calculation
- Date-based analysis

## Dataset

The project uses a synthetic expense dataset created for learning and project development purposes.

### Raw Dataset

- Rows: 505
- Columns: 5

### Cleaned Dataset

After data cleaning:

- Rows: 500
- Columns: 5
- Missing values: 0
- Duplicate rows: 0

### Dataset Columns

| Column | Description |
|---|---|
| Date | Date of the expense |
| Category | Expense category |
| Description | Description of the transaction |
| Amount | Expense amount |
| Payment_Method | Method used for payment |

### Expense Categories

- Food
- Travel
- Shopping
- Entertainment
- Bills
- Health
- Education

### Payment Methods

- UPI
- Cash
- Card
- Net Banking

## Data Cleaning

The raw dataset contains missing values and duplicate records.

The following cleaning operations were performed:

1. Converted the `Date` column to datetime format.
2. Identified missing values.
3. Filled missing categories using transaction descriptions.
4. Replaced missing descriptions with `Unknown`.
5. Removed duplicate rows.
6. Verified that the cleaned dataset contains no missing values or duplicates.
7. Saved the cleaned data as `cleaned_expenses.csv`.

## Exploratory Data Analysis

The Jupyter Notebook performs several analyses including:

- Total expense
- Average expense
- Highest transaction
- Lowest transaction
- Category-wise spending
- Payment-method spending
- Monthly spending
- Average daily expense
- High-value transactions
- Top 10 expenses
- Number of transactions by category

## Project Structure

```text
personal-expense-analyzer/
│
├── data/
│   ├── expenses.csv
│   └── cleaned_expenses.csv
│
├── notebooks/
│   └── expense_analysis.ipynb
│
├── results/
│   ├── category_expense.csv
│   ├── category_expense.png
│   ├── monthly_expense.png
│   └── category_distribution.png
│
├── src/
│   ├── functions.py
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt