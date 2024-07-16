import pandas as pd


def extract_time_and_create_columns(input_file, output_file):
    """
    Reads a dataset from a CSV file, extracts hour and minute components from
    departure and arrival times, and adds these components as new columns.

    Parameters:
    - input_file: The file path to the input dataset (CSV format).
    - output_file: The file path where the updated dataset should be saved.

    Returns:
    - None. The function saves the updated DataFrame to the specified output file path.
    """

    df = pd.read_csv(input_file)

    departure_hour_list = []
    departure_minute_list = []
    arrival_hour_list = []
    arrival_minute_list = []

    for departure_time in df['segmentsDepartureTimeEpochSeconds']:
        first_time = departure_time.split('||')[0]
        converted_time = pd.to_datetime(int(first_time), unit='s')
        departure_hour_list.append(converted_time.hour)
        departure_minute_list.append(converted_time.minute)

    for arrival_time in df['segmentsArrivalTimeEpochSeconds']:
        last_time = arrival_time.split('||')[-1]
        converted_time = pd.to_datetime(int(last_time), unit='s')
        arrival_hour_list.append(converted_time.hour)
        arrival_minute_list.append(converted_time.minute)

    df['departureHour'] = departure_hour_list
    df['departureMinute'] = departure_minute_list
    df['arrivalHour'] = arrival_hour_list
    df['arrivalMinute'] = arrival_minute_list

    df.to_csv(output_file, index=False)
