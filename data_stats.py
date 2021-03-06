#
#   data_stats.py - Contains the DataStats class that handles the computation of
#   certain statistics on the data from the project csv files.
#

import pandas as pd


class DataStats:
    '''
    A class for computing basic descriptive statistics on bikeshare data.
    '''

    def __init__(self, all_city_data):
        '''
        Initialize DataStats object with data for all cities. This data is
        passed to the object as a dictionary of dataframes. Also initialize the
        city name, filter mode and filter criteria.

        Parameters

            all_city_data: Dictionary containing all dataframes of all bikeshare
                           csv files. Should be generated using the get_data
                           method of a CsvData object.
        '''
        self._all_city_data = all_city_data
        self._filtered_data = None
        self._data_is_filtered = False
        self._city_name = None
        self._filter_mode = None

    def _check_columns_exist(self, cols):
        '''
        Helper method to check if the given columns exist.
        '''
        for col in cols:
            if col not in self._all_city_data[self._city_name].columns:
                return False

        return True

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

    def _convert_seconds(self, seconds):
        '''
        Helper method to convert seconds to years, months, days, hours, minutes
        and seconds.
        '''
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)
        years, months = divmod(months, 12)

        return years, months, days, hours, minutes, seconds

    def filter_data(self, city_name, filter_mode=None):
        '''
        Filter data for the specified city by month, day, or not at all.

        Parameters

            city_name: Name of one of the cities whose csv data was passed to
                       the DataStats constructor method.

            filter_mode: 'm' for month, 'd' for day, or None to forgo filtering.
        '''
        self._filter_mode = filter_mode
        self._city_name = city_name

        # Filter by month or day
        if filter_mode:
            self._data_is_filtered = True
            city_data = self._all_city_data[city_name]

            if filter_mode == 'm':
                self._filtered_data = city_data.groupby('Month')
            elif filter_mode == 'd':
                self._filtered_data = city_data.groupby(['Month', 'Weekday'])
        else:
            self._data_is_filtered = False
            self._filtered_data = None

    def popular_start_time(self, filter_by=None):
        '''
        Calculate the most popular month, day and hour for start time. Return a
        dictionary containing values for each category. If no statistic is
        available, 'None' will be assigned for that category.

        Parameters

            filter_by: Name of month or list containing name of month and
                       weekday depending on the current filter mode.

        Returns

            stats: Dictionary containing the monst popular month, day, and hour.
        '''
        pop_start_time_labs = ['Month', 'Weekday', 'Hour']
        pop_start_time_data = []

        if self._data_is_filtered:
            if self._filter_mode == 'm':
                # Get pop weekday and hour
                for col in pop_start_time_labs[1:]:
                    pop_start_time_data.append(
                            self._get_filtered_pop(col, filter_by))

                stats = {lab: data for lab, data
                         in zip(pop_start_time_labs[1:],
                                pop_start_time_data)}

            if self._filter_mode == 'd':
                # Get pop hour
                hr = pop_start_time_labs[-1]
                pop_start_time_data.append(
                        self._get_filtered_pop(hr, filter_by))

                stats = {lab: data for lab, data
                         in zip(pop_start_time_labs[-1:],
                                pop_start_time_data)}

        else:
            # Get pop month, weekday, and hour
            city = self._all_city_data[self._city_name]
            for col in pop_start_time_labs:
                pop_start_time_data.append(city[col].value_counts().idxmax())

            stats = {lab: data for lab, data
                     in zip(pop_start_time_labs,
                            pop_start_time_data)}

        # Assign None to any missing values
        for lab in pop_start_time_labs:
            stats.setdefault(lab, None)

        return stats

    def trip_duration(self, filter_by=None):
        '''
        Calculate total trip duration and average trip duration.

        Parameters

            filter_by: Name of month or list containing name of month and
                       weekday depending on the current filter mode.

        Returns

            time_conv: Dictionary containing the total and average trip
                       duration.
        '''
        div_labs = ['Years', 'Months', 'Days', 'Hours', 'Minutes', 'Seconds']
        time_labs = ['Total', 'Average']
        time_conv = {}
        col = 'Trip Duration'

        if self._data_is_filtered:
            sec_mean = 0
            sec_sum = 0

            if self._filter_mode == 'm':
                sec_mean = self._filtered_data[col].mean().loc[filter_by]
                sec_sum = self._filtered_data[col].sum().loc[filter_by]
            elif self._filter_mode == 'd':
                f1, f2 = filter_by
                sec_mean = self._filtered_data[col].mean().loc[f1, f2]
                sec_sum = self._filtered_data[col].sum().loc[f1, f2]

            for lab, seconds in zip(time_labs, [sec_sum, sec_mean]):
                convs = self._convert_seconds(int(seconds))
                time_tmp = {lab: conv for lab, conv
                            in zip(div_labs, convs)}
                time_conv[lab] = time_tmp
        else:
            sec_mean = self._all_city_data[self._city_name][col].mean()
            sec_sum = self._all_city_data[self._city_name][col].sum()

            for lab, seconds in zip(time_labs, [sec_sum, sec_mean]):
                convs = self._convert_seconds(int(seconds))
                time_tmp = {lab: conv for lab, conv
                            in zip(div_labs, convs)}
                time_conv[lab] = time_tmp

        return time_conv

    def popular_stations(self, filter_by=None):
        '''
        Determine the most popular start and end stations.

        Parameters

            filter_by: Name of month or list containing name of month and
                       weekday depending on the current filter mode.

        Returns

            pop_stations: Dictionary containing the most popular start and end
                          stations.
        '''
        df_slice = ['Start Station', 'End Station']

        if self._data_is_filtered:
            pop_stations = {}
            for sl in df_slice:
                pop_stations[sl] = self._get_filtered_pop(sl, filter_by)
            return pop_stations
        else:
            city = self._all_city_data[self._city_name]
            return city[df_slice].apply(pd.value_counts).idxmax().to_dict()

    def popular_trip(self, filter_by=None):
        '''
        Return a dictionary containing the start and end destinations of the
        most popular trip.

        Parameters

            filter_by: Name of month or list containing name of month and
                       weekday depending on the current filter mode.

        Returns

            popular_trip: Dictionary containing the start and end stations of
                          the most popular trip
        '''
        labels = ['Start Station', 'End Station']
        trip = ""

        if self._data_is_filtered:
            trip = self._get_filtered_pop('Trip', filter_by)
        else:
            city = self._all_city_data[self._city_name]
            trip = city['Trip'].value_counts().idxmax()

        popular_trip = {lab: street
                        for lab, street
                        in zip(labels, trip.split("_"))}

        return popular_trip

    def counts_gender(self, filter_by=None):
        '''
        Determine the total amount of each gender for the current filter level.

        Parameters

            filter_by: Name of month or list containing name of month and
                       weekday depending on the current filter mode.

        Returns

            counts: Dictionary containing the counts for each gender.
        '''
        if not self._check_columns_exist(['Gender']):
            return None

        if self._data_is_filtered:
            counts = self._filtered_data['Gender'].value_counts()
            if self._filter_mode == 'm':
                return counts.loc[filter_by].to_dict()
            elif self._filter_mode == 'd':
                f1, f2 = filter_by
                return counts.loc[f1, f2].to_dict()
        else:
            city = self._all_city_data[self._city_name]
            return city['Gender'].value_counts().to_dict()

    def counts_user(self, filter_by=None):
        '''
        Determine the total amount of each user type for the current filter
        leve.

        Parameters

            filter_by: Name of month or list containing name of month and
                       weekday depending on the current filter mode.

        Returns

            counts: Dictionary containing counts for each user type.
        '''
        if not self._check_columns_exist(['User Type']):
            return None

        if self._data_is_filtered:
            counts = self._filtered_data['User Type'].value_counts()
            if self._filter_mode == 'm':
                return counts.loc[filter_by].to_dict()
            elif self._filter_mode == 'd':
                f1, f2 = filter_by
                return counts.loc[f1, f2].to_dict()
        else:
            city = self._all_city_data[self._city_name]
            return city['User Type'].value_counts().to_dict()

    def birth_years(self, filter_by=None):
        '''
        Determine the latest, earliest, and most popular birth years for the
        current filter level.

        Parameters

            filter_by: Name of month or list containing name of month and
                       weekday depending on the current filter mode.

        Returns

            year_stats: Dictionary containing the latest, earliest, and most
                        popular birth years.
        '''
        if not self._check_columns_exist(['Birth Year']):
            return None

        year_types = ['Latest', 'Earliest', 'Popular']
        years = []

        if self._data_is_filtered:
            # Get latest and earliest year
            year_min_max = self._filtered_data['Birth Year'].agg(['min', 'max'])
            if self._filter_mode == 'm':
                years.extend(list(year_min_max.loc[filter_by]))
            elif self._filter_mode == 'd':
                f1, f2 = filter_by
                years.extend(list(year_min_max.loc[f1, f2]))

            # Get most popular year
            years.append(self._get_filtered_pop('Birth Year', filter_by))
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
