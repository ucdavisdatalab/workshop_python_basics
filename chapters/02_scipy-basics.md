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
- create DataFrame from csv file
- inspect structure of DataFrame
- learn python and pandas data types
- index Series, using integer position, labels, and booleans
- index DataFrame 
- find and remove missing values in a Series and DataFrame
- make modifications to a DataFrame
- save a DataFrame to csv
:::


## Recap 
### Packages

When packages are installed, they can be loaded into the python session with
the `import` command. To avoid having to type the full name of the module
we define an alias using the `as` keyword. By convention, the alias for
`numpy` is `np` and the alias for `pandas` is `pd`. 

Lets start by loading in numpy and pandas:

```{code-cell}
import numpy as np
import pandas as pd
```

### pandas

**pandas** is a package that provides objects and many functions for working 
with data. It is very popular and used for tasks such as:
- loading and writing data to/from files and databases
- summarizing data
- handling missing data
- reshaping and transforming data
- subsetting and filtering data
- merging and combining datasets


### Load in data

First, we will load in the dataset from a csv file using the `read_csv`
function from pandas: 

:::{Tip} 
Most functions in pandas will have documentation describing what the function 
does and how to use it. You can find this documentation online or directly
from the python shell using the built-in help system: `help(pd.read_csv)`.
In IPython environments, you can use `?` either before or after the function
name as a shorthand for the help function: `?pd.read_csv`

This will also work on many objects and classes. 
:::

```{code-cell}
parks = pd.read_csv("../data/parks_final.csv") 
```

We can use the `head` method to see what we have.
```{code-cell}
parks.head()
```

Here we see a DataFrame, which is the really important part of pandas, which we
will spend lots of time with during this lesson and the next. 
The dataframe is the tool we can merge, join, summarize, etc.

## DataFrames

A **DataFrame** is how pandas structures tabular data - data structured as rows
and columns. In general rows are observations, and columns are variables.
Each entry is called a cell.


### Methods for Exploring DataFrames

As with the `head` method there are many other methods for looking 
at the contents of a pandas DataFrame.

`head` shows the first rows of the DataFrame, to see the last rows, use
`tail`. By default, the number of rows displayed is 5, this amount
can be modified by passing an optional integer argument to the function call.
Both `head` and `tail` accept this optional integer argument.

```{code-cell}
parks.tail(10)
```
To display the columns of the DataFrame we can access the columns attribute
of the DataFrame object.

```{code-cell}
parks.columns
```

To see information about a DataFrame and its content:
```{code-cell}
parks.info()
```

To get some summary statistics about the values of a DataFrame:
```{code-cell}
parks.describe()
```

To see the data types of a DataFrame:
```{code-cell}
parks.dtypes
```

## Data Types

### Built-In Python

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

### In Pandas

Python's built-in data types are very flexible at the cost of precision. 
Numpy provides more control to the programmer by adding many classes for
storing numeric data that can be modified to best match the data, in order
to improve memory and time performance.

pandas, which is built on top of numpy, incorporates these types and some of
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

Each column in the DataFrame is a pandas `Series` object.
A Series is a collection of values that all share the same data type. 
In addition, each value has a label, these labels don't need to be unique
and by default are integers starting at 0.

It is built on top of the numpy ndarray object, and as such, will
perform much faster than the list object for numerical operations.

Lets look at the year column of our data. We can access it with the following:
TODO: explain
```{code-cell}
year = parks["year"].copy()
```

TODO: show index, show values

As with DataFrames, there are several functions for exploring series.

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

To see just the unique set of values we can use the `unique` method:
```{code-cell}
year.unique()
```

Another very useful summary is `value_counts`:
```{code-cell}
year.value_counts()
```

Series are powerful because we can apply operations on them in an element wise
fashion very easily and efficiently. For example:
```{code-cell}
year + 10
```

In addition, we can also use comparison operators:
```{code-cell}
year > 2014
```

### Indexing Series

pandas `Series` provide multiple methods for accessing values of a Series
based on label or value. The main ways are the `iloc` attribute for accessing
values based on their integer location and the `loc` attribute for accessing
values based on their labels. In addition, Series can be indexed with
the `[]` operator, in a way similar to what we saw with python lists. 

To see the labels of our Series we use the `index` attribute:
```{code-cell}
year.index
```

We can modify this to use a different set of labels:
```{code-cell}
year.index = parks["city"]
```

#### iloc
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

Lastly, with `iloc`, we can pass a boolean list or array. Recall that the 
comparison operator returned a series, so we need to extract just the values,
which we can do with the .values attribute:
```{code-cell}
year.iloc[(year > 2014).values]
```

#### loc
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
year.loc[(parks["state"] == "California").values]
```
#### []

Pandas also supports selecting values form the Series using the `[]` operator.
The behavior is somewhat complex, and is inherently less clear than the `iloc`
or `loc` attributes described above.

We can access elements by passing a single label or list of labels:
```{code-cell}
year[["Irvine", "San Diego"]]
```
We can also use a boolean array or list:
```{code-cell}
year[(parks["pop2010"] > 500000).values]
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


## Indexing DataFrames

Conceptually, indexing DataFrames is very similar to the operations on Series. 
However, whereas Series are one dimensional, DataFrames are two dimensional.
A DataFrame is a collection of Series, organized as columns.

As with Series, we can use `iloc` to select rows based on their integer 
position:
```{code-cell}
parks.iloc[[300, 200, -1]]
```

And we can use `loc` to select based on label, in this case the label is 
also integers:
```{code-cell}
parks.loc[732]
```

Again, as with Series, we can use boolean arrays or lists to index:
```{code-cell}
parks.loc[parks["state"] == "California"]
```

This also works with just the `[]` operator:
```{code-cell}
parks[parks["state"] == "California"]
```

:::{Note}
Be careful when passing a bool Series to either `[]` or `loc` that the indexes 
of the bool Series and the DataFrame match. 
For example we would get an error if we were to attempt to run:

```
parks[year > 2020]
```
:::

To use a boolean array or list with `iloc` be sure to pass only the values:
```{code-cell}
parks.iloc[(parks["state"] == "California").values]
```

To access columns from a DataFrame, we use the `[]` operator, as we have 
already seen:
```{code-cell}
parks["pop2020"]
```

We can also pass a list of column names, in any order:
```{code-cell}
parks[["pop2020", "city"]]
```

If we select a single column from the DataFrame, we get a Series, 
which we can index as we saw before:
```{code-cell}
parks["pop2020"].iloc[1:10]
```

So, to combine with what we saw before with boolean indexing:
```{code-cell}
parks[["city", "pop2020"]].loc[parks["state"] == "California"]
```

We can combine multiple conditions with the `&` operator, note 
the paranthesis around the expressions:
```{code-cell}
parks[["city", "pop2020"]].loc[(parks["state"] == "California") & (parks["year"] == 2020)] 
```

## Special Values

Often times, the data we have will work with has missing, or invalid data.
Its important to understand these values, and how to work with them in Pandas.

There are many reasons that could cause these values to be missing or incomplete,
and as a result, Pandas provides lots of flexibility for detecting and handling
these values.

In Pandas, these special values, are generally treated as missing values
in the dataset, and are represented by the Numpy `nan` type. This reduces
some of the nuance of data values and types, but was seemingly done
for computational preformance reasons.

### Types of Values Considered Missing by Pandas

In addition to `np.nan` (which displays as NaN), Pandas interprets 
several other values as missing. 
This includes Python's `None` type, as well as Pandas' experimental `NA` types.

Python's `None` type represents something that has no value. 
It often comes about as the return of a function, if something hasn't
been defined yet, or if something wasn't found.

When creating a Series, we can pass this value:
```{code-cell}
pd.Series([None, "one", "two"])
```

Be aware that `None` is a python object, and in the above example, the 
datatype of the series became 'object'. If we specify a datatype explicitly
then Pandas will convert it to one of its representations:
```{code-cell}
pd.Series([1.5,2.0,3, None], dtype="float")
```

Be aware that `None` is a python object, and in the above example, the 
datatype of the series became 'object'. If we specify a datatype explicitly
then Pandas will convert it to one of its representations:
```{code-cell}
pd.Series(["the", "and", None], dtype="string")
```

### Reading in Missing Values from a CSV file

An obvious source of missing or incomplete values is the data itself. 
When the data was collected, there may have been reasons to code missing data.
For example, in collection of survey responses, there may be times where the 
answer was not applicable. 
Another example would be if a measurement was not taken on some of the samples. 
Obviously, there are no rules on how this was represented in the data set. 
However there are several conventions, and Pandas is aware of many of them. 

When reading data from a csv file, Pandas will automatically detect missing 
values. 
By default, it will convert any empty cell, or string such as 'na', 'nan', 'null',
'N/A', and other variants to NaN.
A full list can be found in the pandas documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html


### Detecting Missing Values

To detect missing values, pandas provides two complementary methods - 
`isna` and `notna`.

We can see information about missing values with the `count` method on 
DataFrames:
```{code-cell}
parks.count()
```

If we look at the `park_benches` columns of the DataFrame, we can see what 
those missing values look like.
```{code-cell}
pb = parks["park_benches"]
pb.count()
```

The return of `isna` is a boolean Series indicating which of the values 
are considered missing:
```{code-cell}
pb.isna()
```

The reverse - to see which values are not considered missing - is returned 
with `notna`:
```{code-cell}
pb.notna()
```

### Replacing Missing Values

We can use this boolean Series to subset. 
For example, to keep only the values that aren't missing:
```{code-cell}
pb.loc[pb.notna()]
```

pandas also provides a shortcut with the `dropna` method:
```{code-cell}
pb.dropna()
```

Another strategy may be to fill the missing values. We could do so using the 
`fillna` method:
```{code-cell}
pb.fillna(-1)
```

Additionally, the data set may have its own indicator for missing values, 
e.g "" or 0. We can convert those to missing using the `replace` method:
```{code-cell}
pb.replace(-1, np.nan)
```
