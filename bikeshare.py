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

    # Display stats
    # Still missing trip duration
    pprint.get_filter_options(filter_city, filter_mode, filter_comp)
    pprint.main_header()
    pprint.show_start_time_stats(pop_start_time)
    pprint.show_stations_stats(popular_stations)
    pprint.show_trip_stats(popular_trip)
    pprint.show_user_count_stats(counts_user)
    pprint.show_gender_count_stats(counts_gender)
    pprint.show_birth_year_stats(birth_years)

    print("\nWould you like to quit? Yes or no.")
    again = input("> ").lower()

    if again in "yes":
        break
