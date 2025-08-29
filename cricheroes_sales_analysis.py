import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("CricHeroes_Sales_2023.xlsx")

# Order months
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)
df = df.sort_values("Month")

# Derived metrics
df["ARPU_INR"] = (df["Total_Revenue_INR"] / df["Registered_Users"]).round(2)
df["CAC_INR"] = (df["Marketing_Spend_INR"] / df["Registered_Users"]).round(2)
df["ROI"] = (df["Total_Revenue_INR"] / df["Marketing_Spend_INR"]).round(2)

# Charts
plt.figure(figsize=(10,5))
plt.plot(df["Month"], df["Total_Revenue_INR"], marker="o")
plt.title("Monthly Total Revenue (INR) - 2023")
plt.xlabel("Month")
plt.ylabel("Total Revenue (INR)")
plt.tight_layout()
plt.savefig("chart_monthly_total_revenue.png", dpi=150)
plt.close()

plt.figure(figsize=(10,5))
width = 0.25
x = np.arange(len(df["Month"]))
plt.bar(x - width, df["Subscription_Revenue_INR"])
plt.bar(x, df["Ad_Revenue_INR"])
plt.bar(x + width, df["Marketplace_Sales_INR"])
plt.xticks(x, df["Month"])
plt.title("Revenue Breakdown by Stream - 2023")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("chart_revenue_breakdown.png", dpi=150)
plt.close()

plt.figure(figsize=(10,5))
plt.plot(df["Month"], df["Registered_Users"], marker="o")
plt.plot(df["Month"], df["Paid_Subscriptions"], marker="o")
plt.title("Registered Users vs Paid Subscriptions - 2023")
plt.xlabel("Month")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("chart_users_vs_subs.png", dpi=150)
plt.close()

plt.figure(figsize=(10,5))
plt.bar(df["Month"], df["ROI"])
plt.title("Marketing ROI by Month - 2023")
plt.xlabel("Month")
plt.ylabel("ROI (x)")
plt.tight_layout()
plt.savefig("chart_roi.png", dpi=150)
plt.close()

plt.figure(figsize=(10,5))
plt.plot(df["Month"], df["Retention_Rate_%"], marker="o")
plt.title("Retention Rate (%) - 2023")
plt.xlabel("Month")
plt.ylabel("Retention Rate (%)")
plt.tight_layout()
plt.savefig("chart_retention.png", dpi=150)
plt.close()

print("Analysis complete. Charts saved.")