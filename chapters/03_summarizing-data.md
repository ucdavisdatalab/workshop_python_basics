Summarizing Data
================

## Recap


## The Python Data Visualization Landscape

Popular packages for creating visualizations in Python are

The plotnine package
The ggplot2 package is so popular that there are now knockoff packages for
other data-science-oriented programming languages like Python and Julia. 
This reader 
we'll use
ggplot2 for visualizations in this and all future lessons.

[tidy]: https://www.tidyverse.org/

ggplot2 has detailed [documentation][ggplot2-docs] and also a
[cheatsheet][ggplot2-cheat].

[ggplot2-docs]: https://ggplot2.tidyverse.org/
[ggplot2-cheat]: https://github.com/rstudio/cheatsheets/blob/master/data-visualization-2.1.pdf


## The Grammar of Graphics

The "gg" in ggplot2 stands for _grammar of graphics_. The idea of a grammar of
graphics is that visualizations can be built up in layers. In ggplot2, the
three layers every plot must have are:

* Data
* Geometry
* Aesthetics

There are also several optional layers. Here are a few:

Layer       | Description
----------  | -----------
scales      | Title, label, and axis value settings
facets      | Side-by-side plots
guides      | Axis and legend position settings
annotations | Shapes that are not mapped to data
coordinates | Coordinate systems (Cartesian, logarithmic, polar)


As an example, let's plot the earnings data. First, we need to load ggplot2. As
always, if this is your first time using the package, you'll have to install
it. Then you can load the package:

```
import plotnine
```

What kind of plot should we make? It depends on what data we want the plot to
show. Let's make a line plot that shows median earnings for each quarter in
2019, with separate lines for men and women.


### Layer 1: Data

The data layer determines the data set used to make the plot. plotnine is
designed for working with **tidy** data frames. Tidy means:

1. Each observation has its own row.
2. Each feature has its own column.
3. Each value has its own cell.

To set up the data layer, call the `ggplot` function on a data frame:
```
ggplot(parks)
```

This returns a blank plot. We still need to add a few more layers.


### Layer 2: Geometry

The **geom**etry layer determines the shape or appearance of the visual
elements of the plot. In other words, the geometry layer determines what kind
of plot to make: one with points, lines, boxes, or something else.

There are many different geometries available in ggplot2. The package provides
a function for each geometry, always prefixed with `geom_`.

To add a geometry layer to the plot, choose the `geom_` function you want and
add it to the plot with the `+` operator:
```
ggplot(earn19) + geom_line()
```

This returns an error message that we're missing aesthetics `x` and `y`. We'll
learn more about aesthetics in the next section, but this error message is
especially helpful: it tells us exactly what we're missing. When you use a
geometry you're unfamiliar with, it can be helpful to run the code for just the
data and geometry layer like this, to see exactly which aesthetics need to be
set.

As we'll see later, it's possible to add multiple geometries to a plot.


### Layer 3: Aesthetics

The **aes**thetic layer determines the relationship between the data and the
geometry. Use the aesthetic layer to map features in the data to **aesthetics**
(visual elements) of the geometry.

The `aes` function creates an aesthetic layer. The syntax is:
```
aes(AESTHETIC = FEATURE, ...)
```

The names of the aesthetics depend on the geometry, but some common ones are
`x`, `y`, `color`, `fill`, `shape`, and `size`. There is more information about
and examples of aesthetic names in the documentation.

For example, we want to put `quarter` on the x-axis and `median_weekly_earn` on
the y-axis. We also want to use a separate line style for each `sex` category.
So the aesthetic layer should be:
```
aes(x = quarter, y = median_weekly_earn, linetype = sex)
```

In the `aes` function, column names are never quoted.

Unlike most layers, the aesthetic layer is not added to the plot with the `+`
operator. Instead, you can pass the aesthetic layer as the second argument to
the `ggplot` function:
```{r}
ggplot(earn19, aes(x = quarter, y = median_weekly_earn, linetype = sex)) +
  geom_line()
```

If you want to set an aesthetic to a constant value, rather than one that's
data dependent, do so *outside* of the aesthetic layer. For instance, suppose
we want to make the lines blue:

```
ggplot(earn19, aes(x = quarter, y = median_weekly_earn, linetype = sex)) +
  geom_line(color = "blue")
```

If you set an aesthetic to a constant value inside of the aesthetic layer, the
results you get might not be what you expect:
```
ggplot(earn19, aes(x = quarter, y = median_weekly_earn, linetype = sex,
    color = "blue")) + geom_line()
```

<!--
#### Per-geometry Aesthetics {-}

When you pass an aesthetic layer to the `ggplot` function, it applies to the
entire plot. You can also set an aesthetic layer individually for each
geometry, by passing the layer as the first argument in the `geom_` function:
```{r}
#ggplot(favs) + geom_point(aes(x = distance_mi, y = walk_min))
```

This is really only useful when you have multiple geometries. As an example,
let's color-code the points by major:
```{r}
#ggplot(favs, aes(x = distance_mi, y = walk_min, color = major)) +
#  geom_point()
```

Now let's also add labels to each point. To do this, we need to add another
geometry:
```{r}
#ggplot(favs, aes(x = distance_mi, y = walk_min, color = major, label = major)) +
#  geom_point() + geom_text(size = 2)
```

Where we put the aesthetics matters:
```{r}
#ggplot(favs, aes(x = distance_mi, y = walk_min, label = major)) +
#  geom_point() + geom_text(aes(color = major), size = 2)
```
-->

### Layer 4: Scales

The scales layer controls the title, axis labels, and axis scales of the plot.
Most of the functions in the scales layer are prefixed with `scale_`, but not
all of them.

The `labs` function is especially important, because it's used to set the title
and axis labels:
```
ggplot(earn19, aes(x = quarter, y = median_weekly_earn, linetype = sex)) +
  geom_line() + labs(x = "Quarter", y = "Median Weekly Salary (USD)",
    title = "2019 Median Weekly Salaries, by Sex", linetype = "Sex")
```


### Saving Plots

In ggplot2, use the `ggsave` function to save the most recent plot you created:

```
ggsave("line.png")
```

The file format is selected automatically based on the extension. Common
formats are PNG and PDF.



## Grouping Data

## Functions

The main way to interact with Python is by calling functions, which was first
explained way back in TODO. This section explains how you can write your own
functions.

First, a review of what functions are, and some of the jargon associated with
them. It's useful to think of functions as factories: raw materials (inputs) go
in, products (outputs) come out. Here's a visual representation of this idea:

```
         +-------+
-- in -->|   f   |-- out -->
         +-------+
```

Programmers use several specific terms to describe the parts and usage of
functions:

* **Parameters** are placeholder variables for inputs.
    + **Argument** are the actual values assigned to the parameters in a call.
* The **return value** is the output.
* The **body** is the code inside.
* **Calling** a function means using a function to compute something.

<!--
You can view the body of a function by typing its name without trailing
parentheses (in contrast to how you call functions). The body of a function is
usually surrounded by curly braces `{}`, although they're optional if the body
only contains one line of code. Indenting code inside of curly
braces by 2-4 spaces also helps make it visually distinct from other code.

For example, let's look at the body of the `append` function, which appends a
value to the end of a list or vector:

```{r}
append
```

Don't worry if you can't understand everything the `append` function's code
does yet. It will make more sense later on, after you've written a few
functions of your own.

Many of R's built-in functions are not entirely written in R code. You can spot
these by calls to the special `.Primitive` or `.Internal` functions in their
code.

For instance, the `sum` function is not written in R code:

```{r}
sum
```
-->

The `def` keyword creates a new function. Here's the syntax:

```
def my_function(parameter1, parameter2):
  # Your code goes here
  
  # The result goes here
```

A function can have any number of parameters. Use the `return` key

Like variables, functions have names. Choosing descriptive names is a good
habit. For functions, that means choosing a name that describes what the
function does. It often makes sense to use verbs in function names.

Let's create a function that detects negative numbers. It should take a Series
of numbers as input, compare them to zero, and then return the logical result
from the comparison as output. Here's the code to do that:

```
def is_negative(x):
  return x < 0
```

The name of the function, `is_negative`, describes what the function does and
includes a verb. The parameter `x` is the input. The return value is the result
of `x < 0`.

Any time you write a function, the first thing you should do afterwards is test
that it actually works. Try the `is_negative` function on a few test cases:

```
x = pd.Series([5, -1, -2, 0, 3])

is_negative(6)
is_negative(-1.1)
is_negative(x)
```

Notice that the parameter `x` inside the function is different from the
variable `x` you created outside the function. Remember that parameters and
variables inside of a function are separate from variables outside of a
function.

A **default argument** is an argument assigned to a parameter if no argument is
assigned in the call to the function. You can use `=` to assign default
arguments to parameters when you define a function with the `def` keyword.

For example, suppose you want to write a function that gets the largest values
in a Series. You can make a parameter for the number of values to get, with a
default argument of `5`. Here's the code and some test cases:

```{r}
def top_n(x, n = 5):

top = function(x, n = 5) {
  sorted = sort(x, decreasing = TRUE)
  head(sorted, n)
}

y = c(-6, 7, 10, 3, 1, 15, -2)
top(y, 3)
top(y)
```

### Returning Values

We've already seen that a function will automatically return the value of its
last line.

The `return` keyword causes a function to return a result immediately, without
running any subsequent code in its body. It only makes sense to use `return`
from inside of an if-statement. If your function doesn't have any
if-statements, you don't need to use `return`.

For example, suppose we want the `is_negative` function to return `NA` if the
argument isn't a number. This is an ideal case to use `return`, since we skip
the computation `x < 0` when the argument isn't a number. Here's the new
version of the function, as well as a new test case:

```{r}
is_negative = function(x) {
  if (!is.numeric(x))
    return (NA)
  
  # TRUE for negative numbers, FALSE otherwise
  x < 0
}

is_negative("hi")
```

It's idiomatic to only use `return` when strictly necessary. 

A function returns one R object, but sometimes computations have multiple
results. In that case, return the results in a vector, list, or other data
structure.

For example, let's make a function that computes the mean and median for a
vector. We'll return the results in a named list, although we could also use a
named vector:

```{r}
compute_mean_med = function(x) {
  m1 = mean(x)
  m2 = median(x)
  list(mean = m1, median = m2)
}
compute_mean_med(c(1, 2, 3, 1))
```

The names make the result easier to understand for the caller of the function,
although they certainly aren't required here.


### Planning Your Functions

Before you write a function, it's useful to go through several steps:

1. Write down what you want to do, in detail. It can also help to
   draw a picture of what needs to happen.

2. Check whether there's already a built-in function. Search online and in the
   R documentation.

3. Write the code to handle a simple case first. For data science
   problems, use a small dataset at this step.

Let's apply this in one final example: a function that detects leap years. A
year is a leap year if either of these conditions is true:

* It is divisible by 4 and not 100
* It is divisible by 400

That means the years 2004 and 2000 are leap years, but the year 2200 is not.
Here's the code and a few test cases:

```{r}
# If year is divisible by 4 and not 100 -> leap
# If year is divisible by 400 -> leap
year = 2004
is_leap = function(year) {
  if (year %% 4 == 0 & year %% 100 != 0) {
    leap = TRUE
  } else if (year %% 400 == 0) {
    leap = TRUE
  } else {
    leap = FALSE
  }
  leap
}
is_leap(400)
is_leap(1997)
```

Functions are the building blocks for solving larger problems. Take a
divide-and-conquer approach, breaking large problems into smaller steps. Use a
short function for each step. This approach makes it easier to:

* Test that each step works correctly.
* Modify, reuse, or repurpose a step.
