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
            # self._filtered_data = None
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

    def popular_stations(self, filter_by=None):
        '''
        Determine the most popular start and end stations.
        '''
        df_slice = ['Start Station', 'End Station']

        if self._data_is_filtered:
            pop_stations = {}
            for sl in df_slice:
                counts = self._filtered_data[sl].value_counts()
                pop_stations[sl] = counts.loc[filter_by].idxmax()
            return pop_stations
        else:
            city = self._all_city_data[self._city_name]
            return city[df_slice].apply(pd.value_counts).idxmax().to_dict()

    def popular_trip(self, filter_by=None):
        '''
        Return a dictionary containing the start and end destinations of the
        most popular trip.
        '''
        labels = ['Start Station', 'End Station']
        trip = ""

        if self._data_is_filtered:
            counts = self._filtered_data['Trip'].value_counts()
            trip = counts.loc[filter_by].idxmax()
        else:
            city = self._all_city_data[self._city_name]
            trip = city['Trip'].value_counts().idxmax()

        popular_trip = {lab: street
                        for lab, street
                        in zip(labels, trip.split("_"))}

        return popular_trip

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

    def birth_years(self, filter_by=None):
        '''
        Return a dictionary containing the latest, earliest, and most popular
        birth years.
        '''
        year_types = ['Latest', 'Earliest', 'Popular']
        years = []

        if self._data_is_filtered:
            # Get latest and earliest year
            year_min_max = self._filtered_data['Birth Year'].agg(['min', 'max'])
            years.extend(list(year_min_max.loc[filter_by]))

            # Get most popular year
            year_counts = self._filtered_data['Birth Year'].value_counts()
            years.append(year_counts.loc[filter_by].idxmax())
        else:
            city = self._all_city_data[self._city_name]

            # Get latest and earliest year
            years.extend(list(city['Birth Year'].agg(['min', 'max'])))

            # Get most popular year
            years.append(city['Birth Year'].value_counts().idxmax())

        # Combine year_types and years into dict
        year_stats = {year_type: int(year)
                      for year_type, year
                      in zip(year_types, years)}

        return year_stats
