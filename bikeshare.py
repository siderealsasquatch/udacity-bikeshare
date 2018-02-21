#!/usr/bin/env python
#
#   bikeshare.py - program to interactively explore bike share data across
#   thress U.S. cities.
#

import pandas as pd

from csv_data import CsvData

# Test CsvData class.
bikeshare_data = CsvData()
all_city_data = bikeshare_data.get_data()

if len(all_city_data):
    print("Here are the first five lines of each csv file:\n")
    for city_df in all_city_data.values():
        print(city_df.head())
else:
    print("There are no csv files in the current directory.")
