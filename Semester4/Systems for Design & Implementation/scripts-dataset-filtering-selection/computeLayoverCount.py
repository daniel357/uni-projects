import pandas as pd


def add_layover_count_and_save(dataset_path, output_path=None):
    """
    Adds layoverCount column to the dataset based on segmentsDurationInSeconds
    and saves the updated DataFrame to a new file.

    Parameters:
    - dataset_path: The file path to the dataset (CSV format).
    - output_path: The file path where the updated dataset should be saved. If not specified,
                   the original dataset will be overwritten.

    Returns:
    - None. The function saves the updated DataFrame to the specified output file path.
    """

    df = pd.read_csv(dataset_path, low_memory=False)

    df['layoverCount'] = df['segmentsDurationInSeconds'].apply(lambda x: len(x.split('||')))

    if output_path is None:
        output_path = dataset_path

    df.to_csv(output_path, index=False)
