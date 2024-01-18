import pandas as pd
import os

def dataframe_to_excel(df, filename='output.xlsx'):
    """
    Save a pandas DataFrame to an Excel file in a folder named 'excel_outputs' 
    in the current directory.

    Parameters:
    df (pd.DataFrame): The DataFrame to be saved as an Excel file.
    filename (str): The name of the Excel file to be saved.
    """
    # Define the directory name
    dir_name = "excel_outputs"

    # Create the directory if it doesn't exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Define the full path for the file
    file_path = os.path.join(dir_name, filename)

    try:
        # Save the DataFrame to an Excel file
        df.to_excel(file_path, index=False)

        print(f"File '{file_path}' saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")