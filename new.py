import os
import json

# Create a folder for the notebooks (optional)
# os.makedirs("notebooks", exist_ok=True)

# Minimal content for an empty Jupyter notebook
notebook_template = {
    "cells": [],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 2
}

for i in range(1, 101):
    filename = f"day{i}.ipynb"
    filepath = filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(notebook_template, f, indent=2)

print("✅ Created 100 notebook files in the 'notebooks' folder.")
