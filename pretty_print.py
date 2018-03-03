#
#   pretty_print.py - Contains the PrettyPrint class that takes the stats from
#   DataStats objects and displays them in a pleasing manner.
#

import datetime as dt


class PrettyPrint:
    '''
    A class that handles displaying the stats from a DataStats object.
    '''

    def __init__(self):
        '''
        Initialize internal variables that keep track of filter options.
        '''
        self._city_name = None
        self._filter_mode = None
        self._filter_by = None

    def _fancy_header_main(self, header_strings):
        '''
        Helper method to create fancy borders for the main header.
        '''
        longest_string = max([len(string) for string in header_strings])
        header_strings_new = header_strings
        if len(header_strings) == 1:
            header_strings_new.append('Unfiltered')
        header_strings_new.append(' ')
        num_strings = len(header_strings_new)

        for i, string in enumerate(header_strings_new):
            if i == 0:
                print('#' * (longest_string + 4))
                # print('#{s:^{fill}}#'.format(s=' ', fill=longest_string+2))
                print('#{s:^{fill}}#'.format(s=string,
                    fill=longest_string+2))
                # print('#{s:^{fill}}#'.format(s=' ', fill=longest_string+2))
            elif i == (num_strings-1):
                # print('#{s:^{fill}}#'.format(s=' ', fill=longest_string+2))
                print(('#' * (longest_string + 4)) + '\n')
            else:
                if i == 1:
                    print('#{s:-^{fill}}#'.format(s='-',
                        fill=longest_string+2))
                # if i != 3:
                    # print('#{s:^{fill}}#'.format(s=' ', fill=longest_string+2))
                print('#{s:^{fill}}#'.format(s=string,
                    fill=longest_string+2))

    def _fancy_header_stat_group(self, stat_group):
        '''
        Helper method to create nice headers for each group of statistics.
        '''
        header_len = len(stat_group)
        # border_edge = '=' * (header_len + 4)
        border_edge = '=' * header_len
        # print(border_edge)
        # print('={s:^{fill}}='.format(s=stat_group, fill=header_len+1))
        print(stat_group)
        print(border_edge)

    def _print_stats_from_dict(self, stat_dict):
        '''
        Helper method to print out the statistics for every method except the
        trip duration stats.
        '''
        non_none_dict = {k: v for k, v in stat_dict.items() if v is not None}
        non_none_dict_len = len(non_none_dict)
        # for i, stats in enumerate(stat_dict.items()):
        for i, stats in enumerate(non_none_dict.items()):
            time, stat = stats

            if i == 0:
                if non_none_dict_len == 1:
                    print("\n{}: {}\n".format(time, stat))
                else:
                    print("\n{}: {}".format(time, stat), end=' | ')
            elif i == (non_none_dict_len - 1):
                print("{}: {}\n".format(time, stat))
            else:
                print("{}: {}".format(time, stat), end=' | ')

    def main_header(self):
        '''
        Print a header displaying the current filter options: city, filter mode,
        and the month or day (or both) depending on the filter mode.
        '''
        str_title = 'Statistics for {}'.format(self._city_name)
        all_filter_str = [str_title]
        if self._filter_mode:
            str_filter_header = 'Filtered by'
            str_filter_comp = []
            if self._filter_mode == 'd':
                month, day = self._filter_by
                str_filter_comp.append('Month: {}'.format(month))
                str_filter_comp.append('Day: {}'.format(day))
            else:
                str_filter_comp.append('Month: {}'.format(self._filter_by))
            all_filter_str = [str_title, str_filter_header, *str_filter_comp]
        self._fancy_header_main(all_filter_str)

    def get_filter_options(self, city_name, filter_mode=None, filter_by=None):
        '''
        Get the current filter options and assign them to the proper internal
        variables.
        '''
        self._city_name = city_name
        self._filter_mode = filter_mode
        self._filter_by = filter_by

    def show_start_time_stats(self, start_time_stats=None):
        '''
        Display the start time statistics using the current filter options.
        '''
        header = 'Popular Month, Day, and Hour for Start Time'

        if start_time_stats:
            # Convert 'Hour' int to string
            start_time_stats_time_format = start_time_stats
            start_time_stats_time_format['Hour'] = '{}:00'.format(
                    start_time_stats_time_format['Hour'])

            # Remove parts of the header string depending on how the data was
            # filtered
            if not start_time_stats_time_format['Month']:
                header = header.replace(',', '').replace(' Month', '')
            if not start_time_stats_time_format['Weekday']:
                header = header.replace(' Day and', '')

            # Print new header string
            self._fancy_header_stat_group(header)
            self._print_stats_from_dict(start_time_stats_time_format)
        else:
            self._fancy_header_stat_group(header)
            print("\nThere was no data for these particular statistics.\n")

    def show_stations_stats(self, stations_stats=None):
        '''
        Display the popular start and end stations for the current filter
        options.
        '''
        header = 'Popular Start and End Stations'
        self._fancy_header_stat_group(header)

        if stations_stats:
            self._print_stats_from_dict(stations_stats)
        else:
            print("\nThere was no data for these particular statistics.\n")

    def show_trip_stats(self, trip_stats=None):
        '''
        Display the most popular trip for the current filter options.
        '''
        header = 'Most Popular Trip'
        self._fancy_header_stat_group(header)

        if trip_stats:
            self._print_stats_from_dict(trip_stats)
        else:
            print("\nThere was no data for these particular statistics.\n")

    def show_trip_duration_stats(self, trip_duration_stats=None):
        '''
        Display the total and average trip duration for the current filter
        options.
        '''
        header = 'Total and Average Trip Duration'
        self._fancy_header_stat_group(header)

        if trip_duration_stats:
            trip_dur_len = len(trip_duration_stats)
            for i, trip_dat in enumerate(trip_duration_stats.items()):
                dur_type, dur_dat_dict = trip_dat

                dur_string = "{}\t:: ".format(dur_type)
                if i == 0:
                    dur_string = "\n" + dur_string

                dur_dat_dict_len = len(dur_dat_dict)
                for j, dur_dat in enumerate(dur_dat_dict.items()):
                    time_category, time = dur_dat
                    if j == (dur_dat_dict_len - 1):
                        dur_string += "{}: {}".format(time_category, time)
                    else:
                        dur_string += "{}: {}, ".format(time_category, time)

                if i == (trip_dur_len - 1):
                    dur_string = dur_string + '\n'

                print(dur_string)
        else:
            print("\nThere was no data for these particular statistics.\n")

    def show_user_count_stats(self, user_count_stats=None):
        '''
        Display totals for each user type for the current filter options.
        '''
        header = 'Counts of each User Type'
        self._fancy_header_stat_group(header)

        if user_count_stats:
            self._print_stats_from_dict(user_count_stats)
        else:
            print("\nThere was no data for these particular statistics.\n")

    def show_gender_count_stats(self, gender_count_stats=None):
        '''
        Display totals for each gender for the current filter options.
        '''
        header = 'Counts of each Gender'
        self._fancy_header_stat_group(header)

        if gender_count_stats:
            self._print_stats_from_dict(gender_count_stats)
        else:
            print("\nThere was no data for these particular statistics.\n")

    def show_birth_year_stats(self, birth_year_stats=None):
        '''
        Display latest, earliest, and most popular birth years for the current
        filter options.
        '''
        header = 'Latest, Earliest, and most Popular Birth Years'
        self._fancy_header_stat_group(header)

        if birth_year_stats:
            self._print_stats_from_dict(birth_year_stats)
        else:
            print("\nThere was no data for these particular statistics.\n")
