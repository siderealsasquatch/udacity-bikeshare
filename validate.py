#
#   Validate.py - Contains the Validate class that handles data validation.
#

import calendar as cal


class Validate:
    '''
    A class for validating data into CsvData and DataStats object methods.
    '''
    _month_names = cal.month_name[1:7]
    _weekday_names = cal.day_name

    def __init__(self):
        '''
        Initialize the filter mode.
        '''
        self._filter_mode = None

    def get_city_filter(self, city_names):
        '''
        Make sure user entered city name matches one of the cities contained in
        the current CsvData object.

        Parameters

            city_names: List of city names.

        Returns

            city_name_user: User-entered city name.
        '''
        while True:
            print("\nWould you like to see data for Chicago, New York or",
                    "Washington?")
            city_name_user = input("> ").lower()

            for city_name in city_names:
                if city_name_user in city_name.lower():
                    return city_name

            print("That doesn't seem to be correct. Try again.\n")

    def get_filter_mode(self):
        '''
        Make sure user entered filter mode matches one of the available filter
        modes.
        '''
        while True:
            print("\nHow would you like to filter the data? By month, day, or",
                    "not at all? Enter None to forgo filtering.")
            filter_mode_user = input("> ").lower()

            if filter_mode_user in "month":
                self._filter_mode = 'm'
                return 'm'
            elif filter_mode_user in "day":
                self._filter_mode = 'd'
                return 'd'
            elif filter_mode_user in "none":
                self._filter_mode = None
                return None
            else:
                print("That doesn't seem to be correct. Try again.")

    def _get_month_component(self):
        '''
        Helper method to get month component for filter.
        '''
        while True:
            print("\nWhich month? January, Feburary, March, April, May",
                    "or June?")
            month_name_user = input("> ").lower()

            for month_name in self._month_names:
                if month_name_user in month_name.lower():
                    return month_name

            print("That doesn't seem correct. Try again.\n")

    def _get_day_component(self):
        '''
        Helper method to get day component for filter.
        '''
        while True:
            print("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday,",
                    "Saturday, or Sunday?")
            day_name_user = input("> ").lower()

            for day_name in self._weekday_names:
                if day_name_user in day_name.lower():
                    return day_name

            print("That doesn't seem correct. Try again.\n")

    def get_filter_components(self):
        '''
        Get the month and day depending on the filter mode.
        '''
        filter_comp = []

        if self._filter_mode:
            month_name_user = self._get_month_component()
            if self._filter_mode == 'd':
                day_name_user = self._get_day_component()
                return [month_name_user, day_name_user]
            return month_name_user
        else:
            return None
