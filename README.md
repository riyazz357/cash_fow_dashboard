# 💰 Personal Expense Tracker (Day 7)

A persistent, data-driven expense dashboard built with **Streamlit**. It allows users to log transactions, saves data to a local CSV file, and provides real-time visualization of spending habits.

**Part of the "15 Days, 15 Projects" Challenge.**

## 🚀 Features

* **Data Entry Form:** Easy input for Date, Category (Food, Rent, Transport, etc.), and Amount.
* **Persistent Storage:** Automatically saves all data to `expenses.csv`. Data remains even after closing the app.
* **Smart Analytics:**
    * **Pie Chart:** Visual breakdown of spending by category using Plotly.
    * **Trend Line:** (Optional) Shows spending over time.
    * **Total KPI:** Instantly calculates total money spent.
* **Data Management:** View raw data in a sortable table and delete entries (via CSV management).

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Data Processing:** [Pandas](https://pandas.pydata.org/)
* **Visualization:** [Plotly Express](https://plotly.com/python/)

## ⚙️ Installation

### 1. Install Dependencies
```bash
# 💰 Personal Expense Tracker (Day 7)

A persistent, data-driven expense dashboard built with **Streamlit**. It allows users to log transactions, saves data to a local CSV file, and provides real-time visualization of spending habits.

**Part of the "15 Days, 15 Projects" Challenge.**

## 🚀 Features

* **Data Entry Form:** Easy input for Date, Category (Food, Rent, Transport, etc.), and Amount.
* **Persistent Storage:** Automatically saves all data to `expenses.csv`. Data remains even after closing the app.
* **Smart Analytics:**
    * **Pie Chart:** Visual breakdown of spending by category using Plotly.
    * **Trend Line:** (Optional) Shows spending over time.
    * **Total KPI:** Instantly calculates total money spent.
* **Data Management:** View raw data in a sortable table and delete entries (via CSV management).

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Data Processing:** [Pandas](https://pandas.pydata.org/)
* **Visualization:** [Plotly Express](https://plotly.com/python/)

## ⚙️ Installation

### 1. Install Dependencies
```bash
pip install streamlit pandas plotly
streamlit run app.py