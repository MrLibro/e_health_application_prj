import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import my_colors as color
import preprocessing as pre
import database_functions as dbf

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([
    dcc.Link('ICIJ - Medical Devices', href='/medicaldevices'),
    html.Br(),
    dcc.Link('PubMed', href='/pubmed'),
])

layout_ICIJ = html.Div([
    html.H2('ICIJ Medical Devices'),
    html.Button(id='summary_icij', n_clicks=0, children='Database Summary'),
    html.Button(id='datamining_icij', n_clicks=0, children='Data Mining Results'),
    html.Button(id='user_analysis_icij', n_clicks=0, children='Go To Analysis'),

    html.Div(id='output-state'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/pubmed"', href='/pubmed'),
])

layout_Pubmed = html.Div([
    html.H2('ICIJ Medical Devices'),
    html.Button(id='summary_pubmed', n_clicks=0, children='Dental Implant Summary'),
    html.Button(id='user_analysis_pubmed', n_clicks=0, children='Go To Discover'),

    html.Div(id='output-pubmed'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/medicaldevices"', href='/medicaldevices'),
])