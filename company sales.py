import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [12000, 15000, 17000, 16000, 18000, 21000, 
              20000, 23000, 25000, 24000, 26000, 30000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot line chart
plt.plot(df["Month"], df["Sales"], marker="o")

# Add labels and title
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Apple Company")

# Show grid
plt.grid(True)

# Display plot
plt.show()
