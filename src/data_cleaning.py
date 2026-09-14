import pandas as pd


def load_data(file_path):
    """Load both sheets of the Online Retail II Excel dataset."""
    
    sheet1 = pd.read_excel(file_path, sheet_name=0)
    sheet2 = pd.read_excel(file_path, sheet_name=1)

    df = pd.concat(
        [sheet1, sheet2],
        ignore_index=True
    )

    return df


def clean_data(df):
    """Clean the retail transaction dataset."""

    # Rename columns
    df = df.rename(columns={
        "Invoice": "InvoiceNo",
        "Price": "UnitPrice",
        "Customer ID": "CustomerID"
    })

    # Remove duplicate records
    df = df.drop_duplicates().copy()

    # Keep transactions with known customers
    df = df.dropna(subset=["CustomerID"]).copy()

    # Handle missing product descriptions
    df["Description"] = (
        df["Description"]
        .fillna("Unknown Product")
    )

    # Remove cancelled invoices
    cancelled = (
        df["InvoiceNo"]
        .astype(str)
        .str.startswith("C")
    )

    df = df[~cancelled].copy()

    # Remove invalid quantities and prices
    df = df[
        (df["Quantity"] > 0) &
        (df["UnitPrice"] > 0)
    ].copy()

    # Convert CustomerID to integer
    df["CustomerID"] = (
        df["CustomerID"].astype("int64")
    )

    # Create Revenue
    df["Revenue"] = (
        df["Quantity"] *
        df["UnitPrice"]
    )

    # Create PurchaseMonth
    df["PurchaseMonth"] = (
        df["InvoiceDate"]
        .dt.to_period("M")
        .astype(str)
    )

    return df


if __name__ == "__main__":

    input_file = "data/raw/online_retail_II.xlsx"
    output_file = "data/processed/cleaned_retail.csv"

    df = load_data(input_file)

    cleaned_df = clean_data(df)

    cleaned_df.to_csv(
        output_file,
        index=False
    )

    print("Data cleaning completed successfully.")
    print("Final shape:", cleaned_df.shape)