# 📖 Lecture 13: Object-Oriented Programming in Python

<p align="center">
  <img src="https://img.shields.io/badge/Topic-OOP%20in%20Python-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Concept-Classes%20%26%20Objects-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/Level-Beginner-success?style=for-the-badge">
</p>

<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="300">
</p>

<p align="center">
  <i>🐍 Building programs around objects, classes, and reusable behavior</i>
</p>

---

## 🧠 Core Concept

**Object-Oriented Programming (OOP)** is a programming approach that organizes programs around **classes and objects**.

This lecture introduces the basic OOP idea in Python, including **classes, objects, `self`, `__init__()`, and major OOP concepts such as inheritance, polymorphism, encapsulation, and abstraction**.

Python supports multiple programming paradigms, including **object-oriented, procedural, and functional programming**.

---

## ⚡ What You Will Learn

- What is Object-Oriented Programming
- Programming paradigms
- Procedural Programming
- Functional Programming
- Imperative and Declarative approaches
- Difference between Procedural Programming and OOP
- What is a Class
- What is an Object
- Creating classes in Python
- Creating objects from classes
- Understanding `self`
- Understanding `__init__()`
- Basic class methods
- Introduction to Inheritance
- Introduction to Polymorphism
- Introduction to Encapsulation
- Introduction to Abstraction

---

## 🖼️ Visual Understanding

<p align="center">
  <img src="https://miro.medium.com/v2/resize%3Afit%3A697/1%2Aq0Tw3AvDkXhS_Ot3Y5_fxw.png" width="650">
</p>

<p align="center">
  <i>💡 OOP → Class + Object + Inheritance + Encapsulation + Polymorphism + Abstraction</i>
</p>

---

## 🧩 Programming Paradigms

A **programming paradigm** is a style or approach used to structure and solve programming problems.

The lecture introduces:

### 🔹 Procedural Programming

Programs are organized around **procedures/functions** that perform operations on data.

### 🔹 Object-Oriented Programming

Programs are organized around **objects** that combine data and behavior.

### 🔹 Functional Programming

Programs are structured around **functions** and the transformation of data.

---

## ⚖️ Imperative vs Declarative

### Imperative Programming

Focuses on **how** a task should be performed.

```python
numbers = [1, 2, 3, 4, 5]

total = 0

for number in numbers:
    total += number

print(total)
```

### Declarative Programming

Focuses more on **what result is required** rather than describing every step.

The lecture introduces this distinction as part of programming paradigms.

---

## 🔄 Procedural Programming vs OOP

| Procedural Programming | Object-Oriented Programming |
|---|---|
| Organized around procedures/functions | Organized around classes and objects |
| Data and functions are generally treated separately | Data and behavior can be bundled together |
| Suitable for smaller/simple programs | Useful for organizing larger systems |
| Focuses on procedures | Focuses on objects |

---

## 🏗️ What is a Class?

A **class** is a blueprint used to create objects.

A class can define:

- Attributes
- Methods
- Object behavior

### Basic Example

```python
class Student:
    pass
```

Here, `Student` is a class.

<p align="center">
  <img src="https://miro.medium.com/v2/resize%3Afit%3A750/0%2AJQyADOVh5lH7_8N3.png" width="600">
</p>

---

## 👤 What is an Object?

An **object** is an instance created from a class.

```python
class Student:
    pass

student1 = Student()

print(student1)
```

Here:

```text
Student  → Class
student1 → Object
```

The class provides the structure, while the object is an actual instance of that class.

---

## 🧪 Creating a Class and Object

```python
class Student:

    def display(self):
        print("This is a student object")


student1 = Student()

student1.display()
```

### Output

```text
This is a student object
```

The method is defined inside the class and called using the object.

---

## 👤 Understanding `self`

In Python, `self` represents the **current object/instance** inside an instance method.

```python
class Student:

    def display(self):
        print("Hello Student")


student1 = Student()
student1.display()
```

The `self` parameter allows the method to work with the current instance.

<p align="center">
  <img src="https://media.licdn.com/dms/image/sync/v2/D5627AQFRnW-7ErPPNA/articleshare-shrink_800/B56Zm1KRNNHkAI-/0/1759680997217?e=2147483647&t=ph4K7KLyj6Urh87Zjp6g63BYbsI8Kdi8k4lQzl0WwRM&v=beta" width="650">
</p>

---

## ⚙️ The `__init__()` Function

The `__init__()` method is commonly used to initialize an object's attributes when an object is created.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Ali", 21)

print(student1.name)
print(student1.age)
```

### Output

```text
Ali
21
```

### Understanding the Code

```text
__init__() → initializes object data
self.name  → stores the student's name
self.age   → stores the student's age
```

---

## 🧱 Class → Object Relationship

The basic OOP relationship can be visualized as:

```text
             CLASS
               │
               │ creates
               ▼
            OBJECT
               │
        ┌──────┴──────┐
        ▼             ▼
    Attributes      Methods
```

A class acts as a blueprint, while objects are instances created from that blueprint.

---

## 🧬 Inheritance

**Inheritance** allows a class to derive features from another class.

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    pass


dog = Dog()
dog.sound()
```

### Output

```text
Animal makes a sound
```

Here:

```text
Animal → Parent/Base Class
Dog    → Child/Derived Class
```

Python classes support inheritance, including multiple inheritance. citeturn0search0

---

## 🔁 Polymorphism

**Polymorphism** means that the same interface or method name can be associated with different behaviors.

Conceptually:

```text
Same operation
      ↓
Different objects
      ↓
Different behavior
```

Example:

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

### Output

```text
Bark
Meow
```

---

## 🔒 Encapsulation

**Encapsulation** refers to keeping data and the operations that work with that data together inside a class.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student = Student("Ali")
student.display()
```

The class groups the student's data and related behavior together.

---

## 🎯 Abstraction

**Abstraction** focuses on exposing the important interface while hiding unnecessary implementation details.

A simple conceptual example:

```text
User
  │
  ▼
Simple Interface
  │
  ▼
Complex Internal Implementation
```

Python also provides infrastructure for abstract base classes through the `abc` module. citeturn0search6

---

## 🧠 The Main OOP Concepts

<p align="center">
  <img src="https://cs-prod-assets-bucket.s3.ap-south-1.amazonaws.com/Four_pillars_of_OOP_de774cc4e8.webp" width="700">
</p>

| Concept | Basic Idea |
|---|---|
| 🏗️ Class | Blueprint for creating objects |
| 👤 Object | Instance of a class |
| 🧬 Inheritance | Deriving a class from another class |
| 🔁 Polymorphism | Different behavior through a common interface |
| 🔒 Encapsulation | Bundling data and related behavior |
| 🎯 Abstraction | Focusing on essential features |

---

## 🧪 Complete Mini Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Ali", 21)

student1.display()
```

### Output

```text
Name: Ali
Age: 21
```

This small example combines the core ideas of:

```text
Class
  ↓
Object
  ↓
__init__()
  ↓
self
  ↓
Attributes + Methods
```

---

## 🌍 Real-World Understanding

OOP can be understood using real-world entities.

For example, a **Student** can be represented as:

```text
              STUDENT
                 │
       ┌─────────┴─────────┐
       │                   │
   Attributes            Methods
       │                   │
   ┌───┴────┐          ┌───┴────┐
   │        │          │        │
 Name      Age       Study    Display
```

This way of thinking helps convert real-world entities into program structures.

---

## 📚 Quick Revision

```text
OOP
│
├── Class
│   └── Blueprint
│
├── Object
│   └── Instance of Class
│
├── self
│   └── Current Instance
│
├── __init__()
│   └── Initialize Object Data
│
├── Inheritance
│   └── Reuse/derive from another class
│
├── Polymorphism
│   └── Different behaviors
│
├── Encapsulation
│   └── Bundle data + behavior
│
└── Abstraction
    └── Focus on essential features
```

---

## 💡 Why This Matters

OOP provides a structured way to organize programs around **objects and classes**.

✔ Organize related data and behavior  
✔ Represent real-world entities in code  
✔ Create reusable class structures  
✔ Understand inheritance  
✔ Build a foundation for advanced Python programming  
✔ Prepare for larger software projects  

Python's official documentation describes classes as a way to bundle data and functionality together and supports inheritance through its class mechanism. citeturn0search0

---

## 🎯 Outcome

By the end of this lecture, you will:

- Understand Object-Oriented Programming
- Identify major programming paradigms
- Understand procedural vs OOP approaches
- Create basic Python classes
- Create objects from classes
- Understand `self`
- Use `__init__()` to initialize object data
- Understand the basic idea of inheritance
- Understand polymorphism
- Understand encapsulation
- Understand abstraction
- Be ready for more advanced OOP concepts

---

## 🖼️ More Visual Learning

<p align="center">
  <img src="https://miro.medium.com/1%2A_s3K27a_Fz9Wk0-9O-0cFw.png" width="500">
</p>

<p align="center">
  <img src="https://cdn.sanity.io/images/2bvrjzxq/production/a75dd9b8714af01ab0fc5cd99e5f3aa217f092f9-2912x1472.png" width="700">
</p>

<p align="center">
  <i>🧠 Class → Object → Inheritance → Encapsulation → Polymorphism → Abstraction</i>
</p>

---

## 📌 Important Note

The lecture introduces these OOP concepts at a foundational level. The purpose is to understand the **basic structure and terminology of OOP in Python** before moving toward more advanced concepts.

For Python's class and inheritance behavior, the official Python documentation is a useful reference.

---

<p align="center">
  <b>🚀 Think in objects. Build with classes. Program smarter with OOP.</b>
</p>
