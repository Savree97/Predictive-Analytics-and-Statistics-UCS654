# TOPSIS Multi-Criteria Decision Analysis  
### UCS654 – Predictive Analytics & Statistics  
**Version: 0.0.3**

---

## 📌 Project Overview

This repository contains three complete implementations of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** algorithm:

TOPSIS is a multi-criteria decision-making technique that ranks alternatives based on their distance from the ideal best and ideal worst solutions.

This project includes:

| Program | Description |
|---------|------------|
| Program 1 | Command-line Python implementation |
| Program 2 | Published PyPI package (`topsis-savree-102317097`) |
| Program 3 | Flask-based Web Application |

---

# 🚀 Program 1: Command-Line Implementation

Standalone Python script to perform TOPSIS analysis.

### ▶️ Usage

```bash
python 102317097.py input.csv "1,1,1,1" "+,+,-,+" result.csv
```

### 📥 Input Requirements
- First column: Names / Alternatives
- Remaining columns: Numeric criteria values
- Weights: Comma-separated numbers
- Impacts: Comma-separated (+ for benefit, - for cost)

### 📤 Output
Generates a CSV file with:
- Topsis Score
- Rank

---

# 📦 Program 2: PyPI Package (Version 0.0.3)

Published package:  
👉 https://pypi.org/project/Topsis-Savree-102317097/

### 📥 Install

```bash
pip install topsis-savree-102317097==0.0.3
```

### ▶️ Usage

```bash
topsis input.csv "1,1,1,1" "+,+,-,+" result.csv
```

---

# 🌐 Program 3: Web Application

A Flask-based web interface to perform TOPSIS analysis through a browser.

## ⚙️ Dependencies

Install required libraries before running:

```bash
pip install numpy pandas flask topsis-savree-102317097==0.0.3
```

Recommended Python version:
```
Python 3.8+
```

---

## ▶️ Run the Web App

Navigate to the WebApp folder:

```bash
cd "Program III- WebApp"
```

Run:

```bash
python app1.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# 📊 Input Format

## Example CSV File

| Model | Price | Storage | Camera | Looks |
|-------|-------|---------|--------|-------|
| M1 | 250 | 16 | 12 | 5 |
| M2 | 200 | 16 | 8 | 3 |

### Weights:
```
1,2,1,1
```

### Impacts:
```
+,+,-,+
```

---

# 🗂 Repository Structure

```
TOPSIS-Assignment/
│
├── Program1/
│   ├── 102317097.py
│   ├── 102317097-data.csv
│   └── 102317097-result.csv
│
├── Program2/
│   ├── topsis_savree_102317097/
│   ├── setup.py
│   └── README.md
│
├── Program III- WebApp/
│   ├── app1.py
│   ├── templates/
│   │   └── index.html
│   └── uploads/
│
└── README.md
```

---

# ✨ Features

✔ Multi-criteria decision ranking  
✔ CLI implementation  
✔ Published PyPI package  
✔ Web-based interface  
✔ Automatic result generation  
✔ Clean modular structure  

---

# 👤 Author

**Savree Dohar**  
Roll Number: 102317097  
B.Tech CSE – Thapar Institute of Engineering and Technology  

PyPI Package:  
https://pypi.org/project/Topsis-Savree-102317097/

---

⭐ If you found this useful, consider starring the repository!
