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
* Adding titles and labels
* Customizing graphs
* Understanding `figure()` and `show()`

---

## 🖼️ Visual Understanding

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_pyplot_001.png" width="600">
</p>

<p align="center">
  <i>📊 Data → Matplotlib → Visualization → Better Understanding</i>
</p>

---

## 🧪 Code Example

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.title("Simple Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
```

---

## 📈 Common Matplotlib Charts

### 1️⃣ Line Plot

Used to show **trends and changes over time**.

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 200]

plt.plot(months, sales)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
```

---

### 2️⃣ Bar Chart

Used to **compare different categories**.

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

---

### 3️⃣ Scatter Plot

Used to identify **relationships and patterns between two variables**.

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

---

## 🔧 Important Matplotlib Functions

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

---

## 💡 Why This Matters

Data is much easier to understand when it is visualized.

✔ Convert raw data into meaningful graphs
✔ Identify trends and patterns
✔ Compare different categories
✔ Communicate data effectively
✔ Build a foundation for Data Science and Machine Learning

---

## 🎯 Outcome

By the end of this lecture, you will:

* Create basic visualizations using Matplotlib
* Understand line, bar, and scatter plots
* Add titles and axis labels
* Customize basic graphs
* Visualize real-world datasets
* Be ready for **Pandas Data Visualization and Data Analysis**

---

## 🚀 Mini Project

### 📊 Student Performance Visualization

Create a graph showing:

```python
students = ["Ali", "Ahmed", "Sara", "Hassan", "Ayesha"]
marks = [75, 82, 91, 68, 88]
```

Your task:

1. Create a bar chart
2. Add a title
3. Add X and Y labels
4. Display the graph
5. Identify the student with the highest marks

---

<p align="center">
  <b>🚀 Don't just look at data — visualize it, understand it, and make decisions from it.</b>
</p>
