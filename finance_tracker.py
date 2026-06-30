"""
Personal Finance Tracker with Basic Spending Predictor
Author: Aryan Jain

A simple command-line application to track expenses, analyze spending
patterns, and predict next month's estimated spending.
"""

import csv
import os
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

DATA_FILE = "expenses.csv"


class Expense:
    """Represents a single expense entry."""

    def __init__(self, date, category, amount, note=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.note = note

    def to_row(self):
        return [self.date, self.category, self.amount, self.note]

    def __repr__(self):
        return f"{self.date} | {self.category:12} | ₹{self.amount:>8.2f} | {self.note}"


class FinanceTracker:
    """Handles storage, analysis, and prediction of expenses."""

    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "category", "amount", "note"])

    def add_expense(self, category, amount, note=""):
        date = datetime.now().strftime("%Y-%m-%d")
        expense = Expense(date, category, amount, note)
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(expense.to_row())
        print(f"Added: {expense}")

    def load_expenses(self):
        expenses = []
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append(
                    Expense(row["date"], row["category"], float(row["amount"]), row["note"])
                )
        return expenses

    def total_spent(self):
        expenses = self.load_expenses()
        return sum(e.amount for e in expenses)

    def category_breakdown(self):
        expenses = self.load_expenses()
        breakdown = defaultdict(float)
        for e in expenses:
            breakdown[e.category] += e.amount
        return dict(breakdown)

    def monthly_breakdown(self):
        expenses = self.load_expenses()
        monthly = defaultdict(float)
        for e in expenses:
            month_key = e.date[:7]  # "YYYY-MM"
            monthly[month_key] += e.amount
        return dict(sorted(monthly.items()))

    def predict_next_month(self):
        """Simple prediction: average of last 3 months' spending."""
        monthly = self.monthly_breakdown()
        if not monthly:
            return 0
        values = list(monthly.values())
        last_n = values[-3:] if len(values) >= 3 else values
        prediction = sum(last_n) / len(last_n)
        return round(prediction, 2)

    def plot_category_breakdown(self):
        breakdown = self.category_breakdown()
        if not breakdown:
            print("No data to plot yet.")
            return
        plt.figure(figsize=(7, 5))
        plt.bar(breakdown.keys(), breakdown.values(), color="#1B4F72")
        plt.title("Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig("category_breakdown.png")
        print("Saved chart: category_breakdown.png")

    def plot_monthly_trend(self):
        monthly = self.monthly_breakdown()
        if not monthly:
            print("No data to plot yet.")
            return
        plt.figure(figsize=(7, 5))
        plt.plot(list(monthly.keys()), list(monthly.values()), marker="o", color="#1B4F72")
        plt.title("Monthly Spending Trend")
        plt.xlabel("Month")
        plt.ylabel("Amount (₹)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig("monthly_trend.png")
        print("Saved chart: monthly_trend.png")


def main_menu():
    tracker = FinanceTracker()

    while True:
        print("\n===== PERSONAL FINANCE TRACKER =====")
        print("1. Add Expense")
        print("2. View Total Spent")
        print("3. View Category Breakdown")
        print("4. View Monthly Trend")
        print("5. Predict Next Month's Spending")
        print("6. Generate Charts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            category = input("Category (e.g. Food, Travel, Rent): ").strip()
            try:
                amount = float(input("Amount (₹): ").strip())
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            note = input("Note (optional): ").strip()
            tracker.add_expense(category, amount, note)

        elif choice == "2":
            print(f"Total Spent: ₹{tracker.total_spent():.2f}")

        elif choice == "3":
            breakdown = tracker.category_breakdown()
            print("\n--- Category Breakdown ---")
            for cat, amt in breakdown.items():
                print(f"{cat:15}: ₹{amt:.2f}")

        elif choice == "4":
            monthly = tracker.monthly_breakdown()
            print("\n--- Monthly Trend ---")
            for month, amt in monthly.items():
                print(f"{month}: ₹{amt:.2f}")

        elif choice == "5":
            prediction = tracker.predict_next_month()
            print(f"\nEstimated spending for next month: ₹{prediction:.2f}")

        elif choice == "6":
            tracker.plot_category_breakdown()
            tracker.plot_monthly_trend()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
