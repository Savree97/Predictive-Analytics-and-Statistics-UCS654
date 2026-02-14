# Topsis-Savree-102317097

A Python package implementing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) for multi-criteria decision analysis.

---

## What is TOPSIS?

TOPSIS is a multi-criteria decision-making method that ranks alternatives based on:
- Shortest distance from the ideal best solution
- Farthest distance from the ideal worst solution

It is widely used in decision science, engineering, and management problems.

---

## Installation

Install from PyPI:

pip install Topsis-Savree-102317097

---

## Command Line Usage

topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>

Example:

topsis input.csv "1,1,1,2" "+,+,-,+" result.csv

---

## Python Usage

from topsis_savree_102317097.topsis import topsis

topsis("input.csv", "1,1,1,2", "+,+,-,+", "result.csv")

---

## Input File Format

- CSV file with 3 or more columns
- First column: Alternative names
- Remaining columns: Numeric values only

Example:

Model,Price,Storage,Camera
M1,250,16,12
M2,200,16,8
M3,300,32,16

---

## Parameters

- Weights: Comma-separated numeric values
- Impacts: Comma-separated + or - symbols  
  + → Benefit criterion  
  - → Cost criterion  

---

## Output

The result file contains:
- All original columns
- Topsis Score
- Rank

---

## Error Handling

The package handles:
- Invalid file format
- Non-numeric values
- Mismatched weights & impacts
- Invalid impact symbols

---

## Author

Savree Dohar
Roll No: 102317097  
UCS654 – Predictive Analytics & Statistics
