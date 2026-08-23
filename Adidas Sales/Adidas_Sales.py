# import pandas so i can read data
import pandas as pd

# import plotlib
import matplotlib.pyplot as mplt

# reading data to my project
data = pd.read_csv("C:/Users/Ritshidze/OneDrive/Desktop/Data Science/Adidas Sales/data.csv"
                   ,skiprows=4)

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
data.dropna(axis=0,inplace=True)

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

# visualise
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
product_performance = data.groupby("Product")[
    ["Total Sales", "Units Sold"]
].sum()

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


# Regions
region_performance = data.groupby("Region")[
    ["Total Sales", "Units Sold"]
].sum()

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


# Sales Channel
sales_channel = data.groupby("Sales Method")[
    ["Total Sales", "Units Sold"]
].sum()

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



