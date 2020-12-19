import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import my_colors as color
import preprocessing as pre
import database_functions as dbf
import pandas as pd
import plotly.express as px


database = pre.db_finalization()

layout_icij_user = html.Div(children=[

    dcc.Dropdown(
        id='charts-dropdown',
        options=[
            {'label': 'Word Map', 'value': 'wordmap'},
            {'label': 'Categories Percentage', 'value': 'category'},
            {'label': 'Risk Cahrt', 'value': 'riskchart'}
        ],
        value='wordmap'
    ),

    html.Div(id='dd-output-container')

])


def map_graph():
    devices = dbf.true_val_col(database['devices'], 'country')
    cnt = database['wiki_countries']

    country_counts = database['devices']['country'].value_counts(dropna=False).to_frame().reset_index()
    country_counts.rename(columns={'country': 'count', 'index': 'country'}, inplace=True)

    cnt.rename(columns={'English short name lower case': 'name', 'Alpha-3 code': 'country'}, inplace=True)

    print(cnt[['name', 'country']])
    country_counts = pd.merge(country_counts, cnt, on='country')

    Map = go.Figure(data=go.Choropleth(locations=country_counts['country'],
                                       z=country_counts['count'],
                                       text=country_counts['name'],
                                       colorscale='Blues'))
    Map.update_layout(
        title_text='Total MD events per country',
        height=600,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        )
        , )

    return html.Div([
        html.Div(id='Map-chart'),
        dcc.Graph(id='map', figure=Map),
        country_count_bar()

    ])


def country_count_bar():
    devices = dbf.true_val_col(database['devices'],'country')
    countries = devices['country'].unique()
    countries_count = []
    for c in countries:
        countries_count.append(dbf.count_exactvalue(database['devices'], 'country', c))
    Barchart = {
        'data': [
            {'x': countries,
             'y': countries_count,
             'type': 'bar', 'name': 'SF'},
        ],
        'layout': {
            'plot_bgcolor': color.colors['background'],
            'paper_bgcolor': color.colors['background'],
            'font': {
                'color': color.colors['text']
            }
        }
    }

    return html.Div(id='barchart_countries', children=[
        dcc.Graph(id='barchart_countries_chart', figure=Barchart)
    ])


def categories():
    ############# Categories Pie Chat
    data = dbf.true_val_col(database['devices'], 'classification')
    categories = data['classification'].unique()
    count = []
    for c in categories:
        count.append(dbf.num_rows(data.loc[data['classification'] == c]))

    fig_pie = go.Figure(data=[go.Pie(labels=categories, values=count)])

    ############# Risk Category Bar Chart
    df = dbf.match_cols(data , 'classification' , 'risk_class')
    fig_bar = px.bar(df, x=df.index, y=df.columns, title="Long-Form Input")
    fig_bar.update_layout(title_text='Percentage of MD among countries')


    return html.Div(id='categories_pie', children=[
        dcc.Graph(id='map', figure=fig_pie),
        dcc.Graph(id='graph_risk_class', figure=fig_bar)
    ])


def risk_charts():
    data = dbf.true_val_col(database['devices'], 'risk_class')
    classes = data['risk_class'].unique()
    count = []
    for c in classes:
        count.append(dbf.num_rows(data.loc[data['risk_class'] == c]))

    fig_pie = go.Figure(data=[go.Pie(labels=classes, values=count)])

    return html.Div(id='risk_pie', children=[
        dcc.Graph(id='risk_pie_chart', figure=fig_pie)
    ])