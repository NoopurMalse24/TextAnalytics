import pandas as pd

def main(df):
    df = df[["SKU", "PRODUCT_CATEGORY", "PRICE", "PACK_SIZE", "STATES"]]
    df = df.dropna()
    sku_counts = df['SKU'].value_counts().reset_index()  # Reset index to get a DataFrame
    sku_counts.columns = ['SKU', 'Count']  # Rename columns for clarity
    df = df.merge(sku_counts, on='SKU', how='left')  # Merge counts back into the original DataFrame
    df_sorted = df.sort_values(by='Count', ascending=False)
    return df_sorted

def state(df, name):
    state_df = df[df['STATES'] == name]
    return state_df

def category(df, category_name):
    # Filter the DataFrame based on the given category name
    category_df = df[df['PRODUCT_CATEGORY'] == category_name]
    return category_df

def packsize(df, pack_size):
    # Filter the DataFrame based on the given pack size
    packsize_df = df[df['PACK_SIZE'] == pack_size]
    return packsize_df

def price(df, price):
    # Filter the DataFrame based on the given pack size
    price_df = df[df['PRICE'] == price]
    return price_df

df = pd.read_csv("Reviews Data.csv")
new_df = main(df)
print(new_df)
print(state(new_df, "Maharashtra"))
print(category(new_df, "face"))
print(packsize(new_df, "50ml"))
print(price(new_df, "499.00"))