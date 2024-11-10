# Loan Prediction Project

This project is an end-to-end loan prediction system that uses a decision tree model for predicting loan eligibility. The project includes backend and frontend components, utilizing Flask for the backend and HTML templates for the user interface.

## Package Requirements

To run this project, you need to install the following packages:

### General Requirements

- Python >= 3.7

### Required Libraries

- `pandas==1.3.3`
- `numpy==1.21.2`
- `scikit-learn==0.24.2`
- `flask==2.0.1`
- `joblib==1.1.0`




## Run Instructions

Follow these steps to set up and run the project:

### Train the Model
- Open and run `Loan_prediction_using_DecisionTree.ipynb` in Jupyter Notebook.
- This notebook will train a decision tree model on the loan dataset.
- Running the notebook will produce a file named `model.pkl`, which contains the serialized model.

### Configure Model Path in `utils.py`
- Open `utils.py`.
- Locate the function for loading the trained model (e.g., `load_model()`).
- Set the path to `model.pkl` (the path should match the location where `model.pkl` is saved).

### Run the Application
- In the terminal, navigate to the project folder.
- Run the Flask app (`app.py`):
    ```bash
    flask run
    ```
- A URL similar to `http://127.0.0.1:5000/` will be displayed in the terminal.

### Access the Web Application
- Open the displayed URL in a web browser.
- On the web page, enter the required details and submit the form to see the loan prediction results.

## Project Structure

- `Loan_prediction_using_DecisionTree.ipynb`: Jupyter Notebook for training the model.
- `model.pkl`: Serialized model file created after running the notebook.
- `app.py`: Flask application script for the backend.
- `utils.py`: Contains utility functions, including loading the trained model.
- `templates/`: Folder containing HTML templates for the web pages.
- `Dataset/`: Folder containing the dataset file `loan-train.csv`.

## Notes

- Ensure the correct model path is set in `utils.py` before running `app.py`.
