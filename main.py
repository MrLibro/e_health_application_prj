import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

##########  import other pages  ##########
import userinterfaces.layouts_general as ly
import userinterfaces.layouts_summary as ly_sum
import userinterfaces.layouts_icij_user as ly_icij_user
import userinterfaces.layout_pubmed_summary as ly_sum_pubmed
import userinterfaces.layout_pubmed_user as ly_user_pubmed
import userinterfaces.medicalsubject_lookup as medlook
import preprocessing as pre
import database_presentation as dbp
import database_functions as dbf


##########  Initialization  ###########

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

##########  UI & Layouts  ##########

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = ly.url_bar_and_content_div

# "complete" layout
app.validation_layout = html.Div([
    ly.url_bar_and_content_div,
    ly.layout_index,
    ly.layout_ICIJ,
    ly.layout_Pubmed,
])




##########  Load Databases and Dictionaries  ##########



##########  callbacks  ############

# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/medicaldevices":
        return ly.layout_ICIJ
    elif pathname == "/pubmed":
        return ly.layout_Pubmed
    else:
        return ly.layout_index


# ICIJ callbacks
@app.callback(Output('output-state', 'children'),
              Input('summary_icij', 'n_clicks'),
              Input('datamining_icij', 'n_clicks'),
              Input('user_analysis_icij', 'n_clicks'))
def update_output(n_clicks, input1, input2):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'summary_icij' in changed_id:
        msg = ly_sum.layout_icij_summary
    elif 'datamining_icij' in changed_id:
        msg = ly_sum.layout_icij_datamining
    elif 'user_analysis_icij' in changed_id:
        msg = ly_icij_user.layout_icij_user
    else:
        msg = 'None of the buttons have been clicked yet'
    return msg


# PubMed callbacks
@app.callback(Output('output-pubmed', 'children'),
              Input('summary_pubmed', 'n_clicks'),
              Input('user_analysis_pubmed', 'n_clicks'))
def update_output( input1, input2):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'summary_pubmed' in changed_id:
        msg = "sssssssssssssssssss"
    elif 'user_analysis_pubmed' in changed_id:
        msg = ly_user_pubmed.layout_subject_number
    else:
        msg = 'None of the buttons have been clicked yet'
    return msg

# icij user analysis dropdown
@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('charts-dropdown', 'value')])
def update_output(value):
    if value == 'wordmap':
        result = ly_icij_user.map_graph()
    elif value == 'category':
        result = ly_icij_user.categories()
    else:
        result = ly_icij_user.risk_charts()
    return result

# textbox pubmed lookup result
@app.callback(
    Output("lookup_result", "children"),
    Input("medical_subject", "value"),
    Input("numberOfPapers", "value"),
    Input("show_result_btn", "n_clicks"),
)
def update_output(input1, input2, input3):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if "show_result_btn" in changed_id:
        msg = medlook.get_subject_number(input1,input2)
        return msg

##########  Run Server ###########

if __name__ == '__main__':
    app.run_server(debug=True)
