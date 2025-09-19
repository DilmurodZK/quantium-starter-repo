from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("pink_morsel_sales.csv")
df = df.sort_values(by="date")
fig = px.line(df, x="date", y="sales", color="region", title='Pink Morsel Sales Over Time')

app.layout = html.Div(children=[
    html.H1(children='Soul Foods'),

    html.Div(children='''
        Pink Morsel Sales Over Time
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
