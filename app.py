import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import joblib
import os

# Load trained model
MODEL_PATH = "model.pkl"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at '{MODEL_PATH}'. Please ensure 'model.pkl' is in the same directory as this app.")
model = joblib.load(MODEL_PATH)

# Initialize Dash app
app = dash.Dash(__name__, title="Health Insurance Predictor")
server = app.server  # for deployment

# Layout with luxurious, serene styling
app.layout = html.Div(
    style={
        "maxWidth": "900px",
        "margin": "40px auto",
        "fontFamily": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        "color": "#2c3e50",
        "backgroundColor": "#f4f6f9",
        "borderRadius": "15px",
        "boxShadow": "0px 5px 15px rgba(0,0,0,0.1)",
        "padding": "20px",
    },
    children=[
        html.H1(
            "💎 Health Insurance Cost Predictor",
            style={"textAlign": "center", "color": "#16a085", "marginBottom": "40px"},
        ),
        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "padding": "20px",
                "borderRadius": "15px",
                "boxShadow": "0px 5px 15px rgba(0,0,0,0.1)",
            },
            children=[
                html.H2("Enter Your Details", style={"textAlign": "center", "marginBottom": "20px"}),
                html.Div(
                    style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "20px"},
                    children=[
                        html.Label("Age:", style={"fontWeight": "bold"}),
                        dcc.Input(id="age", type="number", value=30, min=0),
                        html.Label("BMI:", style={"fontWeight": "bold"}),
                        dcc.Input(id="bmi", type="number", value=25, min=0),
                        html.Label("Number of Children:", style={"fontWeight": "bold"}),
                        dcc.Input(id="children", type="number", value=0, min=0),
                        html.Label("Sex:", style={"fontWeight": "bold"}),
                        dcc.Dropdown(
                            id="sex",
                            options=[{"label": "Male", "value": "male"}, {"label": "Female", "value": "female"}],
                            value="male",
                        ),
                        html.Label("Smoker:", style={"fontWeight": "bold"}),
                        dcc.Dropdown(
                            id="smoker",
                            options=[{"label": "Yes", "value": "yes"}, {"label": "No", "value": "no"}],
                            value="no",
                        ),
                        html.Label("Region:", style={"fontWeight": "bold"}),
                        dcc.Dropdown(
                            id="region",
                            options=[
                                {"label": "Northeast", "value": "northeast"},
                                {"label": "Northwest", "value": "northwest"},
                                {"label": "Southeast", "value": "southeast"},
                                {"label": "Southwest", "value": "southwest"},
                            ],
                            value="northeast",
                        ),
                        html.Br(),
                        html.Button(
                            "Predict Insurance Cost",
                            id="predict-button",
                            n_clicks=0,
                            style={
                                "backgroundColor": "#1abc9c",
                                "color": "white",
                                "padding": "10px 20px",
                                "border": "none",
                                "borderRadius": "10px",
                                "fontSize": "16px",
                                "cursor": "pointer",
                            },
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "padding": "20px",
                "borderRadius": "15px",
                "boxShadow": "0px 5px 15px rgba(0,0,0,0.1)",
                "marginTop": "40px",
            },
            children=[
                html.H2(
                    "💰 Predicted Insurance Cost",
                    style={"textAlign": "center", "color": "#16a085"},
                ),
                html.Div(
                    id="prediction-output",
                    style={
                        "fontSize": "28px",
                        "color": "#e74c3c",
                        "textAlign": "center",
                        "marginTop": "20px",
                    },
                ),
            ],
        ),
        html.Div(
            style={"textAlign": "center", "marginTop": "30px"},
            children=[
                html.A(
                    "Design Inspiration",
                    href="https://www.pinterest.com/pin/82331501718942828/",
                    target="_blank",
                    style={"color": "#2980b9", "textDecoration": "none", "fontStyle": "italic"},
                )
            ],
        ),
    ],
)

# Callback for prediction
@app.callback(
    Output("prediction-output", "children"),
    Input("predict-button", "n_clicks"),
    [
        Input("age", "value"),
        Input("bmi", "value"),
        Input("children", "value"),
        Input("sex", "value"),
        Input("smoker", "value"),
        Input("region", "value"),
    ],
)
def predict_cost(n_clicks, age, bmi, children, sex, smoker, region):
    if n_clicks == 0:
        return ""
    if None in [age, bmi, children, sex, smoker, region]:
        return "Please fill in all fields."
    sex_encoded = 1 if sex.lower() == "male" else 0
    smoker_encoded = 1 if smoker.lower() == "yes" else 0
    region_mapping = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
    region_encoded = region_mapping[region.lower()]
    input_array = np.array([[age, bmi, children, sex_encoded, smoker_encoded, region_encoded]])
    predicted_cost = model.predict(input_array)[0]
    return f"${predicted_cost:,.2f}"

# Run app
if __name__ == "__main__":
    app.run(debug=True)
