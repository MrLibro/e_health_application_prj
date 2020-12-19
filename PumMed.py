import urllib.request
from bs4 import BeautifulSoup
import re


def create_dic(file_name):
    with open(file_name, 'r') as fp:
        cardioDictionary = fp.readlines()

    dic = []

    for el in cardioDictionary:
        tmp = el.split('|')
        tmp = tmp[1]
        tmp = re.sub('\n', '', tmp)
        dic.append(tmp)

    return dic


def get_paperinfo(pmid):
    base_url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    fetch = 'efetch.fcgi?db=pubmed&id=' + pmid + '&retmode=xml'
    url = base_url + fetch
    query_result = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(query_result, 'html.parser')

    data = {}

    try:
        xml_abstract = soup.abstract
        txt_abstrct = xml_abstract.get_text()
    except:
        txt_abstrct = ''
    try:
        xml_title = soup.articletitle
        txt_title = xml_title.get_text()
    except:
        txt_title = ''
    try:
        xml_keywords = soup.keywordlist
        txt_keywords = xml_keywords.get_text()
    except:
        txt_keywords = ''

    data['url'] = url
    data['pmid'] = pmid
    data['abstract'] = txt_abstrct
    data['title'] = txt_title
    data['keywords'] = txt_keywords
    data['alltxt'] = txt_title + txt_abstrct + txt_keywords
    return data


def get_score(self, dic):
    count_list = {}
    count = 0
    for term in dic:
        expr = r'\b' + fr"{term}" + r'\b'
        tmp = re.findall(term, self.abstract, flags=re.IGNORECASE)
        if len(tmp) != 0:
            count += len(tmp)
            count_term = len(tmp)
            count_list[tmp[0]] = count_term
            count_term = 0
    return count, count_list


def get_pmids(query, num_of_pmids):
    base_url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    fetch_1 = 'esearch.fcgi?db=pubmed&term='
    fetch_2 = '&retmode=xml&RetMax=' + str(num_of_pmids)

    final_query = ''
    query_list = query.split(' ')
    for w in query_list:
        final_query += w
        if w != query_list[-1]:
            final_query += '+'

    url = base_url + fetch_1 + final_query + fetch_2
    query_result = urllib.request.urlopen(url).read()
    regex_res = re.findall('<Id>.*?</Id>', str(query_result))

    output = []
    for id in regex_res:
        tem = re.sub('<.*?>', '', id)
        output.append(tem)
    return output
