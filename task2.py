# task2.py
# Written by Ihsan Ahmad on 12/01/2026
# This is task2 of the quantium virtual internship
# This file combines the original .csv files provided into a single .csv file with the following fields
# Sales | Date | Region for all 'Pink Morsels' products.

import csv
import pandas as pd
from pathlib import Path

# This function parses an input .csv file for all 'Pink Morsels' products and creates
# a dataframe in the format 'Sales | Date | Region'
def filtered_df(csv_file):
    df = pd.read_csv(csv_file, parse_dates=['date'])
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
    return df


def main():
    directory_path = Path("./data")
    df = pd.DataFrame()
    
    # combine the data from all input files into a single dataframe
    for file_path in sorted(directory_path.iterdir()):
        print(file_path.name)
        if file_path.is_file():
            df = pd.concat([df, filtered_df(csv_file=file_path)], ignore_index=True) 
    
    df.to_csv('output.csv', index=False)


if __name__=="__main__":
    main()
