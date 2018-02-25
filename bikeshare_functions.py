#
#   bikeshare_functions.py - contains some functions for the main program.
#

def get_filter_options(validator_obj, city_names):
    '''
    Use a Validate object to get all of the filter options.
    '''
    filter_city = validator_obj.get_city_filter(city_names)
    filter_mode = validator_obj.get_filter_mode()
    filter_comp = validator_obj.get_filter_components()

    return [filter_city, filter_mode, filter_comp]

def calculate_stats(data_stats_obj, filter_options):
    '''
    Use a DataStats object to calculate all statistics
    '''
    # Get filter options and filter data
    filter_city, filter_mode, filter_comp = filter_options
    data_stats_obj.filter_data(filter_city, filter_mode)

    # Calculate stats
    pop_start_time = data_stats_obj.popular_start_time(filter_comp)
    popular_stations = data_stats_obj.popular_stations(filter_comp)
    popular_trip = data_stats_obj.popular_trip(filter_comp)
    trip_duration = data_stats_obj.trip_duration(filter_comp)
    counts_user = data_stats_obj.counts_user(filter_comp)
    counts_gender = data_stats_obj.counts_gender(filter_comp)
    birth_years = data_stats_obj.birth_years(filter_comp)

    # Compile all stats into a list
    all_stats = [pop_start_time,
                 popular_stations,
                 popular_trip,
                 trip_duration,
                 counts_user,
                 counts_gender,
                 birth_years]

    return all_stats

def display_stats(pprint_obj, filter_options, all_stats):
    '''
    Use a PrettyPrint object to display all calculated stats.
    '''
    # Get stats and filter options
    p_start, p_stations, p_trip, trip_dur, counts_u, counts_g, birth = all_stats
    filter_city, filter_mode, filter_comp = filter_options

    # Set filter options and print main header
    pprint_obj.get_filter_options(filter_city, filter_mode, filter_comp)
    pprint_obj.main_header()

    # Print all stats
    pprint_obj.show_start_time_stats(p_start)
    pprint_obj.show_stations_stats(p_stations)
    pprint_obj.show_trip_stats(p_trip)
    pprint_obj.show_trip_duration_stats(trip_dur)
    pprint_obj.show_user_count_stats(counts_u)
    pprint_obj.show_gender_count_stats(counts_g)
    pprint_obj.show_birth_year_stats(birth)
