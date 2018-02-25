#
#   pretty_print.py - Contains the PrettyPrint class that takes the stats from
#   DataStats objects and displays them in a pleasing manner.
#


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
                print('#{s:^{fill}}#'.format(s=' ', fill=longest_string+2))
                print('#{s:^{fill}}#'.format(s=string,
                    fill=longest_string+2))
                print('#{s:^{fill}}#'.format(s=' ', fill=longest_string+2))
            elif i == (num_strings-1):
                print('#{s:^{fill}}#'.format(s=' ', fill=longest_string+2))
                print(('#' * (longest_string + 4)) + '\n')
            else:
                if i == 1:
                    print('#{s:-^{fill}}#'.format(s='-',
                        fill=longest_string+2))
                if i != 3:
                    print('#{s:^{fill}}#'.format(s=' ', fill=longest_string+2))
                print('#{s:^{fill}}#'.format(s=string,
                    fill=longest_string+2))

    def _fancy_header_stat_group(self, stat_group):
        '''
        Helper method to create nice headers for each group of statistics.
        '''
        header_len = len(stat_group)
        border_edge = '=' * (header_len + 4)
        print(border_edge)
        print('={s:^{fill}}='.format(s=stat_group, fill=header_len+1))
        print(border_edge)

    def _print_stats_from_dict(self, stat_dict):
        '''
        Helper method to print out the statistics for every method except
        '''
        pass

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
        self._fancy_header_stat_group(header)
        # Convert Hour to a datetime object.

        if start_time_stats:
            stats_dict_len = len(start_time_stats)
            for i, stats in enumerate(start_time_stats.items()):
                time, stat = stats
                if i == 0:
                    print("\n{}: {}".format(time, stat))
                elif i == (stats_dict_len - 1):
                    print("{}: {}\n".format(time, stat))
                else:
                    print("{}: {}".format(time, stat))
        else:
            print("There was no data for these particular statistics.\n")

    def show_stations_stats(self, stations_stats=None):
        '''
        Display the popular start and end stations for the current filter
        options.
        '''
        header = 'Popular Start and End Stations'
        self._fancy_header_stat_group(header)

        if stations_stats:
            pass
        else:
            print("There was no data for these particular statistics.\n")

    def show_trip_duration_stats(self, trip_duration_stats=None):
        '''
        Display the total and average trip duration for the current filter
        options.
        '''
        pass

    def show_user_count_stats(self, user_count_stats=None):
        '''
        Display totals for each user type for the current filter options.
        '''
        pass

    def show_gender_count_stats(self, gender_count_stats=None):
        '''
        Display totals for each gender for the current filter options.
        '''
        pass

    def show_birth_year_stats(self, birth_year_stats=None):
        '''
        Display latest, earliest, and most popular birth years for the current
        filter options.
        '''
        pass
