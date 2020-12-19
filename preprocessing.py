from sklearn import preprocessing
import load as ld
import datetime


def risk_normalization(df):
    df['risk_class'].replace({"II": "2"}, inplace=True)
    df['risk_class'].replace({"Unclassified": "Not Classified"}, inplace=True)
    return df


def encode_values(df, col, dropORfillNan):
    if dropORfillNan:
        df.dropna(subset=[col], inplace=True)
    else:
        df[col].fillna("No Value", inplace=True)
    le = preprocessing.LabelEncoder()
    encode_result = le.fit_transform(df[col])

    return list(encode_result)


def encoded_data(df, dropORfillNan, *col):
    cols = []
    for c in col:
        cols.append(encode_values(df, c, dropORfillNan))
    return cols


def zip_features(cols):
    features = list(zip(*cols))
    return features


def encodeable_date_feature(df, col_date, name):
    data = df[col_date]
    year = []
    month = []
    day = []

    for d in range(len(data)):
        try:
            data_dateformat = datetime.datetime.strptime(str(data.iloc[d]), '%Y-%m-%d')
            year.append(data_dateformat.year)
            month.append(data_dateformat.month)
            day.append(data_dateformat.day)
        except ValueError:
            print('Value not date')

    df = df.drop(columns=[col_date])
    df["y_" + name] = year
    df["m_" + name] = month
    df["d_" + name] = day

    return df

"""""
def database_loader(name, ):
    database = {}
    devices = ld.load_db('devices', 'database')
    events = ld.load_db('events', 'database')
    manus = ld.load_db('manufacturers', 'database')
    wiki_countries = ld.load_db('wikipedia-iso-country-codes', 'dictionary')
    countries = ld.load_db('countries', 'dictionary')
    train_dentalimplant = ld.load_db('train_dentalimplant_papers', 'database')
    dic_dentalimplant = ld.load_db('pubmed_dentalimplant', 'dictionary')
    final_database = ld.load_db('final_database','database')

    devices = risk_normalization(devices)

    database['train_dentalimplant']  = train_dentalimplant
    database['dic_dentalimplant'] = dic_dentalimplant
    database['devices'] = devices
    database['events'] = events
    database['manus'] = manus
    database['wiki_countries'] = wiki_countries
    database['countries'] = countries
    database['final_database'] = final_database
    return database
"""""