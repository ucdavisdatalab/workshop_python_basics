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
:tags: [remove_cell]
import os

os.chdir("..")
```

Exploring Data
==============

Now that you have a solid foundation in the basic functions and data structures
of Python, you can move on to using it for data analysis. In this chapter,
you'll learn how to efficiently explore and summarize with visualizations and
statistics. Along the way, you'll also learn how to write and apply functions
along entire sets of data in Pandas Data Frames and Series.

Indexing Data Frames
--------------------

This section explains how to get and set data in a DataFrame, expanding on the
indexing technique you learned in {numref}`indexing-in-pandas`. To begin, load
the banknotes data with Pandas. Load NumPy as well.

```{code-cell}
import numpy as np
import pandas as pd

banknotes = pd.read_csv("data/banknotes.csv")
```

(data-visualization)=
Data Visualization
------------------

```{image} ../img/visualization_landscape.png
:alt: A network of Python visualization packages.
```

_Image from [Jake VanderPlas][jake]. See [here][viz] for a version with links
to all of the packages!_

[jake]: http://vanderplas.com/
[viz]: https://rougier.github.io/python-visualization-landscape/landscape-colors.html

So many visualization packages are available for Python that there is even [a
website][pyviz] dedicated to helping people decide which to use. This reader
focuses on **static visualization**, where the visualization is a still image.
Some popular packages for creating static visualizations are:

[pyviz]: https://pyviz.org/

* **[matplotlib][]** is the foundation for most other visualization packages.
  matplotlib is low-level, meaning it's flexible but even simple plots may take
  [5 lines of code or more][ex]. It's good to know a little bit about
  matplotlib, but it probably shouldn't be your primary visualization package.
  Familiarity with MATLAB makes it easier to learn matplotlib.

* **[pandas][]** provides built-in plotting functions, which can be convenient
  but are more limited than what you'll find in dedicated visualization
  packages. They're also inconsistent about the expected format of the data.

* **[plotnine][]** is a copy of the popular R package [ggplot2][]. The package
  uses the **grammar of graphics**, a convenient way to describe visualizations
  in terms of layers. Familiarity with R's [ggplot2][] or Julia's
  [Gadfly.jl][gadfly] package makes it easier to learn plotnine (and
  vice-versa).

* **[seaborn][]** is designed specifically for making statistical plots. It's
  well-documented and stable.

[matplotlib]: https://matplotlib.org/
[ex]: https://dsaber.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/
[pandas]: https://pandas.pydata.org/docs/user_guide/visualization.html
[ggplot2]: https://ggplot2.tidyverse.org/
[plotnine]: https://plotnine.readthedocs.io/en/stable/
[gadfly]: http://gadflyjl.org/stable/
[seaborn]: https://seaborn.pydata.org/

There are also many packages available for making **interactive
visualizations**.

This reader focuses on plotnine, so that the visualization skills you learn
here will also be relevant if you end up using R or Julia. plotnine has
detailed [documentation][plotnine]. It's also useful to look at the [ggplot2
documentation][ggplot2] and [cheatsheet][ggplot2-cheat].

[ggplot2-cheat]: https://github.com/rstudio/cheatsheets/blob/master/data-visualization-2.1.pdf


### Configuring Jupyter

Jupyter notebooks can display most static visualizations and some interactive
visualizations. If you're going to use visualization packages that depend on
matplotlib (such as plotnine), it's a good idea to set up your notebook by
running:

```{code-cell}
# Initialize matplotlib

%matplotlib inline

import matplotlib.pyplot as plt

# We'll see what this code does later on:
plt.rcParams["figure.figsize"] = [10, 8]
```

The last line sets the default size of plots. You can increase the numbers to
make plots larger, or decrease them to make plots smaller.


(installing-packages)=
Installing Packages
-------------------

Matplotlib is included with Anaconda, but plotnine is not. So you need to
install the plotnine package in order to use it.

You can use Anaconda's conda utility to install packages. The conda utility
is a program, not part of Python. In JupyterLab, open a Terminal (`File` ->
`New` -> `Terminal`). Then enter:

```
conda install -c conda-forge plotnine
```

The command `conda install PACKAGE` installs the package called `PACKAGE`. The
flag `-c conda-forge` tells conda to use a version from the conda-forge package
repository. Packages on conda-forge are usually more up to date than the ones
in Anaconda's default package repository.

You can learn more about Anaconda and conda in the [official
documentation][conda].

[conda]: https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/


(grammar-of-graphics)=
The Grammar of Graphics
-----------------------

Recall that plotnine is a clone of ggplot2. The "gg" in ggplot2 stands for
*grammar of graphics*. The idea of a grammar of graphics is that visualizations
can be built up in layers. Visualizations that adhere to this grammar must
have:

* Data
* Geometry
* Aesthetics

There are also several optional layers. Here are a few:

| Layer       | Description                                        |
| :---------- | :------------------------------------------------- |
| scales      | Title, label, and axis value settings              |
| facets      | Side-by-side plots                                 |
| guides      | Axis and legend position settings                  |
| annotations | Shapes that are not mapped to data                 |
| coordinates | Coordinate systems (Cartesian, logarithmic, polar) |

In {numref}`modules`, you learned how to import a module in a Python package
with the `import` keyword. Python also provides a `from` keyword to import
specific objects within a module. The syntax is

```python
from <module> import <object>
```

When you import an object this way, you can access the object without the
module name as a prefix. For instance, if you imported Pandas using:

```python
from pandas import DataFrame
```

You could then write:

```python
df = DataFrame()
```

You can also use the from keyword to import all objects in a module with the
wildcard character `*`. Generally you shouldn't do this, because objects in a
module will overwrite objects in your code if they have the same name. However,
the plotnine package is designed to be imported this way:

```{code-cell}
from plotnine import *
```

From here, we can make a plot. But what kind of plot should we make? It depends
on what we want to know about the data set. Suppose we want to understand the
relationship between a banknote's value and how long ago the person on the
banknote died, as well as whether this is affected by gender. One way to show
this is to make a scatter plot.

Before plotting, we need to do a tiny amount of data cleaning. The
visualizations below use values from `death_year`, but some rows do not contain
information for this variable. We will remove those rows and then convert the
column to an integer type.

```{code-cell}
is_blank = banknotes["death_year"].isin([np.nan, "-"])
banknotes = banknotes[is_blank == False]
banknotes["death_year"] = banknotes["death_year"].astype(int)
```

Now we're ready to make the plot.


### Layer 1: Data

The data layer determines the data set used to make the plot. plotnine is
designed to work with *tidy* data. Tidy means:
1. Each observation has its own row
2. Each feature has its own column
3. Each value has its own cell

Tidy data sets are convenient in general. A later lesson will cover how to make
an untidy data set tidy. Until then, we'll take it for granted that the data
sets we work with are tidy.

To set up the data layer, call the ``ggplot` function on a Data Frame:

```{code-cell}
ggplot(banknotes)
```

This returns a blank plot. We still need to add a few more layers.


### Layer 2: Geometry

The geometry layer determines the shape or appearance of the visual elements of
the plot. In other words, the geometry layer determines what kind of plot to
make: one with points, lines, boxes, or something else.

There are many different geometries available in plotnine. The package provides
a function for each geometry, always prefixed with `geom_`.

To add a geometry layer to the plot, choose the `geom_` function you want and
add it to the plot with the `+` operator:

```{code-cell}
:tags: [raises-exception]
ggplot(banknotes) + geom_point()
```

This returns an error message that we're missing aesthetics `x` and `y`. We'll
learn more about aesthetics in the next section, but this error message is
especially helpful: it tells us exactly what we're missing. When you use a
geometry you're unfamiliar with, it can be helpful to run the code for just the
data and geometry layer like this, to see exactly which aesthetics need to be
set.

As we'll see later, it's possible to add multiple geometries to a plot.


### Layer 3: Aesthetics

The aesthetic layer determines the relationship between the data and the
geometry. Use the aesthetic layer to map features in the data to aesthetics
(visual elements) of the geometry.

The `aes` function creates an aesthetic layer. The syntax is:

```python
aes(AESTHETIC = FEATURE, ...)
```

The names of the aesthetics depend on the geometry, but some common ones are
`x`, `y`, `color`, `fill`, `shape`, and `size`. There is more information about
and examples of aesthetic names in the documentation.

For example, we want to put `death_year` on the x-axis and `scalled_bill_value`
on the y-axis. It's best to use `scaled_bill_value` here rather than
`current_bill_value` because different countries use different scales of
curency. One United States Dollar is worth approximately one hundred Japanese
Yen, for example. Below, we will set the aesthetics for both of these values.
Notice however that the aesthetic layer is not added to the plot with the `+`
operator. Instead, it is passed as the second argument to the `ggplot`
function:

```{code-cell}
ggplot(
    banknotes,
    aes(x = "death_year", y = "scaled_bill_value")
) + geom_point()
```

**Per-geometry Aesthetics**

When you add the aesthetic layer or pass it to the `ggplot` function, it
applies to the entire plot. You can also set an aesthetic layer individually
for each geometry by passing the layer as the first argument in the `geom_`
function:

```{code-cell}
(ggplot(banknotes) +
    geom_point(aes(x = "death_year", y = "scaled_bill_value"))
)
```

:::{tip}
Enclose expressions with `()` to create multiline code. It would be possible to
write out all of the above on one line, but this would come at the expense of
readability.
:::


This is really only useful when you have multiple geometries. As an example,
let's color-code the points by gender. To do so, we need to convert `gender` to
*categorical* data, which measures a qualitative category.

```{code-cell}
(ggplot(banknotes) +
    geom_point(aes(x = "death_year", y = "scaled_bill_value", color = "factor(gender)"))
)
```

Now let's add labels to each point. To do this, we need to add another
geometry:

```{code-cell}
(ggplot(banknotes,
    aes(x = "death_year", y = "scaled_bill_value", color = "factor(gender)",
        label = "name")) +
    geom_point() + 
    geom_text()
)
```

Where you put the aesthetics matters:

```{code-cell}
(ggplot(banknotes,
    aes(x = "death_year", y = "scaled_bill_value", label = "name")) + 
    geom_point() + 
    geom_text(aes(color = "factor(gender)"))
)
```

**Constant Aesthetics**

If you want to set an aesthetic to a constant value, rather than one that's
data dependent, do so in the geometry layer rather than the aesthetic layer.
For instance, suppose you want to use point shape rather than color to indicate
gender, and you want to make all of the points blue.

```{code-cell}
(ggplot(banknotes,
    aes(x = "death_year", y = "scaled_bill_value", shape = "factor(gender)")) +
    geom_point(color = "blue")
)
```

If you set an aesthetic to a constant value inside of the aesthetic layer, the
results you get might not be what you expect:

```{code-cell}
:tags: [raises-exception]
(ggplot(banknotes,
    aes(x = "death_year", y = "scaled_bill_value", shape = "factor(gender)",
        color = "blue")) +
    geom_point()
)
```


### Layer 4: Scales

The scales layer controls the title, axis labels, and axis scales of the plot.
Most of the functions in the scales layer are prefixed with `scale_`, but not
all of them.

The `labs` function is especially important, because it's used to set the title
and axis labels. All graphs need a title and axis labels.

```{code-cell}
(ggplot(banknotes,
    aes(x = "death_year", y = "scaled_bill_value", shape = "factor(gender)")) + 
    geom_point() +
    labs(x = "Death Year", y = "Scaled Bill Value",
         title = "Does death year affect bill value?", shape = "Gender")
)
```

### Saving Plots

If you assign a plot to a variable, you can use the `save` method or the
`ggsave` function to save that plot to a file:

```
plot = (
    ggplot(banknotes,
    aes(x = "death_year", y = "scaled_bill_value", shape = "factor(gender)")) +
    geom_point() +
    labs(x = "Death Year", y = "Scaled Bill Value", 
         title = "Does death year affect bill value?", shape = "Gender")
)

ggsave(plot, "myplot.pdf")
```

The file format is selected automatically based on the extension. Common
formats are PNG and PDF.


(example-bar-plot)=
### Example: Bar Plot

Now suppose you want to plot the number of banknotes with people from each
profession in the banknotes data set. A bar plot is an appropriate way to
represent this visually.

The geometry for a bar plot is `geom_bar`. Since bar plots are mainly used to
display frequencies, the `geom_bar` function automatically computes frequencies
when used in conjunction with the `factor()` syntax from above.

We can also use a fill color to further breakdown the bars by gender. Here's
the code to make the bar plot:

```{code-cell}
(ggplot(banknotes,
    aes(x = "factor(profession)", fill = "factor(gender)")) +
    geom_bar(position = "dodge")
)
```

The setting `position = "dodge"` instructs `geom_bar` to put the bars
side-by-side rather than stacking them.

In some cases, you may want to make a bar plot with frequencies you've already
computed. To prevent `geom_bar` from computing frequencies automatically, set
`stat = "identity"`.


(visualization-design)=
### Visualization Design

Designing high-quality visualizations goes beyond just mastering which Python
functions to call. You also need to think carefully about what kind of data you
have and what message you want to convey. This section provides a few
guidelines.

The first step in data visualization is choosing an appropriate kind of plot.
Here are some suggestions (not rules):

| Feature 1   | Feature 2   | Plot                          |
| :---------- | :---------- | :---------------------------- |
| categorical | categorical | bar, dot                      |
| categorical | categorical | bar, dot, mosaic              |
| numerical   |             | box, density, histogram       |
| numerical   | categorical | box, density, ridge           |
| numerical   | numerical   | line, scatter, smooth scatter |

If you want to add a:

* 3rd numerical feature, use it to change point/line size
* 3rd categorical feature, use it to change point/line style
* 4th categorical feature, use side-by-side plots

Once you've selected a plot, here are some rules you should almost always
follow:

* Always add a title and axis labels. These should be descriptive, not variable
  names!
* Specify units after the axis label if the axis has units. For instance,
  "Height (ft)"
* Don't forget that many people are colorblind! Also, plots are often printed
  in black and white. Use point and line styles to distinguish groups; color is
  optional
* Add a legend whenever you've used more than one point or line style
* Always write a few sentences explaining what the plot shows. Don't describe
  the plot, because the reader can just look at it. Instead, explain what they
  can learn from the plot and point out important details that may be
  overlooked
* For side-by-side plots, use the same axis scales for both plots so that
  comparing them is not deceptive

Visualization design is a deep topic, and whole books have been written about
it. One resource where you can learn more is DataLab's [Principle's of Data
Visualization Workshop Reader][rdr].

[rdr]: https://ucdavisdatalab.github.io/workshop_data_viz_principles/


(for-loops-list-comprehensions)=
For-Loops and List Comprehensions
---------------------------------


### For-Loops

{numref}`summarizing-columns` introduced column-wise operations in Pandas.
These operations are a convenient and efficient way to compute multiple results
at once, and with only a few lines of code.

Under the hood, Pandas has to **iterate** over each value in a cell to perform
functions like `mean` or `min`. We can do this too using a **for-loop**.
For-loops iterate over some object and compute something for each element. Each
one of these computations is one **iteration**. A for-loop begins with the
`for` keyword, followed by:

* A placeholder variable, which will be automatically signed to an element at
  the beginning of each iteration
* The `in` keyword
* An object with elements
* A colon `:`

Code in the body of the loop must be indented by 4 spaces.

For example, to print out all the column names in `banknotes.columns`, you can
write:

```{code-cell}
for column in banknotes.columns:
    print(column)
```

Within the indented part of a for-loop, you can compute values, check
conditions, etc.

```{code-cell}
:tags: [output_scroll]
for value in banknotes["bill_count"]:
    if value < 1:
        print(value)
```

Oftentimes you want to save the result of the code you perform within a
for-loop. The easiest way to do this is by creating an empty list and using
`append` to add values to it.

```{code-cell}
:tags: [output_scroll]
result = []
for value in banknotes["current_bill_value"]:
    if value % 25 == 0:
        result.append(value)

result
```


### List Comprehensions

A more succint way to perform certain `append` operations is with a **list
comprehension**. A List comprehension is very similar to a for-loop, but it
automatically creates a new list based on what your iterations do. This means
you do not need to create an empty list ahead of time.

Below, this comprehsion divides each value in the `current_bill_value` column
by 2.

```{code-cell}
:tags: [output_scroll]
[value / 2 for value in banknotes["current_bill_value"]]
```

Folding comparisons into list comprehensions works similar to subsetting in
Pandas:

```{code-cell}
[year for year in banknotes["death_year"] if year > 2000]
```

You can assign the results to a new variable and perform further computations
on them:

```{code-cell}
recent_deaths = [year for year in banknotes["death_year"] if year > 2000]
np.median(recent_deaths)
```


(aggregate-functions)=
Aggregate Functions
-------------------

