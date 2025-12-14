# 💰 Expense Tracker Pro

A desktop GUI application built with Python's **Tkinter** to track personal finances. It allows users to log daily expenses, persist data in a CSV file, and visualize spending habits with embedded **Matplotlib** charts.



## 🚀 Features

* **Desktop GUI:** Native Windows/Mac/Linux interface using `tkinter`.
* **Data Persistence:** Automatically saves and loads transactions from `expenses.csv`.
* **Interactive Charts:** Embeds a real-time **Pie Chart** directly in the application window to visualize spending by category.
* **Smart Validation:** Prevents invalid inputs (e.g., text in the "Amount" field).
* **Live Updates:** The table and total spending summary update instantly upon adding an entry.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **GUI Framework:** `tkinter` (Built-in)
* **Data Handling:** `pandas` (CSV manipulation)
* **Visualization:** `matplotlib` (Charts embedded in GUI)

## ⚙️ Installation

### 1. Install Dependencies
You only need to install `pandas` and `matplotlib`. Tkinter is included with Python.
```bash
pip install pandas matplotlib
python tracker.py