import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- CONFIGURATION ---
FILE_PATH = "expenses.csv"

# --- DATA FUNCTIONS ---
def load_data():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

def save_data(date_val, cat_val, amount_val, desc_val):
    # Validation
    if not amount_val:
        messagebox.showerror("Error", "Amount is required!")
        return

    try:
        float(amount_val)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number!")
        return

    # Load existing
    df = load_data()
    
    # Create new row
    new_row = {
        "Date": date_val,
        "Category": cat_val,
        "Amount": float(amount_val),
        "Description": desc_val
    }
    
    # Append using concat (modern pandas)
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
    
    # Refresh UI
    messagebox.showinfo("Success", "Expense Added!")
    refresh_ui()

# --- UI FUNCTIONS ---
def refresh_ui():
    # 1. Clear Table
    for row in tree.get_children():
        tree.delete(row)
    
    # 2. Load Data
    df = load_data()
    
    # 3. Populate Table
    for _, row in df.iterrows():
        tree.insert("", "end", values=(row["Date"], row["Category"], f"${row['Amount']:.2f}", row["Description"]))
        
    # 4. Update Total
    total = df["Amount"].sum() if not df.empty else 0
    lbl_total.config(text=f"Total Spent: ${total:,.2f}")

    # 5. Update Chart
    update_chart(df)

def update_chart(df):
    # Clear old chart
    for widget in chart_frame.winfo_children():
        widget.destroy()

    if df.empty:
        return

    # Aggregate data
    category_totals = df.groupby("Category")["Amount"].sum()

    # Create Matplotlib Figure
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
    ax.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Spending by Category")

    # Embed in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# --- GUI SETUP ---
root = tk.Tk()
root.title("💰 Expense Tracker Pro")
root.geometry("900x600")

# 1. INPUT FRAME (Left Side)
frame_input = tk.Frame(root, padx=20, pady=20)
frame_input.pack(side=tk.LEFT, fill=tk.Y)

tk.Label(frame_input, text="Add New Expense", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(frame_input, text="Date (YYYY-MM-DD)").pack(anchor="w")
entry_date = tk.Entry(frame_input)
entry_date.insert(0, date.today())
entry_date.pack(fill=tk.X, pady=5)

tk.Label(frame_input, text="Category").pack(anchor="w")
combo_cat = ttk.Combobox(frame_input, values=["Food", "Rent", "Transport", "Shopping", "Other"])
combo_cat.current(0)
combo_cat.pack(fill=tk.X, pady=5)

tk.Label(frame_input, text="Amount ($)").pack(anchor="w")
entry_amount = tk.Entry(frame_input)
entry_amount.pack(fill=tk.X, pady=5)

tk.Label(frame_input, text="Description").pack(anchor="w")
entry_desc = tk.Entry(frame_input)
entry_desc.pack(fill=tk.X, pady=5)

btn_add = tk.Button(frame_input, text="Add Expense", bg="#4CAF50", fg="white", 
                    command=lambda: save_data(entry_date.get(), combo_cat.get(), entry_amount.get(), entry_desc.get()))
btn_add.pack(fill=tk.X, pady=20)

lbl_total = tk.Label(frame_input, text="Total Spent: $0.00", font=("Arial", 14, "bold"))
lbl_total.pack(pady=20)

# 2. DATA FRAME (Right Side)
frame_data = tk.Frame(root, padx=20, pady=20)
frame_data.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Table (Treeview)
cols = ("Date", "Category", "Amount", "Description")
tree = ttk.Treeview(frame_data, columns=cols, show="headings", height=8)

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill=tk.X)

# 3. CHART FRAME (Bottom Right)
chart_frame = tk.Frame(frame_data)
chart_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# Initial Load
refresh_ui()

root.mainloop()