import os
import xarray as xr

home_dir = os.path.expanduser('~')
file_path = os.path.join(home_dir, 'Code/star-struck/data/download.grib')

geo_data = xr.open_dataset(file_path, engine='cfgrib')

