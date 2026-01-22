import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def transform_data(df):
    df["total"] = df["price"] * df["quantity"]
    return df

def save_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    df = load_data("data/raw_sales.csv")
    df = transform_data(df)
    save_data(df, "data/processed_sales.csv")
    print("Pipeline ejecutado correctamente")
