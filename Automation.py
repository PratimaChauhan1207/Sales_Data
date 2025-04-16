import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("https://raw.githubusercontent.com/PratimaChauhan1207/Sales_Data/refs/heads/main/Sales.csv")
df["date"] = pd.to_datetime(df["date"], format = "%d-%m-%Y")
today = datetime.today().date()
df["date"]= df["date"].dt.date
df = df.loc[df["date"]==today]
df = df.groupby("product").agg(
    total_sale =("sales","sum")).reset_index()
df.to_csv(f'{today} report.csv')
plt.bar(df["product"],df["total_sale"])
plt.savefig(f'{today} report.png')





