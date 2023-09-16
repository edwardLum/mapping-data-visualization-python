import os

import pandas as pd
import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# [lon_min, lon_max, lat_min, lat_max]
locations = {"Greece": [19.37, 29.57, 34.8, 41.7],
             "Attica": [23.4, 24.3, 37.6, 38.3],}


def plot_temperature_on_ax(ax, data, title, location_extent):    
    """Plot data to ax with title as ax title."""
    ax.set_extent(location_extent)  # loation = lon_min, lon_max, lat_min, lat_max] covering approx. Greece area

    # Plot the mean temperature data
    data.plot(ax=ax, transform=ccrs.PlateCarree(), cmap='RdBu_r', cbar_kwargs={'label': 'Temperature (°C)'})

    # Adding coastlines and land features for better visualization
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.LAND, edgecolor='black')
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.set_title(title)


def load_dataset(filename):
    home_dir = os.path.expanduser('~')
    file_path = os.path.join(home_dir, 'Code/star-struck/data/', filename)

    ds = xr.open_dataset(file_path, engine='cfgrib')

    # Convert temperature to Celcius
    ds['t2m'] -= 273.15

    ds['t2m'].attrs["units"] = "deg C"

    return ds


def process_data(ds):
    
    datasets = {} 

    # Group by and reduce by mean step
    temperature_array = ds["t2m"]

    # Reduce by mean time to get mean monthly temp
    mean_daily_temperature = temperature_array.groupby("time").mean("step")
    mean_temperature = mean_daily_temperature.mean(dim="time")
    datasets["Mean Temperature"] = mean_temperature

    # Same as above for minimum temperature
    min_daily_temperature = temperature_array.groupby("time").min("step")
    min_temperature = min_daily_temperature.min(dim="time")
    datasets["Min Temperature"] = min_temperature

    # Same as above for minimum temperature
    max_daily_temperature = temperature_array.groupby("time").max("step")
    max_temperature = max_daily_temperature.max(dim="time")
    datasets["Max Temperature"] = max_temperature

    # Hourly temperature for a given day 
    hourly_temperature = temperature_array.sel(time="2022-08-02", latitude=40, longitude=22, method="nearest")
    datasets["Hourly Temperature"] = hourly_temperature
    
    return datasets


def plot_graphs(datasets):

    # Plot everything in one figure
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, subplot_kw={'projection': ccrs.PlateCarree()}) 
    
    axes = [ax1, ax2, ax3, ax4]
    axes_and_datasets = [(name, dataset, ax) for (name, dataset), ax in zip(datasets.items(), axes)]
    
    for name, dataset, ax in axes_and_datasets:
        if name != "Hourly Temperature":
             plot_temperature_on_ax(ax, dataset, name, locations["Greece"])
        
        ax.plot(dataset)
        ax.set_title("Hourly temperature on 2022-08-02")
    
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    filename = "download.grib"
    ds = load_dataset(filename)
    datasets = process_data(ds)
    plot_graphs(datasets)
