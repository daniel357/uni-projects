import dask.dataframe as dd
from dask.diagnostics import ProgressBar
from dask import compute


def filter_and_sort_flights_dask(csv_file_path, output_file_path):
    """
    This function filters and sorts flight data from a CSV file using Dask.
    It filters flights that start from 'ORD' and end at 'LAX',
    then sorts the filtered data by 'legId' and 'flightDate',
    and finally saves the sorted and filtered data to a new CSV file.
    """
    criteria_starting_airport = 'ORD'
    criteria_destination_airport = 'LAX'

    ddf = dd.read_csv(csv_file_path, parse_dates=['flightDate'],
                      dtype={'totalTravelDistance': 'float64'})

    filtered_ddf = ddf[(ddf['startingAirport'] == criteria_starting_airport) &
                       (ddf['destinationAirport'] == criteria_destination_airport)]

    sorted_filtered_ddf = filtered_ddf.sort_values(by=['legId', 'flightDate'])

    with ProgressBar():
        sorted_filtered_df = sorted_filtered_ddf.compute()

    sorted_filtered_df.to_csv(output_file_path, index=False)
