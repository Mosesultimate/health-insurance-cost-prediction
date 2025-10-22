# ====================================================
# 🚀 Luxury Dash App for Health Insurance Cost Prediction
# ====================================================

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# ---------------------- Load Dataset & Model ----------------------
df = pd.read_csv(r"C:\Users\ADMIN\Downloads\insurance.csv")  # your dataset path
model = joblib.load("model.pkl")   # your trained model path

# ---------------------- Initialize Dash ----------------------
app = dash.Dash(__name__)
server = app.server  # for deployment if needed

# ---------------------- App Layout ----------------------
app.layout = html.Div([
    html.H1("💎 Health Insurance Cost Prediction",
            style={'textAlign':'center', 'color':'#34495e', 'marginTop':'20px', 'font-family':'Arial'}),

    # ---------------- Prediction Card ----------------
    html.Div([
        html.Div([
            html.Label("Age:", style={'fontWeight':'bold'}),
            dcc.Input(id='age', type='number', value=30, style={'width':'100%'}),

            html.Label("BMI:", style={'fontWeight':'bold', 'marginTop':'10px'}),
            dcc.Input(id='bmi', type='number', value=25, style={'width':'100%'}),

            html.Label("Number of Children:", style={'fontWeight':'bold', 'marginTop':'10px'}),
            dcc.Input(id='children', type='number', value=0, style={'width':'100%'}),

            html.Label("Sex:", style={'fontWeight':'bold', 'marginTop':'10px'}),
            dcc.Dropdown(
                id='sex',
                options=[{'label':'Male','value':'male'}, {'label':'Female','value':'female'}],
                value='male',
                style={'width':'100%'}
            ),

            html.Label("Smoker:", style={'fontWeight':'bold', 'marginTop':'10px'}),
            dcc.Dropdown(
                id='smoker',
                options=[{'label':'Yes','value':'yes'}, {'label':'No','value':'no'}],
                value='no',
                style={'width':'100%'}
            ),

            html.Label("Region:", style={'fontWeight':'bold', 'marginTop':'10px'}),
            dcc.Dropdown(
                id='region',
                options=[
                    {'label':'Northeast','value':'northeast'},
                    {'label':'Northwest','value':'northwest'},
                    {'label':'Southeast','value':'southeast'},
                    {'label':'Southwest','value':'southwest'}
                ],
                value='northeast',
                style={'width':'100%'}
            ),

            html.Br(),
            html.Button('Predict Insurance Cost', id='predict-button',
                        n_clicks=0,
                        style={'marginTop':'20px', 'backgroundColor':'#1abc9c',
                               'color':'white', 'fontWeight':'bold', 'width':'100%', 'padding':'10px', 'border':'none',
                               'borderRadius':'8px', 'cursor':'pointer'})
        ], style={'backgroundColor':'#ecf0f1', 'padding':'20px', 'borderRadius':'15px', 'boxShadow':'0 4px 8px rgba(0,0,0,0.2)'})
    ], style={'width':'400px', 'margin':'0 auto'}),

    html.H2("Predicted Insurance Cost:", style={'textAlign':'center', 'marginTop':'20px', 'color':'#2c3e50'}),
    html.Div(id='prediction-output', style={'fontSize':32, 'color':'#e74c3c', 'textAlign':'center', 'marginBottom':'40px'}),

    # ---------------- Analytics Section ----------------
    html.Div([
        html.H2("📊 Data Insights", style={'textAlign':'center', 'color':'#2c3e50', 'marginTop':'50px'}),
        html.Div([
            dcc.Graph(
                id='age-charges-graph',
                figure=px.scatter(
                    df, x='age', y='charges',
                    color='smoker', size='bmi',
                    hover_data=['region'],
                    color_discrete_map={'yes':'#e74c3c', 'no':'#16a085'},
                    template='plotly_white'
                ).update_layout(
                    plot_bgcolor='rgba(236, 240, 241, 0.9)',
                    paper_bgcolor='rgba(236, 240, 241, 0.9)',
                    title={'text':'Age vs Charges', 'x':0.5, 'xanchor':'center', 'font':{'size':20}}
                )
            ),
            dcc.Graph(
                id='bmi-charges-graph',
                figure=px.scatter(
                    df, x='bmi', y='charges',
                    color='smoker', size='age',
                    hover_data=['region'],
                    color_discrete_map={'yes':'#e74c3c', 'no':'#16a085'},
                    template='plotly_white'
                ).update_layout(
                    plot_bgcolor='rgba(236, 240, 241, 0.9)',
                    paper_bgcolor='rgba(236, 240, 241, 0.9)',
                    title={'text':'BMI vs Charges', 'x':0.5, 'xanchor':'center', 'font':{'size':20}}
                )
            ),
            dcc.Graph(
                id='region-charges-bar',
                figure=px.bar(
                    df.groupby('region')['charges'].mean().reset_index(),
                    x='region', y='charges',
                    color='region',
                    color_discrete_sequence=['#1abc9c','#3498db','#9b59b6','#e67e22'],
                    template='plotly_white'
                ).update_layout(
                    plot_bgcolor='rgba(236, 240, 241, 0.9)',
                    paper_bgcolor='rgba(236, 240, 241, 0.9)',
                    title={'text':'Average Charges by Region', 'x':0.5, 'xanchor':'center', 'font':{'size':20}},
                    showlegend=False
                )
            )
        ], style={'display':'grid', 'gridTemplateColumns':'repeat(auto-fit, minmax(450px, 1fr))',
                  'gap':'30px', 'marginTop':'20px', 'marginBottom':'50px'})
    ], style={'padding':'20px'})
], style={'fontFamily':'Arial', 'backgroundColor':'#f7f9f9', 'paddingBottom':'50px'})

# ---------------- Prediction Callback ----------------
@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    [Input('age', 'value'),
     Input('bmi', 'value'),
     Input('children', 'value'),
     Input('sex', 'value'),
     Input('smoker', 'value'),
     Input('region', 'value')]
)
def predict_cost(n_clicks, age, bmi, children, sex, smoker, region):
    sex_encoded = 1 if sex.lower() == 'male' else 0
    smoker_encoded = 1 if smoker.lower() == 'yes' else 0
    region_mapping = {'northeast':0, 'northwest':1, 'southeast':2, 'southwest':3}
    region_encoded = region_mapping[region.lower()]

    input_array = np.array([[age, bmi, children, sex_encoded, smoker_encoded, region_encoded]])
    predicted_cost = model.predict(input_array)[0]
    return f"${predicted_cost:,.2f}"

# ---------------- Run App ----------------
if __name__ == '__main__':
    app.run(debug=True)
