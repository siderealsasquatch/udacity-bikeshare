# Exploring US Bike Share Data

Take a deeper look at some bike share data from three U.S. cities: Chicago, New York City,
and Washington, D.C. This project was done as part of the Udacity Data Analyst Nanodegree
program.

## About the data

This project uses bikeshare data provided by [Motivate][1], a bike share system provider
for many major cites in the U.S. Below are links to the original datasets:

+ [Chicago][2]
+ [New York City][3]
+ [Washington][4]

Please note that, while the data used in the project was derived from these datasets, they
had been cleaned up quite a bit. The datasets used in the project had randomly selected
data for the first six months of 2017 with only the following six columns:

+ Start Time (e.g., 2017-01-01 00:07:57)
+ End Time (e.g., 2017-01-01 00:20:53)
+ Trip Duration (in seconds - e.g., 776)
+ Start Station (e.g., Broadway & Barry Ave)
+ End Station (e.g., Sedgwick St & North Ave)
+ User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

+ Gender
+ Birth Year

If you'd like to run the program, you'll have to clean up the origninal data on your own.

## Running the program

This project assumes that pandas version 0.20.0 or above has been installed on your
system. To run the program, call the Python 3 interpreter:

```
python3 bikeshare.py
```

or, if you're in a UNIX-like environment, you can run the file directly:

```
./bikeshare.py
```

[1]: https://www.motivateco.com/
[2]: https://www.divvybikes.com/system-data
[3]: https://www.citibikenyc.com/system-data
[4]: https://www.capitalbikeshare.com/system-data
