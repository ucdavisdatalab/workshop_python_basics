Scientific Python
=================

:::{admonition} Learning Objectives
- review python basics
- describe numpy and pandas packages
- create and explore dataframes
- learn ways to index dataframes
:::


## Recap

## Packages

```python
import numpy as np
import pandas as pd
```

## Numpy

```python
array = np.array( [1, 3, 9, 2])
print(array.dtype)
```

## Pandas

Pandas two data structures - series and dataframes
As well as many useful functions and methods for data analysis tasks

```python
series = pd.Series( [1, 3, 9, 2] )
print(series)
```

## Load in data
```python
dataset = pd.read_csv() # should the input be a url?
```

## Dataframes

```python
print(dataset)
```

## Methods for Exploring Dataframes

```python
dataset.describe()
dataset.head()
dataset.columns
dataset.info
```

## Data Types
```python
dataset.dtypes
```

## Indexing
```python
dataset.loc # label based or boolean array
dataset.iloc # interger based
dataset[colname]
dataset[[colnames]]
dataset[colname][4]
```

## Modiying DataFrames
Concat
Join
cleaning
changing datatypes
```python
```

## Grouping
