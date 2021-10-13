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

## Recap

TODO: go over problem solutions + high level explanation of session 3

## Downloading JSON Data Using Requests Module 

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

In python, dictionaries are created using `{}`:
```{code-cell}
davis = {'city': "Davis", 'state': "CA"}
```

We can change values by assigning a new value to the key:
```{code-cell}
davis['state'] = "California"
```

We can add new keys:
```{code-cell}
davis['population'] = 50000
```

## Loops

In python, loops are used to iterate through items in a sequence.

Loops are used when we want to perform a task many times.

The syntax is to have the `for` keyword followed by a name followed by
`in` keyword and lastly the object we want to sequence through. The expression
is followed by a colon, and each subsequent line within the loop is indented:
```{code-cell}
for k in luke.keys():
    print(k)
```

Dictionaries also have an items attribute, which we can iterate through:
```
for key,value in luke.items():
    print(key, ->, value)
```

A really common technique in python is to iterate over a sequence of numbers,
by using the `range` function:
```{code-cell}
for i in range(10):
    print(i)
```

To iterate through a list with a for loop:
```{code-cell}
a_list = [0,23,2]
for elem in a:
    print(a)
```

We can do more than just print within a loop:
```{code-cell}
a_list = [0,23,2]
for elem in a:
    b = a * 2
    print(b)
```

A really handy function often used with loops in python is `enumerate`, 
which adds a counter that can be used within the loop:
```{code-cell}
colors = ["red", "green", "blue"]
for i,color in enumerate(colors):
   print(i, color)
```

Often times, we create a new list based on the outcome of element wise operation
on another list:
```{code-cell}
a_list = [0,23,2]
b_list = []
for elem in a:
    b.append(a * 2)
```

Heres the same example with a function:
```{code-cell}
def times_four(x):
    return x * 4
b = []
for elem in a:
    b.append(times_four(elem))
```


### List Comprehension

To concisely create a new list based on values of an existing list, you
can use `list comprehension`.

`list comprehension` allows you to simplify the syntax of the above loops
into a single line of code.
In addition, list compehension has the added benefit of generally being
noticeably faster than the traditional syntax demonstrated in the previous 
section.

The simplest syntax for list comprehension looks like:
```{code-cell}
a_list = [0,23,2]
new_list = [x for x in a_list]
```

You can add a condition to the loop within the list comprehension:
```{code-cell}
new_list = [x for x in a_list if x > 10]
new_list
```

You can also add expressions to modify the values:
```{code-cell}
new_list = [x + 4 for x in a_list if x > 10]
new_list
```

## More Functions

Lets write some functions to get the homeworld of each character in swapi.

First, lets write a function to get the homeworld of a single character.
We can practice with the our 'luke' data we parsed earlier.

```{code-cell}
luke["homeworld"]
hw_url = homeworld
```

```{code-cell}
hw_content = requests.get(hw_url).content
hw_content
```

```{code-cell}
hw_json = json.loads(hw_content)
name = hw_json["name"]
```

```{code-cell}
def get_homeworld(person):
    url = person["homeworld"]
    content = requests.get(url).content
    js = json.loads(content)
    return js["name"]

name = get_homeworld(luke)
```

Now we need to get a list of all the people:
```{code-cell}
n_people = json.loads(requests.get("https://swapi.dev/api/people/").content)["count"]
```

```{code-cell}
def get_person(id):
    url = "https://swapi.dev/api/people/" + str(id)
    content = requests.get(url).content
    js = json.loads(content)
    return js
```

```{code-cell}
person_list = [get_person(i) for i in range(1,5)]
homeworlds = [get_homeworld(person) for person in person_list]
homeworlds
```
    
## Exporting Data

### Using Python File IO

Save as list using file io

Read from the file

### Using Python Pickle

### Using Pandas

save using pandas

## Challenge Problems

Create a csv containing of name, height, mass, gender for each character that 
was born in tattoine.

Create a histogram plot of character heights, in inches.
