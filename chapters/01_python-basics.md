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

(getting-started)=
# Getting Started

:::{admonition} Learning Objectives
:class: note
After this lesson, you should be able to:

* Run code in a Python console (in JupyterLab)
* Create variables
* Call functions
* Save and run code in a Jupyter notebook
* Save, run, and import code in a module
* Get or set Python's working directory
* Identify the format of a data file
* Read a data set with Polars and inspect its contents
:::


## Why Python?

:::{admonition} Why should you use a programming language?
:class: note
Code you write is **reproducible**: you can share it with someone else, and if
they run it with the same inputs, they'll get the same results. By writing
code, you create an unambiguous record of every step taken in your analysis.
This is one of the major advantages of programming languages over
point-and-click software like *Tableau* or *Microsoft Excel*.

Another advantage of writing code is that it's often **reusable**. This means
you can:

* Automate repetitive tasks within an analysis
* Recycle code from one analysis into another
* Package useful code for distribution to your colleagues or the general
  public
:::

**[Python][]** is a general-purpose programming language used in wide range of
disciplines and industries. Its generality and popularity make knowing Python a
valuable skill. Compared to other programming languages, some of Python's
particular strengths are its:

* Easy-to-read syntax
* Interactive interpreter and debugger
* Idioms and culture that encourage explicit, straightforward code
* Over 635,000 community-developed **packages**: reusable bundles of code,
  often accompanied by documentation, examples, or data sets
* Flexible support for many different programming abstractions and paradigms

[Python]: https://www.python.org/

The main way you'll interact with Python is by writing Python code or
**expressions**. We'll explain more soon, but first we need to install some
packages that are critical for data science.

:::{note}
The term "Python" can mean the Python language (the code) or the Python
interpreter (the software which runs the code). Most of the time, the meaning
is clear from the context, but we'll be explicit in cases where the distinction
is important.
:::


(sec-packages)=
### Packages for Data Science

:::{important}
We recommend using [Pixi][] to install and manage Python and Python packages.

[Pixi]: https://pixi.sh/

Parts of this workshop require that you have Pixi installed on your computer
and are familiar with how to use it. If you need a refresher, see DataLab's
[Installing Software with Pixi][dl-pixi] workshop reader.

[dl-pixi]: https://ucdavisdatalab.github.io/workshop_installing_software/
:::

Python is general-purpose programming language, so data structures and
functions specialized for research computing are not built-in. Instead, the
community provides these through packages. Nevertheless, and to the community's
credit, Python is a leading language for research computing and data science.
This section introduces some of the fundamental packages for research
computing.

[NumPy][] provides $n$-dimensional arrays (such as vectors and matrices) and a
broad collection of mathematical functions. NumPy is the primary way to do
linear algebra efficiently in Python. Many other packages depend on or are
compatible with NumPy.

[NumPy]: https://numpy.org/

For data science, **data frames**, which represent tables of data, are another
fundamental data structure. Several competing packages provide data frames and
related functions:

* [Pandas][] is the oldest and most widely-used data frame package. It provides
  a broad set of features but also has many quirks. Pandas is generally less
  efficient than other packages in terms of compute time and memory usage.
* [Polars][] is specifically designed to be efficient, prevent bugs, and
  present a consistent programming interface. Polars is what we currently
  recommend for most people.
* [DuckDB][] treats data frames as tables in a database. This makes DuckDB
  extremely efficient and also means all operations on DuckDB data frames must
  be written in Structured Query Language (SQL) rather than Python. If you're
  comfortable with SQL or need to work with big data (hundreds of gigabytes or
  more), DuckDB is a good choice.
* [Ibis][] provides data frames that can use any of the other packages
  under-the-hood. Ibis uses DuckDB by default, so it has similar efficiency but
  a Python programming interface (SQL is also supported).

We'll use Polars, because it's substantially more efficient than Pandas and
provides early warnings for certain kinds of common mistakes.

[Pandas]: https://pandas.pydata.org/
[Polars]: https://pola.rs/
[DuckDB]: https://duckdb.org/
[Ibis]: https://ibis-project.org/

Other notable packages for research computing in Python:

* [Jupyter][] provides interactive notebooks and **IPython**, a more
  convenient command-line prompt for Python.
* [SciPy][] provides even more mathematical functions, to supplement NumPy.
* [Matplotlib][] provides a rich collection of visualization functions and is
  the foundation for many data visualization packages.
* [statsmodels][] provides functions to fit statistical models (where the focus
  is inference and interpretability).
* [scikit-learn][] provides functions to fit machine learning models (where the
  focus is prediction). The package's excellent documentation also provides a
  light but practical introduction to the models.

This is by no means an exhaustive list. You're likely to encounter many more
packages as you learn and use Python.

[Jupyter]: https://jupyter.org/
[SciPy]: https://scipy.org/
[Matplotlib]: https://matplotlib.org/
[statsmodels]: https://www.statsmodels.org/
[scikit-learn]: https://scikit-learn.org/

:::{important}
To follow along with this chapter and the next, you'll need an environment with
Python, Jupyter, NumPy, and Polars.

You can use Pixi to create a project directory called `python_basics` with a
suitable environment. Open a terminal (such as Terminal or Git Bash) and run:

```none
pixi init python_basics
cd python_basics
pixi add python jupyter numpy polars plotnine
```

After creating the environment, to launch JupyterLab in the enviroment, run:

```none
pixi run jupyter lab
```
:::


## The JupyterLab Interface

There are many different ways to edit and run Python code, but we'll use
JupyterLab. JupyterLab is an **integrated development environment** (IDE),
which means it's a comprehensive program for writing, editing, searching, and
running code. You can do all of these things without JupyterLab, but JupyterLab
makes the process easier.

The first time you open JupyterLab, you'll see a window that looks like this:

```{figure} ../img/jupyterlab_startup.png
---
name: fig-jl-startup
alt: A window with two sections. The section on the left lists files in a
  directory. The section on the right is titled "Launcher" and has buttons to
  launch notebooks and consoles for Python and other languages.
---

The JupyterLab startup screen.
```

Don't worry if the text in the panes isn't exactly the same on your computer;
it depends on your operating system and version of JupyterLab.

Start by opening up a Python **console**. In JupyterLab, look for the "Python
3" button in the "Console" section of the pane on the right. If there are
multiple Python 3 buttons, click on the one that mentions "IPython" or
"ipykernel":

```{figure} ../img/jupyterlab_console_button.png
---
name: fig-jl-startup-console-button
alt: A window with two sections. The section on the left lists files in a
  directory. The section on the right is titled "Launcher" and has buttons to
  launch notebooks and consoles for Python and other languages. The Python 3
  console button is highlighted.
---
The JupyterLab startup screen with the console button highlighted.
```

The console is a interactive, text-based interface to Python. If you enter a
Python expression in the console, Python will compute and display the result.
After you open the console, your window should look like this:

```{figure} ../img/jupyterlab_console.png
---
name: fig-jl-console
alt: A window with two sections. The section on the left lists files in a
  directory. The section on the right is a console with text that begins
  "Python 3.9.6" and goes on to provide further details about the versions of
  Python and IPython. At the bottom of the console there is an input box.
---
A Python console running in JupyterLab.
```

At the bottom of the console, the text box beginning with `[ ]:` is called the
**prompt**. The prompt is where you'll type Python expressions. Ask Python to
compute the sum $2 + 2$ by typing the code `2 + 2` in the prompt and then
pressing `Shift`-`Enter`. Your code and the result from Python should look like
this:

```{figure} ../img/jupyterlab_console_sum.png
---
name: fig-jl-console-sum
alt: A window with two sections. The section on the left lists files in a
  directory. The section on the right is a Python console. The console shows "2
  + 2" as input and "4" as output.
---
A Python console running in JupyterLab, showing the sum of two numbers.
```

The Python console displays your code and the result on separate lines. Both
begin with the tag `[1]` to indicate that they are the first expression and
result. Python will increment the tag each time you run an expression. The tag
numbers will restart from 1 each time you open a new Python console.

Now try typing the code `3 - 1` in the prompt and pressing `Shift`-`Enter`:

```{figure} ../img/jupyterlab_console_diff.png
---
name: fig-jl-console-diff
alt: A window with two sections. The section on the left lists files in a
  directory. The section on the right is a Python console. The console shows "3
  + 1" as input and "2" as output.
---
A Python console running in JupyterLab, showing the difference of two numbers.
```

The tag on the code and result is `[2]`, and once again the result is displayed
after the tag.


## Python Basics

Try out some other arithmetic in the Python console. Besides `+` for addition,
the other arithmetic operators are:

* `-` for subtraction
* `*` for multiplication
* `/` for division
* `%` for remainder division (modulo)
* `**` for exponentiation

You can combine these and use parentheses `( )` to make more complicated
expressions, just as you would when writing a mathematical expression. When
Python computes a result, it follows the standard order of operations:
parentheses, exponentiation, multiplication, division, addition, and finally
subtraction.

For example, to compute the area of a triangle, $\frac{1}{2}
(\textrm{base})(\textrm{height})$, with base 3 and height 4, you can write:

```{code-cell}
3 * 4 / 2
```

You can write Python expressions with any number of spaces (including none)
around the operators and Python will still compute the result.  Later on,
you'll learn about other kinds of expressions where the spacing does matter.

:::{tip}
Use spaces!

As with writing text, putting spaces in your code makes it easier for you and
others to read, so it's good to make it a habit. Put a single space on each
side of most operators, after commas, and after keywords.
:::


### Variables

Python and most other programming languages allow you to create named values
called **variables**. You can create a variable with the assignment operator
`=` by writing a name on the left-hand side and a value or expression on the
right hand side. For example, to save the estimated area of the triangle in a
variable called `area`, you can write:

```{code-cell}
area = 3 * 4 / 2
```

In Python, variable names can consist of any combination of letters and
underscores (`_`). Names can also include numbers, but can't start with a
number. Spaces, dots (`.`), and other symbols are not allowed in variable
names. So `geese`, `top50dogs` and `nine_lives` are valid variable names, but
`goose teeth`, `tropical.fish` and `9_lives` are not.

:::{note}
The official Python style guide, [PEP 8][pep8], recommends against using
capital letters in variable names even though Python allows it. Capital letters
are conventionally used for other kinds of names. Following the recommendation
will make your code easier for other Python programmers to understand.

[pep8]: https://pep8.org/
:::

The main reason to use variables is to temporarily save results from
expressions so that you can use them in other expressions. For instance, now
you can use the `area` variable anywhere you want the area of the triangle.

Notice that when you assign a result to a variable, Python doesn't
automatically display that result. If you want to see the result as well, you
have to enter the variable's name as a separate expression:

```{code-cell}
area
```

Another reason to use variables is to make an expression clearer and more
general. For instance, you might want to compute the area of several triangles
with different bases and heights. Then the expression `3 * 4 / 2` is too
specific. Instead, you can create variables `base` and `height`, then rewrite
the expression as `base * height / 2`. This makes the expression easier to
understand, because the reader does not have to intuit that `3` and `4` are the
base and height in the formula. Here's the new code to compute and display the
area of a triangle with base 3 and height 4:

```{code-cell}
base = 3
height = 4
area = base * height / 2
area
```

Now if you want to compute the area for a different triangle, all you have to
do is change `base` and `height` and run the code again (Python will not update
`area` until you do this). Writing code that's general enough to reuse across
multiple problems can be a big time-saver in the long run. Later on, you'll see
ways to make this code even easier to reuse.

:::{tip}
Try to choose descriptive variable names, so that you and your collaborators
can understand the meaning and purpose of each variable when reading the code.
:::


(strings)=
### Strings

Python treats anything inside single or double quotes as literal text rather
than as an expression to evaluate. In programming jargon, a piece of literal
text is called a **string**. You can use whichever kind of quotes you prefer,
but the quote at the beginning of the string must match the quote at the end. 

```{code-cell}
'Hi'
```

```{code-cell}
"Hello!"
```

Numbers and strings are not the same thing, so for example Python considers `1`
different from `"1"`. You can use the number `1` in mathematical expressions,
but not the string `"1"`.


(comparisons)=
### Comparisons

Besides arithmetic, you an also use Python to compare values. Programming tasks
often involve comparing values. Use **comparison operators** to do so:

| Operator | Meaning                  |
| :------: | :----------------------- |
| `<`      | less than                |
| `>`      | greater than             |
| `<=`     | less than or equal to    |
| `>=`     | greater than or equal to |
| `==`     | equal to                 |
| `!=`     | not equal to             |

Notice that the "equal to" operator is two equal signs. This is to distinguish
it from the assignment `=` operator.

Here are a few examples:

```{code-cell}
1.5 < 3
```

```{code-cell}
"a" > "b"
```

```{code-cell}
3 == 3.14
```

```{code-cell}
"hi" == "hi"
```

When you make a comparison, Python returns a **Boolean value**. There are only
two possible Boolean values: `True` and `False`. Booleans are commonly used for
expressions with yes-or-no responses.

Boolean values are values, so you can use them in other computations. For
example:

```{code-cell}
True
```

```{code-cell}
True == False
```

:::{tip}
Python supports chained comparisons. For example, if you want to test whether
`x` is between `1` and `2`, you can write:
```python
1 < x < 2
```

This is **syntactic sugar** (a shortcut) for a longer expression:
```python
1 < x and x < 2
```

You can use any of the comparison operators in chained comparisons, and Python
will implicitly combine each comparison with `and`.
:::


(calling-functions)=
### Calling Functions

Python can do a lot more than just arithmetic. Most of Python's features are
provided through **functions**, pieces of reusable code. You can think of a
function as a machine that takes some inputs and uses them to produce some
output. In programming jargon, the inputs to a function are called
**arguments**, the output is called the **return value**, and when you use a
function, you're **calling** the function.

To call a function, write its name followed by parentheses. Put any arguments
to the function inside the parentheses. For example, the function to round a
number to a specified decimal place is named `round`. So you can round the
number `8.153` to the nearest integer with this code:

```{code-cell}
round(8.153)
```

Many functions accept more than one argument. For instance, the `round`
function accepts two arguments: the number to round, and the number of decimal
places to keep. When you call a function with multiple arguments, separate the
arguments with commas. So to round `8.153` to 1 decimal place:

```{code-cell}
round(8.153, 1)
```

When you call a function, Python assigns the arguments to the function's
**parameters**. Parameters are special variables that represent the inputs to a
function and only exist while that function runs. For example, the `round`
function has parameters `number` and `ndigits`. The next section,
{ref}`getting-help`, explains how to look up the parameters for a function.

Some parameters have **default arguments**. A parameter is automatically
assigned its default argument whenever the parameter's argument is not
specified explicitly. As a result, assigning arguments to these parameters is
optional. For instance, the `ndigits` parameter of `round` has a default
argument (round to the nearest integer), so it is okay to call `round` without
setting `ndigits`, as in `round(8.153)`. In contrast, the `numbers` parameter
does not have a default argument. {ref}`getting-help` explains how to look up
the default arguments for a function.

Python normally assigns arguments to parameters based on their position. The
first argument is assigned to the function's first parameter, the second to the
second, and so on. So in the code above, `8.153` is assigned to `number` and
`1` is assigned to `ndigits`.

You can make Python assign arguments to parameters by name with `=`, overriding
their positions. So some other ways you can write the call above are:

```{code-cell}
round(8.153, ndigits = 1)
```

```{code-cell}
round(number = 8.153, ndigits = 1)
```

```{code-cell}
round(ndigits = 1, number = 8.153)
```

All of these are equivalent. When you write code, choose whatever seems the
clearest to you. Leaving parameter names out of calls saves typing, but
including some or all of them can make the code easier to understand.

Parameters are not regular variables, and only exist while their associated
function runs. You can't set them before a call, nor can you access them after
a call. So this code causes an error:

```{code-cell}
:tags: [raises-exception]
number = 4.755
round(ndigits = 2)
```

In the error message, Python says that you forgot to assign an argument to the
parameter `number`. You can keep the variable `number` and correct the call by
making `number` an argument (for the parameter `number`):

```{code-cell}
round(number, ndigits = 2)
```

:::{note}
It might be surprising that Python's `round` function rounds 4.755 to 4.75
instead of 4.76, but it's [not a bug][py-round]. Most rounding functions are
slightly inaccurate because of how computers represent decimal numbers.

[py-round]: https://docs.python.org/3/library/functions.html#round

NumPy provides its own rounding function, `np.round`, which uses a different,
faster rounding algorithm and may give different results.
:::

Or, written more explicitly:

```{code-cell}
round(number = number, ndigits = 2)
```

The point is that variables and parameters are distinct, even if they happen to
have the same name. The variable `number` is not the same thing as the
parameter `number`.


(objects-attributes)=
### Objects & Attributes

Python represents data as **objects**. Numbers, strings, data structures, and
functions are all examples of objects.

An **attribute** is an object attached to another object. An attribute usually
contains metadata about the object to which it is attached. You can access
attributes by typing a `.` after an object.

When an attribute is a function, it's called a **method**. For example, all
strings have a `capitalize` method.  Here's the code to capitalize a string:

```{code-cell}
"snakes everywhere!".capitalize()
```

The built-in `dir` function lists all of the attributes attached to
an object. Here are the attributes for a string:

```{code-cell}
dir("hi")
```

:::{caution}
Attributes that begin with two underscores `__` are used by Python internally
and are usually not intended to be accessed directly.
:::


(sec-comments)=
### Comments

Like most programming languages, Python provides a way to mark parts of your
code as **comments**: expressions to ignore rather than run. Use comments to
plan, explain, and document your code. You can also temporarily comment out
code to prevent it from running, which can be helpful for testing and
debugging.

In Python, comments begin with number sign `#` and extend to the end of the
line:

```{code-cell}
# This is a comment.
```

Python will ignore comments when you run your code.


<!--
:::{tip}
For formal documentation, Python uses [docstrings][].

[docstrings]: https://peps.python.org/pep-0257/
:::
-->


(getting-help)=
## Getting Help

Learning and using a language is hard, so it's important to know how to get
help. The first place to look for help is Python's built-in documentation. In
the console, you can access the help pages with the `help` function.

There are help pages for all of Python's built-in functions, usually with the
same name as the function itself. So the code to open the help page for the
`round` function is:

```{code-cell}
:tags: [output_scroll]
help(round)
```

For functions, help pages usually include a brief description and a list of
parameters and default arguments. For instance, the help page for `round` shows
that there are two parameters `number` and `ndigits`. It also says that
`ndigits=None`, meaning the default argument for `ndigits` is the special
`None` value (you'll learn more about `None` in {ref}`sec-special-values`).

There are also help pages for other topics, such as built-in operators and
modules (you'll learn about modules in {ref}`sec-saving-loading-code`). To look
up the help page for an operator, put the operator's name in single or double
quotes. For example, this code opens the help page for the arithmetic
operators:

```{code-cell}
:tags: [output_scroll]
help("+")
```

It's always okay to put quotes around the name of the page when you use `help`,
but they're only required if the name contains non-alphabetic characters. So
`help(abs)`, `help('abs')`, and `help("abs")` all open the documentation for
`abs`, the absolute value function.

You can also browse the Python documentation [online][pydocs]. This is a good
way to explore the many different functions and data structures built into
Python.

[pydocs]: https://docs.python.org/3/

:::{important}
If you do use the online documentation, make sure to use the documentation for
the same version of Python as the one you have. Python displays the version
each time you open a new console, and the online documentation shows the
version in the upper left corner.
:::

Sometimes you might not know the name of the help page you want to look up. In
that case it's best to use an online search engine. When you search for help
with Python online, include "Python" as a search term.


### When Something Goes Wrong

As a programmer, sooner or later you'll run some code and get an error message
or result you didn't expect. Don't panic! Even experienced programmers make
mistakes regularly, so learning how to diagnose and fix problems is vital.

Try going through these steps:

1. If Python printed a warning or error message, read it! If you're not sure
   what the message means, try searching for it online.
2. Check your code for typographical errors, including incorrect
   capitalization, whitespace, and missing or extra commas, quotes, and
   parentheses.
3. Test your code one line at a time, starting from the beginning. After each
   line that assigns a variable, check that the value of the variable is what
   you expect. Try to determine the exact line where the problem originates
   (which may differ from the line that emits an error!).

If none of these steps help, try asking online. [Stack Overflow][stacko] is a
popular question and answer website for programmers. Before posting, make sure
to read about [how to ask a good question][goodq].

[stacko]: https://stackoverflow.com/
[goodq]: https://stackoverflow.com/help/how-to-ask


(sec-saving-loading-code)=
## Saving & Loading Code

:::{tip}
When you start a new project, it's a good idea to create a specific directory
for all of the project's files. If you're using Python, you should also store
your Python code in that directory. As you work, periodically save your code.
:::

Most of the time, you won't just write code directly into the Python console.
Reproducibility and reusability are important benefits of Python over
point-and-click software, and in order to realize these, you have to save your
code to your computer's hard drive.

The most common way to save Python code is as a Python **module** (or script)
with the extension `.py` (see {ref}`reading-files` for more about extensions).
Editing a module is similar to editing any other text document. You can write,
delete, copy, cut, and paste code.

You can create a new Python module in JupyterLab with this menu option:

```
File -> New -> Python File
```

Every line in a Python module must be valid Python code. Anything else you want
to write in the module (notes, documentation, etc.) must be placed in a
comment.

Arrange your code in the order of the steps to solve the problem, even if you
write some parts before others. Comment out or delete any lines of code that
you try but ultimately decide you don't need. Make sure to save the file
periodically so that you don't lose your work. Following these guidelines will
help you stay organized and make it easier to share your code with others
later.


(sec-importing-modules)=
### Importing Modules

You can **import** a module with the `import` command. Python will run the
module's code so that you can use any functions or data structures it defines.
There are many modules built into Python that provide extra functionality. In
addition, every package consists of one or more modules.

:::{tip}
The best way to learn about the modules in a package is to read the package's
documentation.
:::

Most packages have a main module with the same name as the package. So the
NumPy package provides a module called `numpy`, and the Polars package provides
a module called `polars`. Make sure you have NumPy installed, then try loading
the `numpy` module:

```{code-cell}
import numpy
```

A handful of modules print out a message when loaded, but the vast majority do
not. Thus you can assume the `import` command was successful if nothing is
printed. If something goes wrong while loading a module, Python will print out
an error message explaining the problem.

Once a module is imported, you can access its functions by typing the name of
the module, a dot `.`, and then the name of the function. For instance, to use
the `round` function provided by NumPy:

```{code-cell}
numpy.round(3.3)
```

:::{important}
NumPy's `np.round` is an entirely different function than Python's built-in
`round` function, even though they do the same thing. NumPy's math functions
are generally faster, more precise, and more convenient than Python's built-in
math functions.
:::

Typing the full name of a module is inconvenient, so the `import` command
allows you to define an alias when you import a module. For popular packages,
there's usually a conventional alias for the main module. The conventional
alias for `numpy` is `np`. Using the conventional alias is a good habit,
because it makes it easier for other people to understand your code. Use the
`as` keyword to set an alias when you import a module:

```{code-cell}
import numpy as np
```

Now you can call NumPy functions by typing `np` instead of `numpy`:

```{code-cell}
np.round(3.4)
```

:::{note}
You can also use the `import` command to import code from one of your modules
into another. The module you want to import must be saved somewhere Python can
find it. One way to do this is to put the module you want to import in the
same directory as the module that will import it.
:::


(jupyter-notebooks)=
### Jupyter Notebooks

For data science tasks, it is also common to use a **Jupyter notebook** with
extension `.ipynb` to store code. In addition to Python code, Jupyter notebooks
have full support for formatted text, images, and code from other programming
languages such as Julia and R. The tradeoff is that Jupyter notebooks can only
be viewed in a web browser.

:::{note}
"Jupyter" is short for "Julia, Python, Text, and R."
:::

Jupyter notebooks are more convenient than Python scripts for interactive work
such as data analysis and learning or experimenting with the language. On the
other hand, Python scripts are more appropriate for long-running code that does
not require user interaction (such as web scrapers or scientific simulations)
and for developing packages and software. The remainder of this reader assumes
you're using a Jupyter notebook rather than the Python console or a Python
script, unless otherwise noted.

You can create a new Jupyter notebook in JupyterLab with this menu option:

```
File -> New -> Notebook
```

JupyterLab will prompt you to select a **kernel** for the notebook. The kernel
is the software used to run code in the notebook. For a notebook that will
contain Python code, you should choose a Python kernel.

After you select the kernel, you'll see a pane like this:

```{image} ../img/jupyterlab_notebook.png
:alt: A Jupyter notebook open in JupyterLab.
```

Jupyter notebooks are subdivided into **cells**. You can create as many cells
as you like, but each cell can only contain one kind of content, usually code
or text.

New cells are code cells by default. You can run a code cell by clicking on the
cell and pressing `Shift`-`Enter`. The notebook will display the result and
create a new empty code cell below the result:

```{image} ../img/jupyterlab_notebook_prod.png
:alt: A Jupyter notebook open in JupyterLab, showing an evaluated code cell.
```

You can convert a code cell to a text cell by clicking on the cell and
selecting the "Markdown" option from the cell type dropdown menu:

```{image} ../img/jupyterlab_notebook_cell_menu.png
:alt:
```

Markdown is a simple language you can use to add formatting to your text. For
example, surrounding a word with asterisks, as in `Let *sleeping* dogs lie`,
makes the surrounded word italic. You can find a short, interactive tutorial
about Markdown [here][mdtutorial]. If you "run" a text cell by pressing
`Shift`-`Enter`, the notebook will display the text with any formatting you
added.

[mdtutorial]: https://www.markdowntutorial.com/


## File Systems

This section is a review of how files on a computer work. You'll need to
understand this in order to read a data set from a file, and it's also
important for finding your saved notebooks and modules later.

Your computer's **file system** consists of **files** (chunks of data) and
**directories** (or "folders") to organize those files. For instance, the file
system on a computer shared by [Ada][ada] and [Charles][chuck], two pioneers of
computing, might look like this:

[ada]: https://en.wikipedia.org/wiki/Ada_Lovelace
[chuck]: https://en.wikipedia.org/wiki/Charles_Babbage

```{image} ../img/filesystem.png
:alt: An example of a file system.
:width: 50%
```

Don't worry if your file system looks a bit different from the picture.

File systems have a tree-like structure, with a top-level directory called the
**root directory**. On Ada and Charles' computer, the root is called `/`, which
is also what it's called on all macOS and Linux computers. On Windows, the root
is usually called `C:/`, but sometimes other letters, like `D:/`, are also used
depending on the computer's hardware.

A **path** is a list of directories that leads to a specific file or directory
on a file system (imagine giving directions to someone as they walk through the
file system). Use forward slashes `/` to separate the directories in a path,
rather than commas or spaces. The root directory includes a forward slash as
part of its name, and doesn't need an extra one.

For example, suppose Ada wants to write a path to the file `cats.csv`. She can
write the path like this:

```
/Users/ada/cats.csv
```

You can read this path from left-to-right as, "Starting from the root
directory, go to the `Users` directory, then from there go to the `ada`
directory, and from there go to the file `cats.csv`." Alternatively, you can
read the path from right-to-left as, "The file `cats.csv` inside of the `ada`
directory, which is inside of the `Users` directory, which is in the root
directory."

As another example, suppose Charles wants a path to the `Programs` directory.
He can write:

```
/Programs/
```

The `/` at the end of this path is reminder that `Programs` is a directory, not
a file. Charles could also write the path like this:

```
/Programs
```

This is still correct, but it's not as obvious that `Programs` is a directory.
In other words, when a path leads to a directory, including a **trailing
slash** is optional, but makes the meaning of the path clearer. Paths that lead
to files never have a trailing slash.

:::{warning}
On Windows computers, the components of a path are usually separated with
backslashes ```\``` instead of forward slashes `/`.

Regardless of the operating system, most Python functions accept and understand
paths separated with forward slashes as arguments. In other words, you can use
paths separated with forward slashes in your Python code, even on Windows. This
is especially convenient when you want to share code with other people, because
they might use a different operating system than you.

On Windows, most Python functions *return* paths separated by backslashes. Be
careful of this if your code gets a path by calling a function and then edits
it (for example, by calling `os.getcwd` and then splitting the path into its
components). The separator will be a backslash on Windows, but a forward slash
on all other operating systems. Python's built-in [pathlib][] module provides
helper functions to edit paths that account for differences between operating
systems.
:::

[pathlib]: https://docs.python.org/3/library/pathlib.html


(absolute-relative-paths)=
### Absolute & Relative Paths

A path that starts from the root directory, like all of the ones we've seen so
far, is called an **absolute path**. The path is "absolute" because it
unambiguously describes where a file or directory is located. The downside is
that absolute paths usually don't work well if you share your code.

For example, suppose Ada uses the path `/Programs/ada/cats.csv` to load the
`cats.csv` file in her code. If she shares her code with another pioneer of
computing, say [Gladys][gladys], who also has a copy of `cats.csv`, it might
not work. Even though Gladys has the file, she might not have it in a directory
called `ada`, and might not even have a directory called `ada` on her computer.
Because Ada used an absolute path, her code works on her own computer, but
isn't portable to others.

[gladys]: https://en.wikipedia.org/wiki/Gladys_West

On the other hand, a **relative path** is one that doesn't start from the root
directory. The path is "relative" to an unspecified starting point, which
usually depends on the context.

For instance, suppose Ada's code is saved in the file `analysis.ipynb`, which
is in the same directory as `cats.csv` on her computer. Then instead of an
absolute path, she can use a relative path in her code:

```
cats.csv
```

The context is the location of `analysis.ipynb`, the file that contains the
code. In other words, the starting point on Ada's computer is the `ada`
directory. On other computers, the starting point will be different, depending
on where the code is stored.

Now suppose Ada sends her corrected code in `analysis.ipynb` to Gladys, and
tells Gladys to put it in the same directory as `cats.csv`. Since the path
`cats.csv` is relative, the code will still work on Gladys' computer, as long
as the two files are in the same directory. The name of that directory and its
location in the file system don't matter, and don't have to be the same as on
Ada's computer. Gladys can put the files in a directory
`/Users/gladys/from_ada/` and the path (and code) will still work.

Relative paths can include directories. For example, suppose that Charles wants
to write a relative path from the `Users` directory to a cool selfie he took.
Then he can write:

```
charles/cool_hair_selfie.jpg
```

You can read this path as, "Starting from wherever you are, go to the `charles`
directory, and from there go to the `cool_hair_selfie.jpg` file." In other
words, the relative path depends on the context of the code or program that
uses it.

:::{tip}
When you use paths in code, they should almost always be relative paths. This
ensures that the code is portable to other computers, which is an important
aspect of reproducibility. Another benefit is that relative paths tend to be
shorter, making your code easier to read (and write).
:::

When you write paths, there are three shortcuts you can use. These are most
useful in relative paths, but also work in absolute paths:

* `.` means the current directory.
* `..` means the directory above the current directory.
* `~` means the **home directory**. Each user has their own home directory,
  whose location depends on the operating system and their username. Home
  directories are typically found inside `C:/Users/` on Windows, `/Users/` on
  macOS, and `/home/` on Linux.

As an example, suppose Ada wants to write a (relative) path from the `ada`
directory to Charles' cool selfie. Using these shortcuts, she can write:

```
../charles/cool_hair_selfie.jpg
```

Read this as, "Starting from wherever you are, go up one directory, then go to
the `charles` directory, and then go to the `cool_hair_selfie.jpg` file." Since
`/Users/ada` is Ada's home directory, she could also write the path as:

```
~/../charles/cool_hair_selfie.jpg
```

This path has the same effect, but the meaning is slightly different. You can
read it as "Starting from your home directory, go up one directory, then go to
the `charles` directory, and then go to the `cool_hair_selfie.jpg` file."

The `..` and `~` shortcut are frequently used and worth remembering. The `.`
shortcut is included here in case you see it in someone else's code. Since it
means the current directory, a path like `./cats.csv` is identical to
`cats.csv`, and the latter is preferable for being simpler. There are a few
specific situations where `.` is necessary, but they fall outside the scope of
this text.


### The Working Directory

```{code-cell}
:tags: [remove-cell]
# Save working dir to reset at the end of this section.
import os

_wd = os.getcwd()
```

{ref}`absolute-relative-paths` explained that relative paths have a starting
point that depends on the context where the path is used. The **working
directory** is the starting point Python uses for relative paths. Think of the
working directory as the directory Python is currently "at" or watching.

Python's built-in `os` module provides functions to manipulate the working
directory. The function `os.getcwd` returns the absolute path for the current
working directory, as a string. It doesn't require any arguments:

```{code-cell}
import os

os.getcwd()
```

On your computer, the output from `os.getcwd` will likely be different. This is
a very useful function for getting your bearings when you write relative paths.
If you write a relative path and it doesn't work as expected, the first thing
to do is check the working directory.

The related `os.chdir` function changes the working directory. It takes one
argument: a path to the new working directory. Here's an example:

```{code-cell}
os.chdir("..")

# Now check the working directory.
os.getcwd()
```

:::{warning}
Generally, you should avoid using calls to `os.chdir` in your Jupyter notebooks
and Python scripts. Calling `os.chdir` makes your code more difficult to
understand, and can always be avoided by using appropriate relative paths. If
you call `os.chdir` with an absolute path, it also makes your code less
portable to other computers. It's fine to use `os.chdir` interactively (in the
Python console), but avoid making your saved code dependent on it.
:::
 
Another function that's useful for dealing with the working directory and file
system is `os.listdir`. The `os.listdir` function returns the names of all of
the files and directories inside of a directory. It accepts a path to a
directory as an argument, or assumes the working directory if you don't pass a
path. For instance:

```{code-cell}
# List files and directories in /home/.
os.listdir("/home/")

# List files and directories in the working directory.
os.listdir()
```

As usual, since you have a different computer, you're likely to see different
output if you run this code. If you call `os.listdir` with an invalid path or
an empty directory, Python raises a `FileNotFoundError`:

```{code-cell}
:tags: [raises-exception]
os.listdir("/this/path/is/fake/")
```

```{code-cell}
:tags: [remove-cell]
# Reset the working dir.
os.chdir(_wd)
```


(reading-files)=
## Reading Files

The first step in most data analyses is loading a data set. The Polars package
provides functions to read data sets saved in a variety of file formats. In
order to know which function to use, you must first identify the file format.

Most of the time, you can guess the format of a file by looking at its
**extension**, the characters (usually three) after the last dot `.` in the
filename. For example, the extension `.jpg` or `.jpeg` indicates a [JPEG image
file][jpg]. Some operating systems hide extensions by default, but you can find
instructions to change this setting online by searching for "show file
extensions" and your operating system's name. The extension is just part of the
file's name, so it should be taken as a hint about the file's format rather
than a guarantee.

[jpg]: https://en.wikipedia.org/wiki/JPEG

The table below shows several formats that are frequently used to distribute
data. Polars provides reader functions for many of these, but some can only be
read with help from other packages or Python's built-in modules.

| Name                        | Extension            | Function or Package      | Tabular?  | Text?
| :-------------------------- | :--------------      | :------------------      | :-------- | :----
| Comma-separated Values      | `.csv`               | `read_csv`               | Yes       | Yes
| Tab-separated Values        | `.tsv`               | `read_table`             | Yes       | Yes
| Fixed-width File            | `.fwf`               | See [this issue][pl-fwf] | Yes       | Yes
| Microsoft Excel             | `.xls`, `.xlsx`      | `read_excel`             | Yes       | No
| [Apache Parquet][arrow]     | `.parquet`           | `read_parquet`           | Yes       | No
| [Apache Arrow][arrow]       | `.arrow`, `.feather` | `read_ipc`               | Yes       | No
| Extensible Markup Language  | `.xml`, `.html`      | [parsel][] package       | No        | Yes
| JavaScript Object Notation  | `.json`              | `json` module            | No        | Yes
| Arbitrary File              |                      | `open` (built-in)        |           |

[pl-fwf]: https://github.com/pola-rs/polars/issues/3151
[parquet]: https://parquet.apache.org/
[arrow]: https://arrow.apache.org/
[parsel]: https://parsel.readthedocs.io/en/latest/

A **tabular** data set is one that's structured as a table, with rows and
columns. We'll focus on tabular data sets for most of this reader, since
they're easier to get started with. Here's an example of a tabular data set:

| Fruit  | Quantity | Price
| :----  | -------: | ----:
| apple  | 32       | 1.49
| banana | 541      | 0.79
| pear   | 10       | 1.99

A **text** file is one that contains human-readable lines of text. You can
check this by opening the file with a text editor such as Microsoft Notepad or
macOS TextEdit. Many file formats use text in order to make the format easier
to work with.

For instance, a **comma-separated values** (CSV) file records a tabular data
using one line per row, with commas separating columns. If you store the table
above in a CSV file and open the file in a text editor, here's what you'll see:

```
Fruit,Quantity,Price
apple,32,1.49
banana,541,0.79
pear,10,1.99
```

A **binary** file is one that's not human-readable. You can't just read off the
data if you open a binary file in a text editor, but they have a number of
other advantages. Compared to text files, binary files are often faster to read
and take up less storage space (bytes).


(sec-hello-data)=
### Hello, Data!

The California least tern is a endangered subspecies of seabird that nests
along the coast of California and Mexico. The California Department of Fish and
Wildlife (CDFW) monitors least tern nesting sites across the state to estimate
breeding pairs, fledglings, and predator activity in each annual breeding
season.

```{figure} ../img/ca_least_tern_usfws_pacificsw.jpg
---
height: 25em
alt: "A gray bird with a white belly, black head, and orange beak sitting on a
clutch of eggs."
---
A California least tern. Original photo by [Mark Pavelka, U.S. Fish & Wildlife
Service][pavelka] ([CC BY 2.0][]).
```

[pavelka]: https://www.flickr.com/photos/usfws_pacificsw/5704890596/
[CC BY 2.0]: https://creativecommons.org/licenses/by/2.0/

The CDFW publishes most of the data it collects to the [California Open Data
portal][data.ca.gov]. The examples in this and subsequent chapters use a
cleaned 2000-2023 version of the California least tern data.

[data.ca.gov]: https://data.ca.gov/

:::{important}
[Click here][ca-least-tern] to download the 2000-2023 California least tern
data set.

[ca-least-tern]: https://ucdavis.box.com/s/m2w5l2ebp2rey2do5lnn38y1e3u31pin

If you haven't already, we recommend you create a directory for this workshop.
In your workshop directory, create a `data/` subdirectory. Download and save
the California least tern data set in the `data/` subdirectory.
:::

:::{admonition} Documentation for 2000-2023 California Least Tern Data Set
:class: note, dropdown

Each row in the data set contains measurements from one year-site combination.

| Column                | Description
| --------------------: | :----------
| `year`                | Year of the breeding season
| `site_name`           | Site name
| `site_name_2013_2018` | Site name from 2013-2018
| `site_name_1988_2001` | Site name from 1988-2001
| `site_abbr`           | Abbreviated site name
| `region_3`            | Region of state: S.F. Bay, Central, or Southern (includes Ventura)
| `region_4`            | Region of state: S.F. Bay, Central, Ventura, or Southern
| `event`               | Climate events
| `bp_min`              | Reported minimum breeding pairs
| `bp_max`              | Reported maximum breeding pairs
| `fl_min`              | Reported minimum fledges
| `fl_max`              | Reported maximum fledges
| `total_nests`         | Total reported nests (maximum if a range was reported)
| `nonpred_eggs`        | Total non-predator-related mortalities of eggs
| `nonpred_chicks`      | Total non-predator-related mortalities of chicks
| `nonpred_fl`          | Total non-predator-related mortalities of fledges
| `nonpred_ad`          | Total non-predator-related mortalities of adults
| `pred_control`        | Site predator control (yes/no)
| `pred_eggs`           | Total predator-related mortalities of eggs
| `pred_chicks`         | Total predator-related mortalities of chicks
| `pred_fl`             | Total predator-related mortalities of fledges
| `pred_ad`             | Total predator-related mortalities of adults
| `pred_pefa`           | Predation by peregrine falcons (yes/no)
| `pred_coy_fox`        | Predation by coyotes or foxes (yes/no)
| `pred_meso`           | Predation by other mesocarnivores: dogs, cats, skunks, opossums, raccoons, weasels, etc. (yes/no)
| `pred_owlspp`         | Predation by owls (yes/no)
| `pred_corvid`         | Predation by corvids: ravens or crows (yes/no)
| `pred_other_raptor`   | Predation by raptors other than peregrine falcons and owls (yes/no)
| `pred_other_avian`    | Predation by birds other than raptors and corvids (yes/no)
| `pred_misc`           | Predation by other animals (yes/no)
| `total_pefa`          | Total mortalities due to peregrine falcons
| `total_coy_fox`       | Total mortalities due to coyotes and foxes
| `total_meso`          | Total mortalities due to other mesocarnivores
| `total_owlspp`        | Total mortalities due to owls
| `total_corvid`        | Total mortalities due to ravens and crows
| `total_other_raptor`  | Total mortalities due to other raptors
| `total_other_avian`   | Total mortalities due to other birds
| `total_misc`          | Total mortalities due to other animals
| `first_observed`      | Date CA least terns first observed at site
| `last_observed`       | Date CA least terns last observed at site
| `first_nest`          | Date first egg observed at site
| `first_chick`         | Date first chick observed at site
| `first_fledge`        | Date first fledge observed at site

The messy source data set (with more years and more columns) is available
[here][ca-least-tern-source].

[ca-least-tern-source]: https://data.ca.gov/dataset/california-least-tern-monitoring-sites-generalized-cdfw-ds3146
:::

Let's use Polars to read the California least tern data set. The default file
name is `2000-2023_ca_least_tern.csv`, which suggests it's a CSV file. The
Polars function to read a CSV file is `read_csv`. The function's first and only
required argument is the path to the CSV file. In the following code, the path
to the California least tern data set is `data/2000-2023_ca_least_tern.csv`,
but it might be different for you, depending on Python's working directory and
where you saved the file. We'll save the result from the `read_csv` function in
a variable called `terns`. We can use this variable to access the data in
subsequent code.

```{code-cell}
import polars as pl

terns = pl.read_csv("data/2000-2023_ca_least_tern.csv")
```

:::{note}
The variable name `terns` is arbitrary; you can choose something different if
you want. However, in general, it's a good habit to choose variable names that
describe the contents of the variable somehow.
:::

If you tried running the line of code above and got an error message, pay
attention to what the error message says, and remember the strategies to get
help in {ref}`getting-help`. The most common mistake when reading a file is
incorrectly specifying the path, so first check that you got the path right.

If the code ran without errors, it's a good idea to check that the data set
looks like what the documentation describes. When working with a new data set,
it usually isn't a good idea to print the whole thing (at least until you know
how big it is). Large data sets can take a long time to print, and the output
can be difficult to read.

Instead, use the `.head` method to print only the beginning, or head, of the
data set:

```{code-cell}
terns.head()
```

If you run this code and see a similar table, then congratulations, you've read
your first data set into Python! ✨

{ref}`sec-packages` explained that we use data frames to represent tabular
data. Typically, each row in a data frame corresponds to a single subject and
is called an **observation**. Each column corresponds to a measurement of the
subject and is called a **feature** or **covariate**.

:::{note}
Sometimes people also refer to columns as “variables," but we'll try to avoid
this, because in programming contexts a variable is a name for a value (which
might not be a column).
:::

You can check to make sure Polars has indeed created a data frame with the
`type` function (more about this function in {ref}`data-types`):

```{code-cell}
type(terns)
```

Everything looks good here.


(inspecting-dataframe)=
## Inspecting a Data Frame

Similar to how the `.head` method shows the first few rows of a data frame, the
`.tail` method shows the last few:

```{code-cell}
terns.tail()
```

Both `.head` and `.tail` accept an optional argument that specifies the number
of rows to print to screen:

```{code-cell}
:tags: [output_scroll]
terns.head(10)
```

:::{tip}
For data frames with many rows or columns, Polars will usually replace some
rows or columns with `...` when printing to the screen.

You can control how many rows and columns are printed with the
`pl.Config.set_tbl_rows` and `pl.Config.set_tbl_cols` functions, respectively.
You can later restore the default settings with the
`pl.Config.restore_defaults` function.
:::

One way to get a quick idea of what your data looks like without having to skim
through all the columns and rows is by inspecting its **shape**. This is the
number of rows and columns in a data frame, and you can access this information
with the `.shape` attribute:

```{code-cell}
terns.shape
```

:::{note}
The `.shape` attribute uses the same dot (`.`) syntax as the `.head` and
`.tail` methods. The key difference is that because `.shape` is not a method,
there are no parentheses `()` at the end. Parentheses are necessary when you
want to call a method, but not when you want just want to access the value of
attribute.

How can you tell whether or not an attribute is a method? If its value must be
computed (for example, by taking a subset), it's probably a method. If its
value is an inherent property of the object, it's probably not. You can always
use `help` or `type` to check if you're not sure.
:::

Polars stores the data frame's column names in the `.columns` attribute:

```{code-cell}
:tags: [output_scroll]
terns.columns
```

(sec-summarizing-data)=
### Summarizing Data

The `.glimpse` method provides a structural summary of a data frame. The method
lists the data frame's shape and column names, as well as the type of data in
each column and a few example values. Try calling `.glimpse` on the `terns`
data frame:

```{code-cell}
terns.glimpse()
```

The next chapter explains data types in more detail. For now, just take note
that there are multiple types (`i64`, `str`, and `f64` in the `terns` data
frame).

In contrast to the `.glimpse` method, the `.describe` method provides a
statistical summary of a data frame:

```{code-cell}
terns.describe()
```

(sec-summarizing-columns)=
### Summarizing Columns

You can select individual columns with **bracket notation**. Put the name of
the column in quotes and place that inside of square brackets `[]`. For
example, to select the `total_nests` column:

```{code-cell}
terns["total_nests"]
```

Polars provides a variety of methods to compute on columns. For instance, you
can use the `.mean` method to compute the mean:

```{code-cell}
terns["total_nests"].mean()
```

Similarly, you can use the `.min` method to compute the smallest value in a
column:

```{code-cell}
terns["total_nests"].min()
```

<!--
Functions from other packages will usually work with Polars, but might be less
efficient. Here's how to find smallest value in the column with the `np.min`
function from NumPy:

```{code-cell}
np.min(terns["total_nests"])
```
-->

For columns of categories, statistics like means and minimums aren't defined.
Instead, it's often informative to count the number of observations of each
category. You can do this with the `.value_counts` method:

```{code-cell}
terns["year"].value_counts()
```

We'll explain more ways to work with data frames and columns in the next
chapter.


## Exercises

### Exercise

In a string, an **escape sequence** or **escape code** consists of a backslash
`\` followed by one or more characters. Escape characters make it possible to:

* Write quotes or backslashes in a string
* Use spaces in file paths
* Write characters that don't appear on your keyboard (for example characters
  in a different script system)

For example, the escape sequence `\n` means "newline character." A full list of
these sequences is available at [W3Schools][w3].

[w3]: https://www.w3schools.com/python/gloss_python_escape_characters.asp

1. Assign a string that contains a newline to the variable `newline`. Then
   display `newline` via the Python console.
2. The `print` function renders output in a properly formatted manner. Use this
   function to print `newline`.
3. How does the output between these two displays differ? Why do you think this
   is?

### Exercise

1. Chose a directory on your computer that you're familiar with, such as your
   current working directory. Determine the path to the directory, then use
   `os.listdir` to display its contents. Do the files displayed match what you
   see in your systems file browser?
2. Send a path to `os.path.exists` and inspect its output. What does this
   function do? See if you can change its output. If you can, why did it
   change?

### Exercise

1. Open the help file for the Polars `read_csv` function. The `separator`
   parameter controls which characters Polars looks for when determining the
   columns in a file. What is the default character?
2. A TSV file is similar to CSV files, except it uses tabs to delimit columns.
   Tabs are represented by escape sequences in Python. Find the right sequence
   and explain how you would load a TSV file with `read_csv`.
