import pandas as pd


def compute_dynamic_best_time_to_purchase(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file, low_memory=False)

    # Convert 'searchDate' and 'flightDate' to datetime objects
    df['searchDate'] = pd.to_datetime(df['searchDate'])
    df['flightDate'] = pd.to_datetime(df['flightDate'])

    # Sort by 'legId' and then by 'searchDate' in descending order
    df.sort_values(by=['legId', 'searchDate'], ascending=[True, False], inplace=True)

    # Initialize the column for storing the best time to purchase as -1 (indicating not calculated/set yet)
    df['bestTimeToPurchase'] = -1

    # Iterate over each 'legId'
    for legId, group in df.groupby('legId'):
        # Track the cheapest fare seen so far and its corresponding search date
        cheapest_fare = float('inf')
        cheapest_fare_search_date = None

        for idx, row in group.iterrows():
            # Update the cheapest fare and its search date if a new lower fare is found
            if row['baseFare'] <= cheapest_fare or cheapest_fare_search_date is None:
                cheapest_fare = row['baseFare']
                cheapest_fare_search_date = row['searchDate']

            # Calculate the difference in days between the flight date and the search date of the cheapest fare found so far
            if cheapest_fare_search_date is not None:
                df.at[idx, 'bestTimeToPurchase'] = (row['flightDate'] - cheapest_fare_search_date).days

    # Write the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)


# Example usage
input_file = '../2_AllJfkToMiamiSortedByLegId_day_month_weekD_holidays_minutes_HourMinutes_Wcount_filterd_14.csv'
output_file = '../2_AllJfkToMiamiSortedByLegId_day_month_weekD_holidays_minutes_HourMinutes_Wcount_cheapest_filterd_14.csv'
compute_dynamic_best_time_to_purchase(input_file, output_file)
