import pandas as pd

csv_files = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]

cleaned_data = []

for file in csv_files:
    df = pd.read_csv(file)

    df = df[df["product"] == "pink morsel"]

    df["price"] = df["price"].replace(r"\$", "", regex=True).astype(float)

    df["sales"] = df["quantity"] * df["price"]

    df = df[["date", "region", "sales"]]

    cleaned_data.append(df)

final_df = pd.concat(cleaned_data, ignore_index=True)

final_df.to_csv("cleaned_sales_data.csv", index=False)

print("Cleaned data saved as 'cleaned_sales_data.csv'.")

