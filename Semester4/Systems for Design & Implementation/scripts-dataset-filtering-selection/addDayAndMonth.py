import pandas as pd


def add_date_components_and_save(dataset_path, output_path=None):
    """
    Adds searchDay, searchMonth, flightDay, and flightMonth columns to the dataset
    and saves the updated DataFrame to a new file.

    Parameters:
    - dataset_path: The file path to the dataset (CSV format).
    - output_path: The file path where the updated dataset should be saved. If not specified,
                   the original dataset will be overwritten.

    Returns:
    - None. The function saves the updated DataFrame to the specified output file path.
    """

    df = pd.read_csv(dataset_path, low_memory=False)

    df['searchDate'] = pd.to_datetime(df['searchDate'])
    df['flightDate'] = pd.to_datetime(df['flightDate'])

    df['searchDay'] = df['searchDate'].dt.day
    df['searchMonth'] = df['searchDate'].dt.month

    df['flightDay'] = df['flightDate'].dt.day
    df['flightMonth'] = df['flightDate'].dt.month

    if output_path is None:
        output_path = dataset_path

    df.to_csv(output_path, index=False)