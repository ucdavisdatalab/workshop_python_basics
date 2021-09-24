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
- create dataframe from csv file
- inspect structure of dataframe
- learn the pandas/numpy datatypes including missing values
- index and work with Series objects
- index dataframe based on label (loc), integer index (iloc), logical conditions, and [] operator
- concatenate and merge dataframes
- drop columns and rows from dataframes
- change datatypes of columns
- apply function to column and add as new column to dataframe
:::


## Recap

## Packages

When packages are installed, they can be loaded into the python session with
the `import` command. To avoid having to type the full name of the module
we define an alias using the `as` keyword. By convention, the alias for
`numpy` is `np` and the alias for `pandas` is `pd`. 

Lets start by loading in numpy and pandas:

```{code-cell}
import numpy as np
import pandas as pd
```

## Pandas

**Pandas** is a package that provides the **data frame** object. As well as
many functions for working with data, including functions for:
- loading and writing data to/from files and databases
- summarizing data
- handling missing data
- reshaping and transforming data
- subsetting and filtering data
- merging and combining datasets


## Load in data

First, we will load in a dataset from a csv using the `read_csv()` function 
from pandas: 

```{tip} 
You can look at the documentation for this function either online, 
from the python shell using: `help(pd.read_csv)`, or using the ? operator 
in Ipython (or notebook)
```

```{code-cell}
dataset = pd.read_csv() # should the input be a url?
```

We can use the `head()` method to see what we have.
```{code-cell}
dataset.head()
```

Here we see a dataframe, which is the really important part of pandas, which we
will spend lots of time with during this lesson and the next. 
The dataframe is the tool we can merge, join, summarize, etc.

## Dataframes

A **dataframe** is how pandas structures tabular data - data structured as rows
and columns. In general rows are observations, and columns are variables.
Each entry is called a cell.


## Methods for Exploring Dataframes

As with the `head()` method there are many other methods for looking 
at the contents of a pandas dataframe.

`head()` shows the first rows of the dataframe, to see the last rows, use
`tail()`. By default, the the number of rows displayed is 5, this amount
can be modified by passing an optional integer argument to the function call.
Both `head()` and `tail()` accept this optional integer argument.

```{code-cell}
dataset.tail(10)
```
To display the columns of the dataframe we can access the columns attribute
of the dataframe object.

```{code-cell}
dataset.columns
```
```{code-cell}
dataset.info
```

```{code-cell}
dataset.describe()
```

## Missing Values

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
dropping values
dropping columns
Concat 
Join
cleaning
changing datatypes
```{code-cell}
```
