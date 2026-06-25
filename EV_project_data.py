import pandas as pd

print("Step 1: Loading raw data...")
# Read the pure CSV file
df = pd.read_csv('raw_data_3.csv')

print("Step 2: Normalizing Currencies to Euro Baseline...")
exchange_rates = {"IFRS": 1.0, "US-GAAP": 0.92}
df["Exchange_Rate"] = df["Reporting_Standard"].map(exchange_rates)

# Ensure numeric columns are strictly numbers
numeric_cols = ["Revenue_Local_M", "EBIT_Local_M", "CapEx_Local_M", "RnD_Local_M", "Total_Deliveries", "BEV_Deliveries", "Lithium_Price_USD"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert local currency to EUR
df["Revenue_EUR"] = round(df["Revenue_Local_M"] * df["Exchange_Rate"], 2)
df["EBIT_EUR"] = round(df["EBIT_Local_M"] * df["Exchange_Rate"], 2)
df["CapEx_EUR"] = round(df["CapEx_Local_M"] * df["Exchange_Rate"], 2)
df["RnD_EUR"] = round(df["RnD_Local_M"] * df["Exchange_Rate"], 2)

print("Step 3: Exporting clean database...")
export_cols = [
    'Company', 'Year', 'Reporting_Standard', 'Revenue_EUR', 'EBIT_EUR',  
    'CapEx_EUR', 'RnD_EUR', 'Total_Deliveries', 'BEV_Deliveries', 'Lithium_Price_USD'
]

df[export_cols].to_csv("clean_automotive_dataset.csv", index=False)
print("SUCCESS:")