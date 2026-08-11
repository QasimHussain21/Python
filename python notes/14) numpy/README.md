# 📖 Lecture 14: NumPy Arrays in Python

<p align="center">
  <img src="https://img.shields.io/badge/Topic-NumPy%20Arrays-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Concept-Multidimensional%20Arrays-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Level-Beginner-success?style=for-the-badge">
</p>

---

## 🧠 Core Concept

**NumPy** is a Python library used to work with **arrays and numerical data**.

This lecture focuses on understanding **NumPy arrays, dimensions, indexing, slicing, data types, shape, joining, splitting, flattening, unique values, and deleting elements**.

The main idea is to learn how data can be organized and manipulated efficiently using **NumPy arrays**.

---

## ⚡ What You Will Learn

* What is NumPy
* Creating NumPy arrays
* Understanding array dimensions
* 1-D, 2-D, 3-D and higher-dimensional arrays
* Checking number of dimensions using `ndim`
* Creating arrays with `ndmin`
* NumPy array indexing
* Accessing 1-D, 2-D and 3-D arrays
* Array slicing
* Checking array data types using `dtype`
* Creating arrays with a defined data type
* Understanding array shape
* Joining NumPy arrays using `concatenate()`
* Splitting arrays using `array_split()`
* Converting multidimensional arrays into 1-D using `ravel()` and `flatten()`
* Finding unique values using `unique()`
* Getting indexes and counts with `unique()`
* Deleting elements using `delete()`

---

## 🖼️ Visual Understanding

<p align="center">
  <img src="https://numpy.org/images/logo.svg" width="250">
</p>

<p align="center">
  <i>💡 NumPy → Array → Dimensions → Indexing → Slicing → Data Manipulation</i>
</p>

---

## 🧪 Code Example

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Data Type:", arr.dtype)
```

### Output

```text
[[1 2 3]
 [4 5 6]]

Dimensions: 2
Shape: (2, 3)
Data Type: int64
```

---

## 🔢 Array Dimensions

NumPy arrays can have different dimensions.

### 0-D Array

```python
arr = np.array(42)

print(arr)
print(arr.ndim)
```

### 1-D Array

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(arr.ndim)
```

### 2-D Array

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr)
print(arr.ndim)
```

### 3-D Array

```python
arr = np.array([[[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]])

print(arr)
print(arr.ndim)
```

The lecture also demonstrates creating higher-dimensional arrays using `ndmin`.

---

## 🔍 Array Indexing

Array indexing is used to access individual elements.

Indexes start from **0**.

```python
arr = np.array([1, 2, 3, 4])

print(arr[0])
```

### Output

```text
1
```

For a 2-D array, row and column indexes can be used:

```python
arr = np.array([[10, 20, 30, 40, 50],
                [60, 70, 80, 90, 100]])

print(arr[0, 1])
```

### Output

```text
20
```

For a 3-D array:

```python
arr = np.array([[[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12]]])

print(arr[0, 1, 2])
```

### Output

```text
6
```

These examples demonstrate indexing across 1-D, 2-D and 3-D arrays.

---

## ✂️ Array Slicing

Slicing allows you to select a range of elements from an array.

```python
arr = np.array([1, 2, 3, 4, 5, 8, 9])

print(arr[1:5])
```

### Output

```text
[2 3 4 5]
```

You can also use a step:

```python
print(arr[::2])
```

### Output

```text
[1 3 5 9]
```

### Slicing a 2-D Array

```python
a = np.array([[10, 20, 30, 40, 50],
              [60, 70, 80, 90, 100]])

print(a[1, 1:4])
```

### Output

```text
[70 80 90]
```

The notebook demonstrates slicing in both 1-D and 2-D arrays.

---

## 🧬 Data Type of an Array

The `dtype` attribute is used to check the data type of an array.

```python
arr = np.array([1, 2, 3, 4])

print(arr.dtype)
```

You can also create an array with a specific data type:

```python
arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)
```

The lecture also demonstrates string data types and byte-string data types.

---

## 📐 Array Shape

The **shape** of an array represents the number of elements in each dimension.

```python
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

print(arr.shape)
```

### Output

```text
(2, 4)
```

For a 3-D array:

```python
arr = np.array([[[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [1, 2, 3, 4]]])

print(arr.shape)
```

### Output

```text
(1, 3, 4)
```

---

## 🔗 Joining NumPy Arrays

The `concatenate()` function is used to join arrays.

### 1-D Arrays

```python
arr1 = np.array([1, 2, 3, 7])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
```

### Output

```text
[1 2 3 7 4 5 6]
```

### 2-D Arrays

Arrays can also be joined using an axis:

```python
arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 7],
                 [8, 9]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
```

Using `axis=0` joins the arrays along the rows.

---

## ✂️ Splitting NumPy Arrays

The `array_split()` function divides an array into multiple parts.

### Split into 3 Parts

```python
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
```

### Output

```text
[array([1, 2]), array([3, 4]), array([5, 6])]
```

### Split into 4 Parts

```python
newarr = np.array_split(arr, 4)

print(newarr)
```

This can produce parts of unequal size when the array cannot be divided equally.

---

## 🔄 Ravel & Flatten

`ravel()` and `flatten()` can be used to convert a multidimensional array into a **1-D array**.

### Using `ravel()`

```python
m = np.array([[[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]])

n = m.ravel()

print(n)
print(n.ndim)
```

### Output

```text
[1 2 3 4 5 6 7 8 9]
1
```

### Using `flatten()`

```python
n = m.flatten()

print(n)
print(n.ndim)
```

Both are demonstrated in the lecture for converting multidimensional data into a 1-D array.

---

## 🧹 Unique Function

The `np.unique()` function is used to find the **unique values** in an array.

```python
k = np.array([1, 2, 5, 4, 7, 8, 2, 3, 45, 5, 60, 9, 8, 7, 6])

x = np.unique(k)

print(x)
```

### Output

```text
[ 1  2  3  4  5  6  7  8  9 45 60]
```

You can also obtain the first indexes and occurrence counts:

```python
unique_values, indices, counts = np.unique(
    k,
    return_index=True,
    return_counts=True
)

print("Unique values:", unique_values)
print("First indices:", indices)
print("Counts:", counts)
```

The notebook specifically demonstrates `return_index=True` and `return_counts=True`.

---

## 🗑️ Delete Elements

The `np.delete()` function can be used to remove elements from an array.

```python
a = np.array([12, 13, 14, 15])

d = np.delete(a, [1])

print(d)
```

### Output

```text
[12 14 15]
```

For a 2-D array, an axis can also be specified:

```python
x = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])

m = np.delete(x, 1, axis=0)

print(m)
```

This removes the row at index `1`.

---

## 💡 Why This Matters

This lecture builds the foundation for working with **numerical and multidimensional data in Python**.

✔ Organize data using arrays
✔ Work with multiple dimensions
✔ Access specific elements efficiently
✔ Select data using slicing
✔ Understand array shape and data types
✔ Combine and split arrays
✔ Convert multidimensional arrays into 1-D
✔ Find unique values and their counts
✔ Delete unwanted array elements

---

## 🎯 Outcome

By the end of this lecture, you will:

* Create NumPy arrays
* Understand 0-D, 1-D, 2-D, 3-D and higher-dimensional arrays
* Access elements using indexing
* Extract data using slicing
* Check dimensions using `ndim`
* Check structure using `shape`
* Check data types using `dtype`
* Join and split arrays
* Use `ravel()` and `flatten()`
* Find unique values using `np.unique()`
* Delete elements using `np.delete()`
* Be ready to work with numerical data using NumPy

---

<p align="center">
  <b>🚀 Master arrays, and you unlock the power of numerical computing in Python.</b>
</p>
