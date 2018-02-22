#
#   data_stats.py - Contains the DataStats class that handles the computation of
#   certain statistics on the data from the project csv files.
#

import pandas as pd
import datetime as dt
import calendar as cal


class DataStats:
    '''
    A class for computing basic descriptive statistics on bikeshare data.
    '''

    _mon_str_conversions = {mon_name: mon_int
                            for mon_int, mon_name
                            in enumerate(cal.month_abbr)
                            if mon_int > 0}

    def __init__(self, all_city_data):
        '''
        Initialize DataStats object with data for all cities. This data is
        passed to the object as a dictionary of dataframes. Also initialize the
        city name, filter mode and filter criteria.
        '''
        self._all_city_data = all_city_data
        self._filtered_data = None
        self._data_is_filtered = False
        self._city_name = None
        # self._filter_mode = None
        # self._filter_term = None

    # def set_filter(self, city_name, filter_mode=None, filter_by=None):
        # '''
        # Set the filter mode and filter criteria.
        # '''
        # self._city_name = city_name
        # self._filter_mode = filter_mode
        # self._filter_by = filter_by

    def filter_data(self, city_name, filter_mode=None):
        '''
        Filter data for the specified city by month, day, or not at all.
        '''
        # self._filter_term = filter_term

        # Filter by month or day
        if filter_mode:
            self._data_is_filtered = True
            city_data = self._all_city_data[city_name]

            if filter_mode.lower() == 'm':
                self._filtered_data = city_data.groupby(
                        city_data['Start Time'].dt.month)
            elif filter_mode.lower() == 'd':
                self._filtered_data = city_data.groupby(
                        city_data['Start Time'].dt.day)
        else:
            self._city_name = city_name
            self._filtered_data = None
            self._data_is_filtered = False

    def popular_start_time(self):
        '''
        Calculate stats related to start time.
        '''
        pass

    def trip_duration(self):
        '''
        Calculate total trip duration and average trip duration.
        '''
        pass

    def popular_station(self):
        '''
        Determine the most popular start and end stations.
        '''
        pass

    def popular_trip(self):
        '''
        Determine the most popular trip.
        '''
        pass

    def counts_gender(self, filter_by=None):
        '''
        Return a dictionary containing counts for each gender.
        '''
        if self._data_is_filtered:
            counts = self._filtered_data['Gender'].value_counts()
            return counts.loc[filter_by].to_dict()
        else:
            city = self._all_city_data[self._city_name]
            return city['Gender'].value_counts().to_dict()

    def counts_user(self, filter_by=None):
        '''
        Return a dictionary containing counts for each user type.
        '''
        if self._data_is_filtered:
            counts = self._filtered_data['User Type'].value_counts()
            return counts.loc[filter_by].to_dict()
        else:
            city = self._all_city_data[self._city_name]
            return city['User Type'].value_counts().to_dict()

    def birth_years(self):
        '''
        Determine the latest, earliest, and most popular birth years.
        '''
        pass
