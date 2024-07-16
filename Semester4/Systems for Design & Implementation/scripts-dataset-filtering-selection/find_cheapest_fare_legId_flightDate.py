import pandas as pd


def find_cheapest_fares(input_csv_path, output_csv_path):
    # Load the dataset
    df = pd.read_csv(input_csv_path)

    # Convert 'flightDate' to datetime format for correct sorting
    df['flightDate'] = pd.to_datetime(df['flightDate'])

    # Group by 'legId' and 'flightDate', and then find the entry with the smallest 'baseFare' for each group
    cheapest_fares = df.loc[df.groupby(['legId', 'flightDate'])['baseFare'].idxmin()]

    # Now that we have the cheapest fares for each pair, sort these by 'flightDate'
    cheapest_fares_sorted = cheapest_fares.sort_values(by='flightDate')

    # Select only the required columns for the output
    cheapest_fares_output = cheapest_fares_sorted[['legId', 'flightDate', 'baseFare']]

    # Write the result to a new CSV file
    cheapest_fares_output.to_csv(output_csv_path, index=False)


# Adjust these paths to match your dataset and desired output location

csv_file_path = r"/AllJfkToMiamiSortedByLegId.csv"

output_file_path = "../cheapestPerLegId.csv"

find_cheapest_fares(csv_file_path, output_file_path)
