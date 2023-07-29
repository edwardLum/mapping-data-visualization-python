import os
from datetime import datetime

import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Exercise 1
def load_dataset(filename):

    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, 'Code/star-struck/data/', filename)

    ds = xr.open_dataset(file_path, engine='cfgrib')

    return ds

def format_timeseries(fig, ax, title, date_format):
   
    ax.set_title(title , fontsize=16) # Set title
    # Use ax.gca() (Get Current axs) to get the axs object and then modify it
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))  # Set major ticks every fifth day
    ax.xaxis.set_major_formatter(mdates.DateFormatter(date_format))  # Set format
    
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Temperature (K)', fontsize=14)
       
    fig.autofmt_xdate()

def slice_location(ds, location):
    lat_min, lat_max = location['latitude']
    lon_min, lon_max = location['longitude']

    spatial_subset = ds.t2m.sel(latitude=slice(lat_min, lat_max), longitude=slice(lon_min, lon_max))

    return spatial_subset

def plot_time_series(da, region_name, date_format):

    fig, ax = plt.subplots()
    da.plot.line('bo-', ax=ax, linewidth=2)  # a thicker blue line
    title = "Daily Mean 2m Temperature over " + region_name
    format_timeseries(fig, ax, title, date_format)

    plt.show()


def process_data_daily_mean(ds, location):
    spatial_subset = slice_location(ds, location) 
    
    spatial_mean = spatial_subset.mean(dim=['latitude', 'longitude'])

    daily_mean_temp = spatial_mean.mean(dim=['step'])

    return daily_mean_temp

def process_data_hourly_mean(ds, location, day):
    spatial_subset = slice_location(ds, location) 
    
    spatial_mean = spatial_subset.mean(dim=['latitude', 'longitude'])

    hourly_temp = spatial_mean.sel(time=day)

    return hourly_temp



if __name__ == "__main__":
    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, 'Code/star-struck/data/download.grib')

    ds = load_dataset(file_path)
    # Define Attica region
    lat_min, lat_max = 38.25, 37.70 
    lon_min, lon_max = 23.45, 24.25
    region_name = 'Attica'
    
    print(ds)
    location = {'latitude': (lat_min, lat_max),
                'longitude': (lon_min, lon_max)}
    
    date_format = '%Y-%m-%d'
    hourly_format = '%H:%M'
    
    day = '2022-07-01'
    daily_mean_temp = process_data_daily_mean(ds, location)
    hourly_mean_temp = process_data_hourly_mean(ds, location, day)
    # plot_time_series(hourly_mean_temp, region_name, hourly_format)
    print(hourly_mean_temp.step)

