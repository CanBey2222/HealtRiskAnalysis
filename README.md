# Health Insurance Charge Prediction

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas">
  <img alt="Scikit-Learn" src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit">
  <img alt="Model Score" src="https://img.shields.io/badge/R%C2%B2%20Score-0.86-success">
</p>

This project is a machine learning application that predicts insurance charges (`charges`) based on individuals' health and demographic information.  
Data analysis, preprocessing, model training, and an interactive Streamlit interface are combined into a single workflow.

## Project Summary

- Performed Exploratory Data Analysis (EDA) on the health insurance dataset.
- Conducted missing/duplicate/data consistency checks.
- Converted categorical variables into numerical format.
- Built a prediction model using `RandomForestRegressor`.
- Deployed the model as a Streamlit app for real-time user input predictions.

## Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**

## Model Performance

- **$R^2$ Score: 0.86**
- Error analysis was supported with the **MAE** metric.
- Model outputs were interpreted using the `Actual vs Predicted` visualization.

> An $R^2 = 0.86$ indicates that the model explains a large portion of the variance in the target variable.

## Project Structure

```text
HealtRiskAnalysis/
│
├── app.py                 # Streamlit prediction app
├── main.ipynb             # EDA, preprocessing, model training
├── insurance.csv          # Dataset
├── insurance_model.pkl    # Trained RandomForest model
└── scaler.pkl             # StandardScaler object
