#!/usr/bin/env python
#
#   bikeshare.py - program to interactively explore bike share data across
#   thress U.S. cities.
#

from csv_data import CsvData
from data_stats import DataStats
from validate import Validate
from pretty_print import PrettyPrint
import bikeshare_functions as bike_funs

# Init all objects
print("Initializing program. Please wait.\n")
bikeshare_data = CsvData()
bikeshare_stats = DataStats(bikeshare_data.get_data())
validator = Validate()
pprint = PrettyPrint()

# Main loop
city_names = bikeshare_data.get_city_names()

# Intro
print("Hello. Let's explore some bike share data.")

while True:
    # Get filter options
    filter_options = bike_funs.get_filter_options(validator, city_names)

    # Calculate stats
    all_stats = bike_funs.calculate_stats(bikeshare_stats, filter_options)

    # Display stats
    bike_funs.display_stats(pprint, filter_options, all_stats)

    # Ask the user if they would like to quit
    if validator.quit_program():
        print("\nBye! Hope you found that useful.")
        break
