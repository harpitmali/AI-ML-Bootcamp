# Loan Default Prediction

A machine learning classification project that predicts whether a customer is likely to default on a loan based on financial, credit, employment, and demographic information.

## Problem Statement

Loan default prediction is a classification problem where the goal is to identify customers who are more likely to default on their loans.

This project builds and compares multiple machine learning models and selects the best-performing model based primarily on F1-score and cross-validation performance.

## Dataset

The dataset contains 8,000 customer records with information such as:

- Age
- Income
- Employment Length
- Loan Amount
- Interest Rate
- Credit Score
- Loan Term
- Home Ownership
- Loan Purpose
- Education
- Marital Status
- Default

The target variable is:

- `Default = 0` → No default
- `Default = 1` → Default

## Project Workflow

1. Data Loading
2. Data Inspection
3. Data Cleaning
4. Exploratory Data Analysis
5. Feature Engineering
6. Train/Test Split
7. Data Preprocessing
8. Model Training
9. Model Evaluation
10. Cross-Validation
11. Hyperparameter Tuning
12. Error Analysis
13. Final Model Training
14. Model Saving
15. Prediction Script

## Exploratory Data Analysis

Important observations from the dataset:

- The target classes are imbalanced, with non-default customers forming the majority.
- Higher credit scores were associated with lower observed default rates.
- Higher loan amounts were associated with higher observed default rates.
- Lower income levels were associated with higher observed default rates.
- Default rates varied across different home ownership, loan purpose, and education categories.

These observations represent associations in the dataset and do not imply causation.

## Feature Engineering

Two additional features were created:

### Loan-to-Income Ratio

```text
Loan_to_Income = Loan_Amount / Income

This represents the loan amount relative to the customer's income.

### Loan per Month

```python
Loan_Per_Month = Loan_Amount / Loan_Term
```

This represents the loan amount divided by the loan term.

## Models Compared

The following classification models were evaluated:

- Logistic Regression
- K-Nearest Neighbors
- Support Vector Machine
- Decision Tree
- Random Forest
- Gradient Boosting

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- 5-fold Cross-Validation F1-score

## Model Comparison

| Model | Test F1 | Mean CV F1 | Precision | Recall |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.571 | 0.568 | 0.686 | 0.489 |
| Gradient Boosting | 0.554 | 0.566 | 0.682 | 0.466 |
| SVM | 0.556 | 0.557 | 0.703 | 0.461 |
| Random Forest | 0.533 | 0.537 | 0.698 | 0.432 |
| Decision Tree | 0.547 | 0.526 | 0.646 | 0.474 |
| KNN | 0.502 | 0.498 | 0.601 | 0.432 |

## Final Model

Logistic Regression was selected as the final model because it achieved the strongest overall F1 performance and showed a very small difference between training and test F1-score.

Final model:

```text
Logistic Regression
C = 1.0
max_iter = 1000
```

The final model was retrained using the complete labeled dataset after model selection.

## Preprocessing Pipeline

The final model uses a preprocessing pipeline:

### Numerical Features

- Median imputation
- Standard scaling

### Categorical Features

- Most-frequent imputation
- One-hot encoding
- Unknown categories ignored

The preprocessing and Logistic Regression model are stored together in a single pipeline.

## Error Analysis

For the final Logistic Regression model:

- False Negatives: 265
- False Positives: 116

False negatives are especially important in loan default prediction because they represent customers who actually defaulted but were predicted as non-default.

## Model Deployment

The trained model is saved as:

```text
models/loan_default_model.pkl
```

A prediction script is available at:

```text
src/predict.py
```

Run the prediction script from the project root:

```bash
python src/predict.py
```

The script accepts raw customer information, performs feature engineering, and returns:

- Predicted class
- Default probability

## Project Structure

```text
Loan-Default-Prediction/
│
├── data/
│   └── loan_default_prediction_8000.csv
│
├── notebooks/
│   └── loan_default.ipynb
│
├── src/
│   └── predict.py
│
├── models/
│   └── loan_default_model.pkl
│
├── README.md
└── requirements.txt
```

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

## Key Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Classification
- Model Comparison
- Cross-Validation
- Hyperparameter Tuning
- Error Analysis
- Scikit-learn Pipelines
- Model Persistence
- Python Prediction Scripts