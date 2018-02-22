#!/usr/bin/env python
#
#   bikeshare.py - program to interactively explore bike share data across
#   thress U.S. cities.
#

from csv_data import CsvData
from data_stats import DataStats

# Test DataStats class
bikeshare_data = CsvData()
bikeshare_stats = DataStats(bikeshare_data.get_data())

# Function to print results
def print_counts(birth_year_data, desc=None):
    if desc:
        for d, byd in zip(desc, birth_year_data):
            print("\nBirth year stats for {}".format(d))
            for k, v in byd.items():
                print("{} Year: {}".format(k, v))
    else:
        print("\nUnfiltered birth year stats.")
        for k, v in birth_year_data.items():
            print("{} Year: {}".format(k, v))

# Filter data by month and get birth year statistics for Feb and March
bikeshare_stats.filter_data('Chicago', 'm')
months = ['February', 'March']
birth_year_feb = bikeshare_stats.birth_years(2)
birth_year_march = bikeshare_stats.birth_years(4)
birth_year_month = [birth_year_feb, birth_year_march]

print_counts(birth_year_month, months)

# Filter data by day and get gender and user type data for the 5th and 20th of
# each month
bikeshare_stats.filter_data('Chicago', 'd')
days = ['5th', '20th']
birth_year05 = bikeshare_stats.birth_years(5)
birth_year20 = bikeshare_stats.birth_years(20)
birth_year_day = [birth_year05, birth_year20]

print_counts(birth_year_day, days)

# Don't filter data and get total counts of gender and user type
bikeshare_stats.filter_data('Chicago')
birth_year_no_filter = bikeshare_stats.birth_years()

print_counts(birth_year_no_filter)
