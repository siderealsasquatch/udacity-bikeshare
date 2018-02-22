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
        Initialize CsvData object with dictionary of the names of the csv files
        in the current directory. If there are none, initialize empty
        dictionary.
        '''
        self._filenames = {}
        self._csv_files_available = True
        self.get_filenames()

    def get_filenames(self):
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

    def get_city_names(self):
        '''
        Return a list of city names corresponding to the csv file names
        currently stored in the CsvData object.
        '''
        return list(self._filenames.keys())

    def _convert_to_dataframe(self, csv_file):
        '''
        Convert the specified csv file into a dataframe.
        '''
        city_data = pd.read_csv(csv_file,
                                parse_dates=['Start Time', 'End Time'])
        city_data['Trip'] = city_data['Start Station'] + "_" + \
            city_data["End Station"]
        return city_data

    def get_data(self, city=None):
        '''
        Return dataframe containing data for a specified city. If no city is
        specified, return a dictionary containing dataframes with data for all
        cities whose csv files are known to the CsvData object.

        Parameters

            chunk_size: size of the chunks of data produced by the pandas
                        iterator.

            city: name of the city whose bikeshare data is to be displayed.
                  Three choices: "Chicago", "New York", and "Washington".
        '''
        # Might need to raise custom error if _filenames is empty
        # Or just have method return empty dict
        if city:
            city_file = self._filenames[city]
            return self._convert_to_dataframe(city_file)
        else:
            all_city_data = {}
            for city_name, city_file in self._filenames.items():
                all_city_data[city_name] = self._convert_to_dataframe(city_file)
            return all_city_data
