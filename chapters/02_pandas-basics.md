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
* Create Pandas Series, NumPy arrays, lists, and tuples
* Check the type and class of an object
* Convert an object into a different type
* Describe and differentiate `None`, `NA`, and `NaN`
* Index sequences with empty, integer, string, and logical arguments
* Negate or combine conditions with logic operations
* Subset Series objects and DataFrames
* Find and remove missing values in a DataFrame and Series
:::


Setup
-----

### Packages

We will be working with two packages in this chapter, NumPy and Pandas. Start
by using what you learned in {numref}`modules` to load these packages with
their conventional aliases:

```{code-cell}
import numpy as np
import pandas as pd
```

{numref}`getting-started` described how to use the Pandas package to load a
tabular dataset into a DataFrame. As an example, you saw how to load the
banknotes dataset. You'll need that dataset for the examples in this chapter as
well, so load a fresh copy of it:

```{code-cell}
banknotes = pd.read_csv("data/banknotes.csv")
banknotes.head()
```

Now you're ready for the chapter.


(arrays-lists-sequences)=
Containers for Data
-------------------

A **data structure** is a collection of data organized in a particular way. In
Python, data structures are also called **containers**, because they contain
data. Containers make working with lots of data manageable and efficient.
DataFrames, introduced in the previous chapter, are an example of a
two-dimensional data structure. In this section, you'll learn about several
one-dimensional data structures that are fundamental to programming in Python.


(pandas-series)=
### Pandas Series

Recall that you can select a single column from a DataFrame with the square
brackets `[ ]`. Select the `current_bill_value` column from the banknotes
dataset:

```{code-cell}
banknotes["current_bill_value"]
```

Notice that Python prints the column differently from the `banknotes`
DataFrame. For instance, the length of the column is displayed rather than the
number of rows. This is a visual clue: the column is not a DataFrame. Instead,
it's a Pandas **Series**, a one-dimensional container for values. Every column
in a DataFrame is a Series.

Series and DataFrames are the fundamental data structures for data analysis in
Pandas, and they have many common features. As you'll learn in this chapter,
both allow you to:
* summarize data
* handle missing data
* reshape and transform data
* subset and filter data
* merge and combine data

You'll be working with the `current_bill_value` column for the next few
examples, so go ahead and assign it to a variable:

```{code-cell}
bill_value = banknotes["current_bill_value"]
```

The values in a Series (and many other kinds of data structures) are called
**elements**, and the **length** of a Series is the number of elements it
contains. Series are **ordered**, which means the elements have specific
positions. The 1st element in `bill_value` is `100`, the 2nd element is again
`100`, the 3rd element is `50`, the 4th is `20`, and so on.

You can get the length of a Series and many other types of objects with
Python's built-in `len` function:

```{code-cell}
len(bill_value)
```

A Series can also contain **metadata**, extra information about its elements.
Metadata can usually be accessed through attributes (see
{numref}`objects-attributes`). Here are a few examples of metadata this Series
contains (more on this later):

```{code-cell}
bill_value.name
```

```{code-cell}
bill_value.shape
```

Finally, notice that the elements of `bill_value` are all integers. For any
given Series, the elements will usually all be the same qualitative type of
data (integers, decimal numbers, strings, and so on). In other words, the
elements are usually **homogeneous**. There are some exceptions, and you'll
learn more about element types in {numref}`data-types`.


(numpy-arrays)=
### NumPy Arrays

Under the hood, Pandas Series are based on other data structure, the NumPy
**array** (or `ndarray`). You can think of a NumPy array as a stripped-down
Series: an ordered, one-dimensional container for values without the extra
metadata and functionality.

:::{tip}
Series tend to be a good choice for data analysis, while arrays tend to be a
good choice for sophisticated mathematical computations (such as simulations).
:::

Most examples in this reader use Series and DataFrames, but it will be pointed
out anywhere it's important to use a NumPy array.

You can convert a Series to an array with the `.to_numpy` method:

```{code-cell}
bill_value.to_numpy()
```

Conversely, you can convert an array into a Series with the `pd.Series`
function. You'll see some examples of this function later on.


(lists)=
### Lists

Series and arrays are designed for data analysis and mathematical computations,
respectively. In contrast, a **list** is a general-purpose one-dimensional
container. Lists are built into Python, so they're probably the most common
kind of container, and you don't need to load any modules in order to use them.

You can make a list by enclosing comma-separated values in square brackets
`[]`, like this:

```{code-cell}
x = [1, 2, 3]
x
```

Like a Series, a list is ordered, so it has a first element, second element,
and so on up to the length of the list. You can get the length of a list with
the `len` function:

```{code-cell}
len(x)
```


Lists can be empty:

```{code-cell}
[]
```

You can convert many types objects into lists with the `list` function:

```{code-cell}
:tags: [output_scroll]
list(bill_value)
```

Unlike a Series, the elements of a list can be qualitatively different. There
is no expectation that they will be homogeneous. For instance, this list
contains a number, string, and another list (with one element):

```{code-cell}
li = [8, "hello", [4.2]]
li
```


(indexing)=
### Indexing

So far you've learned two ways to use square brackets `[]`:

1. To select columns from a DataFrame, as in `banknotes["country"]`
2. To create lists, as in `["a", "b", 1]`

The first case is an example of **indexing**, which means getting or setting
elements of a container. The square brackets `[]` are Python's indexing
operator.

You can use indexing to get an element of a list based on the element's
position. Python uses **zero-based indexing**, which means the positions of
elements are counted starting from 0 rather than 1. So the first element of
a list is at position 0, the second is at position 1, and so on.

:::{note}
Many programming languages use zero-based indexing. It may seem strange at
first, but it makes some kinds of computations simpler by eliminating the need
to add or subtract 1.
:::

The indexing operator requires at least one argument, called the **index**,
which goes inside of the square brackets `[]`. The index says which elements
you want to get. For DataFrames, you used column names as the index. For a
list, you can use a position. So the code to get the first element of the list
`li` is:

```{code-cell}
li[0]
```

Likewise, to get the third element:

```{code-cell}
li[2]
```

The same idea extends to containers stored inside of other containers. For
example, to get the value stored in the list inside of `x`:

```{code-cell}
li[2][0]
```

You can set the element of a list by assigning a value at that index. So the
code to change the first element of `x` to the string "hi" is:

```{code-cell}
li[0] = "hi"
li
```


(references)=
### References

Assigning elements of a container is not without complication. Suppose you
assign a list to a variable `x` and then create a new variable, `y`, from `x`.
If you change an element of `y`, it will also change `x`:

```{code-cell}
x = [1, 2]
y = x
y[0] = 10
x
```

This happens because of how Python handles containers. When you create a
container, Python stores it in your computer's memory. If you then assign the
container to a variable, the variable points, or **refers**, to the location of
the container in memory. If you create a second variable from the first, both
will refer to the same location. As a result, operations on one variable will
affect the value of the other, because there's really only one container in
memory and both variables refer to it.

The example above uses lists, but other containers such as Series and
DataFrames behave the same way. The variable `bill_value` is just reference to
a column in the `banknotes` DataFrame.

If you want to assign an independent copy of a container to a variable rather
than a reference, you need to use a function or method to explicitly make a
copy. Many containers have a `.copy` method that makes a copy:

```{code-cell}
x = [1, 2]
y = x.copy()
y[0] = 10
x
```


### Tuples

References can be confusing, and if you know that the elements of a container
shouldn't change, one way to prevent problems is to use a **tuple**. Like a
list, a tuple is a one-dimensional container. The key difference is that tuples
are **immutable**: once you create a tuple, you cannot alter it nor its
elements.

You can make a tuple by enclosing comma-separated values in parentheses `()`,
like this:

```{code-cell}
(1, 2)
```

You can also convert another container into a tuple with the `tuple` function:

```{code-cell}
x = [1, 2]
y = x
x = tuple(x)
y[0] = 10
x
```


(data-types)=
Data Types
----------

Data can be categorized into different **types** based on sets of shared
characteristics. For instance, statisticians tend to think about whether data
are numeric or categorical:

* numeric
    + continuous (real or complex numbers)
    + discrete (integers)
* categorical
    + nominal (categories with no ordering)
    + ordinal (categories with some ordering)

Of course, other types of data, like graphs (networks) and natural language
(books, speech, and so on), are also possible. Categorizing data this way is
useful for reasoning about which methods to apply to which data.

Python and most other programming languages also categorize data by type. To
check the type of an object in Python, use the built-in `type` function. Recall
you used this function to check the type of the banknotes DataFrame in
{numref}`inspecting-dataframe`:

```{code-cell}
type(banknotes)
```

Take a look at the types of a few other objects:

```{code-cell}
type(bill_value)
```

```{code-cell}
type(bill_value[0])
```

```{code-cell}
type("hi")
```

```{code-cell}
type(x)
```

:::{note}
In Python 3, **class** is just another word for type. The `type` function
returns the class of an object. Python also provides a `class` keyword to
create your own classes. Creating classes is beyond the scope of this reader,
but is explained in detail in most Python programming textbooks.
:::

For Pandas Series and DataFrames, the `type` function returns the type of
container, but doesn't return any information about the types of the elements.
The same is true for the NumPy arrays.

{numref}`summarizing-data` described one way to print the types of the
elements in a Pandas object: by calling the `info` method. In the printout, the
element types are listed in the `Dtype` column:

```{code-cell}
banknotes.info()
```

The column label `Dtype` is short for "data types". You can also access the
element types for a DataFrame with the `.dtypes` attribute:

```{code-cell}
banknotes.dtypes
```

For a Series or NumPy array, you can instead use `.dtype` to get the element
type:

```{code-cell}
bill_value.dtype
```

Some of the element types listed for the `banknotes` DataFrame are built into
Python, while others are provided by Pandas and NumPy. At the expense of being
more complicated, the Pandas/NumPy types tend to be more specific and
consistent. They provide programmers with greater control over how data are
stored in memory, which makes it possible to write more efficient code. For
computations that generate or process a large amount of data, as is often the
case in research computing, efficiency is a major concern.

Here's a non-exhaustive table of data types that you'll often encounter in data
analysis:

Built-in   | Pandas/NumPy              | Example         | Description
---------- | ------------------------- | --------------- | -----------
`bool`     |                           | `True`, `False` | Boolean values
`int`      | `int32`, `int64`          | `-8`, `0`, `42` | Whole numbers 
`float`    | `float32`, `float64`      | `-2.1`, `0.5`   | Decimal numbers
`complex`  | `complex64`, `complex128` | `3j`, `1-2j`    | Complex numbers
`str`      |                           | `"hi"`, `"2.1"` | Text strings
`datetime` | `datetime64`              |                 | Dates and times

For most of the built-in types, you can explicitly construct an object with
that type by calling the function with the same name as the type. For instance,
here's a way to construct an integer (type `int`):

```{code-cell}
n = int(4)
type(n)
```

This example is a bit silly, since you could just write `4` instead of `int(4)`
and you'd still get an integer:

```{code-cell}
n = 4
type(n)
```

That said, suppose you want to construct an integer from a decimal number:


```{code-cell}
n = int(4.67)
type(n)
```

```{code-cell}
n
```

Calling `int` forces the value to be an integer, and the numbers after the
decimal point are removed.

Decimal numbers like `4.67` are better represented by a floating point number,
or `float`. Use this when you need decimal precision of any kind:

```{code-cell}
n = 4.67
type(n)
```

```{code-cell}
n
```

Notice that the Pandas/NumPy types have the same names as the built-in types,
but with a number appended to the end. {numref}`bit-sizes` explains what those
numbers mean.


(strings-the-object-dtype)=
### Strings & The `object` Dtype

Strings (type `str`), which were introduced in {numref}`getting-help`, are a
bit more complicated than Boolean values and numbers because they have many
attributes and methods associated with them.

<!--
, and they also tend to use much more memory.
-->

Recall that you can use double `"` or single `'` quotes to construct a string:

```{code-cell}
"Hello, world!"
```

In Pandas and NumPy, strings usually associated with the `object` data type
(printed as `object` or `O`). For example, look at the `names` column in the
`banknotes` data:

```{code-cell}
banknotes["name"]
```

The `object` data type is provided as a catch-all for non-numeric data
types. For example, if you create a Series from several different types of
data, Pandas will choose `object` as the element type:

```{code-cell}
mixed = pd.Series(["hi", 1, True])
mixed
```

The individual elements of an `object` Series retain their original data types:

```{code-cell}
type(mixed[0])
```

```{code-cell}
type(mixed[2])
```

So one way to think about the `object` data type is as an invisble wrapper
around each element's original type. The Series can claim all of its elements
are generic "objects", but when you access an element the wrapper is peeled off
and you get the original type.

You're most likely to encounter the `object` type when working with Series or
arrays of strings. In that case, you can generally assume all of the elements
are type `str`. If you're ever unsure of the type of an element, you can always
use `type` to check.

:::{note}
NumPy doesn't have a dedicated string type because the way strings are stored
in memory is very different from the way numbers are stored. Since Pandas is
based on NumPy, until recently Pandas didn't have a dedicated string type
either. So both use `object` as the element type for Series and arrays of
strings.

As of Pandas 1.0, the developers have added an [experimental `string`
type][pd-string] so that users can distinguish Series of strings from Series of
mixed types. Hopefully in the future the `string` type will become the main way
to handle strings rather than an experimental feature.

[pd-string]: https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html
:::


(coercion-conversion)=
### Coercion & Conversion

Although `bool`, `int`, and `float` are different types, in most situations
Python will automatically convert between them as needed. For example, you can
multiply a floating point number by an integer and then add a Boolean value:

```{code-cell}
n = 3.1 * 2 + True
n
```

First, the integer `2` is converted to floating point number and multiplied by
`3.1`, yielding `6.2`. Then the Boolean `True` is converted to a floating point
number and added to `6.2`. In Python and most other programming languages,
`False` corresponds to `0` and `True` corresponds to `1`. Thus the result is
`7.2`, a floating point number:

```{code-cell}
type(n)
```

This automatic conversion of types is known as **implicit coercion**.
Conversion always proceeds from less general to more general types, so that no
information is lost.

Implicit coercion usually only applies to numeric types (including Boolean
values). Mixing other types will usually cause an error. For instance, you
can't add a number to a string:

```{code-cell}
:tags: [raises-exception]
"hi" + 1
```

Implicit coercion also works for numeric Pandas/NumPy types. For example, you
can multiply `bill_value` by one and a half times its current value:

```{code-cell}
bill_value * 1.5
```

Notice that the `dtype` has changed from `int64` to `float64`.


**Type conversion** is when you explicitly convert an object from one type to
another. You already saw examples of this with the `int` and `float` functions
in {numref}`data-types`. Here are a few more:

```{code-cell}
bool(0)
```

```{code-cell}
str(105)
```

Python can even convert strings into numbers and Boolean values:

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

For a Pandas Series or NumPy array, you can use the `.astype` method to convert
the elements to a specific type. Pass the name of the target type to the method
as a string. For example, here's how to convert the `bill_value` elements to
`float64`:

```{code-cell}
bill_value.astype("float64")
```


(bit-sizes)=
### Bit Sizes & Memory

Recall the table of types from the beginning of this Section
({numref}`data-types`). The names of the Pandas/NumPy types in the table all
end in numbers such as `32` or `64`. These numbers indicate the **bit size**,
the number of bits of memory used to store a value of that type.

For example, a single value with type `int64` uses 64 bits of memory. So the
`int64` series `bill_value` uses about 64 bits per element, for a total of:

```{code-cell}
64 * len(bill_value) # bits
```

In contrast, Python's built-in data types don't specify how much memory they
use:

```{code-cell}
type(3)
```

In fact, the amount of memory can vary depending on your computer's hardware
and operating system!

Why is bit size important? Your computer has a limited amount of memory, so
it's a good habit to only use what you need. The tradeoff is that using more
memory allows you to use larger or more precise numbers.

For instance, a 64-bit integer can hold values between
`-9,223,372,036,854,775,808` and `9,223,372,036,854,775,807`, whereas a 16-bit
integer can only hold values between `-32,768` and `32,767`. Understanding this
matters when you're working with large numbers. Without that knowledge, you
might assign `32,768` to an `int16` variable and find that you've caused an
**overflow error**.

The same holds for instances where you need a certain amount of precision in
your data. For example, Python and NumPy have the ability to represent
irrational numbers, like pi. Ultimately, your computer has to represent such
numbers with decimal values, so the number of decimal places a variable can
hold will affect what pi "means" in your code:

```{code-cell}
np.pi
```

:::{tip}
You can also use bit sizes to estimate the amount of memory your data will
require, as we did for the `bill_value` object. When a computation runs out of
memory, an estimate of how much memory is necessary can help you understand
whether to get better hardware or to change your computing strategy.
:::


<!--
(booleans)=
### Booleans

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
banknotes["has_portrait"]
```

```{code-cell}
coded_in_java = False
type(coded_in_java)
```
-->





(indexing-in-pandas)=
Indexing in Pandas
------------------

If you want to inspect the elements of a Series more closely, you can use
indexing. Conceptually, indexing a Series is very similar to indexing a list or
tuple, but Pandas offers additional ways to select and subset data via indexes.


(the-pandas-index)=
### What's an Index?

A Pandas index is more than just a positional location. Indexes serve three
important roles:

1. As metadata to provide additional context about a data set
2. As a way to explicitly and automatically align data
3. As a convenience for getting and setting subsets of data

The index of a series is available via the `index` attribute:

```{code-cell}
bill_value.index
```

Index labels can be numbers, strings, dates, or other values. Pandas provides
subclasses of `Index` for specific purposes, which you can read more about
[here][pd-index].

[pd-index]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.html

Indexes, like tuples, are **immutable**. The labels in an index cannot be
changed. That said, every index also has a name that _can_ be changed:

```{code-cell}
bill_value.name = "bill_value"
bill_value
```

The above also applies to DataFrames:

```{code-cell}
banknotes.index
```

Oftentimes, an index is a range of numbers, but this can be changed. The code
below uses the `set_index` method to change the index of `banknotes` to
`country`:

```{code-cell}
banknotes.set_index("country", inplace = True)
banknotes.index
```

The `inplace` argument instructs Pandas to change the index directly without
making a copy first, so that we don't have to reassign `banknotes.index`
explicitly.


(indexing-by-position)=
### Indexing by Position

Changing the index affects how you select elements. There are three main
methods for accessing specific values in Pandas:
1. By integer position
2. By label/name
3. By a condition

To access elements in a series by integer position, use `.iloc`:

```{code-cell}
bill_value.iloc[5]
```

Using `.iloc` is extensible to sequences of values:

```{code-cell}
bill_value.iloc[[5, 15, 25, 35]]
```

Use a **slice** to select a range of elements. The syntax for a slice is
`start:stop:step`, with the second colon `:` and arguments being optional. This
syntax also applies to lists. For example:

```{code-cell}
bill_value.iloc[0:5]
```

Below, we use a slice to get every twentieth element in the Series:

```{code-cell}
bill_value.iloc[::20]
```

Slices also accept negative values. This counts back from the end of a
sequence. For instance:

```{code-cell}
bill_value.iloc[-5:]
```

The result is the same as if you had used the `.tail` method:

```{code-cell}
bill_value.tail()
```


(indexing-by-label)=
### Indexing by Label

Use `.loc` to index a Series or DataFrame by label:

```{code-cell}
:tags: [output_scroll]
banknotes.loc["Peru"]
```

You can select specific columns as well:

```{code-cell}
:tags: [output_scroll]
banknotes.loc["Peru", "name"]
```

Just as with `.iloc`, it's possible to pass sequences into `.loc`:

```{code-cell}
:tags: [output_scroll]
banknotes.loc[["Peru", "Serbia", "Ukraine"]]
```

This can be a very powerful operation, but it's easy to get mixed up when
labels are integers, as with the `bill_value` data.

For example, this:

```{code-cell}
bill_value.loc[0:5]
```

Is *NOT* the same as this:

```{code-cell}
bill_value.iloc[0:5]
```

Recall that bracket notation selects columns in DataFrames. With a Series, the
same notation acts as another way to perform `.loc` operations:

```{code-cell}
bill_value[0:5]
```

Finally, `.iloc` and `.loc` can be used in tandem with one another. This is
called **chaining**. Below, we use the country-indexed `banknotes` DataFrame to
select all rows with "Peru." Then, we select the second row from this subset.

```{code-cell}
banknotes.loc["Peru"].iloc[1]
```


(indexing-by-condition)=
### Indexing by a Condition

The last way to index in Pandas is by condition. Pandas does this by evaluating
a condition and returning a Boolean Series or array. This is by far the most
powerful method of indexing in Pandas.

For example, suppose you want to find bill values that are divisible by 25. You
can use the modulo operator `%` to get the remainder when one positive integer
is divided by another. So the condition to test for divisibility by 25 is:

```{code-cell}
bill_value % 25 == 0
```

The result is a Boolean Series with as many elements as `bill_value`. You can
use this condition in `.loc` to get only the elements where the result was
`True`:

```{code-cell}
bill_value.loc[bill_value % 25 == 0]
```

<!--
This is a **subset** of the Series.
-->

You can also use square brackets `[]` without `.loc` to index by condition:

```{code-cell}
bill_value[bill_value - 100 > 5]
```

With a DataFrame, indexing by condition gives you a subset of the rows:

```{code-cell}
:tags: [output_scroll]
banknotes[banknotes["currency_code"] == "MWK"]
```

If you want to specify specific columns, use `.loc`:

```{code-cell}
banknotes.loc[banknotes["current_bill_value"] == 10.0, "currency_name"]
```

The above lets you select multiple columns, but you could also do the
following:

```{code-cell}
cols = ["currency_code", "currency_name"]
banknotes[cols].loc[banknotes["current_bill_value"] == 10.0]
```


(special-values)=
Special Values
--------------

You may have noticed that some of the data in `banknotes` is missing. This is
common, and it's important to understand how to handle missing or invalid
values.

There are many reasons that could cause these values to be missing or
incomplete, and as a result, Pandas provides lots of flexibility for detecting
and handling these values.

In Pandas, these special values are generally treated as missing values in the
dataset, and are represented by the NumPy `nan` type. This reduces some of the
nuance of data values and types, but was seemingly done for computational
performance reasons.

```{code-cell}
banknotes.iloc[-25]
```

(missing-values-in-pandas)=
### Types of Values Considered Missing by Pandas

In addition to `np.nan` (which displays as NaN), Pandas interprets several
other values as missing.  This includes Python's `None` type, as well as
Pandas' experimental `NA` types.

Python's `None` type represents something that has no value. It often comes
about as the return of a function, if something hasn't been defined yet, or if
something wasn't found.

When creating a Series, we can pass this value:
```{code-cell}
pd.Series([None, "one", "two"])
```

Be aware that `None` is a Python object, and in the above example, the 
datatype of the series became 'object'. If we specify a datatype explicitly
then Pandas will convert it to one of its representations:
```{code-cell}
pd.Series([1.5, 2.0, 3, None], dtype="float")
```


(missing-values-in-csvs)=
### Reading in Missing Values from a CSV file

An obvious source of missing or incomplete values is the data itself. 
When the data was collected, there may have been reasons to code missing data.
For example, in collection of survey responses, there may be times where the 
answer was not applicable.

Another example would be if a measurement was not taken on some of the samples. 
Obviously, there are no rules on how this was represented in the data set. 
However there are several conventions, and Pandas is aware of many of them. 

When reading data from a CSV file, Pandas will automatically detect missing
values. By default, it will convert any empty cell, or string such as 'na',
'nan', 'null', 'N/A', and other variants to NaN.  A full list can be found in
the [Pandas documentation][readcsv].


[readcsv]: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html


(detecting-missing-values)=
### Detecting Missing Values

To detect missing values, Pandas provides two complementary methods: `isna` and
`notna`.

We can see information about missing values with the `count` method on 
DataFrames:

```{code-cell}
banknotes.count()
```

If we look at the `hover_text` columns of the DataFrame, we can see what 
those missing values look like.

```{code-cell}
ht = banknotes["hover_text"]
ht.count()
```

The return of `isna` is a Boolean Series indicating which of the values are
considered missing:

```{code-cell}
ht.isna()
```

The reverse---to see which values are not considered missing---is returned 
with `notna`:

```{code-cell}
ht.notna()
```

(replacing-missing-values)=
### Replacing Missing Values

We can use this Boolean Series to subset with `loc`. For example, to keep only
the values that aren't missing:

```{code-cell}
ht.loc[ht.notna()]
```

Pandas also provides a shortcut with the `dropna` method:

```{code-cell}
ht.dropna()
```

Another strategy may be to fill the missing values. We could do so using the 
`fillna` method:

```{code-cell}
ht.fillna(-1, inplace=True)
ht
```

Additionally, the data set may have its own indicator for missing values, e.g
"" or 0. We can convert those to missing using the `replace` method:

```{code-cell}
ht.replace(-1, np.nan)
```


Exercises
---------

### Exercise

Python's `range` function offers another way to create a sequence of numbers.
Read the help file for this function.

1. Create an example range. How does this differ from a list?
2. Describe the three arguments that you can use in `range`. Give examples of
  each.
3. Convert one of those ranges to a list and print it to screen. What changes
  in the way Python represents this sequence?


### Exercise

Return to the discussion in {numref}`coercion-conversion`.

1. Why does `"3" + 4` raise an error?
2. Why does `True - 1` return 0?
3. Why does `int(4.6) < 4.6` return `True`?


### Exercise

Use a search engine or consult StackOverflow to figure out how to subset a
DataFrame with multiple conditions.

1. Create a new DataFrame from `banknotes` with the following conditions:
  current bill value is less than or equal to 20; gender is female; contains
  the columns `country`, `name`, `comments`, `has_portrait`
2. Use a Pandas function to count the number of entries that have portraits.
  How many are there?
3. Return the last available comment. What does it say?

