from functions import (
    load_data,
    show_expenses,
    calculate_total,
    calculate_average,
    find_highest_expense,
    find_lowest_expense,
    category_analysis,
    payment_analysis,
    monthly_analysis,
    filter_by_category,
    expenses_above_amount,
    plot_category_expense,
    plot_monthly_expense,
    calculate_budget_status,
    category_budget_status,
    financial_summary,
    category_percentage,
    plot_category_percentage
)


def display_menu():
    print("\n" + "=" * 50)
    print("       PERSONAL EXPENSE ANALYZER")
    print("=" * 50)

    print("1.  Show all expenses")
    print("2.  Total expense")
    print("3.  Average expense")
    print("4.  Highest expense")
    print("5.  Lowest expense")
    print("6.  Category-wise expense")
    print("7.  Payment-method expense")
    print("8.  Monthly expense")
    print("9.  Filter by category")
    print("10. Expenses above an amount")
    print("11. Category expense chart")
    print("12. Monthly expense chart")
    print("13. Budget analysis")
    print("14. Category budget analysis")
    print("15. Financial summary")
    print("16. Category spending percentage")
    print("17. Category distribution chart")
    print("18. Exit")

    print("=" * 50)


def main():

    # Load cleaned dataset
    try:
        df = load_data()
        print("\nExpense data loaded successfully.")

    except FileNotFoundError:
        print("\nError: cleaned_expenses.csv was not found.")
        print("Make sure the file exists inside the data folder.")
        return

    except Exception as e:
        print(f"\nError while loading data: {e}")
        return

    # Menu loop
    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        # 1. Show all expenses
        if choice == "1":

            show_expenses(df)

        # 2. Total expense
        elif choice == "2":

            total = calculate_total(df)

            print(f"\nTotal Expense: ₹{total:,.2f}")

        # 3. Average expense
        elif choice == "3":

            average = calculate_average(df)

            print(f"\nAverage Expense: ₹{average:,.2f}")

        # 4. Highest expense
        elif choice == "4":

            highest = find_highest_expense(df)

            print("\nHighest Expense:")
            print(highest)

        # 5. Lowest expense
        elif choice == "5":

            lowest = find_lowest_expense(df)

            print("\nLowest Expense:")
            print(lowest)

        # 6. Category-wise expense
        elif choice == "6":

            result = category_analysis(df)

            print("\nCategory-wise Expense:")
            print(result)

        # 7. Payment-method expense
        elif choice == "7":

            result = payment_analysis(df)

            print("\nPayment-method Expense:")
            print(result)

        # 8. Monthly expense
        elif choice == "8":

            result = monthly_analysis(df)

            print("\nMonthly Expense:")
            print(result)

        # 9. Filter by category
        elif choice == "9":

            category = input("\nEnter category: ")

            result = filter_by_category(df, category)

            if result.empty:
                print("\nNo expenses found for this category.")

            else:
                print(f"\nExpenses in category '{category}':")
                print(result)

        # 10. Expenses above an amount
        elif choice == "10":

            try:

                amount = float(input("\nEnter amount: "))

                if amount < 0:
                    print("\nAmount cannot be negative.")
                    continue

                result = expenses_above_amount(df, amount)

                if result.empty:
                    print("\nNo expenses found above this amount.")

                else:
                    print(f"\nExpenses above ₹{amount:,.2f}:")
                    print(result)

            except ValueError:

                print("\nInvalid amount. Please enter a number.")

        # 11. Category expense chart
        elif choice == "11":

            print("\nGenerating category expense chart...")

            plot_category_expense(df)

        # 12. Monthly expense chart
        elif choice == "12":

            print("\nGenerating monthly expense chart...")

            plot_monthly_expense(df)

        # 13. Budget analysis
        elif choice == "13":

            try:

                budget = float(input("\nEnter your total budget: "))

                if budget < 0:
                    print("\nBudget cannot be negative.")
                    continue

                total, remaining = calculate_budget_status(df, budget)

                print("\nBudget Analysis")
                print("-" * 30)
                print(f"Budget:          ₹{budget:,.2f}")
                print(f"Total Expense:   ₹{total:,.2f}")

                if remaining >= 0:

                    print(f"Remaining:       ₹{remaining:,.2f}")
                    print("\nStatus: You are within your budget.")

                else:

                    print(f"Over Budget By:  ₹{abs(remaining):,.2f}")
                    print("\nStatus: You have exceeded your budget.")

            except ValueError:

                print("\nInvalid budget. Please enter a number.")

        # 14. Category budget analysis
        elif choice == "14":

            category = input("\nEnter category: ")

            try:

                budget = float(input("Enter budget for this category: "))

                if budget < 0:
                    print("\nBudget cannot be negative.")
                    continue

                result = category_budget_status(
                    df,
                    category,
                    budget
                )

                if result is None:

                    print(f"\nNo expenses found for category '{category}'.")

                else:

                    total, remaining = result

                    print("\nCategory Budget Analysis")
                    print("-" * 30)
                    print(f"Category:        {category}")
                    print(f"Budget:          ₹{budget:,.2f}")
                    print(f"Total Expense:   ₹{total:,.2f}")

                    if remaining >= 0:

                        print(f"Remaining:       ₹{remaining:,.2f}")
                        print("\nStatus: Within category budget.")

                    else:

                        print(f"Over Budget By:  ₹{abs(remaining):,.2f}")
                        print("\nStatus: Category budget exceeded.")

            except ValueError:

                print("\nInvalid budget. Please enter a number.")

        # 15. Financial summary
        elif choice == "15":

            summary = financial_summary(df)

            print("\n" + "=" * 40)
            print("          FINANCIAL SUMMARY")
            print("=" * 40)

            print(
                f"Total Expense:       ₹{summary['total_expense']:,.2f}"
            )

            print(
                f"Average Expense:     ₹{summary['average_expense']:,.2f}"
            )

            print(
                f"Highest Expense:     ₹{summary['highest_expense']:,.2f}"
            )

            print(
                f"Lowest Expense:      ₹{summary['lowest_expense']:,.2f}"
            )

            print(
                f"Transactions:        {summary['transaction_count']}"
            )

            print(
                f"Highest Category:    {summary['highest_category']}"
            )

            print(
                f"Highest Expense Month: {summary['highest_month']}"
            )

            print("=" * 40)

        # 16. Category spending percentage
        elif choice == "16":

            result = category_percentage(df)

            print("\nCategory Spending Percentage:")
            print(result)

        # 17. Category distribution chart
        elif choice == "17":

            print("\nGenerating category distribution chart...")

            plot_category_percentage(df)

        # 18. Exit
        elif choice == "18":

            print("\nThank you for using Personal Expense Analyzer!")

            break

        # Invalid choice
        else:

            print("\nInvalid choice.")
            print("Please enter a number between 1 and 18.")


# Run the application
if __name__ == "__main__":
    main()