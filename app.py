# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

CSV_FILE = 'output.csv'
region_colour_map = {
    "north": "royalblue",
    "south": "firebrick",
    "east": "forestgreen",
    "west": "purple"
}
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(CSV_FILE, parse_dates=['Date'])

app.layout = html.Div(children=[
    html.H1(children='Soul Origin Dashboard'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='pink-morsels-sales',
    ),

    dcc.RadioItems(
        id='region-radio',
        options=df.Region.unique(),
        value=df.Region.unique()[0]
    )

])

@app.callback(
    Output('pink-morsels-sales', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(selected_region):
    # Filter data based on radio selection
    filtered_df = df[df['Region'] == selected_region]
    
    # Create line graph with only the selected data
    fig = px.line(
        filtered_df, 
        x='Date', 
        y='Sales', 
        color='Region', 
        color_discrete_map=region_colour_map, 
        title=f'Pink Morsel Sales'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)
