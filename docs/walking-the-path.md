# Walking The Path

## Intro

## Learnings

### Libraries

Info regarding libraries that are used throughout this course.

#### Matplotlib

It is one of the core Python packages for data visualization and is used by many spatial and non-spatial packages to create charts and maps.

Documentation [here](https://matplotlib.org/stable/index.html),
cheat sheets [here](https://matplotlib.org/cheatsheets/).

Most of the functionality is available in the pyplot submodule. There are two important important objects:

* [Figure](https://matplotlib.org/stable/api/figure_api.html): This is the main container of the plot. A figure can contain multiple plots inside it
* [Axes](https://matplotlib.org/stable/api/axes_api.html): The Axes class represents one (sub-)plot in a figure. It contains the plotted data, axis ticks, labels, title, legend, etc. Its methods are the main interface for manipulating the plot. 

#### Numpy

NumPy is the fundamental package for scientific computing in Python. 

User guide [here](https://numpy.org/doc/stable/user/index.html#user), absolute basics [here](https://numpy.org/doc/stable/user/absolute_beginners.html)

**Useful methods**

**np.exp**: Calculate the exponential of all elements in the input array. Ref [here](https://numpy.org/doc/stable/reference/generated/numpy.exp.html).

#### Pandas

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





## Questions

## Notes

## Future Work