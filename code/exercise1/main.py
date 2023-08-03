import os
from numpy import who

import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from xarray.coding.cftime_offsets import MonthEnd

class PlotFormatter:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax

    def format_grid(self, linestyle='--', linewidth=0.5):
        self.ax.grid(True, which='both', linestyle=linestyle, linewidth=linewidth)
        
    def format_title(self, title, fontsize=16):
        self.ax.set_title(title, fontsize=fontsize)

    def format_labels(self, xlabel='Date', ylabel='Temperature (K)', fontsize=14):
        self.ax.set_xlabel(xlabel, fontsize=fontsize)
        self.ax.set_ylabel(ylabel, fontsize=fontsize)
        
    def format_date(self, date_format, interval=2):
        self.ax.xaxis.set_major_locator(mdates.DayLocator(interval=interval))
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter(date_format))
        self.fig.autofmt_xdate()


def load_dataset(filename):

    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, 'Code/star-struck/data/', filename)

    ds = xr.open_dataset(file_path, engine='cfgrib')
    
    # conver Kelvin to Celcius
    ds['t2m'] -= 273.15

    return ds

def slice_location(ds, location):
    lat_min, lat_max = location['latitude']
    lon_min, lon_max = location['longitude']

    spatial_subset = ds.t2m.sel(latitude=slice(lat_min, lat_max), longitude=slice(lon_min, lon_max))

    return spatial_subset

#def plot_time_series(da, region_name, date_format):
#
#    fig, ax = plt.subplots()
#    da.plot.line('bo-', ax=ax, linewidth=2)  # a thicker blue line
#    title = "Daily Mean 2m Temperature over " + region_name
#    format_timeserie_s(fig, ax, title, date_format)
#
#    plt.show()

def plot_time_series(ds1, ds2, region_name, date_format):

    fig, axs = plt.subplots(2)
    ds1.plot.line(ax=axs[0])  
    ds2.plot.line(ax=axs[1])  
    
    title1 = "Daily Mean 2m Temperature over " + region_name
    title2 = "Hourly Mean 2m Temperature over " + region_name

    formatter1 = PlotFormatter(fig, axs[0])
    formatter1.format_title(title1)
    formatter1.format_grid()
    formatter1.format_labels()
    formatter1.format_date(date_format)
    
    formatter2 = PlotFormatter(fig, axs[1])
    formatter2.format_title(title2)
    formatter2.format_grid()
    formatter2.format_labels()

    plt.tight_layout()
    plt.show()

def get_spatial_mean_temperature(ds, location):
    spatial_subset = slice_location(ds, location)

    return spatial_subset.mean(dim=['latitude', 'longitude'])

def get_monthly_mean_temperature(ds, location):
    spatial_mean_temperature = get_spatial_mean_temperature(ds, location)

    return spatial_mean_temperature.mean('step')

def process_data_hourly(ds, location):
    
    spatial_subset = slice_location(ds, location) 
    spatial_mean = spatial_subset.mean(dim=['latitude', 'longitude'])
    hourly_temperature = spatial_mean.groupby('step').mean('time')

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

