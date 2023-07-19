import os
import xarray as xr

home_dir = os.path.expanduser('~')
file_path = os.path.join(home_dir, 'Code/star-struck/data/download.grib')

ds = xr.open_dataset(file_path, engine='cfgrib')

# Print dimension coordinates of the given dataset

print(ds['time'])

print(ds['step'])

print(ds['latitude'])

print(ds['longitude'])

# Print non dimension coordinates 

print(ds['number'])

print(ds['surface'])

print(ds['valid_time'])
