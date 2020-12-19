import PumMed as pm
import text_processing as txt
import preprocessing as pre
import dash
import dash_core_components as dcc
import dash_html_components as html

database = pre.db_finalization()


def get_subject_number(sub, num):
    my_test_pmids = pm.get_pmids(sub, num)
    data = []
    for i in my_test_pmids:
        paper_data = pm.get_paperinfo(i)
        score = txt.text_dic_evaluation(paper_data['alltxt'], database['dic_dentalimplant'])

        ui = html.Div(style={ 'border': '2px solid red' ,'border-radius': '5px'}, children=[
            "PMID and Title: {} | {}".format(paper_data['pmid'], paper_data['title']),
            "Similarity with 'Dental Implant' subjct: {}".format(score),
            "URL: {}".format(paper_data['url']),
        ])

        data.append(ui)

    return html.Div(data)
