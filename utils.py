import numpy as np
import joblib

def preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome,
                  CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
                  Property_Area):
    """
    Preprocesses the input data and returns the model prediction.

    Parameters:
    - Gender (int): 1 for Male, 0 for Female
    - Married (int): 1 for Yes, 0 for No
    - Education (int): 1 for Graduate, 0 for Not Graduate
    - Self_Employed (int): 1 for Yes, 0 for No
    - ApplicantIncome (float)
    - CoapplicantIncome (float)
    - LoanAmount (float)
    - Loan_Amount_Term (float)
    - Credit_History (int): 1 for Good, 0 for Bad
    - Property_Area (int): 0 for Urban, 1 for Semiurban, 2 for Rural

    Returns:
    - prediction (int): 1 for "YES", 0 for "NO"
    """
    try:
        # Prepare the input data as a 2D array (without Dependents)
        test_data = np.array([[Gender, Married, Education, Self_Employed,
                               ApplicantIncome, CoapplicantIncome, LoanAmount,
                               Loan_Amount_Term, Credit_History, Property_Area]])

        # Load the trained model
        model_path = "C:/Users/mehul/Desktop/SEM 1/ml/ml major project/model.pkl"   # Ensure model.pkl is in the same directory as utils.py
        trained_model = joblib.load(model_path)

        # Make prediction
        prediction = trained_model.predict(test_data)[0]

        return prediction

    except Exception as e:
        print(f"Error in preprocessdata: {e}")
        return 0  # Default to "NO" in case of error
