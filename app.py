import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import psutil
import logging
from collections import deque
from datetime import datetime
import sys

# Set up basic logging to debug
logging.basicConfig(level=logging.INFO)

# Initialize the Dash app
app = dash.Dash(__name__)