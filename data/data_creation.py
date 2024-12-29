import pandas as pd
import random
import numpy as np

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Generate Historical Sales Data
def generate_historical_sales_data():
    data = []
    regions = ["India", "US", "Sweden"]
    products = [f"P{i:03d}" for i in range(1, 21)]  #20 products
    years = range(2021, 2025)  # 2021 to 2024
    months = range(1, 13)

    for year in years:
        for month in months:
            for product in products:
                for region in regions:
                    sales_volume = random.randint(50, 1000)
                    price = random.choice([100, 1500, 20000,50000,100000,250000])
                    revenue = sales_volume * price
                    stockouts = random.choice([0, 1])  # Binary: 0 = No, 1 = Yes
                    data.append([product, region, year, month, sales_volume, revenue, price, stockouts])

    columns = ["Product ID", "Region", "Year", "Month", "Sales Volume", "Revenue", "Price", "Stockouts"]
    return pd.DataFrame(data, columns=columns)

# Generate External Factors Data
def generate_external_factors_data():
    data = []
    regions = ["India", "US", "Sweden"]
    festivals = [
        {"name": "Christmas", "month": 12, "start_day": 24, "end_day": 25},
        {"name": "Diwali", "month": 11, "start_day": 12, "end_day": 15},
        {"name": "Easter", "month": 4, "start_day": 9, "end_day": 9},
    ]
    years = range(2021, 2025)

    for year in years:
        for region in regions:
            for festival in festivals:
                inflation_rate = round(random.uniform(2.0, 5.0), 1)  # Inflation rate as a percentage
                data.append([
                    festival["name"],
                    f"{year}-{festival['month']:02d}-{festival['start_day']:02d}",
                    f"{year}-{festival['month']:02d}-{festival['end_day']:02d}",
                    region,
                    inflation_rate,
                ])

    columns = ["Festival Name", "Start Date", "End Date", "Region", "Inflation Rate"]
    return pd.DataFrame(data, columns=columns)

# Generate Inventory Logs Data
def generate_inventory_logs_data():
    data = []
    regions = ["India", "US", "Sweden"]
    products = [f"P{i:03d}" for i in range(1, 21)]  # 20 products
    years = range(2021, 2025)  # 2021 to 2024
    months = range(1, 13)

    for year in years:
        for month in months:
            for product in products:
                for region in regions:
                    stock_level = random.randint(50, 300)
                    replenishment_time = random.randint(5, 15)  # Days
                    data.append([product, region, year, month, stock_level, replenishment_time])

    columns = ["Product ID", "Region", "Year", "Month", "Stock Level", "Replenishment Time"]
    return pd.DataFrame(data, columns=columns)

# Create datasets
historical_sales_data = generate_historical_sales_data()
external_factors_data = generate_external_factors_data()
inventory_logs_data = generate_inventory_logs_data()

# Save datasets to CSV
historical_sales_data.to_csv(r"C:\Users\Devadarsan\Desktop\Karthik_projects\SCM-Sales-RAGAS\DemandForecasting_SCM_RAG_GEN-AI\data\Historical_Sales_Data.csv", index=False)
external_factors_data.to_csv(r"C:\Users\Devadarsan\Desktop\Karthik_projects\SCM-Sales-RAGAS\DemandForecasting_SCM_RAG_GEN-AI\data\External_Factors_Data.csv", index=False)
inventory_logs_data.to_csv(r"C:\Users\Devadarsan\Desktop\Karthik_projects\SCM-Sales-RAGAS\DemandForecasting_SCM_RAG_GEN-AI\data\Inventory_Logs_Data.csv", index=False)

#"/mnt/data/Historical_Sales_Data.csv", "/mnt/data/External_Factors_Data.csv", "/mnt/data/Inventory_Logs_Data.csv"
