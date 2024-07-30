# Import packages
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq

# Initialize the app
app = Dash(
    __name__,
    title="Real Estate Price Prediction",
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    use_pages=True,
)

sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="bi bi-house"), html.Span("Home")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="bi bi-clipboard-data"),
                        html.Span("Analysis"),
                    ],
                    href="/analytics",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="bi bi-map"),
                        html.Span("Map"),
                    ],
                    href="/map",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="bi bi-cash-coin"),
                        html.Span("Prediction"),
                    ],
                    href="/prediction",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="bi bi-info-square"),
                        html.Span("About"),
                    ],
                    href="/about",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

app.layout = html.Div(
    [
        sidebar,
        html.Div(
            [
                html.H1(
                    "SAMSUNG INNOVATION CAMPUS CAPSTONE PROJECT",
                    "header",
                    className="header",
                ),
                dash.page_container,
            ],
            className="main",
        ),
    ]
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
