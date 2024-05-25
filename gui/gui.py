from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

daily_data = pd.read_csv('DailyDelhiClimateTest.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

app.layout = [
    html.Div(className='row', children='Daily Delhi Climate Test Data',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    html.Div(className='row', children='Source: https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data?resource=download',
            style={'textAlign': 'center', 'color': 'blue', 'fontSize': 20}),

    html.Div(className='row', children=[
        dcc.RadioItems(options=['meantemp', 'humidity', 'wind_speed', 'meanpressure'],
                       value='meantemp',
                       inline=True,
                       id='my-radio-buttons-final')
    ]),

    html.Div(className='row', children=[
        html.Div(className='line-chart', children=[
            dcc.Graph(figure={}, id='line-chart-final')
        ])
    ])
]

@callback(
    Output(component_id='line-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(daily_data, x='date', y=col_chosen)
    return fig

if __name__ == '__main__':
    app.run(debug=True)