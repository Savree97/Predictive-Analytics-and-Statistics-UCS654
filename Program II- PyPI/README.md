# Topsis-Savree-102317097

A lightweight Python implementation of the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method for multi-criteria decision analysis.

This package allows users to rank alternatives based on weighted criteria using distance-based evaluation from ideal best and worst solutions.

---

## Why Use This Package?

- Simple command-line interface
- Easy Python integration
- Automatic validation of inputs
- Clean output with score and rank
- Suitable for academic and decision-analysis problems

---

## Installation

Install directly from PyPI:

pip install Topsis-Savree-102317097

---

## Command Line Execution

topsis <input_file> <weights> <impacts> <output_file>

Example:

topsis data.csv "1,2,1,1" "+,+,-,+" result.csv

---

## Using in Python

from topsis_savree_102317097.topsis import topsis

topsis("data.csv", "1,2,1,1", "+,+,-,+", "result.csv")

---

## Input Requirements

• CSV file with at least three columns  
• First column → Alternative names  
• Remaining columns → Numeric criteria values  

Example:

Option,Cost,Quality,Durability
A1,250,7,8
A2,200,6,9
A3,300,8,7

---

## Parameters

Weights:
Comma-separated numeric values (e.g., "1,1,2")

Impacts:
Comma-separated symbols:
+  → Benefit criterion (higher is better)  
-  → Cost criterion (lower is better)

---

## Output

The generated CSV file includes:
• Original data  
• Calculated Topsis Score  
• Final Rank  

Higher score indicates better performance.

---

## Error Handling

The package checks for:

• Incorrect number of weights or impacts  
• Invalid impact symbols  
• Non-numeric values in criteria columns  
• File not found errors  

---

## Developed By

Savree Dohar  
Roll No: 102317097  
UCS654 – Predictive Analytics & Statistics
