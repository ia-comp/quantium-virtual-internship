# task1.py
# Written by Ihsan Ahmad on 12/01/2026
# This file combines the original .csv files provided into a single .csv file with the following fields
# Sales | Date | Region for all 'Pink Morsels' products.

import csv
import pandas
from pathlib import Path

def filter_original_data(csv_file):
    df = pandas.read_csv(csv_file, parse_dates=['date'])
    df = df[df['product'] == 'pink morsel']

    # Remove symbols and convert to float
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)


    df['Sales'] = df['price'].mul(df['quantity'])
    df = df.drop(columns=['product', 'price', 'quantity'])
    df.columns = ['Date', 'Region', 'Sales']
    
    # Reorder columns by passing a new list
    df = df[['Sales', 'Date', 'Region']]

    # Convert sales to string and add the dollar sign in front
    df['Sales'] = df['Sales'].map('${:.2f}'.format)
    print(df)
    df.to_csv('output.csv', index=False)

def main():
    directory_path = Path("./data")
    for file_path in directory_path.iterdir():
        if file_path.is_file():
            filter_original_data(csv_file=file_path)

if __name__=="__main__":
    main()
