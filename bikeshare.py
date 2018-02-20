#!/usr/bin/env python
#
#   bikeshare.py - program to interactively explore bike share data across
#   thress U.S. cities.
#

from csv_data import CsvData

# Test CsvData class.
bikeshare_data = CsvData()
test_iter = bikeshare_data.get_data("Chicago", 100000)

if bikeshare_data.csv_files_available():
    print("Here is the data contained in 'chicago.csv':\n")
    for chunk in test_iter:
        print(chunk)
else:
    print("There are no csv files in the current directory.")
