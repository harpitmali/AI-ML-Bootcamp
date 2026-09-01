from pathlib import Path
import joblib
import pandas as pd 

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "loan_default_model.pkl"

model = joblib.load(
    MODEL_PATH
)

def predict_default(
    age,
    income,
    employment_length,
    loan_amount,
    interest_rate,
    credit_score,
    loan_term,
    home_ownership,
    loan_purpose,
    education,
    marital_status
):
    
    if age < 18:
        raise ValueError("Age must be at least 18.")

    if income <= 0:
        raise ValueError("Income must be greater than 0.")

    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than 0.")

    if interest_rate <= 0:
        raise ValueError("Interest rate must be greater than 0.")

    if not 300 <= credit_score <= 850:
        raise ValueError(
            "Credit score must be between 300 and 850."
        )

    if loan_term <= 0:
        raise ValueError("Loan term must be greater than 0.")
    
    valid_home_ownership = {
        "Rent",
        "Mortgage",
        "Own"
    }

    valid_loan_purpose = {
        "Debt_Consolidation",
        "Home_Improvement",
        "Education",
        "Medical",
        "Business"
    }

    valid_education = {
        "High_School",
        "Bachelor",
        "Master",
        "PhD"
    }

    valid_marital_status = {
        "Single",
        "Married",
        "Divorced"
    }

    if home_ownership not in valid_home_ownership:
        raise ValueError("Invalid home ownership category.")

    if loan_purpose not in valid_loan_purpose:
        raise ValueError("Invalid loan purpose category.")

    if education not in valid_education:
        raise ValueError("Invalid education category.")

    if marital_status not in valid_marital_status:
        raise ValueError("Invalid marital status category.")
    
    customer = pd.DataFrame({
        "Age": [age],
        "Income": [income],
        "Employment_Length": [employment_length],
        "Loan_Amount": [loan_amount],
        "Interest_Rate": [interest_rate],
        "Credit_Score": [credit_score],
        "Loan_Term": [loan_term],
        "Home_Ownership": [home_ownership],
        "Loan_Purpose": [loan_purpose],
        "Education": [education],
        "Marital_Status": [marital_status]
    })

    customer["Loan_to_Income"] = (
        customer["Loan_Amount"]
        / customer["Income"]
    )

    customer["Loan_Per_Month"] = (
        customer["Loan_Amount"]
        / customer["Loan_Term"]
    )
    
    prediction = model.predict(customer)[0]

    probability = model.predict_proba(customer)[0, 1]

    return prediction, probability


def display_prediction(customer_number, customer):
    prediction, probability = predict_default(**customer)

    print(f"\nCustomer {customer_number}")
    print("--------------------")
    print("Predicted Default:", prediction)
    print(
        "Default Probability:",
        round(probability * 100, 2),
        "%"
    )

if __name__ == "__main__":

    customer_1 = {
        "age": 45,
        "income": 100000,
        "employment_length": 15,
        "loan_amount": 12000,
        "interest_rate": 7.0,
        "credit_score": 780,
        "loan_term": 36,
        "home_ownership": "Own",
        "loan_purpose": "Home_Improvement",
        "education": "Master",
        "marital_status": "Married"
    }
    
    customer_2 = {
        "age": 25,
        "income": 30000,
        "employment_length": 1,
        "loan_amount": 25000,
        "interest_rate": 17.0,
        "credit_score": 560,
        "loan_term": 60,
        "home_ownership": "Rent",
        "loan_purpose": "Medical",
        "education": "High_School",
        "marital_status": "Single"
    }

    customer_3 = {
        "age": 35,
        "income": 65000,
        "employment_length": 7,
        "loan_amount": 18000,
        "interest_rate": 9.5,
        "credit_score": 710,
        "loan_term": 60,
        "home_ownership": "Mortgage",
        "loan_purpose": "Debt_Consolidation",
        "education": "Bachelor",
        "marital_status": "Married" 
    }

    customer_4 = {
        "age":16,
        "income":65000,
        "employment_length":7,
        "loan_amount":18000,
        "interest_rate":9.5,
        "credit_score":710,
        "loan_term":60,
        "home_ownership":"Mortgage",
        "loan_purpose":"Debt_Consolidation",
        "education":"Bachelor",
        "marital_status":"Married"
    }

    customer_5 = {
        "age":32,
        "income":-5000,
        "employment_length":7,
        "loan_amount":18000,
        "interest_rate":9.5,
        "credit_score":710,
        "loan_term":60,
        "home_ownership":"Mortgage",
        "loan_purpose":"Debt_Consolidation",
        "education":"Bachelor",
        "marital_status":"Married"
    }

    display_prediction(1, customer_1)
    display_prediction(2, customer_2)
    display_prediction(3, customer_3)