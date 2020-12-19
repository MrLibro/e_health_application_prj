"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
providing functionalities on our Dataframes:
    1- num_rows: calculating the number of rows in our Dataframe   
        input: Dataframe
        output: the number of rows
    2- num_cols: calculating the number of columns in our Dataframe 
        input: Dataframe
        output: the number of rows
    3- num_null_col: number of null values in a exact column
        input: 1- Dataframe 2- name of column (str)
        output: number of null values in a column (int)
    4- 
    6- true_val_col: considers only data which have value according to input column 
        input: 1- Dataframe 2- name of column (str)
        output: edited Dataframe whose result is the data with only true value according to input column  

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import pandas as pd
import random
from database_presentation import *


def num_rows(dataframe): return len(dataframe.index)


def num_cols(dataframe): return len(dataframe.columns)


def num_null_col(dataframe, col_name):
    num_of_null = dataframe.index.size - true_val_col_count(dataframe, col_name)
    return num_of_null


def perc_true_col(dataframe, col_name):
    return true_val_col_count(dataframe, col_name) / num_rows(dataframe) * 100


def perc_exactvalue(df, col_name, val):
    val_count = df[col_name].value_counts(dropna=False)
    return val_count[val] / num_rows(df) * 100

def count_exactvalue(df, col_name, val):
    val_count = df[col_name].value_counts(dropna=False)
    return val_count[val]

def true_val_col(dataframe, col_name, *more):
    df = dataframe.copy()
    df.dropna(subset=[col_name], inplace=True)
    for c in more:
        df.dropna(subset=[c], inplace=True)
    return df


def true_val_col_count(dataframe, col_name, *more):
    df = dataframe.copy()
    df.dropna(subset=[col_name], inplace=True)
    for c in more:
        df.dropna(subset=[c], inplace=True)
    return df.index.size


def match_cols(df, col1, col2):
    if true_val_col_count(df, col1) >= true_val_col_count(df, col2):
        col1_items = df[col1].unique()
        col2_items = df[col2].unique()
    else:
        col2_items = df[col1].unique()
        col1_items = df[col2].unique()

    comp_table = []

    for i1 in col1_items:

        match = 0
        for i2 in col2_items:
            temp = []
            temp.append(i1)
            temp.append(i2)
            result = df.query('{}=="{}" & {} == "{}"'.format(col1, i1, col2, i2))
            temp.append(len(result))
            comp_table.append(temp)

    df = pd.DataFrame(comp_table)
    df.rename(columns={0: 'classification', 1: 'risk_class', 2: 'count'}, inplace=True)
    df = df.pivot_table(index="classification", columns="risk_class", values="count", aggfunc="sum")
    return df


def random_remove(df, col, val, num):
    df = shuffle_dataframe(df)
    df = df.drop(df.loc[df[col] == val].index[0:num])
    return df


def shuffle_dataframe(df):
    df = df.sample(frac=1).reset_index(drop= True)
    return df


def find_None_except (df , filled_col , empty_col):

    df = dbf.true_val_col(df, filled_col)
    bool_series = pd.isnull(df[empty_col])
    return df[bool_series]