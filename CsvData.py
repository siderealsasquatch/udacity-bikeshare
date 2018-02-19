#
#   CsvData.py - Contains the CsvData class that handles the acquisition of raw
#   bikeshare data from csv files.
#

import os


class CsvData:
    '''
    A class for obtaining and filtering raw data from csv files.
    '''

    def __init__(self):
        '''
        Initialize CsvData object with empty list.
        '''
        self._filenames = []
        self._csv_files_available = True
        self._get_filenames()

    def _get_filenames(self):
        '''
        Check for csv files in current directory and add them to the _filename
        list. If there are no csv files, set _csv_files_available to False.
        '''
        for csvfile in os.listdir("."):
            if csvfile.endswith(".csv"):
                self._filenames.append(csvfile)

        if len(self._filenames) == 0:
            self._csv_files_available = False
        else:
            self._csv_files_available = True

    def csv_files_available(self):
        '''
        Return the value of _csv_files_available.
        '''
        return self._csv_files_available

    def show_data(self, city, filter_mode=None, filter_by=None):
        '''
        Return data that is optionally filtered by month or day.

        Parameters

            city: name of the city whose bikeshare data is to be displayed.
                  Three choices: "Chicago", "New York", and "Washington".

            filter_mode: determines how the data is to be filtered. 'm' for
                         month, 'd' for day, and None to eschew filtering.

            filter_by: narrows down the data by either month (e.g. "January";
                       only first six months) or day of week (e.g. "Monday")
        '''
        pass
