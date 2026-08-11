# 📊 Lecture 11: Matplotlib in Python

<p align="center">
  <img src="https://img.shields.io/badge/Topic-Matplotlib-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Concept-Data%20Visualization-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Level-Beginner-success?style=for-the-badge">
</p>

---

## 🧠 Core Concept

**Matplotlib** is a powerful Python library used to create graphs, charts, and visualizations from data.

This lecture is not just about making graphs,
it’s about understanding **how data can be visually represented, analyzed, and communicated**.

---

## ⚡ What You Will Learn

* What is Matplotlib
* Why Matplotlib is used
* Installing and importing Matplotlib
* Creating basic plots
* Line charts
* Bar charts
* Scatter plots
* Histograms
* Adding titles and labels
* Customizing graphs
* Saving graphs

---

## 🖼️ Visual Understanding

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_pyplot_001.png" width="650">
</p>

<p align="center">
  <i>📊 Raw Data → Matplotlib → Visualization → Better Insights</i>
</p>

---

## 🧪 Getting Started

First, import Matplotlib:

```python
import matplotlib.pyplot as plt
```

If Matplotlib is not installed:

```bash
pip install matplotlib
```

---

# 📈 1. Line Plot

A **Line Plot** is used to show trends, changes, and patterns across values or time.

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_simple_plot_001.png" width="600">
</p>

### 🧪 Example

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 220]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
```

💡 **Use Case:**
Sales trends, temperature changes, stock prices, website traffic, and time-series data.

---

# 📊 2. Bar Chart

A **Bar Chart** is used to compare values between different categories.

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_barchart_001.png" width="600">
</p>

### 🧪 Example

```python
import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "ML", "Power BI"]
marks = [85, 78, 90, 88]

plt.bar(subjects, marks)

plt.title("Student Performance")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
```

💡 **Use Case:**
Comparing students, products, departments, sales categories, or performance.

---

# 🔵 3. Scatter Plot

A **Scatter Plot** displays individual data points and helps us understand the relationship between two numerical variables.

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_scatter_demo2_001.png" width="600">
</p>

### 🧪 Example

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [40, 45, 55, 65, 75, 85]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
```

💡 **Use Case:**
Finding relationships, correlations, patterns, and outliers in data.

---

# 📊 4. Histogram

A **Histogram** is used to understand the distribution of numerical data.

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_histogram_features_001.png" width="600">
</p>

### 🧪 Example

```python
import matplotlib.pyplot as plt

marks = [
    45, 50, 52, 55, 60,
    62, 65, 70, 72, 75,
    78, 80, 82, 85, 88,
    90, 92
]

plt.hist(marks, bins=5)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
```

💡 **Use Case:**
Understanding distributions, frequency, data spread, and unusual values.

---

# 🎨 5. Customizing a Plot

Matplotlib allows us to customize graphs using different properties.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(
    x,
    y,
    marker="o",
    linestyle="--",
    linewidth=2
)

plt.title("Customized Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.grid(True)

plt.show()
```

---

# 🧩 Important Matplotlib Functions

| Function        | Purpose             |
| --------------- | ------------------- |
| `plt.plot()`    | Create line plot    |
| `plt.bar()`     | Create bar chart    |
| `plt.scatter()` | Create scatter plot |
| `plt.hist()`    | Create histogram    |
| `plt.title()`   | Add graph title     |
| `plt.xlabel()`  | Label X-axis        |
| `plt.ylabel()`  | Label Y-axis        |
| `plt.legend()`  | Add legend          |
| `plt.grid()`    | Add grid            |
| `plt.show()`    | Display graph       |
| `plt.savefig()` | Save graph as image |

---

## 💡 Why This Matters

Data becomes much easier to understand when we visualize it.

✔ Convert raw data into meaningful graphs
✔ Identify trends and patterns
✔ Compare different categories
✔ Understand relationships between variables
✔ Detect unusual data points
✔ Communicate insights effectively

---

## 🎯 Outcome

By the end of this lecture, you will:

* Create basic visualizations using Matplotlib
* Understand line plots
* Create bar charts
* Create scatter plots
* Create histograms
* Add titles and axis labels
* Customize basic graphs
* Save visualizations
* Understand the fundamentals of data visualization




---

<p align="center">
  <b>🚀 Don't just look at data — visualize it, understand it, and make decisions from it.</b>
</p>
