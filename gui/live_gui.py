from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import random
import datetime
import numpy as np

# Stores css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

app.layout = [
    html.Div([
        html.H4('Random live function plotting'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=500, # in milliseconds
            n_intervals=0
        )
    ])]

@callback(Output('live-update-text', 'children'),
          Input('interval-component', 'n_intervals'))
def update_metrics(n):
    return html.P("Sine wave from " + "   time:  " + str((datetime.datetime.today().timestamp() % 100)))

# This one is gonna hurt to read || It updates the graph
@callback(Output('live-update-graph', 'figure'),
          Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    # Create the graph with subplots
    start_time = int((datetime.datetime.today().timestamp() % 100 ))
    x = range(start_time, start_time+50)
    y = np.sin(x)
    fig = px.line(x=x,y=y)
    return fig

if __name__ == '__main__':
    app.run(debug=True)
    