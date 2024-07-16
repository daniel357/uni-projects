import pandas as pd
from tqdm import tqdm


def fill_missing_distances_optimized_with_progress(input_file_path, output_file_path):
    """
    Fills missing totalTravelDistance values in the dataset by using non-missing values
    from the same group of segmentsArrivalAirportCode and segmentsDepartureAirportCode.
    Displays progress using tqdm.

    Parameters:
    - input_file_path: The file path to the input dataset (CSV format).
    - output_file_path: The file path where the updated dataset should be saved.

    Returns:
    - None. The function saves the updated DataFrame to the specified output file path.
    """

    df = pd.read_csv(input_file_path)

    df.sort_values(by=['segmentsArrivalAirportCode', 'segmentsDepartureAirportCode'], inplace=True)

    unique_pairs = df.groupby(['segmentsArrivalAirportCode', 'segmentsDepartureAirportCode']).size().shape[0]

    for (arrival_code, departure_code), group in tqdm(
            df.groupby(['segmentsArrivalAirportCode', 'segmentsDepartureAirportCode']), total=unique_pairs,
            desc="Filling distances"):
        if group['totalTravelDistance'].isna().any():
            non_missing_distance = group['totalTravelDistance'].dropna().unique()
            if non_missing_distance.size > 0:
                df.loc[(df['segmentsArrivalAirportCode'] == arrival_code) &
                       (df['segmentsDepartureAirportCode'] == departure_code), 'totalTravelDistance'] = \
                    non_missing_distance[0]

    df.to_csv(output_file_path, index=False)
