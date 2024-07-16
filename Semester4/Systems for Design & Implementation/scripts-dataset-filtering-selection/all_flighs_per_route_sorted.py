import dask.dataframe as dd
from dask.diagnostics import ProgressBar
from dask import compute


def filter_and_sort_flights_dask(csv_file_path, output_file_path):
    # Define the criteria for filtering directly in the ISO format
    criteria_starting_airport = 'ORD'
    criteria_destination_airport = 'LAX'

    # Read the CSV using dask.dataframe, specifying dtype for columns that might have mixed types
    ddf = dd.read_csv(csv_file_path, parse_dates=['flightDate'],
                      dtype={'totalTravelDistance': 'float64'})

    # Filter the DataFrame according to the criteria
    filtered_ddf = ddf[(ddf['startingAirport'] == criteria_starting_airport) &
                       (ddf['destinationAirport'] == criteria_destination_airport)]

    # Sort the filtered DataFrame by 'legId' and then by 'flightDate'
    sorted_filtered_ddf = filtered_ddf.sort_values(by=['legId', 'flightDate'])

    # Use ProgressBar from dask.diagnostics for visual feedback
    with ProgressBar():
        # Compute the sorted, filtered dataframe and convert to pandas for saving
        sorted_filtered_df = sorted_filtered_ddf.compute()

    # Save the sorted and filtered dataframe to a CSV file
    sorted_filtered_df.to_csv(output_file_path, index=False)


csv_file_path = r"D:\User\flight-dataset\itineraries.csv"
output_file_path = '../ord_lax_sorted.csv'
filter_and_sort_flights_dask(csv_file_path, output_file_path)
