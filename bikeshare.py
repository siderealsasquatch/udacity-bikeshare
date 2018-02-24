#!/usr/bin/env python
#
#   bikeshare.py - program to interactively explore bike share data across
#   thress U.S. cities.
#

from csv_data import CsvData
from data_stats import DataStats
from validate import Validate
from pretty_print import PrettyPrint

# Init all objects
bikeshare_data = CsvData()
bikeshare_stats = DataStats(bikeshare_data.get_data())
#validator = Validate()
#pretty = PrettyPrint()

# Method prototypes
def get_city_filter(city_names):
    '''
    Get city to filter.
    '''
    while True:
        print("Would you like to see data for Chicago, New York or Washington?")
        city_name_user = input("> ").lower()

        for city_name in city_names:
            if city_name_user in city_name.lower():
                return city_name_user

        print("Please check your spelling and try again.\n")

# Filter options
filter_city = get_city_filter(bikeshare_data.get_city_names())
