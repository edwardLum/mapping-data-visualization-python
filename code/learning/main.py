import os

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from xarray.coding.cftime_offsets import MonthEnd

class PlotFormatter:
    """
    A helper class for formatting matplotlib plots.
    """
    def __init__(self, fig, ax):
        """
        Initialize the PlotFormatter with a given figure and axis.

        Parameters:
        - fig (matplotlib.figure.Figure): The figure containing the plot.
        - ax (matplotlib.axes._subplots.AxesSubplot): The axis of the plot to be formatted.
        """
        self.fig = fig
        self.ax = ax

    def format_grid(self, linestyle='--', linewidth=0.5):
        self.ax.grid(True, which='both', linestyle=linestyle, linewidth=linewidth)
        
    def format_title(self, title, fontsize=16):
        self.ax.set_title(title, fontsize=fontsize)

    def format_labels(self, xlabel, ylabel='Temperature (C)', fontsize=14):
        self.ax.set_xlabel(xlabel, fontsize=fontsize)
        self.ax.set_ylabel(ylabel, fontsize=fontsize)
        
    def format_date(self, date_format, interval=2):
        self.ax.xaxis.set_major_locator(mdates.DayLocator(interval=interval))
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter(date_format))
        # self.fig.autofmt_xdate()

    def format_hour(self, interval=2):
        labels = [(str(x) + ":00" if x > 10 else "0" + str(x) + ":00") for x in range(0, 24, 2)]
        self.ax.set_xticks(np.arange(0,24, 2))
        print(labels)
        self.ax.set_xticklabels(labels)


def load_dataset(filename):
    """
    Load a dataset from a given file path.

    Parameters:
    - filename (str): The path to the dataset file.

    Returns:
    - xarray.Dataset: The loaded dataset with temperature in Celsius.
    """

    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, 'Code/star-struck/data/', filename)

    ds = xr.open_dataset(file_path, engine='cfgrib')
    
    # convert Kelvin to Celcius
    ds['t2m'] -= 273.15

    return ds

def slice_location(ds, location):
    """
    Extracts a spatial subset of the dataset for a given location.

    Parameters:
    - ds (xarray.Dataset): The dataset to be subsetted.
    - location (dict): Dictionary containing latitude and longitude ranges.

    Returns:
    - xarray.DataArray: A spatial subset of the 2m temperature data.
    """

    lat_min, lat_max = location['latitude']
    lon_min, lon_max = location['longitude']

    spatial_subset = ds.t2m.sel(latitude=slice(lat_min, lat_max), longitude=slice(lon_min, lon_max))

    return spatial_subset

def plot_time_series(ds1, ds2, region_name, date_format):
    """
    Plots two time series on separate subplots.

    Parameters:
    - ds1 (xarray.DataArray): Data for the first subplot (e.g., daily mean temperature).
    - ds2 (xarray.DataArray): Data for the second subplot (e.g., hourly mean temperature).
    - region_name (str): The name of the region being plotted.
    - date_format (str): The format of the date to be displayed on the x-axis.
    """

    fig, axs = plt.subplots(2, figsize=(12, 8))
    ds1.plot.line(ax=axs[0])  
    ds2.plot.line(ax=axs[1])  
    
    title1 = "Daily Mean 2m Temperature over " + region_name
    title2 = "Hourly Mean 2m Temperature over " + region_name

    formatter1 = PlotFormatter(fig, axs[0])
    formatter1.format_title(title1)
    formatter1.format_grid()
    formatter1.format_labels(xlabel="Date")
    formatter1.format_date(date_format)
    
    formatter2 = PlotFormatter(fig, axs[1])
    formatter2.format_title(title2)
    formatter2.format_grid()
    formatter2.format_labels(xlabel="Hour")
    formatter2.format_hour()

    # plt.tight_layout()
    plt.subplots_adjust(hspace=0.633, left=0.085, bottom=0.1,
                        right=0.924, top=0.915, wspace=0.2)
    plt.setp(axs[0].get_xticklabels(), rotation=45)
    plt.show()

def get_spatial_mean_temperature(ds, location):
    """
    Get the spatial mean temperature for a given location.

    Parameters:
    - ds (xarray.Dataset): The dataset containing temperature data.
    - location (dict): Dictionary containing latitude and longitude ranges.

    Returns:
    - xarray.DataArray: Spatial mean temperature.
    """
    spatial_subset = slice_location(ds, location)

    return spatial_subset.mean(dim=['latitude', 'longitude'])

def get_monthly_mean_temperature(ds, location):
    """
    Computes the monthly mean temperature for a given location.

    Parameters:
    - ds (xarray.Dataset): The dataset containing temperature data.
    - location (dict): Dictionary containing latitude and longitude ranges.

    Returns:
    - xarray.DataArray: Monthly mean temperature.
    """
    spatial_mean_temperature = get_spatial_mean_temperature(ds, location)

    return spatial_mean_temperature.mean('step')

def process_data_hourly(ds, location):
    """
    Processes the dataset to compute the hourly mean temperature for a given location.

    Parameters:
    - ds (xarray.Dataset): The dataset containing temperature data.
    - location (dict): Dictionary containing latitude and longitude ranges.

    Returns:
    - xarray.DataArray: Hourly mean temperature.
    """
    spatial_subset = slice_location(ds, location) 
    spatial_mean = spatial_subset.mean(dim=['latitude', 'longitude'])
    hourly_temperature = spatial_mean.groupby('step').mean('time')

    # convert nanoseconds to hour in the step coordinate
    hourly_temperature['step'] = hourly_temperature['step'] / (1e9 * 60 * 60)

    return hourly_temperature



if __name__ == "__main__":
    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, 'Code/star-struck/data/download.grib')

    ds = load_dataset(file_path)

    # Define Attica region
    lat_min, lat_max = 38.25, 37.70 
    lon_min, lon_max = 23.45, 24.25
    region_name = 'Attica'
    
    location = {'latitude': (lat_min, lat_max),
                'longitude': (lon_min, lon_max)}
    
    date_format = '%Y-%m-%d'
    hourly_format = '%H:%M'
    
    monthly_mean_temperature = get_monthly_mean_temperature(ds, location)
    hourly_mean_temperature = process_data_hourly(ds, location)
 
    plot_time_series(monthly_mean_temperature, hourly_mean_temperature, region_name, date_format)
    # print(ds.time)

