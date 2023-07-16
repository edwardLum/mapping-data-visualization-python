# Walking The Path

## Intro

## Libraries

### Matplotlib

It is one of the core Python packages for data visualization and is used by many spatial and non-spatial packages to create charts and maps.

Documentation [here](https://matplotlib.org/stable/index.html),
cheat sheets [here](https://matplotlib.org/cheatsheets/).

Most of the functionality is available in the pyplot submodule. There are two important important objects:

* [Figure](https://matplotlib.org/stable/api/figure_api.html): This is the main container of the plot. A figure can contain multiple plots inside it
* [Axes](https://matplotlib.org/stable/api/axes_api.html): The Axes class represents one (sub-)plot in a figure. It contains the plotted data, axis ticks, labels, title, legend, etc. Its methods are the main interface for manipulating the plot. 

### Numpy

NumPy is the fundamental package for scientific computing in Python. 

User guide [here](https://numpy.org/doc/stable/user/index.html#user), absolute basics [here](https://numpy.org/doc/stable/user/absolute_beginners.html)

**Useful methods**

**np.exp**: Calculate the exponential of all elements in the input array. Ref [here](https://numpy.org/doc/stable/reference/generated/numpy.exp.html).

### Pandas

**Data Structures**

Guide page [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#basics-dataframe)

**Data Frames**

DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects. Reference [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) and user guide [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#basics-dataframe).

Useful methods:

**df.groupby**: Dataframe method to group by given column. Documentation [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html), check user guide for examples [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html). 

By “group by” we are referring to a process involving one or more of the following steps:

* Splitting the data into groups based on some criteria.
* Applying a function to each group independently.
* Combining the results into a data structure.

**pd.concat**: Concatenate a list of data frames. Documentation [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

##Further Reading

[Categorical Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#categorical): Categoricals are a pandas data type corresponding to categorical variables in statistics. A categorical variable takes on a limited, and usually fixed, number of possible values (categories; levels in R). Examples are gender, social class, blood type, country affiliation, observation time or rating via Likert scales.

[dtypes](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes): For the most part, pandas uses NumPy arrays and dtypes for Series or individual columns of a DataFrame. NumPy provides support for float, int, bool, timedelta64 and datetime64(note that NumPy does not support timezone-aware datetimes).

## APIs

### CDS

The Climate Data Store (CDS) Application Program Interface (API) is a service providing programmatic access to CDS data. Instructions on how to use the API [here](https://cds.climate.copernicus.eu/api-how-to).

## Questions

## Exercises

###Exercise 1.

1. Download data temparature from [here](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form)
2. Read data with Xarray
3. Plot time series for a specific location
4. Rescale to daily temparature
5. Min, Max, Mean
6. Save only min, max, mean
7. Find mean day/night temp 

## Notes

## Future Work