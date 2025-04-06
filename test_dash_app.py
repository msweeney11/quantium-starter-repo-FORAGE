import pytest
from dash import Dash, html, dcc
import dash.testing.browser
from dash.testing.application_runners import import_app

app = import_app("dashGraph")

@pytest.fixture
def test_app(dash_duo):
    dash_duo.start_server(app)

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert header.text == "Sales Data Dashboard"

def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    legend = dash_duo.find_element(".legend")
    assert legend is not None

