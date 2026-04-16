# Task-2-MuhammadDawood
# 💰 Simple Expense Tracker (Python CLI)

This is a basic Python command-line program that helps you track your daily expenses. It allows users to input multiple expenses, ensures values are positive, and calculates the total.

---

## 🚀 Features

* Add multiple expenses interactively
* Validates that expenses are **positive numbers**
* Keeps asking until valid input is given
* Displays total expense at the end
* Simple and beginner-friendly logic

---

## 📌 How It Works

1. The program starts with total = 0
2. It asks you to enter an expense
3. If the value is negative or zero:

   * It will repeatedly ask until you enter a positive number
4. The valid expense is added to the total
5. You are asked if you want to add more expenses (`y` or `n`)
6. If `y` → continue
7. If `n` → program stops and shows total

---

## 💻 Example Run

```id="8p3h2q"
Enter the expense: 500
Enter 'y' if you want to enter more expenses: y

Enter the expense: -200
Please enter a positive expense: 200
Enter 'y' if you want to enter more expenses: y

Enter the expense: 300
Enter 'y' if you want to enter more expenses: n

Total expense: 1000
```

---

## ⚙️ Requirements

* Python 3.x

---

## ▶️ How to Run

1. Save the code in a file:

   ```
   expense_tracker.py
   ```
2. Open terminal or command prompt
3. Run the program:

   ```
   python expense_tracker.py
   ```

---

## 📚 Concepts Used

* Variables and arithmetic operations
* `while` loop for continuous input
* Conditional statements (`if`, `else`)
* Input validation
* User interaction via `input()`

---

## 🧠 Notes

* Only **positive values** are accepted
* Input must be numeric (integers)
* This is a simple version — can be extended with:

  * Expense categories (food, travel, etc.)
  * Saving data to a file (CSV/Excel)
  * Monthly expense summary

---

## 📄 License

This project is open-source and free to use for learning purposes.
