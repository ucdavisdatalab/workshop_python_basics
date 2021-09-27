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
- drop columns and rows from dataframes
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

**Pandas** is a package that provides objects and many functions for working 
with data. It is very popular and used for tasks such as:
- loading and writing data to/from files and databases
- summarizing data
- handling missing data
- reshaping and transforming data
- subsetting and filtering data
- merging and combining datasets


## Load in data

First, we will load in the dataset from a csv file using the `read_csv`
function from pandas: 

```{tip} 
Most functions in pandas will have documentation describing what the function 
does and how to use it. You can find this documentation online or directly
from the python shell using the built-in help system: `help(pd.read_csv)`.
In IPython environments, you can use `?` either before or after the function
name as a shorthand for the help function: `?pd.read_csv`

This will also work on many objects and classes. 
```

```{code-cell}
df = pd.read_csv("../data/parks_final.csv") 
```

We can use the `head()` method to see what we have.
```{code-cell}
df.head()
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

```{code-cell}
dataset.dtypes
```

## Data Types in python

Python has built-in objects for handling different types of data, including
numeric and non numeric data.

Numeric data can be represented as either an `int` (integer) or `float` object.
An integer is simply a whole number, such as 0, 3, 3000...
When we assign as whole number to a variable, python will use the int class:
```{code-cell}
a = 4
```

We can see the type of an object in python using the `type` function:
```{code-cell}
type(a)
```

We can also explicitly construct an int object in python:
```{code-cell}
b = int(4)
```

Integer objects don't allow for decimal points:
```{code-cell}
b = int(4.5)
b
```

A float (floating point number) stores numeric data with decimal precision:
```{code-cell}
a = 4.7
type(a)
```

Python supports using arithmetic operators on different numeric types by 
automatically altering the more limited type to match. For example:
```{code-cell}
a = 4.7
b = 3
c = a + b
type(c)
```

Additionally, if you divide an integer with another integer in python, you will
get a float:
```{code-cell}
c = 4 / 4
type(c)
```

`bool` short for Boolean is a data type that stores either True or False. 
Booleans are used as values for expressions with yes-or-no responses.
For example:
```{code-cell}
5 < 2
```

In python, text is stored in a String object called `str`. Strings are created
by enclosing a series of characters in quotes, either single or double quotes
can be used.
```{code-cell}
d = "hello world!"
type(d)
```

To convert between data types in python, we use the constructor associated
with each type:
```{code-cell}
a = float(3)
```

Another example:
```{code-cell}
a = str(3)
```

## Data Types in Pandas

Python's built-in data types are very flexible at the cost of precision. 
Numpy provides more control to the programmer by adding many classes for
storing numeric data that can be modified to best match the data, in order
to improve memory and time performance.

Pandas, which is built on top of numpy, incorporates these types and some of
its own.

These include:
- boolean
- int
- float
- complex, 
- datetime
- timedelta
- StringDtype
- python object (including strings)

For **numeric data** pandas supports `int` as well as `float` types.

```{code-cell}
```


These can also be modified to allow for specifying the size of the data in 
bytes.


## Series

Each column in the dataframe is a pandas `Series` object.
A Series is a collection of values that all share the same data type. 
In addition, the values can be access by their integer index, or based
on their label.

It is built on top of the numpy ndarray object, and as such, will
perform much faster than the list object for numerical operations.

## Missing Values

## Indexing Series

## Reindex dataframe (city_year)

## Operating on Series


## Indexing DataFrames
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
