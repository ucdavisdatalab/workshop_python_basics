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

```{code-cell}
:tags: [remove-cell]
import os

os.chdir("..")
```

Data Structures
===============

The previous chapter introduced Python, providing enough background to do
simple computations on data sets. This chapter focuses on the foundational
knowledge and skills you'll need to use Python effectively in the long term.
Specifically, it begins with a deep dive into data structures and data types in
Python and Pandas. Then, it explains how to use this knowledge during data
analysis.

:::{admonition} Learning Objectives
* Create lists, arrays, and Pandas Series
* Check the type and class of an object
* Coerce an object into a different type
* Describe and differentiate `NA`, `NaN`, `Inf`, and `NULL`
* Index sequences with empty, integer, string, and logical arguments
* Negate or combine conditions with logic operations
* Subset DataFrames
* Apply functions across DataFrames and Series objects
* Find and remove missing values in a DataFrame and Series
:::


Getting Started
---------------

### Packages

We will be working with two packages in this chapter, NumPy and Pandas. Start
by using what you learned in {numref}`modules` to load these packages with
their conventional aliases.

```{code-cell}
import numpy as np
import pandas as pd
```

### Loading Data

In the last chapter, you used Pandas to load tabular data into Python.

```{code-cell}
banknotes = pd.read_csv("data/banknotes.csv")
```

Recall that you can select a single column with bracket notation. For the next
little while, you will be working with the `current_bill_value` column. Select
it and assign it to a variable.

```{code-cell}
bill_value = banknotes["current_bill_value"]
```


(arrays-lists-sequences)=
Arrays, Lists, and Other Sequences
----------------------------------

(pandas-series)=
### Pandas Series

Now examine the variable you created.

```{code-cell}
bill_value
```

You may notice that the data looks a little different from how it displays in a
DataFrame. This is a visual clue: instead of being its own DataFrame,
`bill_value` is a Pandas **Series**. Series objects in Pandas are
one-dimensional **arrays**, data elements stored in an ordered sequence. They
also contain additional metadata and a lot of extra functionality. As you will
learn in this chapter, both a Series and a DataFrame allow you to:
* summarize data
* handle missing data
* reshape and transform data
* subset and filter data
* merge and combine data

```{code-cell}
bill_value.name
```

```{code-cell}
bill_value.shape
```


(lists)=
### Lists

In actuality, a Series is just one kind of sequence object available to you in
Python. The most common such object is a **list**. A list is a container for
zero or more values. Its values are called **elements**, and its **length** is
the number of elements it contains. Like a Series, a list is ordered, so it has
a first element, second element, and so on up to the length of the list.

You can make a list by enclosing comma-separated values in square brackets
`[]`, like this:

```{code-cell}
[1, 2, 3]
```

Lists can be empty:

```{code-cell}
[]
```

You can also convert certain objects to lists with `list`:

```{code-cell}
:tags: [output_scroll]
list(bill_value)
```

Unlike a Series, which is built on top of NumPy arrays, the elements of a list
can be qualitatively different. For instance, this list contains a number,
string, and another list (with one element):

```{code-cell}
l = [8, "hello", [4.2]]
l
```

You can get the length of a list with the built-in `len` function:

```{code-cell}
len(l)
```


(indexing)=
### Indexing

Square brackets `[]` also serve as the **indexing operator** in Python. The
indexing operator gets or sets an element of a list based on the element's
position. Python uses **zero-based indexing**, which means the first element of
a data structure is at position 0. The code to get the first element of the
list `l` is:

```{code-cell}
l[0]
```

Likewise, getting the third element is:

```{code-cell}
l[2]
```

The above logic extends to sequences stored inside sequences. Below, we get the
value  stored in the sublist of `l`.

```{code-cell}
l[2][0]
```

You can set the element of a list by assigning a value at that index. So the
code to change the first element of `l` to the string "hi" is:

```{code-cell}
l[0] = "hi"
l
```


(references)=
### References

Assigning values to a list by its index positions is not without complication.
Suppose you assign a list to a variable `x` and then create a new variable,
`y`, from `x`. If you change an element of `y`, it will also change `x`:

```{code-cell}
x = [1, 2]
y = x
y[0] = 10
x
```

This happens because of the way Python handles variables. In Python, variables
point, or **refer**, to a location in your computer's memory. New variables
created from the same data continue to point to that data unless directed
otherwise, and thus operations on separate variables, or **references** can
affect the same data.

The same holds true for Pandas objects. The variable `bill_value` is only a
reference to a portion of the data `banknotes` represents.

We take a **copy** of objects to create a new reference when assigning
variables:

```{code-cell}
x = [1, 2]
y = x.copy()
y[0] = 10
x
```

You can also convert your list to a **tuple** to prevent problems with value
assignments. Tuples operate similarly to lists, but they are **immutable**.
That is, once you create one, you cannot alter it.

```{code-cell}
x = [1, 2]
y = x
x = tuple(x)
y[0] = 10
x
```

To check what kind of object, or **class**, a variable represents, use the
built-in `type` function.

```{code-cell}
type(y)
```

```{code-cell}
type(x)
```

```{code-cell}
type(bill_value)
```


(data-types)=
Data Types
----------

Recall that a list can contain qualitatively different objects, whereas a
Series cannot. What happens, then, if you were to convert `l` into a Series?

```{code-cell}
pd.Series(l)
```

Notice that the `dtype` value, which applies to all values in the Series, is
`object`. This is a Pandas catchall for columns with mixed data types and for
ones with strings. Why did converting `l` to a Series change the data type?

To answer this, you need to know about how Python handles different types of
data, including numeric and non-numeric data. You already caught a glimpse of
these data types in {numref}`summarizing-data`, when you used `info` to inspect
a DataFrame. Types are listed in the `Dtype` column.

```{code-cell}
banknotes.info()
```

Some of these types are built into Python, while others are specific to Pandas.
Pandas does more work than Python to ensure consistency and specificity across
data types. This is because Pandas is built around NumPy, which provides more
control to the programmer by adding extra data types to best match programming
tasks. This also comes with improved memory and time performance.

A list of data types that you will often encounter in data analysis is below.
Entries marked with \* are NumPy/Pandas extensions to base Python types.
* Boolean
* Integer
* Float
* String
* Complex
* Datetime\*
* Time Delta\*
* StringDtype\*
* Object\*


(numeric-types)=
### Numeric Types

From `banknotes.info()` we learn that `current_bill_value` has an `int64` type.
Integers are one of the two ways that Python stores numeric data. When storing
whole numbers, such as 0, 3, 3000, etc., Python uses integers

The `64` part is an add-on from Pandas. Here, `64` refers to the number of bits
used to store the data, which in turn affects the range of numbers a variable
can hold. Normally though, Python just records the `int`, as in the case below,
where we use `type` to identify a data type:

```{code-cell}
type(4)
```

Typically, `int` numbers are 32 bits.

Why is bit size important? Consider the fact that a 64-bit integer can hold
values between -9,223,372,036,854,775,808 and 9,223,372,036,854,775,807,
whereas a 16-bit integer covers everything between -32,768 and 32,767. Knowing
this information really matters when you're working with large numbers. Without
that knowledge, you might assign 32,768 to an `int16` variable and find that
you've caused an **overflow** error.

The same holds for instances where you need a certain amount of precision in
your data. For example, Python and NumPy have the ability to represent
irrational numbers, like pi. Ultimately, your computer has to represent such
numbers with decimal values, so the number of decimal places a variable can
hold will affect what pi "means" in your code:

```{code-cell}
np.pi
```

The above is an example of a `float` (for floating point number) type. Use this
when you need decimal precision of any kind:

```{code-cell}
banknotes["bill_count"]
```

You can explicitly construct both numeric data types in Python. Here is an
integer:

```{code-cell}
n = int(4)
```

Importantly, this doesn't allow for decimal points:

```{code-cell}
n = int(4.67)
n
```

The `float` constructor will, however:

```{code-cell}
n = float(4.67)
n
```

Though `int` won't accept a decimal, you can perform arithmetic operations
across numeric types. For example, multiply `current_bill_value` by one and a
half times its current value:

```{code-cell}
bill_value * 1.5
```

Notice that the `dtype` has changed from `int64` to `float64`. Python does this
automatically, converting the more limited data type to match the more complex
one. In this case, that means converting integers, which can't hold decimals,
to floats, which can.


(booleans)=
### Booleans

The most limited data type is `bool`, or a Boolean. It is a logical value that
stores either True or False. Booleans are commonly used for expressions with
yes-or-no responses, or for storing the state of your code. 

```{code-cell}
banknotes["has_portrait"]
```

```{code-cell}
coded_in_java = False
type(coded_in_java)
```

(strings)=
### Strings

String objects, or `str`, are the most complex data type. They have the most
attributes and methods associated with them, and they also take up the most
amount of memory.

Use double `"` or single `'` quotes to construct a string:

```{code-cell}
"Hello, world!"
```

Back in Pandas, strings are stored under the `object` data type.

```{code-cell}
banknotes["name"]
```

This is because strings aren't fixed-length sequences, like numbers are. So
Pandas has to provide extra room for the possibility that a string will become
shorter or longer.


(coercion-and-conversion)=
### Coercion and Conversion

Since arrays like a Series have to contain the same data type throughout,
Pandas will automatically convert all elements in a Series to an `object` when
even just one element is a string. This is known as implicit **type coercion**.
It's why all the components of the list `l` became `objects`.

You've actually seen a few examples of this already. Multiplying the `int64`
Series `bill_value` by the `float` 1.5 produced `float` numbers. The same holds
for:

```{code-cell}
8 / 0.25
```

And:

```{code-cell}
True + 2
```

In the above, Python converts `True` to `1` and then performs the arithmetic.

**Type conversion** is when you change an object's data type in an explicit
manner.

```{code-cell}
b = int(4.5)
b
```

...is the example you saw earlier. Here is another:

```{code-cell}
bool(0)
```

And one more:

```{code-cell}
str(105)
```

Python can even read strings like numbers and Boolean values:

```{code-cell}
float("7.3")
```

```{code-cell}
bool("True")
```

Note however that such operations have to be logically sound. This will not
work:

```{code-cell}
:tags: [raises-exception]
int("Hello world!")
```

(comparison-operators)=
### Comparison Operators

Programming tasks often involve comparing variables. Use **comparison
operators** to do so.

| Symbol | Meaning                  |
| :----: | :----------------------- |
| `<`    | less than                |
| `>`    | greater than             |
| `<=`   | less than or equal to    |
| `>=`   | greater than or equal to |
| `==`   | equal to                 |
| `!=`   | not equal to             |

Notice that the "equal to" operator is two equal signs. This is to distinguish
it from the assignment `=` operator.

```{code-cell}
sum(bill_value) < 10000
```

```{code-cell}
bill_value == banknotes["current_bill_value"]
```

```{code-cell}
bill_value % 25 != 0
```

```{code-cell}
parks = pd.read_csv("data/parks_final.csv")
```

## Series

Each column in the DataFrame is a Pandas `Series` object.
A Series is a collection of values that all share the same data type. 
In addition, each value has a label, these labels don't need to be unique
and by default are integers starting at 0.

It is built on top of the NumPy ndarray object, and as such, will
perform much faster than the list object for numerical operations.

Lets look at the year column of our data. We can access it with the following:
```{code-cell}
year = parks["year"].copy()
```

In this case, we have assigned a copy of the year column from the parks 
dataframe to a variable we call year. If we didn't use the copy method,
then modifications we made to year, would also modify that column
in the DataFrame. This way, we can make changes without effecting
the original.

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

There are three main methods for accessing specific values in Pandas:
1. by integer position
2. by label/name
3. based on a boolean array

These methods apply to Series, and as we will see later, to DataFrames.

### Selecting Values By Integer Position

To access elements in a Series by integer position, use the `iloc` attribute:
```{code-cell}
year.iloc[33]
```
We can also pass a list or array of integer locations:
```{code-cell}
year.iloc[[33,0,23]]
```
As with lists, we can use Python's slice operator:
```{code-cell}
year.iloc[3:10]
```

### Selecting Values By Label

A Series in Pandas has labels attached to each value, in what Pandas calls
the index. 
We can see the index of a Series with the `index` attribute:
```{code-cell}
year.index
```
Here we see that the index the index is a collection of integers. 
We can change that to something a little more descriptive.
```{code-cell}
year.index = parks["city"]
year.index
```

To access elements based on label or name, we use the `loc` attribute:
```{code-cell}
year.loc["St. Paul"]
```

Notice that there were multiple values that matched with that label, so the
Series returned all of them.

We can also pass a list or array of labels:
```{code-cell}
year.loc[["St. Paul", "Mesa", "Fresno"]]
```

Additionally, Pandas supports the more conventional `[]` operator, directly
on Series.
We can pass labels to this operator:
```{code-cell}
year[["Irvine", "San Diego"]]
```

### Selecting Values Based On A Boolean Array

The third way to select values is based on a Boolean array. 
The Boolean array must have the same length as the number of elements
in the Series.

This is a really powerful method, that ties in well with functions that 
create Boolean Series.

For example, with the example from earlier:
```{code-cell}
year.loc[year > 2014]
```
The `[]` operator also accepts Boolean Series:
```{code-cell}
year[year > 2014]
```

(indexing-dataframes)=
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

A more elegant approach to the above is to use:
```{code-cell}
parks.loc[parks["state"] == "California", ["city", "pop2020"]]
```

## Special Values

Often times, the data we have will work with has missing, or invalid data.
Its important to understand these values, and how to work with them in Pandas.

There are many reasons that could cause these values to be missing or incomplete,
and as a result, Pandas provides lots of flexibility for detecting and handling
these values.

In Pandas, these special values, are generally treated as missing values
in the dataset, and are represented by the NumPy `nan` type. This reduces
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

Be aware that `None` is a Python object, and in the above example, the 
datatype of the series became 'object'. If we specify a datatype explicitly
then Pandas will convert it to one of its representations:
```{code-cell}
pd.Series([1.5,2.0,3, None], dtype="float")
```

Be aware that `None` is a Python object, and in the above example, the 
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

When reading data from a CSV file, Pandas will automatically detect missing 
values. 
By default, it will convert any empty cell, or string such as 'na', 'nan', 'null',
'N/A', and other variants to NaN.
A full list can be found in the Pandas documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html


### Detecting Missing Values

To detect missing values, Pandas provides two complementary methods - 
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

Pandas also provides a shortcut with the `dropna` method:
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


