import dash_bootstrap_components as dbc
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

#####

arrLondonYear = np.arange(2020, 2031, 1)
arrLondonPop =[9121350.691892669, 9211390.568916265, 9298979.218267485, 9384393.558697384, 9467486.974674778, 9548200.151854068, 9626818.379661608, 9703526.175359873, 9778659.788864529, 9852408.59922965, 9924970.290989427]
# London_10_year_fig = px.line( x=arrLondonYear, y=arrLondonPop,title='Population of London 10 years later')

#####

main = html.Div([
    # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div('Home page', style={
        'fontSize': '50px',
        'color': 'white',
        'textAlign': 'center'
    }),
    # link to another page
    html.Div([
        dcc.Link('Simple Chart', href='/simple-chart', style={
             'color': '#f5f5f5'
             }),
        dcc.Link('Data Analysis', href='/data-analysis', style={
            'color': '#f5f5f5'
        })
    ], style={
        'display': 'flex',
        'justify-content': 'space-evenly',

    }, className='mt-4'),

    # introduce tag
    html.Div([
        html.Div([
            html.Div('Giới thiệu về project: ', style={
                'fontSize': '25px',
                'fontWeight': 'bold',
            }),
            html.Div([
                html.Div( [
                    html.Div('- London population prediction (Dự đoán dân số london): nghiên cứu và dự đoán về sự gia tăng dân số của thành phố London (Anh - UK) cùng các vấn đề về dân số liên quan khác trong tương lai gần.'),
                    html.Div('- Project này sử dụng Framework Dash - Plotly để xây dựng và dữ liệu được lấy từ trang data.world để phân tích')
                ],className='col-8'),
                html.Img(src='./assets/pop.jpg', className='col-4')

            ], className='row', style={ 'fontSize': '15px' })
        ])
    ], className='mt-5 bg-light intro'),
     html.Div([
        html.Div([
            html.Div('About my team:', style={
                'fontSize': '25px',
                'fontWeight': 'bold',
            }),
            html.Div([
                html.Img(src='./assets/team.jpg', className='col-4'),
                html.Div([
                html.Div('18081331 - Nguyễn Công Thành Đạt'),
                html.Div('18089811 - Mai kiên cường'),
                html.Div('18084791 - Trương Công Cường'),
                html.Div('18079251 - Đỗ Tùng Dương'),   
                ],className='col-4 team'),
                 html.Div( [
                html.Div('18092791 - Hoàng Hữu Huy'),
                html.Div('18084851 - Châu Quốc An'),
                html.Div('18072661 - Lại Văn Vượng')       
                ],className='col-4'),
            ], className='row', style={ 'fontSize': '15px' })
        ])
    ], className='mt-5 bg-light intro'),

    #my team
    # background
], className='container mt-5')

##-----------------------------------------------------
#Simple Chart Link
simpleChart = html.Div([
     html.Div(style={
        'width': '100%',
        'height': '100%',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'z-index': '-999'
    }, className='bg-dark'),
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Dash - plotly', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Giới thiệu về Dash - Plotly:', className='introMatplotlib'),
                html.Span('Dash là một framework mã nguồn mở dành cho xây dựng ứng dụng phân tích dữ liệu mà không cần đến Ngôn ngữ JavaScript, và nó được tích hợp với thi viện Plotly - một thư viện đồ họa. ',className='content')
            ])
           
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##-----------------------------------------------------

df = pd.DataFrame({'PDD': ['Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop',
                                 'Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth',
                                'Death','Death','Death','Death','Death','Death','Death','Death','Death','Death','Death'],
                   'Units': [9121350.692, 9211390.569,9298979.218,9384393.559,9467486.975,9548200.152,9626818.38,9703526.175,9778659.789,9852408.599,9924970.291,
                            127533.3476,127885.153,128324.9541,128801.6843,129233.04,129600.5457,129961.0983,130317.1128,130663.6129,131047.3682,131487.2486,
                            51176.87663,51135.29448,51177.02141,51294.318,51485.16367,51803.97713,52212.18212,52673.59493,53184.19643,53741.82139,54315.44647
],
                   'Year':[2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,
                             2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,
                             2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,]})

groups = df.groupby(by='PDD')

data = []
colors=['red', 'blue', 'green']

for group, dataframe in groups:
    dataframe = dataframe.sort_values(by=['Year'])
    trace = go.Scatter(x=dataframe.Year.tolist(), 
                       y=dataframe.Units.tolist(),
                       marker=dict(color=colors[len(data)]),
                       name=group)
    data.append(trace)

layout =  go.Layout(xaxis={'title': 'Year'},
                    yaxis={'title': 'Population'},
                    margin={'l': 40, 'b': 40, 't': 50, 'r': 50},
                    hovermode='closest')

lineChartType2 = go.Figure(data=data, layout=layout)  

##-----------------------------------------------------
# Line Chart Link
lineChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                  dcc.Link('Dot Chart', href="/dot-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Line Chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Đây là dạng biểu đồ để thể hiện tiến trình phát triển, động thái phát triển của một đối tượng hay một nhóm đối tượng nào đó qua thời gian. Vì vậy với các bài vẽ biểu đồ đường thường có các cụm từ thể hiện sự phát triển, tốc độ tăng trưởng… với các mốc thời gian nhất định. ',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Line chart (biểu đồ đường): được sử dụng khi dữ liệu được mô tả phụ thuộc vào thời gian với trục hoành biểu diễn thời gian và trục tung biểu diễn đại lượng.',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib')
            ]),
             html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= {
                        'data' : [
                            { 'x': ['Sutton', 'Lewisham', 'Brent', 'Havering', 'Merton', 'Croydon', 'Southwark', 'Enfield', 'Redbridge', 'Camden', 'Westminster', 'Hammersmith and Fulham', 'Greenwich', 'Hackney', 'Hillingdon', 'Tower Hamlets', 'Newham', 'London', 'Richmond upon Thames', 'Kensington and Chelsea', 'Bexley', 'Barking and Dagenham', 'Islington', 'Lambeth', 'Wandsworth', 'Barnet', 'Ealing', 'Bromley', 'Kingston upon Thames', 'Haringey', 'City of London', 'Harrow', 'Hounslow', 'Waltham Forest'] , 'y': [2.941176470588235, 5.88235294117647, 8.823529411764707, 11.76470588235294, 14.705882352941178, 17.647058823529413, 20.588235294117645, 23.52941176470588, 26.47058823529412, 29.411764705882355, 32.35294117647059, 35.294117647058826, 38.23529411764706, 41.17647058823529, 44.11764705882353, 47.05882352941176, 50.0, 52.94117647058824, 55.88235294117647, 58.82352941176471, 61.76470588235294, 64.70588235294117, 67.64705882352942, 70.58823529411765, 73.52941176470588, 76.47058823529412, 79.41176470588235, 82.35294117647058, 85.29411764705883, 88.23529411764706, 91.17647058823529, 94.11764705882352, 97.05882352941177, 100.0], 'type' : 'line', 'name' : 'Line Chart'}
                        ] ,
                        'layout' : {
                            'title' : 'Biểu đồ tần suất tích lũy của các thành phố',
                            'xaxis' : { 'title': 'city' , 'tickangle' : 45},
                            'yaxis' : { 'title': 'phần trăm tích lũy'}
                        }
                    }), className='col-12'
                )
            ], className='row'),
            html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= {
                        'data' : [
                            { 'x': arrLondonYear , 'y': arrLondonPop, 'type' : 'line', 'name' : 'Line Chart'}
                        ] ,
                        'layout' : {
                            'title' : 'Biểu đồ dự đoán dân số của thành phố London 10 năm sau',
                            'xaxis' : { 'title': 'year'},
                            'yaxis' : { 'title': 'population'},
                           
                        }
                    }), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 3:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= lineChartType2), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

# ##-----------------------------------------------------
# # Bar Chart Link
tansobar_fig = go.Figure(data=[go.Bar(
    x=['Sutton', 'Lewisham', 'Brent', 'Havering', 'Merton', 'Croydon', 'Southwark', 'Enfield', 'Redbridge', 'Camden', 'Westminster', 'Hammersmith and Fulham', 'Greenwich', 'Hackney', 'Hillingdon', 'Tower Hamlets', 'Newham', 'London', 'Richmond upon Thames', 'Kensington and Chelsea', 'Bexley', 'Barking and Dagenham', 'Islington', 'Lambeth', 'Wandsworth', 'Barnet', 'Ealing', 'Bromley', 'Kingston upon Thames', 'Haringey', 'City of London', 'Harrow', 'Hounslow', 'Waltham Forest'],
    y=[91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91],
)])
tansobar_fig.update_layout(
    title_text="biểu đồ tần số của các thành phố",
)
tansobar_fig.update_layout(barmode='group', xaxis_tickangle=-45)

#type 2 chart

years = np.arange(2020, 2032, 1)
arr_bar_male = [
    4560247,4609120, 4656663, 4702906,
    4747715, 4791145, 4833286,
    4874275, 4914252, 4953309, 4991563,5029165
]
arr_bar_female= [
      4561103,4602269, 4642315, 4681486,
    4719771, 4757054, 4793531,
    4829250, 4864406, 4899098, 4933406,4967333
]

bar_type2_fig = go.Figure()
bar_type2_fig.add_trace(go.Bar(x=years,
                y=arr_bar_male,
                name='Nam',
                marker_color='rgb(55, 83, 109)'
                ))
bar_type2_fig.add_trace(go.Bar(x=years,
                y=arr_bar_female,
                name='Nữ',
                marker_color='rgb(26, 118, 255)'
                ))

bar_type2_fig.update_layout(
    title='So sánh dân sô giữa nam và nữ của thành phố London',
    xaxis_tickfont_size=14,
    xaxis = dict(
         title='Years',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='pop (population)',
        titlefont_size=16,
        tickfont_size=14,
        range=[4000000,5000000]
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.2, # gap between bars of adjacent location coordinates.
    bargroupgap=0.15, # gap between bars of the same location coordinate.
    height= 700
)


#---------------------------------------------
barChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Bar Chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Dạng biểu đồ này được thể hiện động thái phát triển, so sánh tương quan về độ lớn giữa các đại lượng hoặc thể hiện một thành phần cơ cấu trong một tổng thể.',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Bar chart (biểu đồ cột): thường được dùng khi cần phân loại dữ liệu và so sánh độ tương quản giữa chúng ',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= tansobar_fig), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= bar_type2_fig), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')


##-----------------------------------------------------
## pie chart draw

tuansuat_city_fig = px.pie( values=[0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353, 0.029411764705882353], names=['Sutton', 'Lewisham', 'Brent', 'Havering', 'Merton', 'Croydon', 'Southwark', 'Enfield', 'Redbridge', 'Camden', 'Westminster', 'Hammersmith and Fulham', 'Greenwich', 'Hackney', 'Hillingdon', 'Tower Hamlets', 'Newham', 'London', 'Richmond upon Thames', 'Kensington and Chelsea', 'Bexley', 'Barking and Dagenham', 'Islington', 'Lambeth', 'Wandsworth', 'Barnet', 'Ealing', 'Bromley', 'Kingston upon Thames', 'Haringey', 'City of London', 'Harrow', 'Hounslow', 'Waltham Forest'], title='Biều đồ tuần suất của các thành phố'
)


pieType1Fig = go.Figure(data=[go.Pie(labels=['Trẻ em & vị thành niên', 'Người trưởng thành', 'người lớn tuổi'], values=[2076150, 5548312,1443603])])
pieType1Fig.update_layout(
    title_text="Biểu đồ so sánh dân số 3 độ tuổi của thành phố london trong năm 2020 ",
    # Add annotations in the center of the donut pies.
    )
labels = ['Westminster','London','Wandsworth','Tower Hamlets','Havering','Waltham Forest','Hillingdon','Harrow']
values = [252186, 9121350, 330812, 323916,265106,
         285740,285740,313430,256598]

# Use `hole` to create a donut-like pie chart
compare_8_city_pie = go.Figure(data=[go.Pie(labels=labels, values=values,title='population' , hole=.5, pull=[0, 0.2, 0, 0,0])])
compare_8_city_pie.update_layout(
    title_text="So sánh các thành phố xung quanh london",
    # Add annotations in the center of the donut pies.
    )
##-----------------------------------------------------
## pie chart
##
pieChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                  dcc.Link('Dot Chart', href="/dot-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Pie Chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Đây là dạng biểu đồ thường được dùng để vẽ các biểu đồ liên quan đến cơ cấu, tỷ lệ các thành phần trong một tổng thể chung hoặc cũng có thể vẽ biểu đồ tròn khi tỷ lệ % trong bảng số liệu cộng lại tròn 100.',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Pie chart (biểu đồ tròn) được sử dụng khi cần biểu diễn dữ liệu dưới dạng % ',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib'),
            ]),
              html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= tuansuat_city_fig), className='col-12'
                )
            ], className='row'),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= pieType1Fig), className='col-12'
                )
            ], className='row'),

            html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= compare_8_city_pie), className='col-12'
                )
            ], className='row'),
           
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##______________________________________________________
#scatter charts


yScatter_withoutLondon = [7544, 221719, 402424, 252772, 339690, 339621, 261571, 395866, 352509, 343804, 291611, 187639, 280746, 256598, 265106, 313430,
 278253, 241462, 158643, 180838, 331353, 312153, 213048, 363484, 314637, 201177, 324445, 323916, 210359, 285740, 330812, 252186]

scatterWithoutLondon = go.Figure(data=go.Scatter(x=['City of London','Barking and Dagenham','Barnet','Bexley','Brent','Bromley','Camden',
                                   'Croydon','Ealing','Enfield','Greenwich','Hammersmith and Fulham','Haringey','Harrow','Havering',
                                   'Hillingdon','Hounslow','Islington','Kensington and Chelsea','Kingston upon Thames','Lambeth',
                                   'Lewisham','Merton',
                                  'Newham','Redbridge','Richmond upon Thames','Southwark','Tower Hamlets','Sutton'
                                   ,'Waltham Forest','Wandsworth','Westminster'],
                                y=yScatter_withoutLondon,
                                mode='markers',
                                marker_color=yScatter_withoutLondon,
                                marker=dict(
        size=16,
        color=np.random.randn(500), #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    ),
                                
                                text=['City of London','Barking and Dagenham','Barnet','Bexley','Brent','Bromley','Camden',
                                   'Croydon','Ealing','Enfield','Greenwich','Hammersmith and Fulham','Haringey','Harrow','Havering',
                                   'Hillingdon','Hounslow','Islington','Kensington and Chelsea','Kingston upon Thames','Lambeth',
                                   'Lewisham','Merton',
                                  'Newham','Redbridge','Richmond upon Thames','Southwark','Tower Hamlets','Sutton'
                                   ,'Waltham Forest','Wandsworth','Westminster'])) # hover text goes here

scatterWithoutLondon.update_layout(title='Dân số tất cả thành phố trừ London')

yScatter_HaveLondon =[7544, 221719, 402424, 252772, 339690, 339621, 261571, 395866, 352509, 343804, 291611, 187639, 280746, 256598, 265106, 313430, 278253, 241462, 
158643, 180838, 331353, 312153, 213048, 363484, 314637, 201177, 324445, 323916, 210359, 285740, 330812, 252186, 9121350]

yScatter_HaveLondon = go.Figure(data=go.Scatter(x=['City of London','Barking and Dagenham','Barnet','Bexley','Brent','Bromley','Camden',
                                   'Croydon','Ealing','Enfield','Greenwich','Hammersmith and Fulham','Haringey','Harrow','Havering',
                                   'Hillingdon','Hounslow','Islington','Kensington and Chelsea','Kingston upon Thames','Lambeth',
                                   'Lewisham','Merton',
                                  'Newham','Redbridge','Richmond upon Thames','Southwark','Tower Hamlets','Sutton'
                                   ,'Waltham Forest','Wandsworth','Westminster','london'],
                                y=yScatter_HaveLondon,
                                mode='markers',
                                marker_color=yScatter_HaveLondon,                              
                                text=['City of London','Barking and Dagenham','Barnet','Bexley','Brent','Bromley','Camden',
                                   'Croydon','Ealing','Enfield','Greenwich','Hammersmith and Fulham','Haringey','Harrow','Havering',
                                   'Hillingdon','Hounslow','Islington','Kensington and Chelsea','Kingston upon Thames','Lambeth',
                                   'Lewisham','Merton',
                                  'Newham','Redbridge','Richmond upon Thames','Southwark','Tower Hamlets','Sutton'
                                   ,'Waltham Forest','Wandsworth','Westminster','london'])) # hover text goes here

yScatter_HaveLondon.update_layout(title='Dân số tất cả thành phố trong bộ dữ liệu')



#-------------------------
scatterChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                  dcc.Link('Dot Chart', href="/dot-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Scatter chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Biểu đồ phân tán trong tiếng Anh là Scatter diagram. Biểu đồ phân tán thực chất là một đồ thị biểu hiện mối tương quan giữa nguyên nhân và kết quả hoặc giữa các yếu tố ảnh hưởng đến chất lượng.',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Scatter chart (biểu đồ phân tán) thường được sử dụng để thể hiện mối tương quan giữa các yếu tố trên đồ thị. ',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib'),
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= scatterWithoutLondon), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= yScatter_HaveLondon), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')


##-----------------------------------------------------
##dot chart


u18_array_dot = [2076150, 2094684, 2111713,
 2125502, 2135354, 2141893, 2144074, 2146055,
  2145868, 2143239, 2139107, 2138675]

u60_array_dot = [5548312, 5584214, 5617241, 5648317, 5679015, 5710728, 5744331, 5777102, 5811612, 5848468, 5886780, 5920257]

u90_array_dot = [1443603, 1478678, 1515464, 1555178, 1596731, 1637554, 1678476, 1718474, 1756950, 1794077, 1830304, 1867763]

arangeDot = np.arange(2020, 2032, 1)


dot_chart_1_fig = go.Figure()
dot_chart_1_fig.add_trace(go.Scatter(
    x=u18_array_dot,
    y=arangeDot,
    marker=dict(color="crimson", size=12),
    mode="markers",
    name="dưới 18 tuổi",
))

dot_chart_1_fig.add_trace(go.Scatter(
    x=u60_array_dot,
    y=arangeDot,
    marker=dict(color="gold", size=12),
    mode="markers",
    name="từ 18 tới 59 tuổi",
))
dot_chart_1_fig.add_trace(go.Scatter(
    x=u90_array_dot,
    y=arangeDot,
    marker=dict(color="green", size=12),
    mode="markers",
    name="từ 60 tới 90 tuổi",
))
dot_chart_1_fig.update_layout(title="Biểu đồ dự đoán 3 lứa tuổi của thành phố london trong 10 năm sau",
                  xaxis_title="population",
                  yaxis_title="years")

#--------
#--------

schools = ["2020", "2021", "2022", "2023", "2024", "2025",
           "2026", "2027", "2028", "2029", "2030",
           "2031"]
n_schools = len(schools)

men_salary = arr_bar_male
women_salary = arr_bar_female

df = pd.DataFrame(dict(year=schools*2, population=men_salary + women_salary,
                       gender=["Men"]*n_schools + ["Women"]*n_schools))

# Use column names of df for the different parameters x, y, color, ...
dot_chart_2_fig = px.scatter(df, x="population", y="year", color="gender",
                 title="Biểu đồ thể hiện sự chênh lệch giữa nam và nữ của london 10 năm sau",
                 labels="population" # customize axis label
                )
#------------------------------------------------------
dotChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Dot chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Dot chart (biểu đồ chấm) là một dạng biểu đồ phân tán (Scatter chart) thể hiện sự khác biệt giữa hai hoặc nhiều loại dữ liệu trong cùng một thời điểm hoặc giữa hai hay nhiều điều kiện (condition). Hãy so sánh với Biểu đồ cột (Bar chart), biểu đồ chấm (dot chart) dễ nhìn hơn và cho phép người phân tích dễ dàng so sánh các loại dữ liệu.  ',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Dot chart (biểu đồ chấm) sử dụng khi so sánh dữ liệu phân loại trong cùng một thời gian.',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= dot_chart_1_fig), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= dot_chart_2_fig), className='col-12'
                )
            ], className='row'),  
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##---------------------------------------------------------
DataAnalysis = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Div([
                html.Div('Data Analysis', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('- Dữ liệu thu thập được:', className='introMatplotlib'),
                 html.Div('dữ liệu thứ cấp',className='content')
            ]),
             html.Div([
                 html.Span('- Định nghĩa các biến số:', className='introMatplotlib'),
                 html.Div('gss_code: (Government Statistical Service code): mã dịch vụ thống kê của chính phủ',className='content'),
                 html.Div('component: dân số',className='content'),
                 html.Div('year: năm',className='content'),
                 html.Div('Births:  sinh',className='content'),
                 html.Div('Deaths: tử',className='content'),
                 html.Div('international_in: nhập cư',className='content'),
                 html.Div('international_out: xuất cư',className='content'),
                 html.Div('domestic_in: trong nước',className='content'),
                 html.Div('domestic_out: ngoài nước',className='content'),
                 html.Div('district: thành phố',className='content'),
                 html.Div('sex: giới tính',className='content'),
                 html.Div('age: tuổi',className='content'),
                 html.Div('2010, 2011,... 2050: các năm dự đoán',className='content'),     
            ]),
             html.Div([
                 html.Span('- Dạng dữ liệu:', className='introMatplotlib'),
                 html.Div('Định tính: sex, district, component ',className='content'),
                 html.Div('Định lượng: age, 2010, 2011, … 2050, year, births, deaths, international_in, international_out, domestic_in, domestic_out',className='content'),
            ]),
             html.Div([
                 html.Span('- Thang do cho dữ liệu: ', className='introMatplotlib'),
                 html.Div('Thang do định danh (norminal): district, sex, component ',className='content'),
                html.Div('Thang đo khoảng( (interval): 2010, 2011,… 2050 ,year, births, deaths, international_in, international_out, domestic_in, domestic_out ',className='content')
            ]),
             html.Div([
                 html.Span('Kiểu dữ liệu: ', className='introMatplotlib'),
                 html.Div('String: District, component,sex. ',className='content'),
                 html.Div('Integer: Age. ',className='content'),
                 html.Div('Decimal: 2010, 2011, 2012,.. 2050 year, births, deaths, international_in, international_out, domestic_in, domestic_out ',className='content'),
            ]),
             html.Div([
                 html.Span('Mục tiêu nghiên cứu: ', className='introMatplotlib'),
                 html.Div('nghiên cứu về dân số cùa thành phố london cùng với các thành phố khác trong khu vực và dự đoán dân số. ',className='content')
            ]),
             html.Div([
                 html.Span('Phạm vi nghiên cứu:', className='introMatplotlib'),
                 html.Div('10 năm sau ( 2020 -> 2031 ).',className='content')
            ]),
             html.Div([
                 html.Span('Nhóm biến tham gia quá trình nghiên cứu:', className='introMatplotlib'),
                 html.Div('district, sex, age, 2020,… 2031, births, deaths ',className='content')
            ])
        ],className='col-12 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')



##---------------------------------------------------------
# and this code to transfer to another link
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/simple-chart':
        return simpleChart
    elif pathname == '/line-chart':
        return lineChart
    elif pathname =='/bar-chart':
        return barChart
    elif pathname =='/pie-chart':
        return pieChart
    elif pathname =='/scatter-chart':
        return scatterChart
    elif pathname =='/dot-chart':
        return dotChart
    elif pathname =='/data-analysis':
        return DataAnalysis
    else:
        return main

server = app.server

if __name__ == "__main__":
    app.run_server()
