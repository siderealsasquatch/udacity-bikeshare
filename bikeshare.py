#!/usr/bin/env python
#
#   bikeshare.py - program to interactively explore bike share data across
#   thress U.S. cities.
#

import pandas as pd

from csv_data import CsvData
from data_stats import DataStats

# Test DataStats class
bikeshare_data = CsvData()
bikeshare_stats = DataStats(bikeshare_data.get_data())

# Function to print results
def print_counts(gender_data, user_type_data, desc=None):
    c_types = ["Gender", "User Type"]
    comb_data = [gender_data, user_type_data]
    if desc:
        for c_type, c_data in zip(c_types, comb_data):
            for d, counts in zip(desc, c_data):
                print("{} counts in {}".format(c_type, d))
                count_str = ""
                for k, v in counts.items():
                    count_str += "{}: {}\n".format(k, v)
                print(count_str)
    else:
        for c_type, c_data in zip(c_types, comb_data):
            print("Total {} counts".format(c_type))
            count_str = ""
            for k, v in c_data.items():
                count_str += "{}: {}\n".format(k, v)
            print(count_str)

# Filter data by month and get gender and user type data for January and May
bikeshare_stats.filter_data('Chicago', 'm')
months = ['January', 'May']
gender_counts_jan = bikeshare_stats.counts_gender(1)
gender_counts_may = bikeshare_stats.counts_gender(5)
gender_counts_month = [gender_counts_jan, gender_counts_may]
user_type_counts_jan = bikeshare_stats.counts_user(1)
user_type_counts_may = bikeshare_stats.counts_user(5)
user_type_counts_month = [user_type_counts_jan, user_type_counts_may]

print_counts(gender_counts_month, user_type_counts_month, months)

# Filter data by day and get gender and user type data for the 1st and 15th of
# each month
bikeshare_stats.filter_data('Chicago', 'd')
days = ['1st', '15th']
gender_counts01 = bikeshare_stats.counts_gender(1)
gender_counts15 = bikeshare_stats.counts_gender(15)
gender_counts_day = [gender_counts01, gender_counts15]
user_type_counts01 = bikeshare_stats.counts_user(1)
user_type_counts15 = bikeshare_stats.counts_user(15)
user_type_counts_day = [user_type_counts01, user_type_counts15]

print_counts(gender_counts_day, user_type_counts_day, days)

# Don't filter data and get total counts of gender and user type
bikeshare_stats.filter_data('Chicago')
gender_counts_total = bikeshare_stats.counts_gender()
user_type_counts_total = bikeshare_stats.counts_user()

print_counts(gender_counts_total, user_type_counts_total)
