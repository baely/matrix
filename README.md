# Matrix

*Mathematical matrix module for Python*

## Requirements
- Python 3

## Usage
Create a Matrix by specifying dimensions or passing in a list of lists.
```python
matrix_dimension = Matrix(10, 10)
matrix_listlist = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
```

*Note*: All functions and operations will create a new Matrix instance, similar
to the behaviour of Pandas' Dataframes.

## Operations

### Addition

Constant addition:
```python
matrix = Matrix(10, 10)
k = 5

matrix + k
```

Matrix addition:
```python
a_matrix = Matrix(10, 10)
b_matrix = Matrix(10, 10)

a_matrix + b_matrix
```

### Multiplication

Constant multiplication:
```python
matrix = Matrix(10, 10)
k = 5

matrix * k
```

Matrix multiplication:
```python
a_matrix = Matrix(10, 10)
b_matrix = Matrix(10, 10)

a_matrix * b_matrix
```

### Transposing
```python
matrix = Matrix(10, 10)

matrix.transpose()
```