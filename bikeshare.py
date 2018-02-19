#!/usr/bin/env python
#
#   bikeshare.py - program to interactively explore bike share data across
#   thress U.S. cities.
#

from CsvData import CsvData

# Test CsvData class.
bikeshare_data = CsvData()

if bikeshare_data.csv_files_available():
    print("Here are the csv files in the current directory:\n")
    for csvfile in bikeshare_data._filenames:
        print(csvfile)
else:
    print("There are no csv files in the current directory.")
