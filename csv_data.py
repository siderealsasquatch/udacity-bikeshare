#
#   CsvData.py - Contains the CsvData class that handles the acquisition of raw
#   bikeshare data from csv files.
#

import os
import pandas as pd


class CsvData:
    '''
    A class for obtaining and filtering raw data from csv files.
    '''

    def __init__(self):
        '''
        Initialize CsvData object with empty list.
        '''
        self._filenames = {}
        self._csv_files_available = True
        self._get_filenames()

    def _get_filenames(self):
        '''
        Check for csv files in current directory and add them to the _filename
        list. If there are no csv files, set _csv_files_available to False.
        '''
        for f in os.listdir("."):
            if f.endswith(".csv"):
                key = f[:-4].replace("_", " ").title()
                self._filenames[key] = f

        if len(self._filenames) == 0:
            self._csv_files_available = False
        else:
            self._csv_files_available = True

    def csv_files_available(self):
        '''
        Return the value of _csv_files_available.
        '''
        return self._csv_files_available

    def get_data(self, city, chunk_size=1000):
        '''
        Return iterator of pandas data frame. This iterator object should
        produce data from the specified file in chunks.

        Parameters

            chunk_size: size of the chunks of data produced by the pandas
                        iterator.

            city: name of the city whose bikeshare data is to be displayed.
                  Three choices: "Chicago", "New York", and "Washington".
        '''
        filename = self._filenames[city]
        df_iterator = pd.read_csv(filename, iterator=True, chunksize=chunk_size)
        return df_iterator
