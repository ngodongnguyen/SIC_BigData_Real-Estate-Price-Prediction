# Import packages
import dash
from dash import Dash, html, dcc, clientside_callback, Input, Output, State
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
        html.Button(
            html.I(id="sidebar-toggle-icon", className="bi bi-arrow-bar-right"),
            "sidebar-toggle",
            className="sidebar__mode-btn",
        ),
    ],
    "sidebar",
    className="sidebar collapsed",
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
            "main",
            className="collapsed-sidebar",
        ),
        dcc.Store(
            id="sidebar-toggle-state", data={"expanded": False}
        ),  # Store for sidebar state
    ]
)
# Clientside callback to handle sidebar toggle
app.clientside_callback(
    """
    function(n_clicks, data) {
        const sidebar = document.getElementById('sidebar');
        const icon = document.getElementById('sidebar-toggle-icon');
        const main = document.getElementById('main');

        if (data.expanded) {
            sidebar.classList.remove('expanded');
            sidebar.classList.add('collapsed');
            icon.classList.remove('rotate');
            main.classList.remove('expanded-sidebar')
            main.classList.add('collapsed-sidebar')
            return {'expanded': false};
        } else {
            sidebar.classList.remove('collapsed');
            sidebar.classList.add('expanded');
            icon.classList.add('rotate');
            main.classList.remove('collapsed-sidebar')
            main.classList.add('expanded-sidebar')
            return {'expanded': true};
        }
    }
    """,
    Output("sidebar-toggle-state", "data"),
    Input("sidebar-toggle", "n_clicks"),
    State("sidebar-toggle-state", "data"),
    prevent_initial_call=True,
)

# Run the app
if __name__ == "__main__":
    app.run()
