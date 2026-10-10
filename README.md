# 💰 Simple Expense Tracker

A beginner-friendly Python program to track daily expenses in Swedish kronor (SEK).

## ✨ Features

- Add an expense with a name and amount.
- View all saved expenses.
- Calculate your total spending.
- Save expenses automatically in a CSV file.
- Load previous expenses when you reopen the program.
- Reject empty names and invalid amounts.

## 🛠️ Built With

- Python 3
- `csv` — reads and saves expenses.
- `decimal` — handles money amounts.
- `pathlib` — finds the saved file.

All these modules come with Python. No extra packages are needed.

## 🚀 How to Run

1. Install Python 3.
2. Download this repository using **Code → Download ZIP**.
3. Extract the ZIP file.
4. Open a terminal in the folder containing `expense_tracker.py`.
5. Run:

```bash
python expense_tracker.py
```

On Windows, you can also use:

```bash
py expense_tracker.py
```

## 📋 How to Use

When the program starts, you will see:

```text
--- My Expense Tracker ---
1. Add an expense
2. Show expenses and total
3. Exit
```

### 1. Add an expense

Choose `1`, then enter an expense name and amount.

```text
What did you spend money on? Lunch
Amount in SEK: 80
Expense saved!
```

Use a dot for decimal amounts, such as `25.50`.

### 2. View expenses

Choose `2` to see your expenses and total.

```text
Lunch: 80.00 SEK
Bus: 30.00 SEK
Total: 110.00 SEK
```

### 3. Exit

Choose `3` to close the program. Your saved expenses will remain available the next time you open it.

## 📁 Project Files

| File | Purpose |
|---|---|
| `expense_tracker.py` | The Python program |
| `README.md` | Project description and instructions |
| `expenses.csv` | Your saved expenses; created after adding your first expense |

## 💾 How Saving Works

Each new expense is saved in `expenses.csv`, beside the Python file.

Example file contents:

```csv
Lunch,80
Bus,30
```

Expenses are stored on your computer. They are not automatically uploaded to GitHub.

## ⚠️ Current Limitations

- Uses a text menu in the terminal.
- Tracks amounts in SEK only.
- Does not support editing or deleting expenses through the menu.
- Does not record dates or categories.
- Expects the saved CSV file to contain valid expense records.

## 🎯 What I Am Practicing

This project helps me practice:

- Python loops and conditions
- User input and validation
- Lists and tuples
- Reading and writing files
- Handling errors
- Managing a project on GitHub

## 🔮 Future Improvements

- Add dates and expense categories.
- Edit or delete an expense.
- Set a monthly budget.
- Display spending charts.
