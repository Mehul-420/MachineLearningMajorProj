from flask import Flask, request, render_template
from utils import preprocessdata

app = Flask(__name__)

# Home route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Predict route to handle form submission and show prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        gender = request.form.get('gender')
        married = request.form.get('married')
        dependents = request.form.get('dependents')  # Corrected variable name
        education = request.form.get('education')
        self_employed = request.form.get('self_employed')
        applicant_income = request.form.get('applicant_income')
        coapplicant_income = request.form.get('coapplicant_income')
        loan_amount = request.form.get('loan_amount')
        loan_amount_term = request.form.get('loan_amount_term')
        credit_history = request.form.get('credit_history')
        property_area = request.form.get('property_area')

        # Encode categorical variables
        gender = 1 if gender == 'Male' else 0
        married = 1 if married == 'Yes' else 0
        dependents = 3 if dependents == '3+' else int(dependents)
        education = 1 if education == 'Graduate' else 0
        self_employed = 1 if self_employed == 'Yes' else 0
        credit_history = int(credit_history)  # Assuming 1 for Good, 0 for Bad

        # Encode Property Area: Urban=0, Semiurban=1, Rural=2
        property_area_mapping = {'Urban': 0, 'Semiurban': 1, 'Rural': 2}
        property_area = property_area_mapping.get(property_area, 0)  # Default to 0 if not found

        # Convert numerical inputs to float
        applicant_income = float(applicant_income)
        coapplicant_income = float(coapplicant_income)
        loan_amount = float(loan_amount)
        loan_amount_term = float(loan_amount_term)

        # Debugging: Print all processed inputs
        print(f"Processed Inputs: Gender={gender}, Married={married}, Dependents={dependents}, "
              f"Education={education}, Self_Employed={self_employed}, ApplicantIncome={applicant_income}, "
              f"CoapplicantIncome={coapplicant_income}, LoanAmount={loan_amount}, "
              f"Loan_Amount_Term={loan_amount_term}, Credit_History={credit_history}, "
              f"Property_Area={property_area}")

        # Remove Dependents if it's not part of the model
        prediction = preprocessdata(
            Gender=gender,
            Married=married,
            Education=education,
            Self_Employed=self_employed,
            ApplicantIncome=applicant_income,
            CoapplicantIncome=coapplicant_income,
            LoanAmount=loan_amount,
            Loan_Amount_Term=loan_amount_term,
            Credit_History=credit_history,
            Property_Area=property_area
        )

        # Map prediction to "YES" or "NO"
        prediction_text = "Approved" if prediction == 1 else "Rejected"

        # Debugging: Print prediction result
        print(f"Prediction Result: {prediction_text}")

        return render_template('predict.html', prediction=prediction_text)

    except Exception as e:
        # Handle exceptions and display an error message
        print(f"Error during prediction: {e}")
        return render_template('predict.html', prediction="Error in prediction")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
if __name__ == '__main__': 
    app.run(debug=True) 