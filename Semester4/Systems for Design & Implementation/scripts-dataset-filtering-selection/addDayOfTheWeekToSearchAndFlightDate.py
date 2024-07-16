import pandas as pd


def add_day_of_week_and_save(input_csv_path, output_csv_path):
    """
    Reads a dataset from a CSV file, adds columns for the day of the week for both
    searchDate and flightDate, and saves the updated DataFrame to a new CSV file.

    Parameters:
    - input_csv_path: The file path to the input dataset (CSV format).
    - output_csv_path: The file path where the updated dataset should be saved.

    Returns:
    - None. The function saves the updated DataFrame to the specified output file path.
    """

    df = pd.read_csv(input_csv_path, low_memory=False)

    df['searchDate'] = pd.to_datetime(df['searchDate'])
    df['flightDate'] = pd.to_datetime(df['flightDate'])

    df['searchDayOfWeek'] = df['searchDate'].dt.dayofweek
    df['flightDayOfWeek'] = df['flightDate'].dt.dayofweek

    df.to_csv(output_csv_path, index=False)