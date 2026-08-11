# 📖 Lecture 15: Pandas in Python

<p align="center">
  <img src="https://pandas.pydata.org/static/img/pandas.svg" width="300">
</p>


---

## 🧠 Core Concept

**Pandas** is a Python library used for **working with and analyzing data**.

This lecture focuses on understanding **DataFrames, Series, CSV files, data selection, indexing, adding and removing data, and handling missing values**.

The main idea is to learn how structured data can be **loaded, inspected, modified, and organized** using Pandas.

---

## ⚡ What You Will Learn

* What is Pandas
* Importing Pandas
* Loading CSV data
* Creating and working with DataFrames
* Viewing the first and last rows
* Checking data types
* Describing numerical data
* Selecting columns
* Filtering columns based on data types
* Slicing rows and columns
* Adding new columns
* Inserting columns at a specific position
* Understanding Pandas Series
* Creating Series with indexes
* Concatenating Series
* Performing operations on Series
* Dropping columns
* Dropping rows
* Using `inplace=True`
* Setting an index
* Resetting an index
* Creating DataFrames from dictionaries
* Handling missing values using `dropna()`

---

## 🖼️ Visual Understanding

<p align="center">
  <img src="https://pandas.pydata.org/static/img/pandas_white.svg" width="300">
</p>

<p align="center">
  <i>💡 Pandas → Data → DataFrame / Series → Select → Modify → Analyze</i>
</p>

---

## 🧪 Code Example

```python
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

print(df.head())
```

Pandas can load structured CSV data directly into a **DataFrame**.

---

## 📊 DataFrame

A **DataFrame** is a two-dimensional Pandas data structure used to store data in **rows and columns**.

The lecture uses the Titanic dataset as an example:

```python
df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

print(df)
```

---

## 👀 Viewing Data

### First Rows

The `head()` function displays the first rows of the DataFrame.

```python
df.head()
```

You can also specify how many rows to display:

```python
df.head(20)
```

### Last Rows

The `tail()` function displays the last rows.

```python
df.tail()
```

You can specify the number of rows:

```python
df.tail(20)
```

---

## 🔎 Understanding Data

### Data Types

The `dtypes` attribute shows the data type of each column.

```python
df.dtypes
```

### Statistical Description

The `describe()` function provides descriptive statistics for numerical data.

```python
df.describe()
```

This helps in quickly understanding the numerical information contained in the dataset.

---

## 🎯 Selecting Columns

A single column can be selected using its column name:

```python
df['Name']
```

Multiple columns can be selected using a list:

```python
df[['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']]
```

You can also check all column names:

```python
df.columns
```

---

## 🧬 Filtering Columns by Data Type

Pandas allows columns to be selected based on their data types.

### Object Columns

```python
df.dtypes == 'object'
```

### Float Columns

```python
df.dtypes == 'float64'
```

The lecture also demonstrates selecting columns whose data type matches a particular type:

```python
df[df.dtypes[df.dtypes == 'float64'].index]
```

Similarly, integer columns can be selected:

```python
df[df.dtypes[df.dtypes == 'int64'].index]
```

---

## ✂️ Data Slicing

Pandas allows rows to be selected using slicing.

```python
df[['Ticket']][4:16]
```

You can also use a step:

```python
df[['Ticket']][4:16:2]
```

Multiple columns can also be sliced:

```python
df[['Ticket', 'Cabin']][4:17]
```

With a step:

```python
df[['Ticket', 'Cabin']][4:17:3]
```

---

## ➕ Adding a New Column

A new column can be added directly:

```python
df['new_col'] = 7
```

This creates a new column named `new_col` and assigns the value `7`.

---

## 📍 Inserting a Column

The `insert()` function allows a column to be added at a specific position.

```python
df.insert(
    loc=3,
    column='Food',
    value=0
)
```

Another example:

```python
df.insert(
    loc=6,
    column='eqipments',
    value='oxygen cylinder'
)
```

Here:

* `loc` → position of the column
* `column` → column name
* `value` → value stored in the column

---

## 📦 Pandas Series

A **Series** is a one-dimensional Pandas data structure.

A column selected from a DataFrame is also represented as a Series.

```python
a = df['Name'][0:9]

print(a)
print(type(a))
```

The lecture demonstrates creating a Series with custom indexes:

```python
m1 = pd.Series(
    [100, 200, 300, 400, 500],
    index=[1, 2, 3, 4, 5]
)

print(m1)
```

Another Series:

```python
m2 = pd.Series(
    [600, 700, 800, 900, 1000],
    index=[1, 2, 3, 4, 5]
)

print(m2)
```

---

## 🔗 Concatenating Series

Two Series can be combined using `pd.concat()`.

```python
m3 = pd.concat([m1, m2])

print(m3)
```

You can access a value using its index:

```python
print(m3[1])
```

---

## ➗ Operations on Series

Pandas Series support mathematical operations.

### Multiplication

```python
m1 * m2
```

### Addition

```python
m1 + m2
```

Because both Series use the same indexes, Pandas performs the operations based on their indexes.

---

## 🗑️ Dropping Columns

The `drop()` function can remove a column.

```python
df.drop("PassengerId", axis=1)
```

Here:

```text
axis=1 → column
axis=0 → row
```

To permanently apply the change to the DataFrame:

```python
df.drop(
    "PassengerId",
    axis=1,
    inplace=True
)
```

### `inplace=True`

`inplace=True` applies the modification directly to the existing DataFrame.

---

## 🗑️ Dropping Rows

Rows can also be removed using `drop()`.

```python
df.drop(3)
```

To permanently remove the row:

```python
df.drop(3, inplace=True)
```

---

## 🔑 Setting an Index

The `set_index()` function can make an existing column the DataFrame index.

```python
df.set_index("Name")
```

To apply it permanently:

```python
df.set_index("Name", inplace=True)
```

Now the `Name` column becomes the DataFrame's index.

---

## 🔄 Resetting the Index

The `reset_index()` function can restore the index back into the DataFrame.

```python
df.reset_index()
```

This is useful when you want to return from a custom index to the normal DataFrame indexing structure.

---

## 📚 Creating a DataFrame from a Dictionary

A DataFrame can also be created from a Python dictionary.

```python
d = {
    "key1": [1, 2, 3, 4, 5],
    "key2": [6, 7, 8, 9, 10],
    "key3": [11, 12, 13, 14, 15]
}

print(d)
```

Convert the dictionary into a DataFrame:

```python
df = pd.DataFrame(d)

print(df)
```

This creates columns from the dictionary keys and rows from the corresponding lists.

---

## 🧹 Handling Missing Values

Pandas provides `dropna()` to remove rows containing missing values.

```python
df.dropna()
```

To apply the change directly:

```python
df.dropna(inplace=True)
```

### Important

```text
dropna()              → returns a modified result
dropna(inplace=True)  → modifies the existing DataFrame
```

---

## 💡 Why This Matters

This lecture builds the foundation for **data analysis with Python**.

✔ Load real datasets
✔ Understand DataFrames and Series
✔ Inspect and analyze data
✔ Select required columns
✔ Slice rows and columns
✔ Add and insert new data
✔ Perform operations on Series
✔ Remove unwanted rows and columns
✔ Manage DataFrame indexes
✔ Create DataFrames from dictionaries
✔ Handle missing values

---

## 🎯 Outcome

By the end of this lecture, you will:

* Import and use Pandas
* Load CSV datasets
* Work with DataFrames
* Work with Pandas Series
* Inspect datasets using `head()`, `tail()` and `describe()`
* Check data types using `dtypes`
* Select and slice data
* Add and insert columns
* Create and combine Series
* Perform operations on Series
* Drop rows and columns
* Set and reset DataFrame indexes
* Create DataFrames from dictionaries
* Handle missing values using `dropna()`
* Be ready for practical data analysis tasks

---

<p align="center">
  <b>🚀 Turn raw data into meaningful information with Pandas.</b>
</p>
