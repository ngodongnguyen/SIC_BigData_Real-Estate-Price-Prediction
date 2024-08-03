import dash
from dash import html

dash.register_page(__name__, path="/predicting", title="Price Predicting")

layout = html.Div(
    [html.H2("Prediction Page"), html.P("Welcome to the Prediction Page!")],
    className="container",
)
