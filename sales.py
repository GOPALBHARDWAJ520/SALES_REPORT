# Import necessary libraries
import pandas as pd                    # For data manipulation and analysis
import matplotlib.pyplot as plt        # For plotting basic visualizations
import seaborn as sns                  # For advanced visualizations

# Step 1: Load the dataset
df = pd.read_csv("dataset  sales.csv")   # Load data from CSV into a DataFrame

# Step 2: Convert 'Date' column to datetime format for time-based analysis
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Create a new column 'Total' which is Quantity * Price
df['Total'] = df['Quantity'] * df['Price']

# Step 4: Analyze total sales by product
product_sales = df.groupby('Product')['Total'].sum().sort_values(ascending=False)
# Group by 'Product', sum the 'Total' column, then sort in descending order

# Plot total sales by product
plt.figure(figsize=(8, 4))                          # Set the figure size
product_sales.plot(kind='bar', color='skyblue')     # Create a bar plot
plt.title('Total Sales by Product')                 # Set plot title
plt.ylabel("Sales Total")                           # Set y-axis label
plt.tight_layout()                                  # Adjust layout
plt.savefig("total_sales_by_product.png")           # Save plot as PNG
plt.close()                                         # Close plot to free memory

# Step 5: Analyze total sales by region
region_sales = df.groupby('Region')['Total'].sum().sort_values(ascending=False)

# Plot total sales by region
plt.figure(figsize=(8, 4))
region_sales.plot(kind='bar', color='salmon')
plt.title('Total Sales by Region')
plt.ylabel("Sales Total")
plt.tight_layout()
plt.savefig("total_sales_by_region.png")
plt.close()

# Step 6: Analyze daily sales trend
daily_sales = df.groupby('Date')['Total'].sum()     # Group by date and sum total sales

# Plot daily sales
plt.figure(figsize=(10, 5))
daily_sales.plot(color='green')
plt.title('Daily Total Sales')
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("daily_sales_trend.png")
plt.close()

# Step 7: Create correlation heatmap for Quantity, Price, and Total
plt.figure(figsize=(6, 4))
sns.heatmap(df[['Quantity', 'Price', 'Total']].corr(), annot=True, cmap='coolwarm')
# Compute correlation matrix, display with annotations, use a color map
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Step 8: Boxplot of Price distribution by Product
plt.figure(figsize=(8, 5))
sns.boxplot(x='Product', y='Price', data=df, palette='pastel')
# Show how prices are distributed for each product
plt.title("Price Distribution by Product")
plt.tight_layout()
plt.savefig("price_distribution_by_product.png")
plt.close()
