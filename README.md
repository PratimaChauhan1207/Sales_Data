# Project Title: Sales Data Automation with Pandas and Task Scheduler

## Description:
This project automates the process of analyzing and reporting sales data for today’s date.  
The Python script fetches sales data from a CSV file, filters it based on today's date, groups the sales by product, and generates a detailed report.  
The report is saved as both a CSV file and a PNG image (bar graph) for easy visualization.  

By using **Pandas** for data manipulation and **Matplotlib** for creating visual graphs, the project helps in simplifying and automating the repetitive task of daily sales reporting.  
With the help of **Task Scheduler**, this automation can run daily without manual intervention, ensuring the sales data is always up to date.

---

## Technologies Used:
- **Pandas**: For efficient data manipulation and filtering  
- **Matplotlib**: For plotting the sales data as bar graphs  
- **Task Scheduler**: To automate the script execution regularly (e.g., daily)

---

## Features:
- Automatically fetches sales data from a remote CSV file  
- Filters data based on the current date  
- Aggregates sales by product  
- Generates a daily sales report in CSV format  
- Creates a bar chart showing total sales by product  
- Saves the report and chart with today’s date  
- Can be scheduled to run automatically using Task Scheduler  

---

## How to Use:

### 1. Clone this repository:
```bash
git clone https://github.com/PratimaChauhan1207/Sales_Data.git
```

### 2. Navigate to the project folder and (optionally) create a virtual environment:
```bash
python -m venv .venv
```

### 3. Activate the virtual environment:
- **Windows**:
```bash
.venv\Scripts\activate
```
- **macOS/Linux**:
```bash
source .venv/bin/activate
```

### 4. Install required libraries:
```bash
pip install pandas matplotlib
```

### 5. Run the script:
```bash
python Automation.py
```
---

## Automate with Task Scheduler:

To run this script daily without opening it manually:

1. Open **Task Scheduler** on Windows  
2. Create a **new task**  
3. In the “Actions” tab, browse and select your Python executable  
   Example:  
   ```
   C:\Users\YourName\Automation Project\.venv\Scripts\python.exe
   ```
4. In the “Add arguments” field, type the path to your script  
   Example:  
   ```
   "C:\Users\YourName\Automation Project\Automation.py"
   ```
5. Set the trigger time (e.g., every day at 10:00 AM)  

