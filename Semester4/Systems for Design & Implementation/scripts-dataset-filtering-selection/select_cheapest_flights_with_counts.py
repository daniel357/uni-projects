import dask.dataframe as dd
from dask.diagnostics import ProgressBar


def parse_dates(ddf, date_columns):
    """
    Parses date columns in the DataFrame to datetime format.

    Parameters:
    - ddf: The Dask DataFrame.
    - date_columns: A list of date column names to be parsed.

    Returns:
    - The Dask DataFrame with parsed date columns.
    """
    for date_column in date_columns:
        ddf[date_column] = dd.to_datetime(ddf[date_column], format='%m/%d/%Y')
    return ddf


def select_cheapest_flights_with_counts(csv_file_path, output_file_path):
    """
    Selects the cheapest flights and counts the number of entries for each 'legId',
    then saves the updated DataFrame to a new file.

    Parameters:
    - csv_file_path: The file path to the input dataset (CSV format).
    - output_file_path: The file path where the updated dataset should be saved.

    Returns:
    - None. The function saves the updated DataFrame to the specified output file path.
    """
    dtype = {
        'segmentsArrivalTimeEpochSeconds': 'object',
        'segmentsDepartureTimeEpochSeconds': 'object',
        'segmentsDistance': 'object',
        'segmentsDurationInSeconds': 'object',
        'totalTravelDistance': 'float64'
    }

    ddf = dd.read_csv(csv_file_path, dtype=dtype)
    date_columns = ['searchDate', 'flightDate']
    ddf = parse_dates(ddf, date_columns)

    with ProgressBar():
        numberOfEntries = ddf.groupby(['legId']).size().compute().reset_index(name='numberOfEntries')
        idxmin = ddf.groupby(['legId'])['totalFare'].idxmin().compute()
        pdf = ddf.compute()
        cheapest_flights = pdf.loc[idxmin]
        cheapest_flights_with_counts = cheapest_flights.merge(numberOfEntries, on=['legId'], how='left')
        cheapest_flights_sorted = cheapest_flights_with_counts.sort_values(by=['legId'])
        cheapest_flights_sorted.to_csv(output_file_path, index=False)
