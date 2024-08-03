from dash import html
import dash_bootstrap_components as dbc


def sidebar():
    return html.Div(
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
                            html.Span("Analytics"),
                        ],
                        href="/analytics-dashboard",
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
                            html.Span("Price Predicting"),
                        ],
                        href="/predicting",
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
