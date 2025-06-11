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


# Organizing Code

:::{admonition} Learning Objectives
:class: note
After this lesson, you should be able to:

* Write functions to organize and encapsulate reusable code
* Create code that only runs when a condition is satisfied
* Identify when a problem requires iteration
* Select appropriate iteration strategies for problems
:::

(functions)=
## Functions

The main way to interact with Python is by calling functions, which was first
explained back in {ref}`calling-functions`. This section explains how to write
your own functions.

First, a review of what functions are and some of the vocabulary associated
with them:

* **Parameters** are placeholder variables for inputs.
    + **Arguments** are the actual values assigned to the parameters in a call.
* The **return value** is the output.
* **Calling** a function means using a function to compute something.
* The **body** is the code inside.

It's useful to think of functions as factories, meaning arguments go in and a
return value comes out. Here's a visual representation of the idea for a
function `f`:

```{image} ../img/functions.png
:alt: A diagram which shows arguments go into a function and a return value comes out.
```

A function definition begins with the `def` keyword, followed by:

* The name of the function
* A list of parameters surrounded by parentheses
* A colon `:`

A function can have any number of parameters. Code in the body of the function
must be indented by 4 spaces. Use the `return` keyword to return a result. The
`return` keyword causes the function to return a result immediately, without
running any subsequent code in its body.

For example, let's create a function that detects negative numbers. It should
take a series of numbers as input, compare them to zero, and then return the
logical result from the comparison as output. Here's the code to do that:

```{code-cell}
def is_negative(x):
    return x < 0
```

The name of the function, `is_negative`, describes what the function does and
includes a verb. The parameter `x` is the input. The return value is the result
of `x < 0`.

:::{tip}
Choosing descriptive names is a good habit. For functions, that means choosing
a name that describes what the function does. It often makes sense to use verbs
in function names.
:::

Any time you write a function, the first thing you should do afterwards is test
that it actually works. Try the `is_negative` function on a few test cases:

```{code-cell}
import polars as pl

x = pl.Series([5, -1, -2, 0, 3])

is_negative(6)
```

```{code-cell}
is_negative(-1.1)
```

```{code-cell}
is_negative(x)
```

Notice that the parameter `x` inside the function is different from the
variable `x` you created outside the function. Remember that parameters and
variables inside of a function are separate from variables outside of a
function.

Recall that a default argument is an argument assigned to a parameter if no
argument is assigned in the call to the function. You can use `=` to assign
default arguments to parameters when you define a function with the `def`
keyword.

For example, suppose you want to write a function that gets the largest values
in a series. You can make a parameter for the number of values to get, with a
default argument of `5`. Here's the code and some test cases:

```{code-cell}
def get_largest(x, n = 5):
    return x.sort(descending=True).head(n)

y = pl.Series([-6, 7, 10, 3, 1, 15, -2])

get_largest(y, 3)
```

```{code-cell}
get_largest(y)
```

:::{tip}
The `return` keyword causes a function to return a result immediately, without
running any subsequent code in its body. So before the end of the function, it
only makes sense to use `return` from inside of
{ref}`sec-conditional-statements`.
:::

A function returns one object, but sometimes computations have multiple
results. In that case, return the results in a container such as a tuple or
list.

For example, let's make a function that computes the mean and median for a
vector. We'll return the results in a tuple:

```{code-cell}
def compute_mean_med(x):
    m1 = x.mean()
    m2 = x.median()
    return m1, m2

compute_mean_med(pl.Series([1, 2, 3, 1]))
```


:::{tip}
Before you write a function, it's useful to go through several steps:

1. Write down what you want to do, in detail. It can also help to
   draw a picture of what needs to happen.

2. Check whether there's already a built-in function. Search online and in the
   Python documentation.

3. Write the code to handle a simple case first. For data science
   problems, use a small dataset at this step.
:::


Functions are the building blocks for solving larger problems. Take a
divide-and-conquer approach, breaking large problems into smaller steps. Use a
short function for each step. This approach makes it easier to:

* Test that each step works correctly.
* Modify, reuse, or repurpose a step.


(sec-conditional-statements)=
## Conditional Statements

Sometimes you'll need code to do different things depending on a condition. You
can use an **if-statement** to write conditional code.

An if-statement begins with the `if` keyword, followed by a condition and a
colon `:`. The condition must be an expression that returns a Boolean value
(`False` or `True`). The **body** of the if-statement is the code that will run
when the condition is `True`. Code in the body must be indented by 4 spaces.

For example, suppose you want your code to generate a different greeting
depending on an input name:

```{code-cell}
name = "Nick"

# Default greeting
greeting = "Nice to meet you!"

if name == "Nick":
    greeting = "Hi Nick, nice to see you again!"

greeting
```

Use the `else` keyword (and a colon `:`) if you want to add an alternative when
the condition is false. So the previous code can also be written as:

```{code-cell}
name = "Nick"

if name == "Nick":
    greeting = "Hi Nick, nice to see you again!"
else:
    # Default greeting
    greeting = "Nice to meet you!"

greeting
```

Use the `elif` keyword with a condition (and a colon `:`) if you want to add an
alternative to the first condition that also has its own condition. Only the
first case where a condition is `True` will run. You can use `elif` as many
times as you want, and can also use `else`. For example:

```{code-cell}
name = "Susan"

if name == "Nick":
   greeting = "Hi Nick, nice to see you again!"
elif name == "Peter":
   greeting = "Go away Peter, I'm busy!"
else:
   greeting = "Nice to meet you!"

greeting
```

You can create compound conditions with the keywords `not`, `and` and `or`. The
`not` keyword inverts a condition. The `and` keyword combines two conditions
and returns `True` only if both are `True`. The `or` keyword combines two
conditions and returns `True` if either or both are `True`.
For example:

```{code-cell}
name1 = "Arthur"
name2 = "Nick"

if name1 == "Arthur" and name2 == "Nick":
  greeting = "These are the authors."
else:
  greeting = "Who are these people?!"

greeting
```

You can write an if-statement inside of another if-statement. This is called
**nesting** if-statements. Nesting is useful when you want to check a
condition, do some computations, and then check another condition under the
assumption that the first condition was `True`.

:::{tip}
If-statements correspond to **special cases** in your code. Lots of special
cases in code makes the code harder to understand and maintain. If you find
yourself using lots of if-statements, especially nested if-statements, consider
whether there is a more general strategy or way to write the code.
:::


(iteration)=
## Iteration

Python is powerful tool for automating tasks that have repetitive steps. For
example, you can:

* Apply a transformation to an entire column of data.
* Compute distances between all pairs from a set of points.
* Read a large collection of files from disk in order to combine and analyze
  the data they contain.
* Simulate how a system evolves over time from a specific set of starting
  parameters.
* Scrape data from the pages of a website.

You can implement concise, efficient solutions for these kinds of tasks in
Python by using **iteration**, which means repeating a computation many times.
Python provides four different strategies for writing iterative code:

1. Broadcasting, where a function is implicitly called on each element of a
   data structure. This was introduced in {ref}`sec-broadcasting`.
2. Comprehensions, where a function is explicitly called on each element of a
   vector or array. This was introduced in {ref}`sec-comprehensions`.
3. Loops, where an expression is evaluated repeatedly until some condition is
   met.
4. Recursion, where a function calls itself.

Broadcasting is the most efficient and most concise iteration strategy, but
also the least flexible, because it only works with a few functions and data
structures. Comprehensions are more flexible---they work with any function and
any data structure with elements---but less efficient and less concise. Loops
and recursion provide the most flexibility but are the least concise. In recent
versions of Python, comprehensions are slightly more efficient than loops.
Recursion tends to be the least efficient iteration strategy in Python.

The rest of this section explains how to write loops and how to choose which
iteration strategy to use. We assume you're already comfortable with
broadcasting and have at least some familiarity with comprehensions.

### For-Loops

A **for-loop** evaluates the expressions in its body once for each element of a
data structure. A for-loop begins with the `for` keyword, followed by:

* A placeholder variable, which will be automatically signed to an element at
  the beginning of each iteration
* The `in` keyword
* An object with elements
* A colon `:`

Code in the body of the loop must be indented by 4 spaces.

For example, to print out all the column names in `terns.columns`, you can
write:

```{code-cell}
:tags: [scroll-output]
for column in terns.columns:
    print(column)
```

Within the indented part of a for-loop, you can compute values, check
conditions, etc.

<!--
```{code-cell}
for nests in terns["total_nests"]:
    if nests > 100:
        print(nests)
```
-->

Oftentimes you want to save the result of the code you perform within a
for-loop. The easiest way to do this is by creating an empty list and using
`append` to add values to it.

```{code-cell}
diffs = []
values = [10, 12, 11, 2, 3]

for a, b in zip(values[:-1], values[1:]):
    diffs.append(a - b)

diffs
```

### Planning for Iteration

At first it might seem difficult to decide if and what kind of iteration to
use. Start by thinking about whether you need to do something over and over. If
you don't, then you probably don't need to use iteration. If you do, then try
iteration strategies in this order:

1. Broadcasting
2. Comprehensions
    * Try a comprehension if iterations are independent.
3. Loops
    * Try a for-loop if some iterations depend on others.
    <!--
    * Try a while-loop if the number of iterations is unknown.
    -->
4. Recursion (which isn't covered here)
    * Convenient for naturally recursive tasks (like Fibonacci), but often
      there are faster solutions.

Start by writing the code for just one iteration. Make sure that code works;
it's easy to test code for one iteration.

When you have one iteration working, then try using the code with an iteration
strategy (you will have to make some small changes). If it doesn't work, try to
figure out which iteration is causing the problem. One way to do this is to use
`print` to print out information. Then try to write the code for the broken
iteration, get that iteration working, and repeat this whole process.


## Case Study: CA Hospital Utilization

The California Department of Health Care Access and Information (HCAI) requires
hospitals in the state to submit detailed information each year about how many
beds they have and the total number of days for which each bed was occupied.
The HCAI publishes the data to the [California Open Data Portal][data.ca.gov].
Let's use Python to read data from 2016 to 2023 and investigate whether
hospital utilization is noticeably different in and after 2020.

[data.ca.gov]: https://data.ca.gov/

The data set consists of a separate Microsoft Excel file for each year. Before
2018, HCAI used a data format (in Excel) called ALIRTS. In 2018, they started
collecting more data and switched to a data format called SIERA. The 2018 data
file contains a **crosswalk** that shows the correspondence between SIERA
columns and ALIRTS columns.

:::{important}
[Click here][ca-hospitals] to download the CA Hospital Utilization data set (8
Excel files).

If you haven’t already, we recommend you create a directory for this workshop.
In your workshop directory, create a `data/ca_hospitals` subdirectory. Download
and save the data set in the `data/ca_hospitals` subdirectory.

[ca-hospitals]: https://ucdavis.box.com/s/g5tanw22647dw3uyhv3om0zt3duuj5lc
:::

When you need to solve a programming problem, get started by writing some
comments that describe the problem, the inputs, and the expected output. Try to
be concrete. This will help you clarify what you're trying to achieve and serve
as a guiding light while you work.

As a programmer (or any kind of problem-solver), you should always be on the
lookout for ways to break problems into smaller, simpler steps. Think about
this when you frame a problem. Small steps are easier to reason about,
implement, and test. When you complete one, you also get a nice sense of
progress towards your goal. 

For the CA Hospital Utilization data set, our goal is to investigate whether
there was a change in hospital utilization in 2020. Before we can do any
investigation, we need to read the files into Python. The files all contain
tabular data and have similar formats, so let's try to combine them into a
single data frame. We'll say this in the framing comments:

```python
# Read the CA Hospital Utilization data set into Python. The inputs are
# yearly Excel files (2016-2023) that need to be combined. The pre-2018 files
# have a different format from the others. The result should be a single data
# frame with information about bed and patient counts.
#
# After reading the data set, we'll investigate utilization in 2020.
```

"Investigate utilization" is a little vague, but for an exploratory data
analysis, it's hard to say exactly what to do until you've started working with
the data.

We need to read multiple files, but we can simplify the problem by starting
with just one. Let's start with the 2023 data. It's in an Excel file, which you
can read with Polars' `pl.read_excel` function (note: you'll first need to
install the fastexcel package). The function requires the path to the file; you
can also optionally provide the sheet name or number (starting from 1). Open up
the Excel file in your computer's spreadsheet program and take a look. There
are multiple sheets, and the data about beds and patients are in the second
sheet. Back in Python, read just the second sheet:

```{code-cell}
path = "data/ca_hospitals/hosp23_util_data_final.xlsx"
sheet = pl.read_excel(path, sheet_id=2)
sheet.head()
```

The first four rows contain metadata about the columns; the first hospital,
Alameda Hospital, is listed in the fifth row. So let's remove the first four
rows:

```{code-cell}
sheet = sheet[4:, :]
sheet.head()
```

Some data sets also have metadata in the last rows, so let's check for that
here:

```{code-cell}
sheet.tail()
```

Sure enough, the last row contains what appears to be a count of the hospitals
rather than a hospital. Let's remove it by indexing with a negative value,
which counts backward from the end:

```{code-cell}
sheet = sheet[:-1, :]
sheet.tail()
```

There are a lot of columns in sheet, so let's make a list of just a few that
we'll use for analysis. We'll keep:

* Columns with facility name, location, and operating status
* All of the columns whose names start with `TOT`, because these are totals for
  number of beds, number of census-days, and so on.
* Columns about acute respiratory beds, with names that contain `RESPIRATORY`,
  because they might also be relevant.

We can get all of these columns with the `.select` method. The `TOT` and
`RESPIRATORY` columns all contain numbers, but the element type is `str`, so
we'll cast them to floats. We'll also add a column with the year:

```{code-cell}
facility_cols = pl.col(
    "FAC_NAME", "FAC_CITY", "FAC_ZIP", "FAC_OPERATED_THIS_YR", "FACILITY_LEVEL",
    "TEACH_HOSP", "COUNTY", "PRIN_SERVICE_TYPE",
)

sheet = sheet.select(
    pl.lit(2023).alias("year"),
    facility_cols,
    pl.col("^TOT.*$", "^.*RESPIRATORY.*$").cast(pl.Float64),
)
sheet.head()
```

Lowercase names are easier to type, so let's also make all of the names
lowercase with the `.rename` and `str.lower` methods:

```{code-cell}
sheet = sheet.rename(str.lower)
sheet.head()
```

We've successfully read one of the files! Since the 2018-2023 files all have
the same format, it's likely that we can use almost the same code for all of
them. Any time you want to reuse code, it's a sign that you should write a
function, so that's what we'll do. We'll take all of the code we have so far
and put it in the body of a function called `read_hospital_data`, adding some
comments to indicate the steps and a `return` statement at the end:

```python
def read_hospital_data():
    # Read the 2nd sheet of the file.
    path = "data/ca_hospitals/hosp23_util_data_final.xlsx"
    sheet = pl.read_excel(path, sheet_id=2)
    
    # Remove the first 4 and last row.
    sheet = sheet[4:, :]
    sheet = sheet[:-1, :]

    # Select only a few columns of interest.
    facility_cols = pl.col(
        "FAC_NAME", "FAC_CITY", "FAC_ZIP", "FAC_OPERATED_THIS_YR",
        "FACILITY_LEVEL", "TEACH_HOSP", "COUNTY", "PRIN_SERVICE_TYPE",
    )

    sheet = sheet.select(
        pl.lit(2023).alias("year"),
        facility_cols,
        pl.col("^TOT.*$", "^.*RESPIRATORY.*$").cast(pl.Float64),
    )

    # Rename the columns to lowercase.
    sheet = sheet.rename(str.lower)

    return sheet
```

As it is, the function still only reads the 2023 file. The other files have
different paths, so the first thing we need to do is make the `path` variable a
parameter. We'll also make a `year` parameter, for the year value inserted as a
column:

```{code-cell}
def read_hospital_data(path, year):
    # Read the 2nd sheet of the file.
    sheet = pl.read_excel(path, sheet_id=2)
    
    # Remove the first 4 and last row.
    sheet = sheet[4:-1, :]

    # Select only a few columns of interest.
    facility_cols = pl.col(
        "FAC_NAME", "FAC_CITY", "FAC_ZIP", "FAC_OPERATED_THIS_YR",
        "FACILITY_LEVEL", "TEACH_HOSP", "COUNTY", "PRIN_SERVICE_TYPE",
    )

    sheet = sheet.select(
        pl.lit(year).alias("year"),
        facility_cols,
        pl.col("^TOT.*$", "^.*RESPIRATORY.*$").cast(pl.Float64),
    )

    # Rename the columns to lowercase.
    sheet = sheet.rename(str.lower)

    return sheet
```

Test the function out on a few of the files to make sure it works correctly:

```{code-cell}
read_hospital_data(
    "data/ca_hospitals/hosp23_util_data_final.xlsx", 2023
).head()
```

```{code-cell}
read_hospital_data(
    "data/ca_hospitals/hosp21_util_data_final-revised-06.15.2023.xlsx", 2021
).head()
```

The function appears to work correctly for two of the files, so let's try it on
all of the 2018-2023 files. We can use the built-in `pathlib` module's `Path`
class to help get a list of the files. The class' `.glob` method does a
wildcard search for files:

```{code-cell}
from pathlib import Path

paths = Path("data/ca_hospitals/").glob("*.xlsx")
paths = list(paths)
paths
```

In addition to the file paths, we also need the year for each file.
Fortunately, the last two digits of the year are included in each file's name.
We can write a function to get these:

```{code-cell}
def get_hospital_year(path):
    year = Path(path).name[4:6]
    return int(year) + 2000


get_hospital_year(paths[0])
```

Now we can use a for-loop to iterate over all of the files. We'll skip the
pre-2018 files for now:

```{code-cell}
hosps = []

for path in paths:
    year = get_hospital_year(path)
    # Only years 2018-2023.
    if year >= 2018:
        hosp = read_hospital_data(path, year)
        hosps.append(hosp)

len(hosps)
```

With that working, we need to read the pre-2018 files. In the 2018 file, the
fourth sheet is a crosswalk that shows which columns in the pre-2018 files
correspond to columns in the later files. Let's write some code to read the
crosswalk. First, read the sheet:

```{code-cell}
cwalk = pl.read_excel(path, sheet_id=4)
cwalk.head()
```

The new and old column names are in the fourth and fifth columns, respectively,
so we'll get just those:

```{code-cell}
cwalk = cwalk[:, 3:5]
cwalk.head()
```

Finally, use a comprehension to turn the `cwalk` data frame into a dictionary
with the old column names as the keys and the new column names as the values.
This way we can easily look up the new name for any of the old columns. Some of
the column names in `cwalk` have extra spaces at the end, so we'll use `.strip`
method to remove them. We'll also skip any rows where there's no old column
name (because the column is only in the new data):

```{code-cell}
:tags: [scroll-output]
cwalk = {
    old.strip(): new.strip()
    for new, old in cwalk.iter_rows()
    if old is not None
}

cwalk
```

We can now define a new version of the `read_hospital_data` function that uses
the crosswalk to change the column names when `year < 2018`. You can use the
dict `.get` method, which tries to get the value for the key in its first
argument and returns its second argument if that key isn't in the dict. Let's
also change function to exclude columns with `ALOS` in the name, because they
have no equivalent in the pre-2018 files:


```{code-cell}
def read_hospital_data(path, year):
    # Read the 2nd sheet of the file.
    sheet = pl.read_excel(path, sheet_id=2)
    
    # Remove the first 4 and last row.
    sheet = sheet[4:-1, :]

    # Fix pre-2018 column names.
    if year < 2018:
        sheet.columns = [cwalk.get(c, c) for c in sheet.columns]

    # Select only a few columns of interest.
    facility_cols = pl.col(
        "FAC_NAME", "FAC_CITY", "FAC_ZIP", "FAC_OPERATED_THIS_YR",
        "FACILITY_LEVEL", "TEACH_HOSP", "COUNTY", "PRIN_SERVICE_TYPE",
    )

    sheet = sheet.select(
        pl.lit(year).alias("year"),
        facility_cols,
        pl.col("^TOT.*$", "^.*RESPIRATORY.*$")
            .exclude("^.*ALOS.*$")
            .cast(pl.Float64),
    )

    # Rename the columns to lowercase.
    sheet = sheet.rename(str.lower)

    return sheet
```

Now we can test the function on all of the files. This time, we'll check that

```{code-cell}
hosps = []

for path in paths:
    year = get_hospital_year(path)
    hosp = read_hospital_data(path, year)
    hosps.append(hosp)

len(hosps)
```

You can use the `pl.concat` function to concatenate, or stack, a list of data
frames:

```{code-cell}
hosps = pl.concat(hosps)
hosps.head()
```

We've finally got all of the data in a single data frame!

To begin to address whether hospital utilization changed in 2020, let's make a
bar plot of total census-days:

```{code-cell}
from plotnine import *

(
    ggplot(hosps) +
    aes(x = "year", weight = "tot_cen_days") +
    geom_bar()
)
```

According to the plot, total census-days was slightly lower in 2020 than in
2019. This is a bit surprising, but it's possible that California hospitals
typically operate close to maximum capacity and were not able to substantially
increase the number of beds in 2020 in response to the COVID-19 pandemic. You
can use other columns in the data set, such as `tot_lic_beds` or
`tot_lic_bed_days`, to check this.

Let's also look at census-days for acute respiratory care:


```{code-cell}
(
    ggplot(hosps) +
    aes(x = "year", weight = "acute_respiratory_care_cen_days") +
    geom_bar()
)
```

In this plot, there's a clear uptick in census-days in 2020, and then an
interesting decrease to below 2019 levels in the years following. Again, you
could use other columns in the data set to investigate this further. We'll end
this case study here, having accomplished the difficult task of reading the
data and the much easier task of doing a cursory preliminary analysis of the
data.


## Exercises

### Exercise 1

Try writing a function `is_leap` that detects leap years. The input to your
function should be an integer year (or a series of years), and the output
should be a Boolean value. A year is a leap year if either of these conditions
is true:

* It is divisible by 4 and not 100
* It is divisible by 400

That means the years 2004 and 2000 are leap years, but the year 2200 is not.

Hint: The modulo operator `%` returns the remainder after divding a number, so
for example `4 % 3` returns `1`.

Here's a few test cases for your function:

```
is_leap(400)
is_leap(1997)
```

<!--
```python
# If year is divisible by 4 and not 100 -> leap
# If year is divisible by 400 -> leap
year = 2004

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

is_leap(2200)
```
-->
