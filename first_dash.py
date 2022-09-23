from distutils.log import debug
from gc import callbacks
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

app = Dash()

app.layout = html.Div(
    [html.H1('My first Dashboard'),
    dcc.RadioItems(id = 'radio_region', options = sorted(happiness['region'].unique()), value = 'Australia and New Zealand'),
    dcc.Dropdown(id = 'dropdown_country'),
    dcc.Dropdown(id = 'dropdown_value', options = {'happiness_score':'Happiness Score', 'happiness_rank':'Happiness Rank'}),
    dcc.Graph(id = 'display_graph')
    ]
)

@app.callback(
    Output('dropdown_country', 'options'),
    Output('dropdown_country', 'value'),
    Input('radio_region', 'value')
)

def update_dropdown(selected_region):
    happiness_filtered = happiness[happiness['region'] == selected_region]
    filtered_countries = sorted(happiness_filtered['country'].unique())
    return filtered_countries, filtered_countries[0]

@app.callback(
    Output('display_graph', 'figure'),
    Input('dropdown_country', 'value'),
    Input('dropdown_value', 'value')
)

def update_graph(selected_country, selected_value):
    happiness_filtered = happiness[happiness['country'] == selected_country]
    graph = px.line(happiness_filtered, x = 'year', y = selected_value)
    return graph


if __name__ == '__main__':
    app.run_server(debug=True)