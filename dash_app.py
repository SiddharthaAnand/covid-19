# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from moh_scraper import scrape_covid_data
import json
import pandas as pd
import plotly.express as px

state_data = scrape_covid_data()

with open('india_state.geojson') as response:
    states = json.load(response)

df = pd.DataFrame.from_dict(state_data, orient='index',
                            columns=['States', 'Total Confirmed (Indian)', 'Total Confirmed(foreign)', 'Cured',
                                     'Death'])

fig = px.choropleth(df, geojson=states, color='Total Confirmed (Indian)', locations ='States',
                    featureidkey='properties.NAME_1', projection='mercator')
fig.update_geos(fitbounds="locations", visible=False)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':

    app.run_server(debug=True)