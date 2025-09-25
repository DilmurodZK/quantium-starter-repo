from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("pink_morsel_sales.csv")
df = df.sort_values(by="date")

regions = df['region'].unique()
region_options = [{'label': 'All regions', 'value': 'all'}] + \
                 [{'label': region.title(), 'value': region} for region in regions]

app.layout = html.Div([
    html.H1('Soul Foods', id='header'),

    html.Div('Pink Morsel Sales', className='description'),

    html.Div([
        dcc.RadioItems(
            id='region-selector',
            options=region_options,
            value='all',
            labelStyle={'display': 'inline-block'}
        )
    ], className='radio-group'),

    html.Div([
        dcc.Graph(id='sales-linechart')
    ], className='graph-container')
])

@app.callback(
    Output('sales-linechart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        fig = px.line(df, x='date', y='sales', color='region',
                      title='All regions')
    else:
        filtered_df = df[df['region'] == selected_region]
        fig = px.line(filtered_df, x='date', y='sales',
                      title=f"{selected_region.title()} region")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run(debug=True)