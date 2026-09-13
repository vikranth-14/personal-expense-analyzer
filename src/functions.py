import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# Load cleaned expense data
# --------------------------------------------------

def load_data():
    df = pd.read_csv("data/cleaned_expenses.csv")

    # Convert Date column from string to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    return df


# --------------------------------------------------
# Show all expenses
# --------------------------------------------------

def show_expenses(df):
    print(df)


# --------------------------------------------------
# Calculate total expense
# --------------------------------------------------

def calculate_total(df):
    return df["Amount"].sum()


# --------------------------------------------------
# Calculate average expense
# --------------------------------------------------

def calculate_average(df):
    return df["Amount"].mean()


# --------------------------------------------------
# Find highest expense
# --------------------------------------------------

def find_highest_expense(df):
    return df.loc[df["Amount"].idxmax()]


# --------------------------------------------------
# Find lowest expense
# --------------------------------------------------

def find_lowest_expense(df):
    return df.loc[df["Amount"].idxmin()]


# --------------------------------------------------
# Category-wise expense analysis
# --------------------------------------------------

def category_analysis(df):

    return (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )


# --------------------------------------------------
# Payment-method expense analysis
# --------------------------------------------------

def payment_analysis(df):

    return (
        df.groupby("Payment_Method")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )


# --------------------------------------------------
# Monthly expense analysis
# --------------------------------------------------

def monthly_analysis(df):

    return (
        df.groupby(df["Date"].dt.to_period("M"))["Amount"]
        .sum()
        .sort_index()
    )


# --------------------------------------------------
# Filter expenses by category
# --------------------------------------------------

def filter_by_category(df, category):

    filtered_df = df[
        df["Category"].str.lower() == category.lower()
    ]

    return filtered_df


# --------------------------------------------------
# Find expenses above a given amount
# --------------------------------------------------

def expenses_above_amount(df, amount):

    return df[df["Amount"] > amount]


# --------------------------------------------------
# Plot category-wise expense
# --------------------------------------------------

def plot_category_expense(df):

    category_expense = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    category_expense.plot(kind="bar")

    plt.title("Total Expense by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Expense")

    plt.tight_layout()

    plt.savefig("results/category_expense.png")

    plt.show()


# --------------------------------------------------
# Plot monthly expense
# --------------------------------------------------

def plot_monthly_expense(df):

    monthly_expense = (
        df.groupby(df["Date"].dt.to_period("M"))["Amount"]
        .sum()
    )

    monthly_expense.plot(
        kind="line",
        marker="o"
    )

    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Expense")

    plt.tight_layout()

    plt.savefig("results/monthly_expense.png")

    plt.show()


# --------------------------------------------------
# Overall budget analysis
# --------------------------------------------------

def calculate_budget_status(df, budget):

    total_expense = df["Amount"].sum()

    remaining = budget - total_expense

    return total_expense, remaining


# --------------------------------------------------
# Category budget analysis
# --------------------------------------------------

def category_budget_status(df, category, budget):

    category_data = df[
        df["Category"].str.lower() == category.lower()
    ]

    # If category does not exist
    if category_data.empty:
        return None

    total = category_data["Amount"].sum()

    remaining = budget - total

    return total, remaining


# --------------------------------------------------
# Financial summary
# --------------------------------------------------

def financial_summary(df):

    # Basic statistics

    total_expense = df["Amount"].sum()

    average_expense = df["Amount"].mean()

    highest_expense = df["Amount"].max()

    lowest_expense = df["Amount"].min()

    transaction_count = len(df)


    # Highest spending category

    category_expense = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    highest_category = category_expense.idxmax()


    # Highest spending month

    monthly_expense = (
        df.groupby(df["Date"].dt.to_period("M"))["Amount"]
        .sum()
    )

    highest_month = monthly_expense.idxmax()


    # Return all results as dictionary

    return {
        "total_expense": total_expense,
        "average_expense": average_expense,
        "highest_expense": highest_expense,
        "lowest_expense": lowest_expense,
        "transaction_count": transaction_count,
        "highest_category": highest_category,
        "highest_month": highest_month
    }


# --------------------------------------------------
# Category spending percentage
# --------------------------------------------------

def category_percentage(df):

    category_expense = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    total_expense = df["Amount"].sum()

    percentage = (
        category_expense / total_expense
    ) * 100


    result = pd.DataFrame({
        "Total_Expense": category_expense,
        "Percentage": percentage
    })

    return result


# --------------------------------------------------
# Plot category spending distribution
# --------------------------------------------------

def plot_category_percentage(df):

    category_expense = (
        df.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    category_expense.plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution by Category")

    plt.ylabel("")

    plt.tight_layout()

    plt.savefig("results/category_distribution.png")

    plt.show()