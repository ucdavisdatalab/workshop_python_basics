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
- create numpy ndarrays
- indexing numpy arrays
:::

## Numpy

**NumPy** (Numerical Python) is a package that provides functions and 
data structures for working with numerical data. NumPy functions are generally 
more intuitive, and more computationally efficient for working with lots 
of numbers than Python's built-in options. It has become the standard for 
working with numeric data in python.

## Numpy Arrays

NumPy provides an **array** object. Arrays are a critical data structure for
working with numerical data and some version of array can be found in pretty
much every commonly used programming language. NumPy's array is different from 
the python list object in that each element needs to be the same data type, 
and its size is set on its creation.

If you are working in python for data analysis, data science, 
machine learning, etc. you will run into numpy arrays. 

There are several ways to create an ndarray. In this case we will use a 
list (built-in python object) of numbers as the input for our array creation:
```{code-cell}
arr = np.array([1, 3, 9, 2])
arr
```

We can see the number of elements in the array with the `shape` attribute:
```{code-cell}
arr.shape
```

The `shape` attribute reflects the number of elements in each **dimension** of
the ndarray. In this case, there are four elements and only one dimension.

**Dimensions** refers to the number of **axes** that represents the data. For 
example if you are working with lat/long coordinates you will probably
have 2 dimensions in your data. If working with images you may have 3 
dimensions: x,y and color.

To see the number of of dimensions of the array object use `ndim`:
```{code-cell}
arr.ndim
```

As mentioned earlier, unlike python's built-in list type, each element
in an ndarray are the same data type. Recall that we created this array,
we did not specify a data type for numpy to use. As a result, numpy inferred
a data type from values in the list. We can access the datatype from
the `dtype` attribute of the array:
```{code-cell}
arr.dtype 
```

To explicitly define the datatype you want for the array you create, pass
the dtype parameter when creating the array:
```{code-cell}
arr = np.array([1, 3, 9, 2], dtype=np.int8)
arr 
```

```{Note}
For reference here is a list of common datatypes in data analysis:
- bool
- int
- float
- datetime
- string
- object
```

## Indexing Numpy Arrays

To access an element from the array use the `[]` operator:
```{code-cell}
display(arr)
arr[3]
```

We can access more than one element with python slicing:
```{code-cell}
display(arr)
arr[1:3:1]
```

We can use integer arrays as indexes:
```{code-cell}
display(arr)
arr[[1,2,0]]
```

We can also use boolean arrays as indexes:
```{code-cell}
display(arr)
arr[[True,False,True,True]]
```

We can use indexing to modify the selected elements:
```{code-cell}
display(arr)
arr[3] = 78
arr[[1,2]] = [0,9]
arr
```

Notice what happens when we pass a value that is not an integer:
```{code-cell}
display(arr)
arr[3] = 7.8
arr
```

NumPy has converted 7.8 to an integer before entering it into the array. This
will only work if there is an accepted way of converting to integer, for 
example it will fail if something like this is passed:
```{code-cell}
try:
    arr[3] = "hello"
except ValueError as e:
    print(e)
```

## Operating on NumPy Arrays

In general, operations are applied element by element on the array:
```{code-cell}
display(arr)
arr * 2
```

Another example but with comparison operators:
```{code-cell}
display(arr)
arr > 3
```

This fits in nicely with indexing using boolean array from before:
```{code-cell}
display(arr)
arr[arr>3]
```

## Multi Dimensional Arrays + Other Ways to Create Arrays

Now let us see some of these concepts with a 2-D array. As before, we can
define a 2-D array by passing a python list as input:
```{code-cell}
arr = np.array([[1,2], [3,4]], dtype=np.int8)
```

Here is another way of initializing an array:
```{code-cell}
arr = np.zeros((3,4), dtype=np.float64)
arr
```
