import pandas as pd


def load_db(name: str, dbORdic):
    if dbORdic == 'database':
        pathfile = 'C:/Users/Mr. Libro/Desktop/Desktop/Python - My  Codes/E-Health/EHealthPtoject/git_edition_databases/databases/' + name + '.csv'
    elif dbORdic == "dictionary":
        pathfile = 'C:/Users/Mr. Libro/Desktop/Desktop/Python - My  Codes/E-Health/EHealthPtoject/git_edition_databases/dictionaries/' + name + '.csv'
    file_db = pd.read_csv(pathfile, low_memory=False)
    return (file_db)
