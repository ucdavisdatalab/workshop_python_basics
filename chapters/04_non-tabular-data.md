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

:::{admonition} Learning Objectives
- Download json data from the web
- Parse json using the json module
- Understand and use dictionaries
- Learn how to use loops
- Learn list comprehension
- Create a DataFrame
- Save a csv version of a dataframe
- Write a text file using python's io functions
:::

## Downloading Data Using Requests Module

Python is a very flexible programming language that supports many different 
tasks.

Often times, there exists a popular package that provides functions and 
datastructures to make writing code for that task easier. Using these packages
provides lots of benefits, including but not limited to, better tested code
(less bugs), efficient solutions (faster), interconnected to other common
packages, as well as providing a shared set of solutions (easier to find 
questions, documentation, and generally get help).

We have seen this concept so far this series with the `pandas` package - providing
support for tabular data analysis, as well as the `plotnine` package - providing
convenient plotting functions.

Two modules that we will use in this session are the `requests` module and the 
`json` module.

```{code-cell}
import requests
import json
```

### Star Wars API

We will be using data from [Star Wars API (swapi)](https://swapi.dev/). 

TODO: description + walkthrough of site

### The Requests Module

The `requests` module provides functions for working with HTTP from python.

In depth description of HTTP and APIs is outside the scope of this workshop,
but fortunately, with the requests module, we can easily get some data.

The simplest way to download a file from the internet with the `requests`
library is to use the `get` function from requests:
```{code-cell}
url = "https://swapi.dev/api/people/1/"
response = requests.get(url)
```

The `get` function returned a response object. The response contains some 
metadata about the request itself, as well as the 'content' (what we want). 
We can access the content through the `content` attribute of the response
object: 
```{code-cell}
response.content
```

Lets see what this is:
```{code-cell}
type(response.content)
```

`bytes` is a low level python data type that store the literal bits that
were transfered over the internet. In this case we can convert it to a string:
```{code-cell}
content = response.content.decode("ascii")
```

Now we have a string, in this case, its JSON formatted data.

### JSON

JSON is a data interchange format designed to be easy to read and write.
It is an extremely common data format, especially for data transfered over
the internet.

To read JSON in python, we can use the `json` package.

To parse a string of JSON formatted text, use the `loads` function from
the `json` module:
```{code-cell}
luke = json.loads(content0
luke
```

Lets look at the type of our object:
```{code-cell}
type(luke)
```

## Dictionaries

`dict` is the 'Dictionary' type, and is built-into python.

A dictionary is a data structure that stores key values pairs.

Some key features of dictionaries are that: 
- keys must be strings 
- each key must be unique
- values don't need to be of the same type.

We can access the keys of the dictionary with the `keys` method:
```{code-cell}
luke.keys()
```

In the same way, we can access just the values with the `values` method:
```{code-cell}
luke.values()
```

Dictionaries are indexed using the `[]` operator with the desired key passed
as an argument:
```{code-cell}
luke["name"]
```

TODO: describe why integer indexing isnt used, and that only one value
can be used a time

## Loops

In python, loops are used to iterate through values.

## List Comprehension

## Loops Applied

## Exporting Data
