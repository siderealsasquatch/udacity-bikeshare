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
validator = Validate()
#pretty = PrettyPrint()

# Filter options
filter_city = validator.get_city_filter(bikeshare_data.get_city_names())
filter_mode = validator.get_filter_mode()
filter_comp = validator.get_filter_components()

# Show filter options
print("Your filter options:")
for opt in [filter_city, filter_mode, filter_comp]:
    print(opt)
