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


Non-tabular Data
================

:::{admonition} Learning Objectives
* Create and access elements of tuples
* Create and access elements of dictionaries
* Explain what HTTP is, including request methods
* Use the requests package to make HTTP requests
* Explain what a web API is
* Load and access elements of JSON data
* Write loops to do things repeatedly
* Write comprehensions to do things repeatedly
* Save data to a CSV or other file format
:::

The goal and motivation for today's workshop is to use Python to download some
non-tabular data from the internet, convert it into a tabular format, and save
it as a CSV file.



## Recap

### Aggregation

The Pandas method `.aggregate` **aggregates** a Series, meaning it computes a
summary of the series (usually one or two values, such). The mean, median, max,
standard deviation, and range are all examples of aggregate statistics. You can
call `.aggregate` several different ways:

* With the name of a commonly-used statistic in quotes, as in
  `x.aggregate("mean")`
* With a function, as in `x.aggregate(np.mean)`
* With a list of names or functions, as in `x.aggregate(["median", np.mean])`

You can also use the `.aggregate` method on a DataFrame, in which case it will
aggregate each column separately.

The `.agg` method is a shortcut for `.aggregate`. There are also shortcut
methods for commonly used aggregate statistics, such as `.mean`, `.median`, and
`.std`.

You can use `.groupby` to group data into sets of rows before you use
`.aggregate`. The argument to `.groupby` should be a name or list of names of
columns to use for grouping. It usually only makes sense to group by
categorical columns (so that there's more than one row in each group).


### Installing Packages

Some packages are not installed by default with Anaconda.

To install a package, open a JupyterLab Terminal (`File` -> `New` ->
`Terminal`). Then use the command `conda install PACKAGE` where `PACKAGE` is
the name of the package you want. You can add `-c conda-forge` to this command
to get a more recent version of the package.


### Visualization

A wide variety of visualization packages are available for Python. You can read
more about them on the [PyViz website][pyviz]. This reader only covers the
**[plotnine][]** package.

[pyviz]: https://pyviz.org/
[plotnine]: https://plotnine.readthedocs.io/en/stable/

The plotnine package is based on the popular [ggplot2][] package for R. The
package uses the **grammar of graphics**, which is a way to describe
visualizations in terms of layers that get added together. At a minimum, every
visualization requires three layers:

* Data. A DataFrame passed to the `ggplot` function
* Geometry. A `geom_` that specifies what kind of lines or shapes should be on
  the plot
* Aesthetics. A call to `aes` (as the second argument to `ggplot`) that
  specifies which column of data is associated with each aesthetic property
  (`x`, `y`, `color`, `size`, ...) of the plot

Several other layers are also available for further customizing visualizations.

You can save a plotnine visualization to a file by calling the `.save` method
on the object returned by the call to `ggplot`.

[ggplot2]: https://ggplot2.tidyverse.org/


### Conditional Statements

**If-statements**, written with the keywords `if`, `elif`, and `else`, provide
a way to run code only when some condition is satisfied. The condition must be
an expression that returns a Boolean (`False` or `True`) value. Code in the
body of an if-statement must be indented by 4 spaces.

### Functions

You can define your own functions with the `def` keyword. Code in the body of
the function must be indented by 4 spaces. You can make your function return a
value with the `return` keyword. Parameters and variables inside of a
function's body are not accessible from outside of the function's body.

As an example, here's a function to check for even numbers:

```{code-cell}
def is_even(x):
    return x % 2 == 0

is_even(3)
```

```{code-cell}
is_even(12)
```


(containers)=
## Containers

Python provides a variety of containers for data. This section describes the
three most widely-used containers. You can find even more types of containers
in the [collections module][collections].

[collections]: https://docs.python.org/3/library/collections.html


### Lists

Lists were introduced in {numref}`lists`. A list is an ordered collection of
values. Lists are **mutable**, which means that the elements can be changed.

Here's a quick recap of things you can do with lists:

```{code-cell}
# Create a list with square brackets [ ]
x = [1, 3, 5]

# Get an element by position with square brackets [ ]
x[0]

# Set an element
x[2] = -1
```

You can also remove an element of a list with the `del` keyword. For instance:

```{code-cell}
del x[2]

x
```

The `del` keyword can also be used with dictionaries, which are described in
{numref}`dictionaries`.


### Tuples

A **tuple** is an ordered collection of values. Think of coordinates. Tuples
are **immutable**, which means that the elements of a tuple can't be changed.


```{code-cell}
y = ("hi", 1, 3.7)
y
```

```{code-cell}
type(y)
```

You can get elements of a tuple with indexing, just like a list:

```{code-cell}
y[0]
```

If you try to change the elements, Python raises an error:

```{code-cell}
:tags: [raises-exception]
y[1] = 3
```

You can also get the elements of a tuple by **unpacking** them. Unpacking is a
way to assign the elements of a tuple or list to multiple variables. Use `=` to
unpack values, making sure that the structure on the left-hand side matches the
structure on the right-hand side:

```{code-cell}
u, v, w = y
u
```

```{code-cell}
v
```

```{code-cell}
w
```

Unpacking also works with lists.

Tuples are slightly more efficient than lists, and are generally the best way
to return a fixed number of results from a function (see {numref}`functions`).


(dictionaries)=
### Dictionaries

A **dictionary** (or `dict`) is a one-to-one map from **keys** to **values**.
That means that you use keys to look up values in a dictionary. Like lists,
dictionaries are mutable.

You can make a dictionary by enclosing comma-separated `key: value` pairs in
curly braces `{ }`, like this:

```{code-cell}
x = {"hello": 1, 3: 5}
x
```

```{code-cell}
type(x)
```

The dictionary `x` has two keys: `"hello"` and `3`. Most of the time, the keys
in a dictionary will be strings, but you can use other types of keys. However,
the keys are required to be unique.

You can get and set elements of a dictionary by indexing with keys:

```{code-cell}
x["hello"]
```

You can also get elements with the `.get` method, which gets an element by key
or returns a default value if the key isn't in the dictionary:

```{code-cell}
x.get("hello", 10)
```

```{code-cell}
x.get("goodbye", 10) 
```

You can get the keys or the values in a dictionary with the `.keys` and `.dict`
methods respectfully:

```{code-cell}
x.keys()
```

```{code-cell}
x.values()
```

You can use the `list` function to convert either of these to an ordinary list:

```{code-cell}
list(x.keys())
```

Common use cases for dictionaries include creating lookup tables and returning
named results from a function.




## Surfing the Web

The **hypertext transfer protocol** (HTTP) is a set of rules for communication
between computers on a network. HTTP has a request-response model:

1. The **client** sends a **request** to a **server**. For example, the client
   might request a file.
2. The server sends a **response** to the request.

Your web browser goes through this process every time you visit a website. HTTP
requests are also one way to download data sets from the web.

There are several different HTTP request methods:

* **GET** requests data from the server.
    + Example: Visiting a web site
    + You can send a small amount of data with a GET request through the URL
* **POST** sends data to the server.
    + Example: Submitting a web form
    + The response to a POST request often contains data too
* [And many more...][http-requests]

[http-requests]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

:::{tip}
If you browse the web with Chrome or Firefox, you can inspect the HTTP requests
your brower makes when you visit a website. Go to a website and press
`Ctrl-Shift-i` (OS X: `Cmd-Shift-i`) to open your browser's web developer
tools. Click on the "Network" tab and reload the website. You should see the
tab populate with all of the requests your browser makes as it loads the
website.
:::

After you make an HTTP request, the server will send a response. Every HTTP
response includes a 3-digit status code to summarize the meaning of the
response:

Range            | Meaning                              | Name
---------------- | ------------------------------------ | ----
100s (100 - 199) | Request received, still processing   | Informational
200s             | Success                              | Success
300s             | The requested data is somewhere else | Redirect
400s             | Something's wrong with the request   | Client Error
500s             | Something's wrong with the server    | Server Error

You can find a list of common status codes in [Mozilla's developer
documentation][http-status].

[http-status]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

A response usually also contains **content** as text or raw bytes. Some common
formats for the content are:

* Hypertext Markup Language (HTML)
* Extensible Markup Language (XML)
* JavaScript Object Notation (JSON)

### The requests Package

```{code-cell}
:tags: [remove-cell]
import requests
import requests_cache

requests_cache.install_cache("day4_http_cache")
```

The **requests** package provides functions for making HTTP requests from
Python. You can use requests to make a GET request with the `get` function:

```{code-cell}
import requests

response = requests.get("https://datalab.ucdavis.edu")
```

The status code of the response is in the `.status_code` attribute:

```{code-cell}
response.status_code
```

If you want Python to raise an error any time the status code indicates a
problem, you can use the `.raise_for_status` method. It doesn't do anything if
the status code is okay:

```{code-cell}
response.raise_for_status()
```

The content of the response is stored as bytes in the `.contents` attribute and
as text in the `.text` attribute. Choose which one to use based on what kind of
site or file you requested. Web pages (`.html`) are usually text files, so for
the DataLab site it makes more sense to use `.text` to access the content:

```{code-cell}
text = response.text

# Only display the first 200 characters
print(text[:200])
```

(request-etiquette)=
### Request Etiquette

Making an HTTP request is not free. It has a real cost in CPU time and
electricity. Server administrators will not appreciate it if you make too many
requests or make requests too quickly. So:

* Use the `time.sleep` function to slow down any requests you make in a loop
  ({numref}`loops` explains loops). Aim for no more than 20-30 requests per
  second.
* Install and use the __requests_cache__ package to avoid downloading extra
  data when you make the same request twice.

Failing to be polite can get you banned from websites!

```
# In a Terminal (not Python console!):
#   conda install -c conda-forge requests-cache
#

import requests_cache

requests_cache.install_cache("my_cache")
```


### Web APIs

An **application programming interface** (API) is a collection of functions and
data structures for communicating with other software. For instance, whenever
you use a Python package, you're using the API created by the package's
developers.

Websites sometimes provide a *web* API so that programmers can create
applications that access data and settings. The most common kind of web API is
**representational state transfer** (REST). The key ideas of REST are that:

* You can "call" functions by making HTTP requests.
* URLs called **endpoints** serve as function names.
* Separate function calls are handled independently of each other. The server
  doesn't remember previous calls.

For example, the [Star Wars API](https://swapi.dev/) (SWAPI) is a REST API with
endpoints that return data about the Star Wars universe. The best way to learn
how to use a web API is to read its documentation, and fortunately the Star
Wars API is [well-documented][swapi-docs].

[swapi-docs]: https://swapi.dev/documentation


Try making a request to SWAPI's "people" endpoint (the endpoint URL comes from
the SWAPI documentation):

```{code-cell}
url = "https://swapi.dev/api/people/1/"
response = requests.get(url)
```

Don't forget to check the status of the response:

```{code-cell}
response.status_code
```

A 200 status code means the request was successful, so the next step is to take
a look at the content of the response.

Unless you've already read through the SWAPI documentation, you probably don't
know whether the content will be bytes or text. When you're unsure, you can try
printing the `.text` value to check whether the content looks like text. Byte
content will usually look like gibberish if you try to display it as text.
Here's the content of the response:

```{code-cell}
response.text
```

This is text about Luke Skywalker. In fact, according to the SWAPI
documentation, all of the SWAPI endpoints return text.

Although the response content is text, it isn't ordinary English text. It's
full of curly braces, square brackets, quotes, and other punctuation. If you
think back to the beginning ({numref}`containers`) of this chapter, the way the
punctuation is arranged might start to look familiar...


### JavaScript Object Notation

The response content looks a lot like Python lists and dictionaries! The
response is not actually Python code, but it *is* JavaScript code. In
JavaScript, lists and dictionaries are written the same way as in Python. The
response is in a popular non-tabular data format called **JavaScript Object
Notation** (JSON).

JavaScript Object Notation (JSON) looks and works a lot like Python lists and
dictionaries. Lists are surrounded with `[ ]`, and dictionaries are surrounded
with `{ }`. There are many Python packages for converting JSON text into Python
lists and dictionaries.

:::{tip}
You can use Python's built-in [json][] module to read a JSON file you didn't
get from an HTTP request. For example, Jupyter notebooks (`.ipynb` files) are
in JSON format.
:::

When you know the content of a response is in JSON format, you can use the
`.json` method on the response to convert it into Python lists and
dictionaries:

```{code-cell}
luke = response.json()

luke
```

```{code-cell}
type(luke)
```

[json]: https://docs.python.org/3/library/json.html

In this case, the outer object is a dictionary. The keys in the dictionary are:

```{code-cell}
list(luke.keys())
```

These keys describe the included information about Luke. For example, to get
his eye color, you can use indexing:

```{code-cell}
luke["eye_color"]
```

Sometimes data in JSON format will contain several layers of dictionaries and
lists. Remember that you can use indexing with square brackets `[ ]` to
navigate these.

### Using Endpoints

The SWAPI endpoint `/people/` returns information in JSON format about
different people in the Star Wars universe. An ID number after `/people/`
determines the person for which the endpoint returns information. Think of the
ID number as an argument to the endpoint. For instance, Luke Skywalker's ID
number is `1`, so the URL for information about Luke is:

```text
https://swapi.dev/api/people/1/
```

A good way to work with an endpoint that accepts arguments is to use Python to
paste the arguments onto the end. For example, this code pastes the number `2`
onto the end of the string `endpoint`:

```{code-cell}
endpoint = "https://swapi.dev/api/people/"
endpoint + str(2)
```

The `str` function converts the ID number into a string, and `+` pastes the two
strings together.

Now try getting the information for the person with ID number `2`:

```{code-cell}
response = requests.get(endpoint + str(2))

# Raise an error if the request failed
response.raise_for_status()

person = response.json()
person
```

So the "person" with ID number `2` is actually the android C3-PO.

You can make using the endpoint more convenient by writing a Python function
that takes an ID number as input, makes a request to the endpoint, and then
returns the result. Here's the code:

```{code-cell}
def get_swapi_person(id_num):
    endpoint = "https://swapi.dev/api/people/"

    # Note that 'id_num' replaces '2'
    response = requests.get(endpoint + str(id_num))

    # Raise an error if the request failed
    response.raise_for_status()

    return response.json()
```

As always, when you write a function, it's important to test it out. For
example:

```{code-cell}
get_swapi_person(50)
```

When you're working with a web API, it's generally a good idea to create
**wrapper functions**, like `get_swapi_person`, that turn each endpoint into an
actual Python function by wrapping up (or encapsulating) the requests code.



(loops)=
## Loops

Now suppose you want to get the information for the first 15 people in SWAPI.
You could do this by writing 15 calls to `get_swapi_person`, but that would be
very tedious.

One major benefit of using a programming language like Python is that
repetitive tasks can be automated. A **loop** is a way to automate doing a
similar operation several times, so that you don't have to repeat the code
several times. Loops are a feature of almost all modern programming languages,
so it's useful to understand them.

In Python, there are two kinds of loops. We'll focus on **for-loops**.

For-loops **iterate** over some object, and compute something for each element.
Each one of these computations is one **iteration**. A for-loop begins with the
`for` keyword, followed by:

* A placeholder variable, which will automatically be assigned an element at
  the beginning of each iteration
* The `in` keyword
* An object with elements
* A colon `:`

Code in the body of the loop must be indented by 4 spaces.

For example, to print out the names in a list `names`, you can write:

```{code-cell}
names = ["Arthur", "Nick", "Cameron", "Pamela"]

for name in names:
    print(name)
```

The code in the body of the loop is evaluated once for each name in the list
(that is, once for each iteration).

A common technique when programming with for-loops is to iterate over a
sequence of numbers. Then you can use the numbers to index other objects. In
Python, the `range` function generates a sequence of numbers starting from 0.
As an example, here's a version of the loop above that uses indexes:

```{code-cell}
for i in range(4):
    print(names[i])
```

Sometimes you might want both the indexes and the values for an object. In that
case, you can use the `enumerate` function. When you use `enumerate` in a
loop, the loop syntax is slightly different:

```{code-cell}
for i, name in enumerate(names):
    print("This is iteration " + str(i))
    print(name)
```


Most of the time, you'll want to save the results from the iterations into a
variable for use later on, rather than print them all out. The best way to do
this is to create an empty list before the loop, and then append to it with the
`.append` method. For example, here's a loop that computes the cumulative sums
from left to right for the numbers in a list:

```{code-cell}
nums = [1, 3, 2, -2, 10]

sums = []
total = 0

for num in nums:
    total = total + num
    sums.append(total)

sums
```

You can use a loop to get the information about the first 15 people in SWAPI.
When you send HTTP requests (or call a function that sends HTTP requests) in a
loop, be careful to follow the guidelines for request etiquette described in
{numref}`request-etiquette`. For loops, limiting the number of requests per
second is especially important. Here's the code to get the information for the
first 15 people:

```{code-cell}
import time

people = []

for i in range(15):
    # i + 1 because range starts from 0
    person = get_swapi_person(i + 1)
    people.append(person)

    # Do nothing for 1/10 of a second, to prevent making requests too quickly
    time.sleep(0.1)
```

After running the loop, you can inspect the returned information in the list
`people`:

```{code-cell}
people[0]
```


### Comprehensions

Python provides an efficient and powerful alternative to loops called
**comprehensions**. Comprehensions automatically create a list or dictionary. A
**list comprehension** creates a list, and a **dictionary comprehension**
creates a dictionary.

Comprehensions are especially helpful if you have a list or dictionary and want
to transform each element in the same way. For instance, suppose you want to
get the eye color for each person in the `people` list. You can get the eye
color for the first person with the code:

```{code-cell}
people[0]["eye_color"]
```

You could use this code with a loop that changes the first index (`0`) in order
to get the eye color of every person. However, you can do the same thing as a
loop more concisely with a list comprehension. Here's the code:

```{code-cell}
eye_colors = [person["eye_color"] for person in people]

eye_colors[0]
```

The syntax for a list comprehension includes the keywords `for` and `in`, just
like a for-loop. The difference is that in the list comprehension, the repeated
code comes *before* the `for` keyword rather than after it, and the entire
expression is enclosed in square brackets `[ ]`.

You can use list comprehensions to get other information as well. For instance,
here's the code to get lists of names and heights for each person in the list:

```{code-cell}
names = [person["name"] for person in people]
heights = [person["height"] for person in people]
```

You can learn more about comprehensions in the [official Python
documentation][comprehensions].

[comprehensions]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions



## Exporting Data

The extracted `names`, `heights`, and `eye_colors` lists are like columns in a
DataFrame where each row is one person, so you might as well put them in a
DataFrame. You can use the `pd.DataFrame` function and a dictionary of columns
to do this:

```{code-cell}
import pandas as pd

people_df = pd.DataFrame({"name": names, "height": heights,
    "eye_color": eye_colors})

people_df
```

Pandas provides a variety of methods for saving DataFrames to a file. Most of
these begin with `.to_`. For example, to save a DataFrame to a CSV file, use
the `.to_csv` method:

```
people_df.to_csv("swapi_people.csv")
```

It's a good idea to save your data sets like this whenever you reach a
checkpoint in the problem you're trying to solve.


## Practice Exercises


### Exercise 1

Create a CSV file for the first 15 *vehicles* in SWAPI. The file should include
columns for cargo capacity, cost, length, manufacturer, model, and passengers.


### Exercise 2

Create a histogram from the heights of the first 30 people in SWAPI.

:::{admonition} Hint
You can use the `float` function to convert a string to a decimal number.
:::
