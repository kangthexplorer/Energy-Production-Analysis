import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Prepare Data
df["Date"] = pd.to_datetime(df["Date"])
df["Hour"] = df["Start_Hour"]

# Seperate Wind and Solar Energy
wind = df[df["Source"] == "Wind"]
solar = df[df["Source"] == "Solar"]

# Which source produces overall energy?
df.groupby("Source")["Production"].sum()

# Hourly prediction pattern
hourly = df.groupby(["Hour", "Source"])["Production"].mean().unstack()

hourly.plot()
plt.title("Average Hourly Production")
plt.xlabel("Hour of the Day")
plt.ylabel("Energy Production")
plt.show()

# Daily prediction pattern
daily = df.groupby(["Day_Name", "Source"])["Production"].mean().unstack()

daily.plot(kind="bar")
plt.title("Average Production by Day")
plt.ylabel("Production")
plt.show()

# Monthly prediction pattern
monthly = df.groupby(["Month_Name", "Source"])["Production"].mean().unstack()

monthly.plot(kind="bar")
plt.title("Average Production by Month")
plt.ylabel("Production")
plt.show()

# Seasonal prediction pattern
seasonal = df.groupby(["Season", "Source"])["Production"].mean().unstack()

seasonal.plot(kind="bar")
plt.title("Seanson Energy Production")
plt.ylabel("Production")
plt.show()

df.groupby("Source")["Production"].std()

total = df.groupby("Hour")["Production"].sum()

plt.plot(total)
plt.title("Total Energy Production by Hour")
plt.xlabel("Hours")
plt.ylabel("Production")
plt.show()