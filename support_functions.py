import pandas as pd

def read_csv_with_time(path, time_fields, n_rows=None, usecols=None):
    '''
      This function reads a csv and returns a dataframe considering only the first n_rows rows
      and transforming the indicated time_fields from timestamp(seconds) in datetime objects

      Arguments
      _________
        path: str
          The path where the file is located
        time_fields: List[str]
          A list of the fields to be converted in datetime
        n_rows: int
          The number of rows to be considered
        usecols: List[str]
          The list of the columns to be loaded      
      Returns
      _______
        a pandas dataframe containing the processed file
    '''
    
    return pd.read_csv(path, header='infer', nrows=n_rows, 
        parse_dates= [tf for tf in time_fields], date_parser=lambda x: pd.to_datetime(x, unit='s'), usecols=usecols)


def get_integer_ranges(ranges):
    return [(tuple(int(data) for data in x[0].split(':')), tuple(int(data) for data in x[1].split(':'))) for x in ranges]

def get_integer_range_index(tuple_hour, integer_ranges):
    
    for i in range(len(integer_ranges)):
        min_r, max_r = integer_ranges[i]
        if tuple_hour >= min_r and tuple_hour <= max_r:
            return i
    return -1