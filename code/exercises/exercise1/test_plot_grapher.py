import os

import pandas as pd
import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


class GraphPlotter():

    def __init__(self, ax, graph_type):
        self.ax = ax
        self.graph_type = graph_type

