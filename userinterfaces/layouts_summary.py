import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import my_colors as color
import preprocessing as pre
import database_functions as dbf

database = pre.db_finalization()



layout_icij_summary = html.Div(children=[
    html.Div(id='row_datanases', children=[
        "whole Look of three Data Bases",
        dcc.Graph(
            id='Graph1',
            figure={
                'data': [
                    {'x': ['Devices', 'Events', 'Manufacturers'],
                     'y': [dbf.num_rows(database['devices']), dbf.num_rows(database['events']),
                           dbf.num_rows(database['manus'])],
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
        )
    ])

])

layout_icij_datamining = html.Div(children=["HI - datamining"])


