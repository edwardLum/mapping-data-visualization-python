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

Useful methods:

* [pyplot.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html): To manipulate individual properties of an ax when dealing with subplots.

* [subplots_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html): To adjust they layout parameters of a subplot.

### Numpy

NumPy is the fundamental package for scientific computing in Python. 

User guide [here](https://numpy.org/doc/stable/user/index.html#user), absolute basics [here](https://numpy.org/doc/stable/user/absolute_beginners.html)

Vectorization describes the absence of any explicit looping, indexing, etc., in the code - these things are taking place, of course, just “behind the scenes” in optimized, pre-compiled C code.

Broadcasting is the term used to describe the implicit element-by-element behavior of operations; generally speaking, in NumPy all operations, not just arithmetic operations, but logical, bit-wise, functional, etc., behave in this implicit element-by-element fashion, i.e., they broadcast. Moreover, in the example above, a and b could be multidimensional arrays of the same shape, or a scalar and an array, or even two arrays of with different shapes, provided that the smaller array is “expandable” to the shape of the larger in such a way that the resulting broadcast is unambiguous. For detailed “rules” of broadcasting see [Broadcasting](https://numpy.org/devdocs/user/basics.broadcasting.html#basics-broadcasting).

Worth checking this [visual guide](https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d) in Medium

**Useful methods**

**np.exp**: Calculate the exponential of all elements in the input array. Ref [here](https://numpy.org/doc/stable/reference/generated/numpy.exp.html).

**Data types**

**timedelta64**: The timedelta64 data type is a part of the numpy library, which xarray builds upon. It represents a time interval or a duration of time.

The timedelta64 data type requires a unit of time (for example, days, hours, minutes, seconds, etc.), and can be used to perform arithmetic operations involving time. This makes it very useful for handling time-series data. Doc [here](https://numpy.org/doc/stable/reference/arrays.datetime.html).

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

### Xarray

Xarray introduces labels in the form of dimensions, coordinates and attributes on top of raw NumPy-like multidimensional arrays, which allows for a more intuitive, more concise, and less error-prone developer experience. User guide [here](https://docs.xarray.dev/en/stable/user-guide/index.html)

**Data Array**

A multi-dimensional array with labeled or named dimensions. DataArray objects add metadata such as dimension names, coordinates, and attributes (defined below) to underlying “unlabeled” data structures such as numpy and Dask arrays. If its optional name property is set, it is a named DataArray.

**Data Set**

A dict-like collection of DataArray objects with aligned dimensions. Thus, most operations that can be performed on the dimensions of a single DataArray can be performed on a dataset. Datasets have data variables (see Variable below), dimensions, coordinates, and attributes.

## APIs

### CDS

The Climate Data Store (CDS) Application Program Interface (API) is a service providing programmatic access to CDS data. Instructions on how to use the API [here](https://cds.climate.copernicus.eu/api-how-to), macOS specific [here](https://confluence.ecmwf.int/display/CKB/How+to+install+and+use+CDS+API+on+macOS).

Building a query [here](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form)

##Further Reading

[Categorical Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#categorical): Categoricals are a pandas data type corresponding to categorical variables in statistics. A categorical variable takes on a limited, and usually fixed, number of possible values (categories; levels in R). Examples are gender, social class, blood type, country affiliation, observation time or rating via Likert scales.

[dtypes](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes): For the most part, pandas uses NumPy arrays and dtypes for Series or individual columns of a DataFrame. NumPy provides support for float, int, bool, timedelta64 and datetime64(note that NumPy does not support timezone-aware datetimes).

## Questions

## Exercises

###Exercise 1.

1. Download data temperature from [here](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form)
2. Read data with Xarray
3. Plot time series for a specific location
4. Rescale to daily temparature
5. Min, Max, Mean
6. Save only min, max, mean
7. Find mean day/night temp 

**Data Structure**

Dimension Coordinates:

* Time
* Steps
* Longitude
* Latitude

Non-dimensions Coordinates:

* Valid Time
* Surface
* Ensemble member numerical id

## Notes

## Future Work