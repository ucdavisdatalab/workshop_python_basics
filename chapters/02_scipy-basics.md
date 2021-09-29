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

For `int` and `float` data, in pandas we can specify the number the size of
the int or float, such as int64 -> a 64 bit integer.


## Series

Each column in the dataframe is a pandas `Series` object.
A Series is a collection of values that all share the same data type. 
In addition, each value has a label, these labels don't need to be unique
and by default are integers starting at 0.

It is built on top of the numpy ndarray object, and as such, will
perform much faster than the list object for numerical operations.

Lets look at the year column of our data. We can access it with the following:
```{code-cell}
year = dataset["year"]
```

As with dataframes, there are several functions for exploring series.

To get the first values, we can once again use `head`:
```{code-cell}
year.head()
```
And again, to get the last values we can use `tail`:
```{code-cell}
year.tail()
```

Since the data is numeric we can also get some summary data:
```{code-cell}
year.describe()
```

Series are powerful because we can apply operations on them in an element wise
fashion very easily. For example:
```{code-cell}
year + 10
```

In addition, we can also use comparison operators:
```{code-cell}
year > 2014
```

## Indexing Series

Pandas `Series` provide multiple methods for accessing values of a Series
based on label or value. The main ways are the `iloc` attribute for accessing
values based on their integer location and the `loc` attritibute for accessing
values based on their labels. In addition, Series can be indexed with
the `[]` operator, in a way similar to what we saw with python lists. 

To see the labels of our Series we use the `index` attribute:
```{code-cell}
year.index
```

We can modify this to use a different set of labels:
```{code-cell}
year.index = dataset["city"]
```

### iloc
`iloc` is an attribute of Series that we use to access elements based on
their integer position. There are multiple values that can be used with `iloc`.

First, we can access elements by passing a single integer:
```{code-cell}
year.iloc[33]
```

We can also pass a list or array of locations:
```{code-cell}
year.iloc[[33,0,23]]
```

As with lists, we can use python's slice operator:
```{code-cell}
year.iloc[3:10]
```

Lastly, with iloc, we can pass a boolean list or array. Recall that the 
comparison operator returned a series, so we need to extract just the values,
which we can do with the .values attribute:
```{code-cell}
year.iloc[(year > 2014).values]
```

### loc
`loc` is an attribute Series that we use to access elements based on their 
label.

First, we can access elements by passing a single label:
```{code-cell}
year.loc["St. Paul"]
```
Notice that there were multiple values that matched with that label, so the
Series returned all of them.

We can also pass a list or array of labels:
```{code-cell}
year.loc[["St. Paul", "Mesa", "Fresno"]]
```
We can use a boolean array or list:
```{code-cell}
year.loc[(df["state"] == "California").values]
```
### []

Pandas also supports selecting values form the Series using the `[]` operator.
The behavior is somewhat complex, and is inherently less clear than the `iloc`
or `loc` attributes described above.

We can access elements by passing a single label or list of labels:
```{code-cell}
year[["Irvine", "San Diego"]]
```
We can also use a boolean array or list:
```{code-cell}
year[(df["pop2010"] > 500000).values]
```
We can pass an integer, but be weary that it will first attempt to match
based on the label. If there are integer labels, then it will match with 
those, and not fall back on integer location. In this case, since the labels
are the city names, it will fall back on integer location, and we can do
most of the same methods as with `iloc`:
```{code-cell}
year[[-1, 0, 500]]
```

```{code-cell}
year[13:24]
```

## Missing Values

## Indexing DataFrames
Columns and rows are indexed separately in pandas.
```{code-cell}
dataset.loc # label based or boolean array
dataset.iloc # integer based or boolean array
dataset[colname]
dataset[[colnames]]
dataset[colname][4]
dataset[colname].loc[4]
```

## Modiying DataFrames
Lets apply what we have learned and tidy up the dataframe:
dropping values
dropping columns
Concat 
Join
cleaning
changing datatypes
```{code-cell}
```

## Saving
