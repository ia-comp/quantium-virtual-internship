# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

CSV_FILE = 'output.csv'

app = Dash()

df = pd.read_csv(CSV_FILE, parse_dates=['Date'])

fig = px.line(df, x="Date", y="Sales", title='Pink Morsel Sales')

app.layout = html.Div(children=[
    html.H1(children='Soul Origin Dashboard'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='pink-morsels-sales',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
