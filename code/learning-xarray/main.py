import os
import xarray as xr
import matplotlib.pyplot as plt

import matplotlib.dates as mdates

# Exercise 1
def load_dataset(file_path):
    ds = xr.open_dataset(file_path, engine='cfgrib')

    return ds

def format_timeseries(fig, ax, title):
   
    ax.set_title(title , fontsize=16) # Set title
    # Use ax.gca() (Get Current axs) to get the axs object and then modify it
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Set major ticks every fifth day
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Set format
    
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Temperature (K)', fontsize=14)
       
    fig.autofmt_xdate()

def plot_time_series(ds, location, location_desc):

    lat_min, lat_max = location['latitude']
    lon_min, lon_max = location['longitude']

    spatial_subset = ds.t2m.sel(latitude=slice(lat_min, lat_max), longitude=slice(lon_min, lon_max))

    spatial_mean = spatial_subset.mean(dim=['latitude', 'longitude'])
    daily_mean_temp = spatial_mean.mean(dim=['step'])

    print(type(daily_mean_temp.time.values[0]))


    fig, ax = plt.subplots()
    daily_mean_temp.plot.line('bo-', ax=ax, linewidth=2)  # a thicker blue line
    title = "Daily Mean 2m Temperature over " + location_desc
    format_timeseries(fig, ax, title)

    plt.show()

if __name__ == "__main__":
    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, 'Code/star-struck/data/download.grib')

    ds = load_dataset(file_path)
    # Define Attica region
    lat_min, lat_max = 38.25, 37.70 
    lon_min, lon_max = 23.45, 24.25

    location = {'latitude': (lat_min, lat_max),
                'longitude': (lon_min, lon_max)}
    
    plot_time_series(ds, location, "Attica, Greece")
