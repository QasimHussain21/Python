# 📖 Lecture 4: Built-in Functions

<p align="center">
  <img src="https://img.shields.io/badge/Topic-Built--in_Functions-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Focus-Code_Efficiency-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Level-Beginner-success?style=for-the-badge">
</p>

---

## 🧠 Core Concept

Built-in functions are **predefined functions provided by Python**.

They help you perform tasks quickly **without writing complex code from scratch**.

---

## ⚡ What You Will Learn

- Using common built-in functions  
- Improving code efficiency  
- Writing cleaner programs  

---

## 🔑 Common Built-in Functions

### 🔢 Input / Output
- `print()` → Displays output  
- `input()` → Takes user input  

---

### 🔍 Type & Conversion
- `type()` → Shows data type  
- `int()` → Convert to integer  
- `float()` → Convert to float  
- `str()` → Convert to string  

---

### 📊 Mathematical Functions
- `abs()` → Absolute value  
- `round()` → Round value  
- `max()` → Maximum value  
- `min()` → Minimum value  

---

### 📏 Length & Range
- `len()` → Length of object  
- `range()` → Generate sequence  

---

## 🧪 Code Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name)
print("Your age is", age)

print(len(name))
print(max(10, 20, 30))