import pandas as pd

files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
usecols = ["product", "price", "quantity", "date", "region"]

dfs = []
for f in files:
    df = pd.read_csv(f, usecols=usecols, parse_dates=["date"])
    df["product"] = df["product"].fillna("").astype(str).str.strip().str.lower()
    df["price"] = pd.to_numeric(df["price"].astype(str).str.replace("$", ""), errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], downcast="integer", errors="coerce")
    df["region"] = df["region"].fillna("").astype(str).str.strip().str.lower()

    df = df[df["product"] == "pink morsel"]
    df["sales"] = df["price"] * df["quantity"]
    df = df[["sales", "date", "region"]]

    dfs.append(df)

final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv("pink_morsel_sales.csv", index=False)