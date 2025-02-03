# Tfptm
This project uses TOPSIS to rank models based on multiple criteria like accuracy, inference time, and model size. It normalizes data, applies weights, calculates distances from ideal best/worst cases, and ranks models accordingly. This method helps in objective model evaluation and selection.


# Multi-Criteria Decision Analysis Using TOPSIS

This project implements the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** method to rank models based on multiple criteria. It evaluates various models using different performance metrics and assigns ranks based on their overall scores.

## Features
- Normalizes the dataset based on beneficial and non-beneficial criteria.
- Weighs the normalized data based on predefined importance.
- Computes the best and worst distances for ranking.
- Provides a final ranking of models.

## Installation
Ensure you have Python installed, then install dependencies:
```bash
pip install numpy pandas
