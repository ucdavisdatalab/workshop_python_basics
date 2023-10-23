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


Organizing Code
===============

:::{admonition} Learning Objectives
* Create code that only runs when a condition is satisfied
* Write functions to organize and encapsulate reusable code
:::

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


(functions)=
## Functions

The main way to interact with Python is by calling functions, which was first
explained back in {numref}`calling-functions`. This section explains how to
write your own functions.

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
take a Series of numbers as input, compare them to zero, and then return the
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
import pandas as pd

x = pd.Series([5, -1, -2, 0, 3])

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
in a Series. You can make a parameter for the number of values to get, with a
default argument of `5`. Here's the code and some test cases:

```{code-cell}
def get_largest(x, n = 5):
    sorted = y.sort_values()
    return sorted.head(n)

y = pd.Series([-6, 7, 10, 3, 1, 15, -2])

get_largest(y, 3)
```

```{code-cell}
get_largest(y)
```

:::{tip}
The `return` keyword causes a function to return a result immediately, without
running any subsequent code in its body. So before the end of the function, it
only makes sense to use `return` from inside of an if-statement. 
:::

A function returns one object, but sometimes computations have multiple
results. In that case, return the results in a container such as a tuple or
list. See {numref}`arrays-lists-sequences` for examples of several different
containers you can use.

For example, let's make a function that computes the mean and median for a
vector. We'll return the results in a tuple:

```{code-cell}
import numpy as np

def compute_mean_med(x):
    m1 = np.mean(x)
    m2 = np.median(x)
    return (m1, m2)

compute_mean_med(pd.Series([1, 2, 3, 1]))
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


## Practice Exercises

### Exercise 1

Try writing a function `is_leap` that detects leap years. The input to your
function should be an integer year (or a Series of years), and the output
should be a Boolean value. A year is a leap year if either of these conditions
is true:

* It is divisible by 4 and not 100
* It is divisible by 400

That means the years 2004 and 2000 are leap years, but the year 2200 is not.

:::{admonition} Hint
The modulo operator `%` returns the remainder after divding a number, so
for example `4 % 3` returns `1`.
:::

Here's a few test cases for your function:

```
is_leap(400)
is_leap(1997)
```

```{code-cell}
:tags: [remove-cell]
# If year is divisible by 4 and not 100 -> leap
# If year is divisible by 400 -> leap
year = 2004

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    else:
        leap = False

    return leap

is_leap(2200)
```
