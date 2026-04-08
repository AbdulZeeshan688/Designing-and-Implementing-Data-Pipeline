import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
data = pd.read_csv('NY-House-Dataset.csv')
print("Data loaded successfully!")

# 2. DO THE MATH: Calculate the Price per Square Foot
# (This is the step that was missing and causing the KeyError!)
data['Price_per_Sqft'] = data['PRICE'] / data['PROPERTYSQFT']

# Clean up the data by dropping empty rows
data = data.dropna(subset=['Price_per_Sqft', 'LATITUDE', 'LONGITUDE'])

# Find and print the Min and Max
min_price = data['Price_per_Sqft'].min()
max_price = data['Price_per_Sqft'].max()
print(f"\nThe Cheapest Apartment is: ${min_price:.2f} per sqft")
print(f"The Most Expensive Apartment is: ${max_price:.2f} per sqft")

# 3. DRAW THE CHARTS
# Create a blank canvas with 2 side-by-side charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Chart 1: Longitude vs Price per Sqft (Red dots)
ax1.scatter(data['LONGITUDE'], data['Price_per_Sqft'], color='red', s=15, alpha=0.7)
ax1.set_title('Longitude vs. Price per Sqft')
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Price per Sqft')
ax1.grid(True, linestyle='--', alpha=0.5)

# Chart 2: Latitude vs Price per Sqft (Blue dots)
ax2.scatter(data['LATITUDE'], data['Price_per_Sqft'], color='blue', s=15, alpha=0.7)
ax2.set_title('Latitude vs. Price per Sqft')
ax2.set_xlabel('Latitude')
ax2.set_ylabel('Price per Sqft')
ax2.grid(True, linestyle='--', alpha=0.5)

# This command tells Mac to open the pop-up window and show the charts!
plt.tight_layout()
plt.show()