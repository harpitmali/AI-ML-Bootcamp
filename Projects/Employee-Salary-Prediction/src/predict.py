import joblib
import pandas as pd

MODEL_PATH = "../models/employee_salary_model.pkl"

model = joblib.load(MODEL_PATH)

import pandas as pd

def predict_salary(age, experience, projects, performance):
    employee = pd.DataFrame({
        "Age": [age],
        "Experience": [experience],
        "Projects": [projects],
        "Performance": [performance]
    })

    prediction = model.predict(employee)

    return prediction[0]


if __name__ == "__main__":
    salary = predict_salary(
        age=30,
        experience=6,
        projects=5,
        performance=88
    )

    print(f"Predicted Salary: ₹{salary:,.2f}")