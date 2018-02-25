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
pprint = PrettyPrint()

# Main loop
city_names = bikeshare_data.get_city_names()

while True:
    # Get filter options
    filter_city = validator.get_city_filter(city_names)
    filter_mode = validator.get_filter_mode()
    filter_comp = validator.get_filter_components()

    # Calculate stats
    bikeshare_stats.filter_data(filter_city, filter_mode)
    pop_start_time = bikeshare_stats.popular_start_time(filter_comp)
    trip_duration = bikeshare_stats.trip_duration(filter_comp)
    popular_stations = bikeshare_stats.popular_stations(filter_comp)
    popular_trip = bikeshare_stats.popular_trip(filter_comp)
    counts_gender = bikeshare_stats.counts_gender(filter_comp)
    counts_user = bikeshare_stats.counts_user(filter_comp)
    birth_years = bikeshare_stats.birth_years(filter_comp)

    # print(counts_gender)
    # print(birth_years)

    # Display stats
    all_stats = [pop_start_time,
                 popular_stations,
                 popular_trip,
                 trip_duration,
                 counts_user,
                 counts_gender,
                 birth_years]

    all_stat_labs = ["Popular Start Time Stats",
                     "Popular Stations",
                     "Popular Trip",
                     "Trip Duration",
                     "User Type Counts",
                     "Gender Counts",
                     "Birth Year Stats"]

    pprint.get_filter_options(filter_city, filter_mode, filter_comp)
    pprint.main_header()

    for stat_lab1, stat_dict in zip(all_stat_labs, all_stats):
        print("\n{}".format(stat_lab1))
        if stat_dict is None:
            print("Stats unavailable.")
        else:
            for stat_lab2, stat_val in stat_dict.items():
                print("{}: {}".format(stat_lab2, stat_val))

    print("\nWould you like to quit? Yes or no.")
    again = input("> ").lower()

    if again in "yes":
        break
