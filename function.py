import pandas as pd
import numpy as np
import datetime as dt

def date_time_convertion(col):
    col = pd.to_datetime(col)
    min_col = col.min()
    for idx, value in enumerate(col):
        new_val = (value - min_col).total_seconds()
        col.iloc[idx] = new_val
    return col

def list_to_cols(df, col_name):
    max_len = df[col_name].str.len().max()
    new_columns = [f"{col_name}_{i+1}" for i in range(max_len)]
    split_cols = pd.DataFrame(df[col_name].tolist(), columns=new_columns)
    split_cols = split_cols.fillna(0)
    df = df.drop(columns=[col_name])
    return pd.concat([df, split_cols], axis=1)