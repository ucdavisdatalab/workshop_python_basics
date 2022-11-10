#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cleaning script for preparing data from the HCN Land-Grab Universities project
for the Python/R workshop series. The data is available at
https://github.com/HCN-Digital-Projects/landgrabu-data

Usage: `python3 clean_landgrabu.py input.csv output.csv`
"""

import sys
import pandas as pd
import re

USD = re.compile('[$]|[,]')

def main(infile: str, outfile: str):
    """Clean the data

    Parameters
    ----------
    infile
        CSV of the data
    outfile
        CSV of the cleaned data
    """
    df = pd.read_csv(infile)

    # Fix some column names that have spaces in them
    df = df.rename(columns={
        'Adjusted_ Value_Unsold_Acres_1914':
        'Adjusted_Value_Unsold_Acres_1914',
        'Adjusted_ Total_Value_1914': 'Adjusted_Total_Value_1914',
        'Notes_ Value_Unsold_Acres_1914': 'Notes_Value_Unsold_Acres_1914'
    })

    # Change the USD strings into floats
    usd_cols = [
        'US_Paid', 'Adjusted_US_Paid', 'Adjusted_Endow_Raised_1914',
        'Adjusted_Value_Unsold_Acres_1914', 'Adjusted_Total_Value_1914',
        'Adjusted_Inf_Value_Assign_Yr_2020', 'Adjusted_Inf_Value_1914_2020',
    ]
    df.loc[:, usd_cols] = df.loc[:, usd_cols].replace(USD, '', regex=True)
    df.loc[:, usd_cols] = df.loc[:, usd_cols].astype(float) 

    # Change Y/N to bools
    bool_cols = ['Uni_Site_Purchase', 'Uni_Created', 'Bulk_Disposal']
    yn = {'Y': True, 'N': False}
    df.loc[:, bool_cols] = df.loc[:, bool_cols].replace(yn)
    df.loc[:, bool_cols] = df.loc[:, bool_cols].astype(bool)

    # Change years to ints
    year_cols = [
        'Yr_Uni_Founded', 'Yr_ST_Accept', 'Yr_Uni_Assign', 'Year_Uni_Open'
    ]
    df.loc[:, year_cols] = df.loc[:, year_cols].fillna(0)
    df.loc[:, year_cols] = df.loc[:, year_cols].astype(int)

    # This data stores the inflation factors between 1914 and 2020 for each
    # college/university and stores them in Inf_Value_Assign_Yr_2020. We will
    # drop that column and regenerate it during our live session (to do so:
    # df['Total_Value_1914'] / df['Inf_Factor_Adjust_2020'])
    df.drop(columns=['Inf_Value_Assign_Yr_2020'], inplace=True)

    # Finally, there are a few columns that are not likely to be relevant for
    # our sessions, so in the interests of simplifying the dataset a bit, we
    # drop those as well
    df.drop(columns=[
        'Disposal_Notes_Source', 'Notes_Value_Unsold_Acres_1914',
        'Notes_Sold_Acres_1914', 'Tot_Acres_Exp_Source',
        'Source_Principal_Acres_Sold_1914', 'Inflation_Source',
        'Source_Acre_1918', 'Unsold_Value_Source_1918'
    ], inplace=True)

    print(f"Final dataframe shape: {df.shape}")
    df.to_csv(outfile)

if __name__ == '__main__':
    infile = sys.argv[1]
    outfile = sys.argv[2]
    main(infile, outfile)
