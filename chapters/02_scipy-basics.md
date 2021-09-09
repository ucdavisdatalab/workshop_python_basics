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
- describe numpy and pandas packages
- create numpy ndarrays
- create dataframe from csv file
- inspect structure of dataframe
- handle missing values in dataframe
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

## Numpy

**NumPy** (Numerical Python) is a package that provides functions and 
data structures for working with numerical data. NumPy functions are generally 
more intuitive, and more computationally efficient for working with lots 
of numbers than Python's built-in options. It has become the standard for 
working with numeric data in python.

## Numpy Arrays

NumPy provides an **array** object. Arrays are a critical data structure for
working with numerical data and some version of array can be found in pretty
much every commonly used programming language. NumPy's array is different from 
the python list object in that each element needs to be the same data type, 
and its size is set on its creation.

If you are working in python for data analysis, data science, 
machine learning, etc. you will run into numpy arrays. 

There are several ways to create an ndarray. In this case we will use a 
list (built-in python object) of numbers as the input for our array creation:
```{code-cell}
arr = np.array([1, 3, 9, 2])
arr
```

We can see the number of elements in the array with the `shape` attribute:
```{code-cell}
arr.shape
```

The `shape` attribute reflects the number of elements in each **dimension** of
the ndarray. In this case, there are four elements and only one dimension.

**Dimensions** refers to the number of **axes** that represents the data. For 
example if you are working with lat/long coordinates you will probably
have 2 dimensions in your data. If working with images you may have 3 
dimensions: x,y and color.

To see the number of of dimensions of the array object use `ndim`:
```{code-cell}
arr.ndim
```

As mentioned earlier, unlike python's built-in list type, each element
in an ndarray are the same data type. Recall that we created this array,
we did not specify a data type for numpy to use. As a result, numpy inferred
a data type from values in the list. We can access the datatype from
the `dtype` attribute of the array:
```{code-cell}
arr.dtype 
```

To explicitly define the datatype you want for the array you create, pass
the dtype parameter when creating the array:
```{code-cell}
arr = np.array([1, 3, 9, 2], dtype=np.int8)
arr 
```

```{Note}
For reference here is a list of common datatypes in data analysis:
- bool
- int
- float
- datetime
- string
- object
```

## Indexing Numpy Arrays

To access an element from the array use the `[]` operator:
```{code-cell}
display(arr)
arr[3]
```

We can access more than one element with python slicing:
```{code-cell}
display(arr)
arr[1:3:1]
```

We can use integer arrays as indexes:
```{code-cell}
display(arr)
arr[[1,2,0]]
```

We can also use boolean arrays as indexes:
```{code-cell}
display(arr)
arr[[True,False,True,True]]
```

We can use indexing to modify the selected elements:
```{code-cell}
display(arr)
arr[3] = 78
arr[[1,2]] = [0,9]
arr
```

Notice what happens when we pass a value that is not an integer:
```{code-cell}
display(arr)
arr[3] = 7.8
arr
```

NumPy has converted 7.8 to an integer before entering it into the array. This
will only work if there is an accepted way of converting to integer, for 
example it will fail if something like this is passed:
```{code-cell}
try:
    arr[3] = "hello"
except ValueError as e:
    print(e)
```

## Operating on NumPy Arrays

In general, operations are applied element by element on the array:
```{code-cell}
display(arr)
arr * 2
```

Another example but with comparison operators:
```{code-cell}
display(arr)
arr > 3
```

This fits in nicely with indexing using boolean array from before:
```{code-cell}
display(arr)
arr[arr>3]
```

## Multi Dimensional Arrays + Other Ways to Create Arrays

Now let us see some of these concepts with a 2-D array. As before, we can
define a 2-D array by passing a python list as input:
```{code-cell}
arr = np.array([[1,2], [3,4]], dtype=np.int8)
```

Here is another way of initializing an array:
```{code-cell}
arr = np.zeros((3,4), dtype=np.float64)
arr
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
