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
            print("\nStation stats for {}".format(d))
            for k, v in byd.items():
                print("{} Year: {}".format(k, v))
    else:
        print("\nUnfiltered station stats.")
        for k, v in birth_year_data.items():
            print("{} Year: {}".format(k, v))

# Filter data by month and get popular stop and end stations, and popular trip
# for April and June
bikeshare_stats.filter_data('Chicago', 'm')
months = ['April', 'June']
pop_stations_april = bikeshare_stats.popular_stations(4)
pop_stations_june = bikeshare_stats.popular_stations(6)
pop_stations_month = [pop_stations_april, pop_stations_june]

print('Popular Start and End Stations')
print_counts(pop_stations_month, months)

pop_trip_april = bikeshare_stats.popular_trip(4)
pop_trip_june = bikeshare_stats.popular_trip(6)
pop_trip_month = [pop_trip_april, pop_trip_june]

print('\nPopular trips')
print_counts(pop_trip_month, months)

# Filter data by day and get gender and user type data for the 7th and 12th of
# each month
bikeshare_stats.filter_data('Chicago', 'd')
days = ['7th', '12th']
pop_stations07 = bikeshare_stats.popular_stations(7)
pop_stations12 = bikeshare_stats.popular_stations(12)
pop_station_day = [pop_stations07, pop_stations12]

print('Popular Start and End Stations')
print_counts(pop_station_day, days)

pop_trip07 = bikeshare_stats.popular_trip(7)
pop_trip12 = bikeshare_stats.popular_trip(12)
pop_trip_day = [pop_trip07, pop_trip12]

print('\nPopular trips')
print_counts(pop_trip_day, days)

# Don't filter data and get total counts of gender and user type
bikeshare_stats.filter_data('Chicago')
pop_stations_no_filter = bikeshare_stats.popular_stations()
pop_trip_no_filter = bikeshare_stats.popular_trip()

print('Popular Start and End Stations')
print_counts(pop_stations_no_filter)

print('\nPopular trips')
print_counts(pop_trip_no_filter)
