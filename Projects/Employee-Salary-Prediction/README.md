# Employee Salary Prediction

A machine learning project that predicts employee salary using employee attributes such as age, experience, projects, and performance.

## Problem Statement

The goal of this project is to predict an employee's salary based on measurable employee attributes.

The project explores the dataset through data cleaning and exploratory data analysis, then trains and compares multiple regression models to select a final model for salary prediction.

## Dataset

Dataset contains 1,005 rows before cleaning.

The dataset contains employee information including:

- Age
- Experience
- Projects
- Performance
- Department
- Education
- City
- Remote Work
- Salary

The target variable is `Salary`.

## Project Workflow

1. Load and inspect the dataset
2. Handle missing values
3. Remove duplicate records
4. Perform exploratory data analysis
5. Select features for machine learning
6. Split data into training and testing sets
7. Establish a baseline model
8. Train Linear Regression
9. Train Decision Tree Regressors
10. Compare models using MAE, RMSE, and R²
11. Use 5-fold cross-validation
12. Select the final model
13. Save the trained model
14. Build a reusable prediction script

## Features Used

The final model uses:

- `Age`
- `Experience`
- `Projects`
- `Performance`

Target:

- `Salary`

## Models Tested

The following approaches were compared:

- Mean baseline (`DummyRegressor`)
- Linear Regression
- Decision Tree Regressor (`max_depth=3`)
- Decision Tree Regressor (`max_depth=5`)

## Model Selection

The models were compared using:

- Train R²
- Test R²
- Test MAE
- Test RMSE
- Mean 5-fold Cross-Validation R²
- Mean 5-fold Cross-Validation MAE

The final model selected was a Decision Tree Regressor with `max_depth=3`.

This model provided strong test performance and strong cross-validation performance while keeping the tree simpler than the deeper alternative.

## Project Structure

Employee-Salary-Prediction/
│
├── data/
│   └── employee_salary_project.csv
│
├── notebooks/
│   └── employee.ipynb
│
├── src/
│   └── predict.py
│
├── models/
│   └── employee_salary_model.pkl
│
├── README.md
└── requirements.txt


## How to Run

### 1. Clone the repository
### 2. Navigate to the project
### 3. Install dependencies
### 4. Run the prediction script

```bash
git clone <your-repository-url>

cd Employee-Salary-Prediction

pip install -r requirements.txt

python src/predict.py
```

## Example Prediction

Example input:

- Age: 30
- Experience: 6 years
- Projects: 5
- Performance: 88

Predicted Salary:

`₹109,057.75`

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook