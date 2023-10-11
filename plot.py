from dash import Dash, html, dcc, callback, Output, Input,State
import plotly.express as px
import pandas as pd

data = pd.read_csv('women_clothing_ecommerce_sales.csv')

data["order_date"]=pd.to_datetime(data["order_date"])
data['date']=data['order_date'].dt.strftime('%Y-%m-%d')
data['time']=data['order_date'].dt.time

def map_time(time):
    if (time.hour >= 7) and (time.hour < 13):
        return "morning"
    elif (time.hour >= 13) and (time.hour < 19):
        return "afternoon"
    else:
        return "evening"
data['time']=data['time'].apply(map_time)
data['hour']=data['order_date'].dt.hour




## visualize
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Bảng phân tích đôí thủ về thị trường quần áo',style={'textAlign':'center','color':'blue'}),
    html.Div([
        html.Div([
            html.H1(children='Title of Dash App', style={'textAlign':'center'}),
            dcc.Graph( id='controls-and-graph'),
            dcc.Slider(
                data['hour'].min(),
                data['hour'].max(),
                step=None,
                value=data['hour'].min(),
                marks={str(hour):f'{hour}h' for hour in data['hour'].unique()},
                id='test_new',
                vertical=False
            ),
        ],style={'display': 'inline-block', 'width': '50%'}),
        
        html.Div([
            html.H1(children='Title of Dash App', style={'textAlign':'center'}),
            dcc.Graph( id='controls-and-graph2'),
            dcc.Slider(
                data['hour'].min(),
                data['hour'].max(),
                step=None,
                value=data['hour'].min(),
                marks={str(hour):f'{hour}h' for hour in data['hour'].unique()},
                id='test_new_2',
                vertical=False
            ),
        ],style={'display': 'inline-block', 'width': '50%'}),
    ]),
    html.Div([
        html.H1(children='Thật là cảm ơn vì đó là beautifull day',style={'textAlign':'center'}),
        html.Div([
            html.H3('Giá trị hiển thị',style={'textAlign':'center'}),
            dcc.RadioItems(
                options=data['time'].unique(),
                value=data['time'].unique()[0],
                id='value-radio',
                style={'display': 'inline-block','vertical-align': 'top'}
            ),
            html.H2(
                id = 'output-value',
                style={'text-align': 'center','display': 'inline-block','vertical-align': 'top'}
            ),
        ],style={'width': '400px', 'height': '100px'}),
    ])
    
])


## Show value
@callback(
    Output('output-value', 'children'),
    [Input('value-radio', 'value')]
)
def update_value(value):
    data_uv = data[data['time']==value]['revenue'].sum()
    return f'{data_uv} USD'



@callback(
    Output('controls-and-graph2', 'figure'),
    Input('test_new_2', 'value'),
)
def update_graph(value):
    data_hour=data[data['hour']==value]
    fig=px.histogram(data_hour,x='sku',y='revenue',title='biểu đồ thể hiện tổng thu nhập từng loại hàng theo giờ',histfunc='sum',text_auto=True)
    fig.update_traces(textfont_size = 14, textangle = 0, textposition = "outside")
    fig.update_layout(
        margin=dict(l=20, r=40, t=30, b=10),
        paper_bgcolor="LightSteelBlue",
        title = {
            'text': 'hello',
            'x': 0.5,
            'y': 0.98
        }
    )
    return fig




@callback(
    Output('controls-and-graph', 'figure'),
    Input('test_new', 'value'),
)
def update_graph(value):
    data_hour=data[data['hour']==value]
    fig=px.histogram(data_hour,x='sku',y='revenue',title='biểu đồ thể hiện tổng thu nhập từng loại hàng theo giờ',histfunc='sum',text_auto=True)
    fig.update_traces(textfont_size = 14, textangle = 0, textposition = "outside")
    fig.update_layout(
        margin=dict(l=20, r=40, t=30, b=10),
        paper_bgcolor="LightSteelBlue",
        title = {
            'text': 'hello',
            'x': 0.5,
            'y': 0.98
        }
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)