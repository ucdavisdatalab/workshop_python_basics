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

import polars as pl

terns = pl.read_csv("data/2000-2023_ca_least_tern.csv")
```

# Data Types & Structures

:::{admonition} Learning Objectives
:class: note
After this lesson, you should be able to:

* Check the type of an object
* Cast an object to a different type
* Describe and differentiate lists, series, tuples, sets, dicts, and arrays
* Explain what a comprehension is
* Identify and cast categorical data
* Explain what broadcasting is
* Describe and differentiate `None`, `null`, and `NaN`
* Locate missing values in a series
* Select columns of a data frame
* Filter rows of a data frame on a condition
* Negate or combine conditions with logic operators
:::

The previous chapter introduced Python, providing enough background to do
simple computations on data sets. This chapter focuses on the foundational
knowledge and skills you'll need to use Python effectively in the long term.
Specifically, it's a deep dive into data types and data structures in Python
and Polars. Working knowledge of these will make you more effective at
analyzing data and solving problems.


(data-types)=
## Data Types

In {ref}`sec-summarizing-data`, we used the `.glimpse` method to get a
structural summary of the California least tern data set:

```{code-cell}
:tags: [scroll-output]
terns.glimpse()
```

The first two rows describe the shape of the data set. After that, each row
lists a column name, the type of data in that column, and that column's first
few values. For instance, the `site_name` column contains `str`, or string,
data.

We categorize data into different **types** based on sets of shared
characteristics because types are useful for reasoning about what we can do
with the data. For example, statisticians conventionally categorize data as one
of four types within two larger categories:

* numeric
    + continuous (real or complex numbers)
    + discrete (integers)
* categorical
    + nominal (categories with no ordering)
    + ordinal (categories with some ordering)

Which approaches and statistical techniques are appropriate depends on the type
of the data. Of course, other types of data, like graphs (networks) and natural
language (books, speech, and so on), are also possible.

Most programming languages, including Python, also categorize data by type. The
following table lists some of Python's built-in types:

:::{table}
:name: tbl-types

Type      | Example         | Description
--------- | --------------- | -----------
`bool`    | `True`, `False` | Boolean values
`int`     | `-8`, `0`, `42` | Integers
`float`   | `-2.1`, `0.5`   | Real numbers
`complex` | `3j`, `1-2j`    | Complex numbers
`str`     | `"hi"`, `"2.1"` | Strings
:::

You can check the type of an object in Python with the built-in `type`
function. Take a look at the types of a few objects:

```{code-cell}
type("hi")
```

```{code-cell}
type(True)
```

```{code-cell}
type(-8.3)
```

In Python, **class** is just another word for type. So we can also say that the
`type` function returns the class of an object.

:::{note}
Python provides a `class` keyword to create your own classes. Creating classes
is beyond the scope of this reader, but is explained in detail in most Python
programming textbooks.
:::

:::{tip}
You can use the `isinstance` function to test whether a value is of a
particular class. For example, to test whether `5` is a string:

<!-- FIXME: when JupyterBook supports nested code cells -->

```python
isinstance(5, str)
```
```none
False
```
:::


(sec-coercion-casting)=
### Coercion & Casting

Although `bool`, `int`, and `float` are different types, in most situations
Python will automatically convert between them as needed. For example, you can
multiply a floating point number by an integer and then add a Boolean value:

```{code-cell}
n = 3.1 * 2 + True
n
```

First, the integer `2` is converted to a floating point number and multiplied
by `3.1`, yielding `6.2`. Then the Boolean `True` is converted to a floating
point number and added to `6.2`. In Python and most other programming
languages, `False` corresponds to `0` and `True` corresponds to `1`. Thus the
result is `7.2`, a floating point number:

```{code-cell}
type(n)
```

This automatic conversion of types is known as **implicit coercion**.
Conversion always proceeds from less general to more general types, so that no
information is lost.

Implicit coercion only applies in situations where the intent of the code is
relatively unambiguous, such as arithmetic between different types of numbers
(including Booleans). For example, you can't add a number to a string, because
it's unclear what the result should be:

```{code-cell}
:tags: [raises-exception]
"hi" + 1
```

A **cast** explicitly converts an object from one type to another, sometimes
losing information. You can cast an object to a particular type with the
function of the same name. For example, to cast to the `bool` type:

```{code-cell}
bool(0)
```

Or to cast to the `int` type:

```{code-cell}
int(4.67)
```

Casts are especially useful for converting to and from the `str` type:

```{code-cell}
"hi" + str(1)
```

```{code-cell}
float("7.3")
```

Python will raise an error if a cast is not possible. For example, this will
not work:

```{code-cell}
:tags: [raises-exception]
int("Hello world!")
```


(sec-lists)=
## Lists

A **data structure** is a collection of data organized in a particular way. In
Python, data structures are also called **containers**, because they contain
data. Containers make working with lots of data manageable and efficient. Data
frames, introduced in the previous chapter, are an example of a two-dimensional
data structure.

A **list** is a general-purpose one-dimensional data structure. Lists are built
into Python; you don't even need to import a module in order to use them. You
can create a list by enclosing any number of comma-separated values in square
brackets `[]`, like this:

```{code-cell}
x = [10, 20, 30, 40, 50]
x
```

Lists are **ordered**, which means the values, or **elements**, have specific
positions. The first element is `10`, the second is `20`, the fifth is `50`,
and so on.

The elements of a list can be of different types, so we say lists are
**heterogeneous**. For instance, this list contains a number, a string, and
another list (with one element):

```{code-cell}
li = [8, "hello", [4.2]]
li
```

A list can have no elements, in which case we say it's **empty**. For example:

```{code-cell}
empty = []
empty
```

You can get the length of a list with the `len` function:

```{code-cell}
len(empty)
```

The `list` function converts other containers into lists. Strings are
technically containers for individual characters, so:

```{code-cell}
list("data science")
```


(indexing)=
### Indexing

So far you've learned two ways to use square brackets `[]`:

1. To select columns from a data frame, as in `terns["year"]`
2. To create lists, as in `["a", "b", 1]`

The first case is an example of **indexing**, which means getting or setting
elements of a data structure. The square brackets `[]` are Python's indexing
operator.

You can use indexing to get an element of a list based on the element's
position. Python uses **zero-based indexing**, which means the positions of
elements are counted starting from 0 rather than 1. So the first element of a
series is at position 0, the second is at position 1, and so on.

:::{note}
Many programming languages use zero-based indexing. It may seem strange at
first, but it makes some kinds of computations simpler by eliminating the need
to add or subtract 1.
:::

The indexing operator requires at least one argument, called the **index**,
which goes inside of the square brackets `[]`. The index says which elements
you want to get. For a data frame, you can use a position or a column name as
the index. For a list, you can only use a position.

As an example, consider the list `li` we created earlier:

```{code-cell}
li = [8, "hello", [4.2]]
li
```

The code to get the first element is:

```{code-cell}
li[0]
```

Likewise, to get the third element:

```{code-cell}
li[2]
```

The third element is a list too. If you want to get its first element, you can
**chain**, or repeat, the indexing operator:

```{code-cell}
li[2][0]
```

Read this code from right to left as "get the first element of the third
element of the variable `li`."

You can use a **slice** to select a range of elements. The syntax for a slice
is `lower:upper:stride`, where all of the arguments and the second colon `:`
are optional. The lower bound defaults to 0, the upper bound defaults to the
length of the list, and the stride defaults to 1. For example, to get the first
two elements:

```{code-cell}
li[:2]
```

As another example, you can use a slice to get every other element:

```{code-cell}
li[::2]
```
Negative values in a slice index backwards from the end of the list. For
instance, to get the last 2 elements:

```{code-cell}
li[-2:]
```

You can set an element of a list by assigning a value at a given index. So the
code to change the first element of `li` to the string "hi" is:

```{code-cell}
li[0] = "hi"
li
```

Indexing isn't just for lists: most of the examples in this section also apply
to series, data frames, and other data structures.


(references)=
### References

Assigning elements of a container is not without complication. Suppose you
assign a list to a variable `x` and then create a new variable `y` from `x`. If
you change an element of `y`, it will also change `x`:

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

The example above uses lists, but other containers---such as data
frames---behave the same way. If you want to assign an independent copy of a
container to a variable rather than a reference, you need to use a function or
method to explicitly make a copy. Many containers have a `.copy` or `.clone`
method that makes a copy:

```{code-cell}
x = [1, 2]
y = x.copy()
y[0] = 10
x
```

(sec-comprehensions)=
### Comprehensions

A **list comprehension** creates a new list from the elements of an existing
list. We'll use this list to demonstrate comprehensions:

```{code-cell}
values = [10, 11, 12, -5, 13, 14]
```

If you want, for example, to add 1 to each element of the list, you can use a
comprehension to do it. Here's how:

```{code-cell}
[v + 1 for v in values]
```

In words, this code tells Python to create a new list where the elements are
`v + 1` for each element `v` in `values`. The enclosing square brackets `[]`
indicate that the result should be a list. More generally, the syntax for a
comprehension is:

```none
EXPRESSION for ELEMENT in CONTAINER
```

Replace `CONTAINER` with a data structure, `ELEMENT` with a variable name for
the elements, and `EXPRESSION` with an expression to compute (typically using
the elements).

For instance, you can also use a comprehension to compute the type of each
element in a container:

```{code-cell}
[type(v) for v in values]
```

Comprehensions can also filter out some elements based on a condition. Suppose
we only want the positive elements of the list:

```{code-cell}
[v for v in values if v > 0]
```

The syntax for a comprehension with a condition is:

```none
EXPRESSION for ELEMENT in CONTAINER if CONDITION
```

The `CONDITION` must be an expression that evaluates to `True` or `False`
(typically using the elements).

Comprehensions are an efficient way to compute (and compute on) lists. You can
also use comprehensions with Python's other built-in data structures, which
you'll learn about in {ref}`sec-built-in-data-structures`.


(sec-series)=
## Series

A **series** is an ordered, one-dimensional data structure. Series are a
fundamental data structure in Polars, because each column in a data frame is a
series.

For example, in the California least tern data set, the `site_name` column is a
series. Take a look at the first few elements with its `.head` method:

```{code-cell}
terns["site_name"].head()
```

Series and data frames have many attributes and methods in common; the `.head`
method is one of these.

Notice that the elements of the `site_name` series are all strings. Unlike a
list, in a series all elements must be of the same type, so we say series are
**homogeneous**. A series can contain strings, integers, decimal numbers, or
any of several other types of data, but not a mix of these all at once.

The other columns in the least tern data are also series. For instance, the
`year` column is a series of integers:

```{code-cell}
terns["year"]
```

Series can contain any number of elements, including 0 or 1 element. You can
check the number of elements, or length, of a series with Python's built-in
`len` function:

```{code-cell}
len(terns["year"])
```

Since this is a column from the `terns` data frame, its length is the same as
the number of rows in `terns`.

:::{note}
You can also check the length of a series with the `.shape` attribute:

<!-- FIXME: when JupyterBook supports nested code cells -->

```python
terns["year"].shape
```

```none
(791,)
```

Python prints the value of `.shape` differently from the result of `len`
because they are different types of data. Most of the time, it's more
convenient to use the `len` function to check lengths of one-dimensional
objects like series, because it returns an integer.
:::


### Creating Series

Sometimes you’ll want to create series by manually inputting data, perhaps
because your data set isn't digitized or because you want a toy data set to
test out some code. You can create a series from a list (or other sequence)
with the `pl.Series` function:

```{code-cell}
pl.Series([1, 2, 19, -3])
```

```{code-cell}
pl.Series(["hi", "hello"])
```

The Polars documentation recommends setting a name for every series. To do this
with `pl.Series`, pass the name as the first argument and the elements as the
second argument:

```{code-cell}
pl.Series("tens", [10, 20, 30])
```

Polars will print the name when you print the series and will use the name as a
column name if you put the series in a data frame. You can get or set the name
on a series through the `.name` attribute:

```{code-cell}
x = pl.Series("tens", [10, 20, 30])
x.name
```

:::{tip}
If you want to create a series that contains a sequence of numbers, there are
several helper functions you can use. Python's built-in `range` function
creates a sequence of integers. NumPy's `np.arange` and `np.linspace` functions
can create sequences of integers or decimal numbers. You can pass the result
from any of these functions to `pl.Series` to create a series.
:::


### Data Types in Polars

Series are homogeneous, so if you try to create a series from elements of
different types, the `pl.Series` function will raise an error:

```{code-cell}
:tags: [raises-exception, scroll-output]
pl.Series([1, "cool", 2.3])
```

By default, Polars infers the data type of a series' elements from the first
element. This can lead to errors you might not expect:

```{code-cell}
:tags: [raises-exception, scroll-output]
pl.Series([1, 9.2, 2.3])
```

You can explicitly specify a data type for a series with the `pl.Series`
function's third parameter, `dtype`:

```{code-cell}
pl.Series([1, 9.2, 2.3], dtype = float)
```

Polars uses its own data types for series elements, so that:

* It can efficiently support types of data that are not built into Python, such
  as categorical data.
* Every numeric type has an explicit **bit size**: the number of bits of memory
  necessary to store an element. Bit sizes appear as suffixes in the name of
  the type. For instance, `Float32` stores a floating point number in 32 bits.
* A special value, `null`, can be present in any series to indicate missing
  data. We'll explain `null` in {ref}`sec-special-values`.

When you create or access the elements of a series, Polars silently converts
between its types and Python's built-in types. Some of the Polars types and
their Python equivalents are listed in the following table:

:::{list-table}
:name: tbl-polars-types
:header-rows: 1

* - Type
  - Python Equivalent
  - Description
* - `Boolean`
  - `bool`
  - Boolean values
* - `Int8`, `Int16`, `Int32`, `Int64`
  - `int`
  - Integers
* - `Float32`, `Float64`
  - `float`
  - Real numbers (base-2 [floating point][float])
* - [Not yet supported](https://github.com/apache/arrow/issues/16264)
  - `complex`
  - Complex numbers
* - `String`
  - `str`
  - Strings
* - `Categorical`, `Enum`
  - No equivalent
  - Categorical data

[float]: https://en.wikipedia.org/wiki/Floating-point_arithmetic
:::

The Polars documentation has [the complete list][polars-types].

[polars-types]: https://docs.pola.rs/user-guide/concepts/data-types-and-structures/#appendix-full-data-types-table

:::{admonition} Why does bit size matter?
:class: note, dropdown
By using more bits to store values, you can express a wider range of values.
This is best illustrated by the integer types: `Int8` can only express values
from `-128` to `127` (inclusive), whereas `Int64` can express values from
`-9,223,372,036,854,775,808` to `9,223,372,036,854,775,807`.

If a computation produces a value too small or too large to express as its
given type, the value **overflows**, leading to an inaccurate result. The exact
effect of overflow depends on the type, software, and hardware, but one common
outcome is that the value "wraps around" to the other side of the type's range:

<!-- FIXME: when JupyterBook supports nested code cells -->

```python
pl.Series([127], dtype = pl.Int8) + 1
```

```none
shape: (1,)
Series: '' [i8]
[
        -128
]
```

The tradeoff is that the more bits you use to store values, the more memory you
need. For computations that generate or process large quantities of data, as is
often the case in research computing, memory efficiency is a major
concern---computers have a limited amount of memory.

You can use bit size to estimate the amount of memory a series will require.
For example, since a single element of a `Float64` series requires about 64
bits, the `bp_min` column in the least terns data requires roughly this many
bytes:

```python
64 * len(terns["bp_min"]) / 8  # 8 bits per byte 
```

```none
6328.0
```

For series and data frames, you can use the `.estimated_size` method to have
Python do this calculation for you. When a computation runs out of memory, an
estimate of how much memory is necessary can help you decide whether to change
your computing strategy or get more memory.

Most of Python's built-in data types don't specify bit sizes, and their sizes
can even vary depending on your computer's hardware and operating system!
:::

If you call Python's `type` function on a data structure, it returns the type
of the data structure:

```{code-cell}
type(terns["site_name"])
```

For a series, you can get the element type with the `.dtype` attribute:

```{code-cell}
terns["site_name"].dtype
```

:::{note}
Data frames don't have a `.dtype` attribute since they can consist of multiple
series. Instead, they have a `.dtypes` attribute, a list with the element type
for each column.

If your goal is to summarize a data frame, the `.glimpse` method is usually
more convenient.
:::

You can use the `.cast` method to cast the elements of a series to a specific
type. For example, here's how to cast the `total_nests` column to a `String`
series:

```{code-cell}
terns["total_nests"].cast(pl.String)
```

(sec-categorical-data)=
### Categorical Data

A feature is **categorical** if it measures a qualitative category. For
example, the genres `rock`, `blues`, `alternative`, `folk`, `pop` are
categories.

Polars uses the `Categorical` and `Enum` data types to represent categorical
data. Visualizations and statistical models sometimes treat categorical data
differently than other data types, so it's important to make sure you have the
right data type.

When it reads a data set, Polars usually can't tell which features are
categorical. That means identifying and converting the categorical features is
up to you. For beginners, it can be difficult to understand whether a feature
is categorical or not. The key is to think about whether you want to use the
feature to divide the data into groups.

For example, if you want to know how many songs are in the `rock` genre, you
first need to divide the songs by genre, and then count the number of songs in
each group (or at least the `rock` group).

As a second example, months recorded as numbers can be categorical or not,
depending on how you want to use them. You might want to treat them as
categorical (for example, to compute max rainfall in each month) or you might
want to treat them as numbers (for example, to compute the number of months
time between two events).

The bottom line is that you have to think about what you'll be doing in the
analysis. In some cases, you might treat a feature as categorical only for part
of the analysis.

Let's think about which features are categorical in least terns data set. To
refresh your memory of what's in the data set, take a look at the structural
summary:

```{code-cell}
:tags: [scroll-output]
terns.glimpse()
```

The `site_name`, `site_abbr`, and `event` columns are all examples of
categorical data. The `region_` columns and some of the `pred_` columns also
contain categorical data.

One way to check whether a feature is useful for grouping (and thus effectively
categorical) is to count the number of times each value appears. For a series,
you can do this with the `.value_counts` method. For instance, to count the
number of times each category of `event` appears:

```{code-cell}
terns["event"].value_counts()
```

Features with only a few unique values, repeated many times, are ideal for
grouping. Numerical features, like `total_nests`, usually aren't good for
grouping, both because of what they measure and because they tend to have many
unique values, which leads to very small groups.

The `year` column can be treated as categorical or quantitative data. It's easy
to imagine grouping observations by year, but years are also numerical: they
have an order and we might want to do math on them. The most appropriate type
for `year` depends on how we want to use it for analysis.

You can cast a column to the `Categorical` type with the `.cast` method. Try
this for the `event` column:

```{code-cell}
event = terns["event"].cast(pl.Categorical)
event
```

Polars organizes attributes and methods for categorical data under the `.cat`
attribute of series. These raise errors if the element type of the series is
not `Categorical` (or `Enum`). You can get the categories of a categorical
series with the `.cat.get_categories` method:

```{code-cell}
event.cat.get_categories()
```

A categorical series remembers all possible categories even if you take a
subset where some of the categories aren't present:

```{code-cell}
event[:3]
```

```{code-cell}
event[:3].cat.get_categories()
```

This is one way the `Categorical` type is different from the `String` type, and
ensures that when you, for example, plot a categorical series, missing
categories are represented.

:::{note}
The `Categorical` and `Enum` types both represent categorical data. The
`Categorical` type is more flexible, allowing you to add categories as needed.
The `Enum` type is more memory-efficient, but requires that you specify all
possible categories up front. In practice, the `Categorical` type is more
convenient for interactive work.
:::

(sec-broadcasting)=
### Broadcasting

If you use an arithmetic operator on a series, Polars **broadcasts** the
operation to each element:

```{code-cell}
x = pl.Series([1, 3, 0])
x - 3
```

The result is the same as if you had applied the operation element-by-element.
That is:

```{code-cell}
pl.Series([1 - 3, 3 - 3, 0 - 3])
```

Most NumPy (and SciPy) functions also broadcast. For instance:

```{code-cell}
import numpy as np

x = pl.Series([1.0, 3.0, 0.0, np.pi])
np.sin(x)
```

Some examples of functions that broadcast are `np.sin`, `np.cos`, `np.tan`,
`np.log`, `np.exp`, and `np.sqrt`.

NumPy functions that combine or aggregate values usually don't broadcast. For
example, `np.sum`, `np.mean`, and `np.median` don't broadcast.

:::{tip}
Broadcasting is the counterpart to comprehensions (introduced in
{ref}`sec-comprehensions`). Both are highly efficient. Generally, you should:

* Use broadcasting with data structures that support it, such as series and
  NumPy arrays (explained in {ref}`sec-numpy-arrays`).
* Use comprehensions with lists and Python's other built-in data structures
  (explained in {ref}`sec-built-in-data-structures`).
:::

A function can broadcast across multiple arguments. To demonstrate this,
suppose we want to estimate number of nests per breeding pair for the least
terns data. The `total_nests` column contains the total number of nests at each
site, and the `bp_max` column contains the maximum reported number of breeding
pairs. So to compute nests per breeding pair:

```{code-cell}
terns["total_nests"] / terns["bp_max"]
```

The elements are paired up and divided according to their positions. Notice
that the result is a `Float64` series. The `total_nests` column is an `Int64`
series, so besides broadcasting, the example also demonstrates that Series are
subject to implicit coercion (introduced in {ref}`sec-coercion-casting`).

If you try to broadcast a function across two series of different lengths,
Polars raises an error:

```{code-cell}
:tags: [raises-exception]
x = pl.Series([1, 2])
y = pl.Series([9, 8, 7])
x - y
```


## Other Data Structures

In this section, you'll learn about several one-dimensional data structures
that are fundamental to programming in Python.

(sec-built-in-data-structures)=
### Built-in Data Structures

Besides lists, Python provides several other useful data structures:

*   Like lists, **tuples** are ordered and heterogeneous. The main difference
    is that tuples are **immutable**: once you create a tuple, you can't change
    it. This makes tuples safer and more efficient than lists.
  
    You can make a tuple by enclosing comma-separated values in parentheses
    `()`:

    ```python
    (True, 1, "hi")
    ```

    You can cast other data structures to a tuple with the `tuple` function.
    Use a tuple when the number of elements is constant and known in advance.

*   A **set** is unordered and heterogeneous. As in a mathematical set, the
    elements in a set must be unique. Python automatically discards any
    duplicates added to a set. Sets support set theoretic operations such as
    unions and intersections.

    You can make a set by enclosing comma-separated values in curly braces
    `{}`:

    ```python
    {True, 1, "hi"}
    ```

    You can convert other data structures to a set with the `set` function. Use
    a set when you need a guarantee that the elements are unique.

*   A **dict** is an ordered, heterogeneous collection of key-value pairs. Keys
    must be distinct and many different types of keys are valid. The indexing
    operator `[]` gets elements by key rather than position.

    You can make a dict by enclosing comma-separated `key: value` pairs in
    curly braces `{}`:

    ```python
    {"hi": -3.5}
    ```

    Use a dict when you need to index elements by something other than position
    or need a mapping from one collection of data to another.

:::{seealso}
Python's [official documentation][py-types] provides more details about what
you can do with these data structures.

[py-types]: https://docs.python.org/3/library/stdtypes.html
:::


(sec-numpy-arrays)=
### NumPy Arrays

An **array** (or `ndarray`) is an ordered, homogeneous data structure, similar
to a series. Arrays are a fundamental data structure in NumPy.

You can create an array with the `np.array` function and a list of elements:

```{code-cell}
x = np.array([10, 20, 30])
x
```

You can convert an array into a series with the `pl.Series` function:

```{code-cell}
pl.Series(x)
```

Conversely, you can convert a series to an array with the `.to_numpy` method:

```{code-cell}
terns["total_nests"][:5].to_numpy()
```

:::{tip}
Series tend to be a good choice for data analysis, while arrays tend to be a
good choice for sophisticated mathematical computations (such as simulations).
:::

:::{note}
NumPy uses its own data types for array elements, for many of the same reasons
Polars does for series elements. The NumPy documentation has [more
details][np-types].

[np-types]: https://numpy.org/doc/stable/user/basics.types.html

NumPy is primarily designed for numerical computing, so working with strings in
NumPy can be tricky. See the documentation for [details about its string
types][np-strings]. If you need to work with strings, Polars is more convenient
than NumPy.

[np-strings]: https://numpy.org/doc/stable/user/basics.strings.html
:::


(sec-special-values)=
## Special Values

### None

In Python, `None` represents an absent or undefined value. It is useful:

1. As a way to explicitly indicate a value is absent.
2. As the return value for functions that are useful for their side effects and
   don't need to return anything.
3. As a default argument for optional parameters in functions.

For example, Python's built-in `print` function, which prints a string to the
console, returns `None`:

```{code-cell}
print("Hello!")
```

The Python console doesn't print anything when an expression produces `None`:

```{code-cell}
None
```

`None` is the only value of type `NoneType`:

```{code-cell}
type(None)
```

You can check if a value is `None` with Python's `is` keyword:

```{code-cell}
x = None
x is None
```


### Missing Values

In the least terns data set, notice that some of the entries are `null`. For
instance, look at the second element of the `nonpred_eggs` column:

```{code-cell}
terns.head()
```

Polars uses `null`, called the **missing value**, to represent missing entries
in a data set. It’s implied that the entries are missing due to how the data
was collected, although there are exceptions. As an example, imagine the data
came from a survey, and respondents chose not to answer some questions. In the
data set, their answers for those questions can be recorded as `null`.

The missing value `null` is a chameleon: it can be of an element of any type in
a series. Polars implicitly converts `null` to and from `None` when you get or
set an element in a series. This means you can use `None` to create a series
with `null` elements:

```{code-cell}
x = pl.Series([1, 2, None])
x
```

And you get back `None` if you access a `null` element:

```{code-cell}
terns["nonpred_eggs"][1]
```

The missing value `null` is also contagious: it represents an unknown quantity,
so computing on it usually produces another missing value. The idea is that if
the inputs to a computation are unknown, generally so is the output:

```{code-cell}
x - 3
```

Polars makes an exception for aggregation functions, which automatically filter
out missing values:

```{code-cell}
x.mean()
```

You can use the `.is_null` method to test if elements of a series are `null`:

```{code-cell}
x.is_null()
```

Polars also provides an `.is_not_null` method and a `.fill_null` method to fill
missing values with a different value.

<!--
:::{tip}
When reading data from a CSV file, Pandas will automatically detect missing
values. By default, it will convert any empty cell, or string such as 'na',
'nan', 'null', 'N/A', and other variants to NaN.  A full list can be found in
the [Pandas documentation][readcsv].

[readcsv]: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
:::
-->

### Infinity

NumPy (and Polars) use `np.inf` to represent infinity. It is of type `float`.
You’re most likely to encounter it as the result of certain computations:

```{code-cell}
pl.Series([13]) / 0
```

You can us the `.is_infinite` method to test if elements of a series are
infinite:

```{code-cell}
x = pl.Series([1.0, 2.0, np.inf])
x.is_infinite()
```


### Not a Number

NumPy (and Polars) use `np.nan`, called **not a number** and also written
`NaN`, to represent mathematically undefined results. It is of type `float`. As
an example, dividing 0 by 0 is undefined:

```{code-cell}
pl.Series([0]) / 0
```

You can use the `.is_nan` method to test if elements of a series are `NaN`:

```{code-cell}
x = pl.Series([0, 1, 2]) / 0
x.is_nan()
```


(sec-data-frames)=
## Data Frames

### Selecting Columns

An excellent starting point for selecting and transforming columns in a data
frame is the `.select` method. {ref}`sec-summarizing-columns` already showed
how to select a single column by name with the indexing operator `[]`, but the
`.select` method is much more flexible. You can use it to select multiple
columns at once, by name or type, and can transform or rename them.

As with the indexing operator, you can use `.select` to select a single column
by providing the column name as an argument. Here's an example (with `.head` to
limit the output):

```{code-cell}
terns.select("year").head()
```

Unlike the indexing operator, `.select` returns a data frame rather than a
series.

You can also select multiple columns this way:

```{code-cell}
terns.select("year", "site_name").head()
```

The `.select` method is flexible because it can evaluate a **Polars
expression**: instructions for how to select or transform data. One way to
create an expression is with the `pl.col` function, which represents a column
or set of columns. So another way to select the `year` and `site_name` column
from the least terns data is:

```{code-cell}
terns.select(
    pl.col("year", "site_name")
).head()
```

An advantage of using `pl.col` is that you're not limited to selecting columns
by name: you can also select columns by type. Here's how to get only the
`Int64` and `Float64` columns in the least terns data:

```{code-cell}
terns.select(
    pl.col(pl.Int64, pl.Float64)
).head()
```

Selecting columns this way is useful for doing things like computing summaries
of only numeric columns. In fact, to compute widely-used summaries, like the
mean, all you need to do is call the corresponding method on the Polars
expression:

```{code-cell}
terns.select(
    pl.col(pl.Int64, pl.Float64).mean()
).head()
```

A third way to select columns with `pl.col` is with a pattern. Patterns are
strings, and must begin with a caret `^` and end with a dollar sign `$`. Within
a pattern, you can use `.*` as a wild card that matches any characters.

:::{note}
Technically, Polars' patterns are regular expressions, a widely-used language
for describing patterns in text. You can learn more about regular expressions
in the [Date & String Processing][dl-py-string] chapter of DataLab's
Intermediate Python workshop reader.

[dl-py-string]: https://ucdavisdatalab.github.io/workshop_intermediate_python/chapters/01_string-date-processing.html
:::

As motivation to demonstrate patterns, most of the columns with names that
start with `pred_` are categorical but currently have string elements. It would
be good to cast them to the `Categorical` type. To begin, select all of the
columns with names that start with `pred_`:

```{code-cell}
terns.select(
    pl.col("^pred_.*$")
).head()
```

There are a few columns in the result, such as `pred_eggs`, with `Int64`
elements. These columns aren't categorical, so we should exclude them before
casting. You can exclude columns from an expression with the `.exclude` method:

```{code-cell}
terns.select(
    pl.col("^pred_.*$").exclude(pl.Int64).cast(pl.Categorical)
).head()
```

To make this change permanent, we need to reassign the `terns` data frame. The
`.select` method only returns the selected columns, so assigning the result to
`terns` would mean losing all of the other columns.

Instead of using `.select`, you can use `.with_columns` to transform some
columns but return all of the columns. In all other respects, `.with_columns`
works the same way as `.select`. So to make the cast permanent:

```{code-cell}
terns = terns.with_columns(
    pl.col("^pred_.*$").exclude(pl.Int64).cast(pl.Categorical)
)

terns.head()
```

:::{tip}
In general, choose:

* `.select` if you only want to get back the selected columns.
* `.with_columns` if you want get back all of the columns.

The `.select` method is also useful for testing expressions before switching to
the `.with_columns` method.
:::


You can use columns to transform other columns. As a final example, suppose we
want to compute eggs per breeding pair and nests per breeding pair for the
least terns data. Non-predated egg counts are in the `nonpred_eggs` column and
nest counts are in the `total_nests` column. For now, we'll use the maximum
reported breeding pairs, `bp_max`, as the number of breeding pairs:

```{code-cell}
terns.select(
    pl.col("nonpred_eggs", "total_nests") / pl.col("bp_max")
).head()
```

There's also a `bp_min` column with the minimum reported breeding pairs. To be
thorough, we should compute the rates with both `bp_min` and `bp_max`, not just
`bp_max`. We'll also need to rename the resulting columns, so that each column
has a unique name. You can use the `.alias` method to rename a single column,
or the `.name.prefix` and `.name.suffix` methods, respectively, to prefix or
suffix a column's name. Let's add a suffix to the column names to identify
which breeding pair column was used:

```{code-cell}
terns.select(
    (
        pl.col("nonpred_eggs", "total_nests") / pl.col("bp_max")
    ).name.suffix("_per_bp_max"),
    (
        pl.col("nonpred_eggs", "total_nests") / pl.col("bp_min")
    ).name.suffix("_per_bp_min")
).head()
```

:::{seealso}
Much more is possible with Polars expressions and the `.select` and
`.with_columns` methods. See the [Polars User Guide][pl-guide] for details.

[pl-guide]: https://docs.pola.rs/user-guide/concepts/expressions-and-contexts/
:::


### Filtering Rows

Filtering the rows of a data frame is the counterpart selecting columns. The
`.filter` method filters rows based on one or more **conditions**: expressions
that evaluate to a series of Boolean values.

As an example, suppose we want to find all sites in the least terns data where
the number of nests in the `total_nests` column is greater than 5. Here's the
code:

```{code-cell}
terns.filter(pl.col("total_nests") > 5).head()
```

If we only want the site names, we can chain this with a call to `.select` and
use the `.unique` method on the `site_name` column:

```{code-cell}
terns.filter(
    pl.col("total_nests") > 5
).select(
    pl.col("site_name").unique()
)
```

We can conclude that there are 40 sites that had at least 5 nests at some
point.


#### Logic Operators

Series with Boolean elements, such as conditions, can be inverted or combined
with logic operators. All of the logic operators broadcast to series elements.
For demonstration, we'll use the following series:

```{code-cell}
x1 = pl.Series([True, False, True, False])
x2 = pl.Series([True, True, False, False])
```

The **NOT operator** `~` inverts values, so `True` becomes `False` and `False`
becomes `True`:

```{code-cell}
~x1
```

The **OR operator** `|` combines two values, returning `True` unless both
values are `False`:

```{code-cell}
x1 | x2
```

The **AND operator** `&` combines two values, returning `False` unless both
values are `True`:

```{code-cell}
x1 & x2
```

:::{caution}
The logic operators `~`, `|`, and `&` only work on Polars series, NumPy arrays,
and other homogeneous data structures. If you use them on Python's built-in
`bool` values, Python will return an unexpected result or produce an error.

Python instead uses the keywords `not`, `or`, and `and` as the respective logic
operators on `bool` values. Polars, NumPy, and other packages don't use these
keywords because their behavior can't be customized for data structures.
:::


#### Multiple Conditions

As a final example, let's filter the least terns data with multiple conditions.
We'll get all rows for 2023 where there were at least 10 fledglings reported.
We'll use the `fl_min` column for the minimum reported fledgling count. Here's
the call to `.filter`:

```{code-cell}
terns.filter(
    (pl.col("year") == 2023) &
    (pl.col("fl_min") > 10)
)
```

This gives us 14 sites with at least 10 fledglings in 2023. Notice that we had
to put the conditions in parentheses `()` so that Python gets the order of
operations right.


## Exercises

### Exercise

Python's `range` function offers another way to create a sequence of numbers.
Read the help file for this function.

1. Create an example range. How does this differ from a list?
2. Describe the three arguments that you can use in `range`. Give examples of
  each.
3. Convert one of those ranges to a list and print it to screen. What changes
  in the way Python represents this sequence?


### Exercise

Return to the discussion in {ref}`sec-coercion-casting`.

1. Why does `"3" + 4` raise an error?
2. Why does `True - 1` return 0?
3. Why does `int(4.6) < 4.6` return `True`?


### Exercise

1.  Create a new data frame from the least terns data with the following
    characteristics:
      * Each entry's year is between 2010 and 2019 (inclusive).
      * Each entry reports at least 100 breeding pairs.
      * The columns are `year`, `site_name`, `bp_min`, `bp_max`,
        `total_nests`.

    Use this data frame for the remaining questions.

2.  Count the number of entries for each site. How many sites have at least 100
    breeding pairs across all 10 years?

3.  Which site-year combination has the highest number of nests?
