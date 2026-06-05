# 🐍 Learning_Python

> Five practical Python projects showcasing OOP, data validation, and real-world applications. Build a budget tracker, email system, media library, data validator, and geometry calculator—all with zero dependencies. Perfect for learning core Python concepts and building your portfolio.

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Python 100%](https://img.shields.io/badge/Python-100%25-brightgreen?style=flat-square)](https://github.com/priyankardas2007/Learning_Python)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Projects](#-projects)
  - [BudgetApp](#1-budgetapp)
  - [EmailSimulator](#2-emailsimulator)
  - [MediaCatalogue](#3-mediacatalogue)
  - [MedicalDataValidator](#4-medicaldatavalidator)
  - [PolygonAreaCalculator](#5-polygonareaCalculator)
- [Installation](#-installation)
- [Key Concepts](#-key-concepts)
- [Learning Path](#-learning-path)
- [Contributing](#-contributing)

---

## 🎯 Overview

This repository contains **5 practical Python projects** that showcase different programming patterns and techniques. Each project is a standalone application demonstrating best practices in Python development.

✨ **Perfect for**:
- 🎓 Learning OOP principles
- 🔍 Understanding data validation
- 💡 Exploring real-world applications
- 📚 Building portfolio projects

---

## 📦 Projects

### 1. 💰 BudgetApp

A comprehensive budget management system that tracks income and expenses across different spending categories.

#### ✨ Features:
- 📂 **Category Management** - Create and organize spending categories
- 💳 **Transaction Tracking** - Record deposits and withdrawals with descriptions
- ✅ **Fund Checking** - Verify sufficient funds before transactions
- 🔄 **Money Transfers** - Transfer funds between categories seamlessly
- 💹 **Balance Calculation** - Get real-time balance for each category
- 📊 **Visual Charts** - Generate spending distribution charts

#### 🔧 Key Classes:
- `Category` - Manages individual budget categories with ledger
- `create_spend_chart()` - Generates visual bar charts

#### 💻 Example Usage:
```python
food = Category("Food")
food.deposit(1000, "Salary")
food.withdraw(50, "Groceries")
print(food)  # Displays formatted ledger
```

---

### 2. 📧 EmailSimulator

A complete email management system simulating real-world email client functionality.

#### ✨ Features:
- ✉️ **Email Creation** - Send emails with sender, receiver, subject, and body
- ⏰ **Automatic Timestamps** - Track when emails were sent
- 📖 **Read/Unread Status** - Mark emails as read or unread
- 👤 **User Accounts** - Create accounts with personal inboxes
- 📬 **Email Operations**:
  - Send emails between users
  - View inbox with summaries
  - Read full email content
  - Delete emails
- 🎨 **Formatted Display** - Beautiful email presentation

#### 🔧 Key Classes:
- `Email` - Represents individual email messages
- `Inbox` - Manages email collections
- `User` - User accounts with email capabilities

#### 💻 Example Usage:
```python
alice = User("Alice")
bob = User("Bob")
alice.send_email(bob, "Hello", "Hi Bob! 👋")
bob.check_inbox()
bob.read_email(1)
```

---

### 3. 🎬 MediaCatalogue

A media library management system with support for movies and TV series with comprehensive validation.

#### ✨ Features:
- 🎥 **Movie Management** - Store and organize movie information
- 📺 **TV Series Support** - Track seasons and episodes
- ✔️ **Data Validation** - Comprehensive input validation
- ⚠️ **Custom Exceptions** - `MediaError` for error handling
- 🔍 **Smart Filtering** - Separate movies from TV series
- 📋 **Organized Display** - Beautiful formatted output

#### 🔧 Key Classes:
- `Movie` - Movie representation (title, year, director, duration)
- `TVSeries` - Extends Movie (adds seasons, episodes)
- `MediaCatalogue` - Container for media items
- `MediaError` - Custom exception class

#### ✅ Validation Rules:
| Field | Rule |
|-------|------|
| Title | Cannot be empty |
| Year | Must be 1895+ |
| Director | Cannot be empty |
| Duration | Must be positive |
| Seasons | Must be ≥ 1 |
| Episodes | Must be ≥ 1 |

#### 💻 Example Usage:
```python
catalogue = MediaCatalogue()
movie = Movie("Inception", 2010, "Christopher Nolan", 148)
series = TVSeries("Breaking Bad", 2008, "Vince Gilligan", 47, 5, 62)
catalogue.add(movie)
catalogue.add(series)
print(catalogue)
```

---

### 4. 🏥 MedicalDataValidator

A robust validation system for medical records with strict format checking and error reporting.

#### ✨ Features:
- 📋 **Comprehensive Validation** - Check format and content
- 🔤 **Regex Pattern Matching** - Advanced pattern validation
- 🎯 **Type Checking** - Ensure correct data types
- ⚙️ **Constraint Validation** - Complex validation rules
- 🚨 **Detailed Error Reports** - Specific error messages
- 📦 **Batch Processing** - Validate multiple records

#### ✅ Validation Rules:
| Field | Pattern/Rule |
|-------|--------------|
| patient_id | `P####` or `p####` |
| age | Integer ≥ 18 |
| gender | "male" or "female" |
| diagnosis | String or None |
| medications | List of strings |
| last_visit_id | `V####` or `v####` |

#### 🔧 Key Functions:
- `find_invalid_records()` - Identify validation failures
- `validate()` - Validate entire dataset

#### 💻 Example Usage:
```python
records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    }
]
validate(records)  # Returns: True/False with error messages
```

---

### 5. 📐 PolygonAreaCalculator

A geometry calculator for rectangles and squares with comprehensive shape operations.

#### ✨ Features:
- 📏 **Area Calculation** - Calculate shape areas
- 📐 **Perimeter Calculation** - Get perimeter measurements
- 🔗 **Diagonal Calculation** - Compute diagonal using Pythagorean theorem
- 🎨 **ASCII Visualization** - Generate shape pictures
- 📦 **Shape Fitting** - Calculate how many shapes fit inside another
- 🔧 **Dynamic Properties** - Modify dimensions anytime

#### 🔧 Key Classes:
- `Rectangle` - Rectangle operations
  - `get_area()` - Calculate area
  - `get_perimeter()` - Calculate perimeter
  - `get_diagonal()` - Calculate diagonal
  - `get_picture()` - ASCII art representation
  - `get_amount_inside()` - Shape fitting calculation

- `Square` - Extends Rectangle
  - `set_side()` - Set all dimensions uniformly
  - Inherits all Rectangle methods

#### 💻 Example Usage:
```python
rect = Rectangle(10, 5)
print(rect.get_area())      # Output: 50
print(rect.get_picture())   # Display ASCII art

square = Square(8)
print(square.get_perimeter())  # Output: 32
```

---

## 🚀 Installation

### Prerequisites:
- ✅ Python 3.x installed
- ✅ Git (optional, for cloning)
- ✅ Text editor or IDE

### Setup Steps:

1️⃣ **Clone the repository**:
```bash
git clone https://github.com/priyankardas2007/Learning_Python.git
cd Learning_Python
```

2️⃣ **Run individual projects**:
```bash
# Budget Application
python BudgetApp.py

# Email Simulator
python EmailSimulator.py

# Media Catalogue
python MediaCatalogue.py

# Medical Data Validator
python MedicalDataValidator.py

# Polygon Area Calculator
python PolgonAreaCalculator.py
```

3️⃣ **No external dependencies required!** 🎉
All projects use Python's standard library only.

---

## 🧠 Key Concepts

### 🎯 Object-Oriented Programming (OOP)
- ✅ Class definition and instantiation
- ✅ Inheritance (`TVSeries` → `Movie`, `Square` → `Rectangle`)
- ✅ Encapsulation and data hiding
- ✅ Special methods (`__init__`, `__str__`)

### 🔍 Data Validation
- ✅ Type checking
- ✅ Constraint validation
- ✅ Regular expression pattern matching
- ✅ Custom exception handling

### 📚 Data Structures
- ✅ Lists and dictionaries
- ✅ Object composition
- ✅ Container classes

### 🔧 Functional Programming
- ✅ List comprehensions
- ✅ Lambda functions
- ✅ Higher-order functions

### 🎨 String Formatting
- ✅ f-strings
- ✅ String alignment and padding
- ✅ Multi-line construction

---

## 📚 Learning Path

Recommended order to explore these projects:

| Order | Project | Focus | Duration |
|-------|---------|-------|----------|
| 1️⃣ | PolygonAreaCalculator | Basic OOP & Inheritance | 30 mins |
| 2️⃣ | MediaCatalogue | Custom Exceptions & Validation | 45 mins |
| 3️⃣ | MedicalDataValidator | Data Validation Patterns | 45 mins |
| 4️⃣ | BudgetApp | Complex Data Structures | 60 mins |
| 5️⃣ | EmailSimulator | Real-World Application | 60 mins |

---

## 🛠️ Technologies Used

```
┌─────────────────────────────────────┐
│     Languages & Libraries           │
├─────────────────────────────────────┤
│ • Python 3.x (100%)                 │
│ • re (Regular Expressions)          │
│ • datetime (Date/Time)              │
│ • math (Mathematical Operations)    │
└─────────────────────────────────────┘
```

---

## 🤝 Contributing

We ❤️ contributions! Here's how to help:

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit** changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push** to the branch (`git push origin feature/AmazingFeature`)
5. 🔃 **Open** a Pull Request

### 📋 Guidelines:
- ✅ Write clean, documented code
- ✅ Follow PEP 8 style guide
- ✅ Add comments for complex logic
- ✅ Test your changes thoroughly

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 priyankardas2007

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👨‍💻 Author

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/priyankardas2007">
        <img src="https://avatars.githubusercontent.com/u/224995386?v=4" width="100px;" alt="priyankardas2007"/>
        <br />
        <sub><b>priyankardas2007</b></sub>
      </a>
      <br />
      <a href="https://github.com/priyankardas2007">@priyankardas2007</a>
    </td>
  </tr>
</table>

---

## ⭐ Show Your Support

If you found this repository helpful, please consider:
- ⭐ **Giving it a star!**
- 🐦 **Sharing with friends**
- 💬 **Providing feedback**
- 🔗 **Referencing in your projects**

---

## 📞 Questions & Support

- 💭 Have a question? [Open an Issue](https://github.com/priyankardas2007/Learning_Python/issues)
- 🐛 Found a bug? [Report it](https://github.com/priyankardas2007/Learning_Python/issues)
- 💡 Have suggestions? [Start a Discussion](https://github.com/priyankardas2007/Learning_Python/discussions)

---

## 🎓 Learning Resources

Helpful resources to complement these projects:

- 📖 [Python Official Docs](https://docs.python.org/3/)
- 🎬 [Real Python Tutorials](https://realpython.com/)
- 📚 [Python PEP 8 Style Guide](https://pep8.org/)
- 🔗 [GitHub Learning Lab](https://github.blog/2020-03-06-how-github-learning-lab-works/)

---

<div align="center">

### 🌟 Happy Learning! 🌟

Made with ❤️ by [priyankardas2007](https://github.com/priyankardas2007)

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)

</div>
