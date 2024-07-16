import pandas as pd

def filter_legId_by_count(input_file, output_file, min_count):
    """
    This function filters a dataset to retain only the rows where the 'legId'
    occurs at least a specified number of times. The filtered dataset is then
    saved to a new CSV file.
    """
    df = pd.read_csv(input_file, low_memory=False)

    legId_counts = df['legId'].value_counts()

    legIds_to_keep = legId_counts[legId_counts >= min_count].index

    filtered_df = df[df['legId'].isin(legIds_to_keep)]

    filtered_df.to_csv(output_file, index=False)
