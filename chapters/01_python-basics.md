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

Getting Started
===============

**[Python][]** is a popular general-purpose programming language. Python is also a
leading language for scientific computing, due to the introduction of the
**[SciPy ecosystem][SciPy]**, a collection of scientific computing software for
Python, in 2001.

[Python]: https://www.python.org/
[SciPy]: https://scipy.org/

The main way you'll interact with Python is by writing Python code or
**expressions**. Most people use "Python" as a blanket term to refer to both
the Python language and the Python software (which runs code written in the
language). Usually, the distinction doesn't matter, but it will be pointed out
if it does.

Code you write is **reproducible**: you can share it with someone else, and if
they run it with the same inputs, they'll get the same results. By writing
code, you create an unambiguous record of every step taken in your analysis.
This it one of the major advantages of Python and other programming languages
over point-and-click software like *Tableau* or *Microsoft Excel*. 

Another advantage of writing code is that it's often **reusable**. This means
you can:

* Automate repetitive tasks within an analysis
* Recycle code from one analysis into another
* Package useful code for distribution to your colleagues or the general
  public

At the time of writing, there were over 324,000 user-contributed packages
available for Python, spanning a broad range of disciplines.

Python is one of many programming languages used in data science. Compared to
other programming languages, Python's particular strengths are its:

* Interactivity
* Use in a wide variety of disciplines, not just data science
* Broad base of user-contributed packages
* Syntax which resembles pseudocode and encourages good habits



Prerequisites
-------------

Rather than installing Python directly, install **[Anaconda][]**, a collection
of free and open-source data science software. Anaconda includes three things
you'll need to follow along with this reader:

* Python 3
* SciPy ecosystem packages
* **[Conda][]**, a system for installing and managing software

You'll learn more about these later on. Anaconda also includes other popular
software, such as the R programming language. Install Anaconda by following
[this guide][anaconda-guide].

[Anaconda]: https://www.anaconda.com/
[Conda]: https://docs.conda.io/

[anaconda-guide]: https://ucdavisdatalab.github.io/install_guides/python-and-python-tools.html

In addition, you need to install **JupyterLab**. JupyterLab is an **integrated
development environment** (IDE), which means it's a comprehensive program for
writing, editing, searching, and running code. You can do all of these things
without JupyterLab, but JupyterLab makes the process easier. Install JupyterLab
by following [this guide][jupyterlab-guide].

[jupyterlab-guide]: https://ucdavisdatalab.github.io/install_guides/python-and-python-tools.html#jupyterlab

<!--
In addition to Anaconda, you'll need Visual Studio Code (VSCode). VSCode is an
*integrated development environment* (IDE), which means it's a comprehensive
program for writing, editing, searching, and running code. You can do all of
these things without VSCode, but VSCode makes the process easier. VSCode
supports a variety of programming languages, including Python, R, Java, C, and
C++. You can download Visual Studio Code for free [here][vscode], and can find
an install guide [here][vscode-guide].
[vscode]: https://code.visualstudio.com/Download
[vscode-guide]: TODO
-->


The JupyterLab Interface
------------------------

The first time you open JupyterLab, you'll see a window that looks like this:

<!-- TODO: -->

Don't worry if the text in the panes isn't exactly the same on your computer;
it depends on your operating system and version of JupyterLab.

You can open up a Python *console* by clicking on the "Python 3" button on the
right. If you have multiple Python 3 buttons, click on the one that mentions
"IPython":

<!-- TODO: -->

After you open the console, your window should look like this:

<!-- TODO: -->

Let's start by using Python to do some arithmetic. In the console, you'll see
a text box that begins with `[ ]:`, called the *prompt*. You can make Python
compute the sum $2 + 2$ by typing the code `2 + 2` in the prompt and then
pressing `Shift`-`Enter`. Your code and the result from Python should look like
this:

<!-- TODO: -->

Python always puts the result on a separate line (or lines) from your code.
Your code and the result both begin with the tag `[1]` to indicate that they
are the first code and result. Python will increment the tag each time you run
an expression. The result of the sum, `4`, is displayed after the tag. In this
reader, results from Python will usually be prefixed with `##` to indicate that
they aren't code.

Now try typing the code `3 - 1` in the prompt and
pressing `Shift`-`Enter`:

<!-- TODO: -->

The tag on the code and result is `[2]`, and once again the result is displayed
after the tag.

Try out some other arithmetic in the Python console. Besides `+` for addition,
the other arithmetic operators are:

* `-` for subtraction
* `*` for multiplication
* `/` for division
* `%` for remainder division (modulo)
* `**` for exponentiation

You can combine these and use parentheses to make more complicated expressions,
just as you would when writing a mathematical expression. When Python computes
a result, it follows the standard order of operations: parentheses,
exponentiation, multiplication, division, addition, and finally subtraction.

For example, to estimate the area of a circle with radius 3, you can write:

```{code-cell}
3.14 * 3**2
```

You can write Python expressions with any number of spaces (including none)
around the operators and Python will still compute the result. Nevertheless,
putting spaces in your code makes it easier for you and others to read, so it's
good to make it a habit. Put spaces around most operators, after commas, and
after keywords. Later on, you'll learn about other kinds of expressions where
the spacing does matter.


### Variables

Python and most other programming languages allow you to create named values
called **variables**.  The main reason to use variables is to temporarily save
results from expressions so that you can use them in other expressions.

You can create a variable with the assignment operator `=`. For example, to
save the estimated area of the circle in a variable called `area`, you can
write:

```{code-cell}
area = 3.14 * 3**2
```

In Python, variable names can contain any combination of letters, numbers, and
underscores `_`, but must always start with a letter. Spaces, dots, and other
symbols are not allowed in variable names.

Now you can use the `area` variable anywhere you want the computed area. Notice
that when you assign a result to a variable, Python doesn't automatically
display that result. If you want to see the result as well, you have to enter
the variable's name as a separate expression:

```{code-cell}
area
```

Another reason to use variables is to make an expression more general. For
instance, you might want to compute the area of several circles with different
radii. Then the expression `3.14 * 3**2` is too specific. You can rewrite it as
`3.14 * r**2`, and then assign a value to the variable `r` just before you
compute the area. Here's the code to compute and display the area of a circle
with radius 1 this way:

```{code-cell}
r = 1
area = 3.14 * r**2
area
```

Now if you want to compute the area for a different radius, all you have to do
is change `r` and run the code again (Python will not change `area` until you
do this). Writing code that's general enough to reuse across multiple problems
can be a big time-saver in the long run. Later on, you'll see ways to make this
code even easier to reuse.


### Calling Functions

Python can do a lot more than just arithmetic. Most of Python's features are
provided through **functions**, pieces of reusable code. You can think of a
function as a machine that takes some inputs and uses them to produce some
output. In programming jargon, the inputs to a function are called
**arguments**, the output is called the **return value**, and using a function
is called **calling** the function.

To call a function, write its name followed by parentheses. Put any arguments
to the function inside the parentheses. For example, the sine function is named
`sin` (there are also `cos` and `tan`). So you can compute the sine of $\pi /
4$ with this code:

```
sin(pi / 4)
```

There are many functions that accept more than one argument. For instance, the
`sum` function accepts any number of arguments and adds them all together. When
you call a function with multiple arguments, separate the arguments with
commas. So another way to compute $2 + 2$ in R is:

```
sum(2, 2)
```

When you call a function, Python assigns each argument to a **parameter**.
Parameters are special variables that represent the inputs to a function and
only exist while that function runs. For example, the `log` function, which
computes a logarithm, has parameters `x` and `base` for the operand and base of
the logaritm, respectively. The next section, Section \@ref(getting-help),
explains how to look up the parameters for a function.

By default, Python assigns arguments to parameters based on their order. The
first argument is assigned to the function's first parameter, the second to the
second, and so on. So you can compute the logarithm of 64, base 2, with this
code:

```
log(64, 2)
```

The argument 64 is assigned to the parameter `x`, and the argument 2 is
assigned to the parameter `base`. You can also assign arguments to parameters
by name with `=`, overriding their positions. So some other ways you can write
the call above are:

```
log(64, base = 2)
log(x = 64, base = 2)
log(base = 2, x = 64)
log(base = 2, 64)
```

All of these are equivalent. When you write code, choose whatever seems the
clearest to you. Leaving parameter names out of calls saves typing, but
including some or all of them can make the code easier to understand.

Parameters are not regular variables, and only exist while their associated
function runs. You can't set them before a call, nor can you access them after
a call. So this code causes an error:

```
x = 64
log(base = 2)
```

In the error message, Python says that you forgot to assign an argument to the
parameter `x`. You can keep the variable `x` and correct the call by making `x`
an argument (for the parameter `x`):

```
log(x, base = 2)
```

Or, written more explicitly:

```
log(x = x, base = 2)
```

In summary, variables and parameters are distinct, even if they happen to have
the same name. The variable `x` is not the same thing as the parameter `x`.



Getting Help
------------

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


Modules & Packages
------------------


A **package** is a reusable bundle of code. Packages usually include
documentation, and can also contain examples and data sets. Most packages are
developed by members of the Python community, so quality varies. There are also
many packages that are built into Python, to provide extra features.

In Python, packages are further subdivided into **modules**, collections of
related functions and data structures. The best way to learn about the modules
provided by a package is to read the package's documentation.

Most packages have a main module with the same name as the package. So NumPy
provides a module called `numpy`, and Pandas provides a module called `pandas`.
You can use the `import` command to load a module from an installed package.
Anaconda installs NumPy by default, so try loading the `numpy` module:

```{code-cell}
import numpy
```

A handful of modules print out a message when loaded, but the vast majority do
not. Thus you can assume the `import` command was successful if nothing is
printed. If something goes wrong while loading a module, Python will print out
an error message explaining the problem.

Once a module is loaded, you can access its functions by typing the name of the
module, a dot, and then the name of the function. For instance, to use the
`round` function provided by NumPy:

```{code-cell}
numpy.round(3.3)
```

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



The SciPy Ecosystem
-------------------

The SciPy ecosystem is a collection of scientific computing software for Python
introduced in 2001. SciPy is divided into several different Python packages.

Some of the most important packages in the SciPy ecosystem are:

* **NumPy**, which provides an n-dimensional array data structure and a variety
  of math functions
* **SciPy**, which provides additional math functions
* **Pandas**, which provides data frames
* **IPython**, which makes it possible to run Python code in Jupyter
* **Matplotlib**, which provides data visualization functions

You'll learn much more about NumPy, SciPy, and Pandas as you go through this
reader. By using JupyterLab, you've already used IPython. You'll use Matplotlib
indirectly later on, when you learn about visualization.



File Systems
------------

_TODO: Remake image to be Python appropriate or language agnostic._

Most of the time, you won't just write code directly into the Python console.
Reproducibility and reusability are important benefits of Python over
point-and-click software, and in order to realize these, you have to save your
code to your computer's hard drive. Let's start by reviewing how files on a
computer work. You'll need to understand that before you can save your code,
and it will also be important later on for loading data sets.

Your computer's _file system_ is a collection of _files_ (chunks of data) and
_directories_ (or "folders") that organize those files. For instance, the file
system on a computer shared by [Ada][ada] and [Charles][chuck], two pioneers of
computing, might look like this:

[ada]: https://en.wikipedia.org/wiki/Ada_Lovelace
[chuck]: https://en.wikipedia.org/wiki/Charles_Babbage

<img src="../img/filesystem.png" width="50%">

Don't worry if your file system looks a bit different from the picture.

File systems have a tree-like structure, with a top-level directory called the
_root directory_. On Ada and Charles' computer, the root is called `/`, which
is also what it's called on all macOS and Linux computers. On Windows, the root
is usually called `C:/`, but sometimes other letters, like `D:/`, are also used
depending on the computer's hardware.

A _path_ is a list of directories that leads to a specific file or directory on
a file system (imagine giving directons to someone as they walk through the
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
In other words, when a path leads to a directory, including a _trailing slash_
is optional, but makes the meaning of the path clearer. Paths that lead to
files never have a trailing slash.

_TODO: Python doesn't use / for all OSes_

On Windows computers, paths are usually written with backslashes ```\``` to
separate directories instead of forward slashes. Fortunately, R uses forward
slashes `/` for all paths, regardless of the operating system. So when you're
working in R, use forward slashes and don't worry about the operating system.
This is especially convenient when you want to share code with someone that
uses a different operating system than you.

(absolute-relative-paths)=
### Absolute & Relative Paths

A path that starts from the root directory, like all of the ones we've seen so
far, is called an _absolute path_. The path is "absolute" because it
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

On the other hand, a _relative path_ is one that doesn't start from the root
directory. The path is "relative" to an unspecified starting point, which
usually depends on the context.

For instance, suppose Ada's code is saved in the file `analysis.R` (more about
`.R` files in Section \@ref(r-scripts)), which is in the same directory as
`cats.csv` on her computer. Then instead of an absolute path, she can use a
relative path in her code:

```
cats.csv
```

The context is the location of `analysis.R`, the file that contains the code.
In other words, the starting point on Ada's computer is the `ada` directory. On
other computers, the starting point will be different, depending on where the
code is stored.

Now suppose Ada sends her corrected code in `analysis.R` to Gladys, and tells
Gladys to put it in the same directory as `cats.csv`. Since the path `cats.csv`
is relative, the code will still work on Gladys' computer, as long as the two
files are in the same directory. The name of that directory and its location in
the file system don't matter, and don't have to be the same as on Ada's
computer. Gladys can put the files in a directory `/Users/gladys/from_ada/` and
the path (and code) will still work.

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

When use you paths in code, they should almost always be relative paths. This
ensures that the code is portable to other computers, which is an important
aspect of reproducibility. Another benefit is that relative paths tend to be
shorter, making your code easier to read (and write).

When you write paths, there are three shortcuts you can use. These are most
useful in relative paths, but also work in absolute paths:

* `.` means the current directory.
* `..` means the directory above the current directory.
* `~` means the _home directory_. Each user has their own home directory, whose
  location depends on the operating system and their username. Home directories
  are typically found inside `C:/Users/` on Windows, `/Users/` on macOS, and
  `/home/` on Linux.

As an example, suppose Ada wants to write a (relative) path from the `ada`
directory to Charles' cool selfie. Using these shorcuts, she can write:

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


### Jupyter Notebooks


### The Working Directory

Section [](absolute-relative-paths) explained that relative paths have a
starting point that depends on the context where the path is used. The _working
directory_ is the starting point Python uses for relative paths. Think of the
working directory as the directory Python is currently "at" or watching.


Reading Files
-------------

### Hello, Data!
