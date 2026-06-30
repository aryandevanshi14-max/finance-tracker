
# 💰 Personal Finance Tracker with Spending Predictor

A simple Python command-line application that helps you track daily expenses,
analyze spending patterns by category and month, and estimate your spending
for the upcoming month based on recent trends.

## Features

- **Add expenses** with category, amount, date (auto-filled), and notes
- **Persistent storage** using CSV file handling (no database required)
- **Category-wise breakdown** of total spending
- **Monthly trend analysis** to see how spending changes over time
- **Simple spending prediction** for next month (based on average of last 3 months)
- **Visual charts** — bar chart for category breakdown, line chart for monthly trend

## Concepts Used

- Python fundamentals: variables, data types, control flow
- Functions and modular code design
- Basic Object-Oriented Programming (`Expense` and `FinanceTracker` classes)
- File handling (reading/writing CSV)
- Data visualization with `matplotlib`

## How to Run

1. Clone this repository
   ```bash
   git clone https://github.com/aryandevanshi14-max/finance-tracker.git
   cd finance-tracker
   ```

2. Install dependencies
   ```bash
   pip install matplotlib
   ```

3. Run the app
   ```bash
   python finance_tracker.py
   ```

4. Follow the on-screen menu to add expenses, view summaries, and generate charts.

## Example Output

```
===== PERSONAL FINANCE TRACKER =====
1. Add Expense
2. View Total Spent
3. View Category Breakdown
4. View Monthly Trend
5. Predict Next Month's Spending
6. Generate Charts
7. Exit
```

## Future Improvements

- Add a budget limit feature with alerts
- Switch from CSV to SQLite for larger datasets
- Build a simple web interface using Flask
- Use linear regression for more accurate predictions

## Author

**Aryan Jain**
B.S. Student, AI & Cyber Security — IIT Patna
