#
#   data_stats.py - Contains the DataStats class that handles the computation of
#   certain statistics on the data from the project csv files.
#

import pandas as pd
import datetime as dt


class DataStats:
    '''
    A class for computing basic descriptive statistics on bikeshare data.
    '''

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
        self._filter_mode = None
        # self._filter_term = None

    def filter_data(self, city_name, filter_mode=None):
        '''
        Filter data for the specified city by month, day, or not at all.
        '''
        # self._filter_term = filter_term
        self._filter_mode = filter_mode

        # Filter by month or day
        if filter_mode:
            self._data_is_filtered = True
            city_data = self._all_city_data[city_name]

            if filter_mode == 'm':
                self._filtered_data = city_data.groupby('Month')
            elif filter_mode == 'd':
                self._filtered_data = city_data.groupby(['Month', 'Weekday'])
        else:
            self._city_name = city_name
            # self._filtered_data = None
            self._data_is_filtered = False

    def _get_filtered_pop(self, col, filter_by):
        '''
        Helper method to retrieve most popular value from filtered data.
        '''
        counts = self._filtered_data[col].value_counts()
        if self._filter_mode == 'm':
            return counts.loc[filter_by].idxmax()
        elif self._filter_mode == 'd':
            f1, f2 = filter_by
            return counts.loc[f1, f2].idxmax()

    def popular_start_time(self, filter_by=None):
        '''
        Calculate stats related to start time.
        '''
        pop_start_time_labs = ['Month', 'Weekday', 'Hour']
        pop_start_time_data = []

        if self._data_is_filtered:
            if self._filter_mode == 'm':
                # Get pop weekday and hour
                for col in pop_start_time_labs[1:]:
                    pop_start_time_data.append(
                            self._get_filtered_pop(col, filter_by))

                stats_for_month = {lab: data for lab, data
                                   in zip(pop_start_time_labs[1:],
                                          pop_start_time_data)}

                return stats_for_month
            if self._filter_mode == 'd':
                # Get pop hour
                hr = pop_start_time_labs[-1]
                pop_start_time_data.append(
                        self._get_filtered_pop(hr, filter_by))

                stats_for_day = {lab: data for lab, data
                                 in zip(pop_start_time_labs[-1:],
                                        pop_start_time_data)}

                return stats_for_day
        else:
            # Get pop month, weekday, and hour
            city = self._all_city_data[self._city_name]
            for col in pop_start_time_labs:
                pop_start_time_data.append(city[col].value_counts().idxmax())

            stats_unfiltered = {lab: data for lab, data
                                in zip(pop_start_time_labs,
                                       pop_start_time_data)}

            return stats_unfiltered

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
