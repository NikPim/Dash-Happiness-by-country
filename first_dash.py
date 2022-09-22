from distutils.log import debug
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

app = Dash()

app.layout = html.Div(
    [html.H1('My first Dashboard'),
    dcc.Dropdown(id = 'dropdown_country', options = sorted(happiness['country'].unique())),
    dcc.Dropdown(id = 'dropdown_value', options = {'happiness_score':'Happiness Score', 'happiness_rank':'Happiness Rank'}),
    dcc.Graph(id = 'display_graph')
    ]
)

@app.callback(
    Output('display_graph', 'figure'),
    Input('dropdown_country', 'value'),
    Input('dropdown_value', 'value'),
)
def update_graph(selected_country, selected_value):
    happiness_filtered = happiness[happiness['country'] == selected_country]
    graph = px.line(happiness_filtered, x = 'year', y = selected_value)
    return graph


if __name__ == '__main__':
    app.run_server(debug=True)