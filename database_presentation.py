from tabulate import tabulate
import database_functions as dbf
import pandas as pd
import math
from preprocessing import *


def whole_look(df, from_index, to_index):
    print(tabulate(df.iloc[from_index:to_index], headers='keys', tablefmt='psql'))


def col_look(df, from_index, to_index, *columns):
    temp = df.copy()
    temp = temp.loc[:, list(columns)]
    print(tabulate(temp.iloc[from_index:to_index], headers='keys', tablefmt='psql'))


def match_cols(df, col1, col2):
    if dbf.true_val_col_count(df, col1) >= dbf.true_val_col_count(df, col2):
        col1_items = df[col1].unique()
        col2_items = df[col2].unique()
    else:
        col2_items = df[col1].unique()
        col1_items = df[col2].unique()

    print(col2_items)
    print(col1_items)
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
    print(tabulate(df, headers='keys', tablefmt='psql'))


def limited_match_cols(df, col1, col2):
    df_copy = df.copy()

    if dbf.true_val_col_count(df_copy, col1) >= dbf.true_val_col_count(df_copy, col2):
        col1_items = df_copy[col1].unique()
        col2_items = df_copy[col2].unique()
    else:
        col2_items = df_copy[col1].unique()
        col1_items = df_copy[col2].unique()
        col1, col2 = col2, col1

    comp_table = []
    group1 = math.ceil(len(col1_items) / 10)
    group2 = math.ceil(len(col2_items) / 10)
    step1 = 10
    step2 = 10

    for it1 in range(group1):
        for it2 in range(group2):

            for ii1 in col1_items[it1 * 10:it1 * 10 + step1]:
                for ii2 in col2_items[it2 * 10:it2 * 10 + step1]:
                    temp = []
                    temp.append(ii1)
                    temp.append(ii2)
                    result = df.query('{}=="{}" & {} == "{}"'.format(col1, ii1, col2, ii2))
                    temp.append(len(result))
                    comp_table.append(temp)

            df_copy = pd.DataFrame(comp_table)

            df_copy.rename(columns={0: col1, 1: col2, 2: 'count'}, inplace=True)
            df_copy = df_copy.pivot_table(index=col1, columns=col2, values="count", aggfunc="sum")
            print(tabulate(df_copy, headers='keys', tablefmt='psql'))
            comp_table.clear()
            del df_copy
            if (it2 == group2 - 1):
                step2 = len(col2_items) % step2
            input("press Enter ro continue")

        if (it1 == group1 - 1):
            step1 = len(col1_items) % step1


def single_data_presentation(df, col, value):
    data = df.loc[df[col] == value]
    print("there are *** {} *** results".format(len(data)))

    for i in range(len(data)):
        print(data.iloc[i])
        print("********************************")
        input("Next result click the Enter: ")


def loop_wholelook(df):
    i = 0
    for i in range(i, dbf.num_rows(df), 50):
        whole_look(df, i, i + 50)
        input("click Enter to show more\n")


def loop_collook(df, *columns, ):
    i = 0
    for i in range(i, dbf.num_rows(df), 50):
        col_look(df, i, i + 50, *columns)
        input("click Enter to show more\n")


def encode_values_present(df, col, dropORfillNan):
    if dropORfillNan:
        df.dropna(subset=[col], inplace=True)
    else:
        df[col].fillna("No Value", inplace=True)

    result = encode_values(df, col, dropORfillNan)

    categories = df[col]
    encodes = pd.DataFrame(result)

    en = encodes[0].unique()
    ca = categories.unique()

    for i in range(len(en)):
        print('{} == {}'.format(ca[i], en[i]))


def each_val_count_percent(df, col):
    all = dbf.num_rows(df)

    each_val = df[col].unique()

    for i in each_val:
        c = dbf.num_rows(df.loc[df[col] == i])
        p = dbf.num_rows(df.loc[df[col] == i]) / all
        print("{} : count = {} - percentage = {}".format(i, c, p))
