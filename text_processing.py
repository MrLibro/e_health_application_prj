"""""""""""""""""""""""""""""""""""

In this file, we will implement the basic steps of text preprocessing.
These steps are needed for transferring text from human language to machine-readable format 
for further processing.
Text normalization includes:
    * converting all letters to lower or upper case
    * converting numbers into words or removing numbers
    * removing punctuations, accent marks and other diacritics
    * removing white spaces
    * expanding abbreviations
    * removing stop words, sparse terms, and particular words
    * text canonicalization

"""""""""""""""""""""""""""""""""""
import re
from nltk import pos_tag, ne_chunk, RegexpParser
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def txt_prepration(s: str):
  #  try:
    rmv_numbers = re.sub(r'\d+', '', s)  # removing digits
    low = rmv_numbers.lower()  # changed all uppercase letters to lower cases
    rmv_symbols = re.sub(r'[^\w]', ' ', low)  # removing symbols
    rmv_spaces = rmv_symbols.strip()  # removing Enter Spaces (White Spaces)

    stop_words = set(stopwords.words('english'))  # removing stop words
    tokens = word_tokenize(rmv_spaces)  #
    rmv_stops = [i for i in tokens if not i in stop_words]  #

    lemmatizer = WordNetLemmatizer()    # lemmatization = converting to simple form of words
    lem_str = []
    for word in rmv_stops:
        lem_str.append(lemmatizer.lemmatize(word))


    s = ' '.join(lem_str)   # Chunking (shallow parsing)
    tblob = TextBlob(s)
    tmp = list(str(tblob).split(" "))
    #print('value = {}\n' .format(result1))
    return tmp

def parse_tree(tokens):
    reg_exp = "NP: { < DT >? < JJ > * < NN >}"
    rp = RegexpParser(reg_exp)
    result = rp.parse(tokens)
    result.draw()

def database_txt_parsed(db):
    num =0
    device_name = db['name']
    device_description = db['description']
    parsed_name = []
    parsed_description = []

    for dn in device_name:
        num +=1
        parsed_name.append(txt_prepration(dn,num))

    for dn in device_description:
        num +=1
        parsed_description.append(txt_prepration(dn,num))

    return parsed_name, parsed_description

def tf_idf (list_of_strings):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(list_of_strings)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)
    return df

def text_dic_evaluation(txt, dic):
    prepared_txt = txt_prepration(txt)
    paper_score = 0
    words = dic.iloc[:,0]
    scors = dic.iloc[:,1]

    for w in range(len(words)):
        if words.iloc[w] in prepared_txt:
            paper_score += scors.iloc[w]
    return (paper_score)