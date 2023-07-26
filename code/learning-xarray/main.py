import os
import xarray as xr
import matplotlib.pyplot as plt

import matplotlib.dates as mdates

home_dir = os.path.expanduser('~')
file_path = os.path.join(home_dir, 'Code/star-struck/data/download.grib')

ds = xr.open_dataset(file_path, engine='cfgrib')

# Print dimension coordinates of the given dataset
#
#print(ds['time'])
#
#print(ds['step'])
#
#print(ds['latitude'])
#
#print(ds['longitude'])
#
## Print non dimension coordinates 
#
#print(ds['number'])
#
#print(ds['surface'])
#
#print(ds['valid_time'])
#
# Exercise 1.1: Plot time series for a specific location

# Select Attica 
lat_min, lat_max = 38.25, 37.70 
lon_min, lon_max = 23.45, 24.25
subset = ds.t2m.sel(latitude=slice(lat_min, lat_max), longitude=slice(lon_min, lon_max))

mean_temp = subset.mean(dim=['latitude', 'longitude'])

mean_temp = mean_temp.mean(dim=['step'])

mean_temp.plot.line()
# Here we use plt.gca() (Get Current Axes) to get the axes object and then modify it
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Set major ticks every day
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Set format
plt.xticks(rotation=45)  # Rotate labels for readability

plt.title('Mean temperature over time')
plt.ylabel('Temperature (Kelvin)')
plt.show()
# Dataset methods
# print(ds.t2m.dims)

# print(ds.t2m.coords)

# print(ds.t2m.data)

# subset.plot()

# plt.show()
