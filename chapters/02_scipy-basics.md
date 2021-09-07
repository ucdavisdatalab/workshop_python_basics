---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

Scientific Python
=================

:::{admonition} Learning Objectives
- review python basics
- describe numpy and pandas packages
- create and explore dataframes
- learn ways to index dataframes
:::


## Recap

## Packages

```{code-cell}
import numpy as np
import pandas as pd
```

## Numpy

**NumPy** is a package that provides functions and data structures for working
with numerical data. NumPy functions are generally more intuitive, and more
computationally efficient for working with lots of numbers than Python's
built-in options. 

NumPy provides an **array** object. Arrays are a critical data structure for
working with numerical data and some version of array can be found in pretty
much every commonly used programming language. NumPy's array is different from 
the python list object in that each element needs to be the same data type, 
and its size is set on its creation.

If you are working in python for data analysis, data science, 
machine learning, etc. you will run into numpy arrays. 

WHEN TO INTRODUCE FUNCTION VS METHOD VS ATTRIBUTE?


```{code-cell}
arr = np.array( [1, 3, 9, 2])
print(arr)
print(arr.dtype)  
print(arr.shape)
arr = np.array( [1, 3, 9, 2], dtype=np.float64)
```

## Pandas

**Pandas** is a package that provides the **data frame** object. As well as
many functions for working with data, including functions for:
- loading and writing data to/from files and databases
- merging datasets
- summarizing data
- handling missing data
- reshaping and transforming data
- subsetting and filtering data


## Load in data

First, we will load in a dataset from a csv using the `read_csv()` function 
from pandas. 

```{tip} 
You can look at the documentation for this function either online
or from the python shell using: `help(pd.read_csv)`
```

```{code-cell}
dataset = pd.read_csv() # should the input be a url?
```

We can use the `head()` **method** to see what we have.
```{code-cell}
dataset.head()
```

Here we see a dataframe, which is the really important part of pandas, which we
will spend lots of time with. The dataframe is the tool we can merge, join,
summarize, etc.

## Dataframes

A dataframe is how pandas structures tabular data - data structured as rows
and columns.

## Methods for Exploring Dataframes

As with the `head()` method there are many other methods for looking 
at the contents of a pandas dataframe.

```{code-cell}
dataset.tail()
```
```{code-cell}
dataset.describe()
```
```{code-cell}
dataset.columns
```
```{code-cell}
dataset.info
```

## Data Types
```{code-cell}
dataset.dtypes
```

## Indexing
```{code-cell}
dataset.loc # label based or boolean array
dataset.iloc # interger based
dataset[colname]
dataset[[colnames]]
dataset[colname][4]
```

## Modiying DataFrames
Concat
Join
cleaning
changing datatypes
```{code-cell}
```

## Grouping
