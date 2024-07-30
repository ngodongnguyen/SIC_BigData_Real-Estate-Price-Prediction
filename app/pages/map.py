import dash
from dash import html

dash.register_page(__name__, path="/map")

layout = html.Div(
    [html.H2("Map Page"), html.P("Welcome to the Map Page!")], className="container"
)
