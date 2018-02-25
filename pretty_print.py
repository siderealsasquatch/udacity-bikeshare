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
                print('#' * (longest_string + 4))
            else:
                if i == 1:
                    print('#{s:-^{fill}}#'.format(s='-',
                        fill=longest_string+2))
                if i != 3:
                    print('#{s:^{fill}}#'.format(s=' ', fill=longest_string+2))
                print('#{s:^{fill}}#'.format(s=string,
                    fill=longest_string+2))

    def _fancy_header_stat_group(self, stat_type, stats):
        '''
        Helper method to create nice headers for each group of statistics.
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
        if start_time_stats:
            pass
        else:
            pass
