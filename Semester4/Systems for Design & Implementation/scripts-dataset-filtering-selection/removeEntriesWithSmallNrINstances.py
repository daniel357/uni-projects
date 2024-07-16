import pandas as pd


def filter_dataset_by_search_instances(input_file, output_file, min_instances=5):
    """
    Reads a dataset, filters out rows with 'numberOfInstances' less than a specified minimum,
    and writes the filtered dataset to a new file.

    Parameters:
    - input_file (str): Path to the input CSV file.
    - output_file (str): Path where the filtered dataset will be saved.
    - min_instances (int): Minimum number of instances to include a row in the output. Default is 10.
    """

    # Load the dataset
    df = pd.read_csv(input_file, low_memory=False)

    # Filter the DataFrame
    filtered_df = df[df['numberOfInstances'] >= min_instances]

    # Save the filtered DataFrame to a new CSV file
    filtered_df.to_csv(output_file, index=False)


# Example usage
if __name__ == "__main__":
    input_file = '../ord_lax_sorted_wDaysBeforeDeparture_cheapestPerLogId_wDay_Month_wDayOfWeek_wHolidays.csv'
    output_file = '../ord_lax_sorted_wDaysBeforeDeparture_cheapestPerLogId_wDay_Month_wDayOfWeek_wHolidays_removedEntries.csv'

    filter_dataset_by_search_instances(input_file, output_file)
    print(f"Filtered dataset saved to {output_file}.")
