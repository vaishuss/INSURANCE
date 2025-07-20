Insurance Charges Prediction App
Project Overview
This is a simple machine learning web app built using Flask that predicts medical insurance charges based on user input like age, BMI, smoking status, number of children, etc.
Features
- Predicts insurance charges using a trained ML model.
- Clean web interface for data input.
- Built with Python, Flask, NumPy, scikit-learn.
Project Structure
├── app.py                    # Flask web app
├── insurance.csv             # Dataset used for training
├── Insurance.ipynb           # Jupyter notebook for data preprocessing and model training
├── my_first_project.joblib   # Trained model (joblib format)
├── templates/
│   └── index.html            # HTML input form (not included in uploads)
How to Run
1. Set up environment
   - Ensure Python is installed.
   - Install dependencies:
     pip install flask numpy joblib scikit-learn pandas

2. Run the app
   python app.py

3. Visit in browser
   http://127.0.0.1:5000/
Model Details
- Trained on insurance.csv.
- Code and training workflow are in Insurance.ipynb.
- Model is saved as my_first_project.joblib using joblib.
Prediction Flow
1. User fills the form.
2. Data is sent via POST to /predict.
3. Model predicts based on input features.
4. Result is shown on the same page.
Notes
- Ensure index.html is placed under a folder named templates.
- The model file (my_first_project.joblib) should be in the same directory as app.py.
