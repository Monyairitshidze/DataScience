# import pandas so i can read data
import pandas as pd

# import plotlib
import matplotlib.pyplot as mplt

# reading data to my project
data = pd.read_csv("C:/Users/Ritshidze/OneDrive/Desktop/Data Science/Adidas Sales/data.csv",
                   skiprows=4)

# data cleaning

# remove the empty first column
data = data.drop(columns=["Unnamed: 0"])

# Remove $ and commas from money columns
data["Price per Unit"] = data["Price per Unit"].str.replace("$", "").str.replace(",", "").astype(float)

data["Units Sold"] = data["Units Sold"].str.replace(",", "").astype(int)

data["Total Sales"] = data["Total Sales"].str.replace("$", "").str.replace(",", "").astype(float)

data["Operating Profit"] = data["Operating Profit"].str.replace("$", "").str.replace(",", "").astype(float)

# Remove % from operating margin
data["Operating Margin"] = data["Operating Margin"].str.replace("%", "").astype(float)

# Force Pandas to show all columns
pd.set_option('display.max_columns', None)

# dropin null values
data.dropna(axis=0, inplace=True)

# print data
print(data)


# /First Objective
# calculating the overall_sales

overall_sales = data['Total Sales']
overall_sales_results = sum(overall_sales)

print('the total overall sales ' + str(overall_sales_results))


# calculating the profit during period

# Convert Invoice Date to a proper date
data["Invoice Date"] = pd.to_datetime(
    data["Invoice Date"],
    dayfirst=True
)

# Group by month and calculate total operating profit
profit = data.groupby(
    data["Invoice Date"].dt.to_period("M")
)["Operating Profit"].sum()

operating_profit = str(profit)


# visualise monthly profit
profit.plot(kind="line")

mplt.title("Monthly Operating Profit")
mplt.xlabel("Month")
mplt.ylabel("Operating Profit")
mplt.show()


# printing profits in each months
print('The operating profit in esach month' + operating_profit)


# /Second Objective
# identifying top performing and underperforming product category,regions and sales channel


# Product Category

product_performance = data.groupby("Product").agg({
    "Total Sales": "sum",
    "Units Sold": "sum"
})

print("Product Performance:")
print(product_performance)

print("Worst performing product based on sales:")
print(product_performance["Total Sales"].idxmin())

print("Best performing product based on sales:")
print(product_performance["Total Sales"].idxmax())

print("Product selling the most units:")
print(product_performance["Units Sold"].idxmax())

print("Product selling the least units:")
print(product_performance["Units Sold"].idxmin())


# visualise product sales
product_performance["Total Sales"].plot(kind="bar")

mplt.title("Product Performance")
mplt.xlabel("Product")
mplt.ylabel("Total Sales")
mplt.xticks(rotation=45)
mplt.show()


# visualise product units
product_performance["Units Sold"].plot(kind="bar")

mplt.title("Products Based on Units Sold")
mplt.xlabel("Product")
mplt.ylabel("Units Sold")
mplt.xticks(rotation=45)
mplt.show()


# Regions

region_performance = data.groupby("Region").agg({
    "Total Sales": "sum",
    "Units Sold": "sum"
})

print("Region Performance:")
print(region_performance)

print("Worst performing region based on sales:")
print(region_performance["Total Sales"].idxmin())

print("Best performing region based on sales:")
print(region_performance["Total Sales"].idxmax())

print("Region selling the most units:")
print(region_performance["Units Sold"].idxmax())

print("Region selling the least units:")
print(region_performance["Units Sold"].idxmin())


# visualise region sales
region_performance["Total Sales"].plot(kind="bar")

mplt.title("Regional Performance")
mplt.xlabel("Region")
mplt.ylabel("Total Sales")
mplt.show()


# visualise region units
region_performance["Units Sold"].plot(kind="bar")

mplt.title("Regions Based on Units Sold")
mplt.xlabel("Region")
mplt.ylabel("Units Sold")
mplt.show()


# Sales Channel

sales_channel = data.groupby("Sales Method").agg({
    "Total Sales": "sum",
    "Units Sold": "sum"
})

print("Sales Channel Performance:")
print(sales_channel)

print("Worst sales channel based on sales:")
print(sales_channel["Total Sales"].idxmin())

print("Best sales channel based on sales:")
print(sales_channel["Total Sales"].idxmax())

print("Sales channel selling the most units:")
print(sales_channel["Units Sold"].idxmax())

print("Sales channel selling the least units:")
print(sales_channel["Units Sold"].idxmin())


# visualise sales channel sales
sales_channel["Total Sales"].plot(kind="bar")

mplt.title("Sales Channel Performance")
mplt.xlabel("Sales Channel")
mplt.ylabel("Total Sales")
mplt.show()


# visualise sales channel units
sales_channel["Units Sold"].plot(kind="bar")

mplt.title("Units Sold by Sales Channel")
mplt.xlabel("Sales Channel")
mplt.ylabel("Units Sold")
mplt.show()


# Task 3
# Compare sales contributions of major retail partners
# (Foot Locker, Walmart, Sports Direct)

sales = data.groupby('Retailer')['Total Sales'].sum()

# calculate sales contribution
sales_contribution = sales / overall_sales_results * 100


# visualise
sales_contribution.plot(kind="bar")

mplt.title("Sales Contribution of Retailers")
mplt.xlabel("Retailer")
mplt.ylabel("Sales Contribution (%)")
mplt.xticks(rotation=45)
mplt.show()


# print
print(sales_contribution)


# Task 4
# Assess the effectiveness of different sales methods
# (In-store vs. Outlet vs. Online)


# Group the data by Sales Method
sales_channel = data.groupby("Sales Method").agg({
    "Total Sales": "sum",
    "Units Sold": "sum",
    "Operating Profit": "sum",
    "Operating Margin": "mean"
})


# Display the performance of each sales channel
print("Sales Channel Performance:")
print(sales_channel)


# Find the worst performing channel based on total sales
print("Worst sales channel based on sales:")
print(sales_channel["Total Sales"].idxmin())


# Find the best performing channel based on total sales
print("Best sales channel based on sales:")
print(sales_channel["Total Sales"].idxmax())


# Find the channel that sold the most products
print("Sales channel selling the most units:")
print(sales_channel["Units Sold"].idxmax())


# Find the channel that sold the least products
print("Sales channel selling the least units:")
print(sales_channel["Units Sold"].idxmin())


# Find the most profitable sales channel
print("Most profitable sales channel:")
print(sales_channel["Operating Profit"].idxmax())


# Find the sales channel with the highest operating margin
print("Sales channel with the highest operating margin:")
print(sales_channel["Operating Margin"].idxmax())


# Visualise sales channel sales
sales_channel["Total Sales"].plot(kind="bar")

mplt.title("Sales Channel Performance Based on Sales")
mplt.xlabel("Sales Channel")
mplt.ylabel("Total Sales")
mplt.show()


# Visualise sales channel units
sales_channel["Units Sold"].plot(kind="bar")

mplt.title("Units Sold by Sales Channel")
mplt.xlabel("Sales Channel")
mplt.ylabel("Units Sold")
mplt.show()


# Visualise sales channel profit
sales_channel["Operating Profit"].plot(kind="bar")

mplt.title("Operating Profit by Sales Channel")
mplt.xlabel("Sales Channel")
mplt.ylabel("Operating Profit")
mplt.show()


# Visualise sales channel margin
sales_channel["Operating Margin"].plot(kind="bar")

mplt.title("Operating Margin by Sales Channel")
mplt.xlabel("Sales Channel")
mplt.ylabel("Operating Margin (%)")
mplt.show()