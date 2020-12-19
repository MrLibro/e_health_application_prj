import pandas as pd


def load_db(name: str, dbORdic):
    if dbORdic == 'database':
        pathfile = 'databases/' + name + '.csv'
    elif dbORdic == 'dictionary':
        pathfile = 'dictionaries/' + name + '.csv'
    file_db = pd.read_csv(pathfile, low_memory=False)
    return (file_db)
