# 📊 Matplotlib

<p align="center">
  <strong>Powerful, Flexible, and Customizable Data Visualization in Python</strong>
</p>

<p align="center">
  <img src="https://matplotlib.org/stable/_images/sphx_glr_logos2_001_2_00x.png" alt="Matplotlib Logo" width="350">
</p>

<p align="center">
  <a href="https://matplotlib.org/">Documentation</a> •
  <a href="https://github.com/matplotlib/matplotlib">GitHub</a> •
  <a href="https://matplotlib.org/stable/gallery/index.html">Examples</a>
</p>

---

## 📌 About

**Matplotlib** is one of the most widely used Python libraries for creating static, animated, and interactive visualizations.

It provides a powerful API for transforming data into meaningful charts and graphs, making it an essential tool for **Data Science, Machine Learning, Scientific Computing, Statistics, and Data Analysis**.

From simple line charts to complex scientific visualizations, Matplotlib gives you detailed control over almost every aspect of a figure.

---

## ✨ Why Matplotlib?

Matplotlib is useful because it allows you to:

* 📈 Visualize trends and patterns
* 📊 Create professional statistical charts
* 🔍 Explore datasets visually
* 🧠 Understand machine-learning results
* 📉 Analyze distributions and relationships
* 🎨 Customize colors, labels, fonts, and layouts
* 💾 Save visualizations in multiple formats
* 🔬 Create publication-quality scientific figures

---

## 🚀 Features

| Feature          | Description                                 |
| ---------------- | ------------------------------------------- |
| 📈 Line Plot     | Visualize trends over time                  |
| 📊 Bar Chart     | Compare categories                          |
| 🥧 Pie Chart     | Show proportions                            |
| 🔵 Scatter Plot  | Analyze relationships                       |
| 📦 Box Plot      | Understand distributions and outliers       |
| 📉 Histogram     | Analyze frequency distributions             |
| 🗺️ Subplots     | Display multiple charts together            |
| 🎨 Customization | Control colors, styles, labels, and layouts |
| 💾 Export        | Save figures as PNG, JPG, SVG, PDF, etc.    |
| 🎬 Animation     | Create animated visualizations              |

---

## 🛠️ Installation

Install Matplotlib using `pip`:

```bash
pip install matplotlib
```

Or install it using Conda:

```bash
conda install matplotlib
```

Verify the installation:

```bash
python -c "import matplotlib; print(matplotlib.__version__)"
```

---

# 🧑‍💻 Quick Start

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("Simple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
```

### Output

This creates a simple line chart showing the relationship between `x` and `y`.

---

# 📈 Common Visualizations

## 1. Line Plot

Useful for showing trends.

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 170, 220]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
```

---

## 2. Bar Chart

Useful for comparing categories.

```python
import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Monitor"]
sales = [50, 90, 40, 65]

plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Units Sold")

plt.show()
```

---

## 3. Scatter Plot

Useful for finding relationships between variables.

```python
import matplotlib.pyplot as plt

height = [150, 160, 165, 170, 175, 180]
weight = [50, 55, 60, 65, 70, 78]

plt.scatter(height, weight)

plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")

plt.show()
```

---

## 4. Histogram

Useful for understanding data distributions.

```python
import matplotlib.pyplot as plt

ages = [18, 20, 21, 22, 22, 23, 24, 25, 25, 26, 28, 30]

plt.hist(ages, bins=5)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()
```

---

## 5. Pie Chart

Useful for displaying proportions.

```python
import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "JavaScript"]
values = [40, 25, 20, 15]

plt.pie(values, labels=labels, autopct="%1.1f%%")

plt.title("Programming Language Usage")

plt.show()
```

---

# 🎨 Customizing Plots

Matplotlib provides extensive customization options.

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

plt.title("Customized Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)

plt.show()
```

You can customize:

* Titles
* Axis labels
* Legends
* Grid lines
* Markers
* Line styles
* Figure size
* Fonts
* Tick labels
* Annotations
* Subplots

---

# 🧩 Subplots

Multiple visualizations can be placed inside one figure.

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot([1, 2, 3], [2, 4, 6])
axes[0].set_title("Line Plot")

axes[1].bar(["A", "B", "C"], [10, 20, 15])
axes[1].set_title("Bar Chart")

plt.tight_layout()
plt.show()
```

---

# 💾 Saving Figures

You can save visualizations instead of only displaying them.

```python
plt.savefig("sales_chart.png", dpi=300, bbox_inches="tight")
```

Matplotlib supports formats such as:

* PNG
* JPG
* SVG
* PDF
* EPS

---

# 🧠 Matplotlib in Data Science

Matplotlib is commonly used throughout a Data Science workflow:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Visualization
   ↓
Feature Engineering
   ↓
Machine Learning
   ↓
Model Evaluation
   ↓
Visualization of Results
```

It works especially well with:

* 🐼 Pandas
* 🔢 NumPy
* 🤖 Scikit-learn
* 📊 Seaborn
* 📓 Jupyter Notebook

---

# 📚 Learning Path

A practical learning path for Matplotlib:

### Beginner

* `plt.plot()`
* `plt.bar()`
* `plt.scatter()`
* `plt.hist()`
* `plt.pie()`
* Titles and labels
* Legends
* Grid

### Intermediate

* Figure and Axes
* Subplots
* Customization
* Annotations
* Tick formatting
* Multiple datasets
* Saving figures

### Advanced

* Object-oriented API
* Advanced layouts
* Custom projections
* Animations
* Interactive figures
* Publication-quality visualization
* Integration with scientific and ML workflows

---

# 📁 Recommended Project Structure

```text
matplotlib-project/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── visualization.ipynb
│
├── src/
│   └── visualization.py
│
├── outputs/
│   └── charts/
│
└── .gitignore
```

---

# 📦 Requirements

Example `requirements.txt`:

```text
matplotlib
numpy
pandas
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🌟 Best Practices

When creating visualizations:

1. **Choose the right chart for the question.**
2. Keep charts simple and readable.
3. Always label important axes.
4. Use meaningful titles.
5. Avoid unnecessary visual clutter.
6. Choose appropriate scales.
7. Highlight important insights.
8. Use legends when multiple datasets are shown.
9. Save important figures at high resolution.
10. Focus on communicating the data, not decorating the chart.

---

# 🔗 Resources

* 📖 [Official Documentation](https://matplotlib.org/stable/)
* 🎨 [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
* 💻 [GitHub Repository](https://github.com/matplotlib/matplotlib)
* 📚 [Pyplot Tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

---

# 🤝 Contributing

Contributions are welcome!

If you find a bug or have an idea for improvement:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Commit your work.
6. Open a Pull Request.

```bash
git checkout -b feature/my-feature
git add .
git commit -m "Add new visualization feature"
git push origin feature/my-feature
```

---

# 📄 License

Matplotlib is distributed under the **Matplotlib license**, based on the permissive PSF-style license.

For complete licensing information, refer to the project's official repository.

---

## ⭐ Support

If you find Matplotlib useful, consider giving the project a ⭐ on GitHub and exploring its extensive visualization gallery.

---

<p align="center">
  <strong>Turn Data Into Insight. 📊</strong>
</p>

<p align="center">
  Made with Python 🐍 and Matplotlib 📈
</p>
