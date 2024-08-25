# Import Libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import gradio as gr
import joblib

# Read the dataset file with the Pandas 
dataset_df = pd.read_csv("../Outputs/Employee_attrition.csv")

# Load machine learning model
random_forest_model = joblib.load("../Outputs/random_forest_model.pkl")


# Deploy with Gradio
def predict_attrition(Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField,
                      EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction,
                      MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, OverTime, PercentSalaryHike,
                      PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears,
                      TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole,
                      YearsSinceLastPromotion, YearsWithCurrManager):
    
    # Preprocess input
    input_data = pd.DataFrame({
        'Age': [Age],
        'BusinessTravel': [BusinessTravel],
        'DailyRate': [DailyRate],
        'Department': [Department],
        'DistanceFromHome': [DistanceFromHome],
        'Education': [Education],
        'EducationField': [EducationField],
        'EnvironmentSatisfaction': [EnvironmentSatisfaction],
        'Gender': [Gender],
        'HourlyRate': [HourlyRate],
        'JobInvolvement': [JobInvolvement],
        'JobLevel': [JobLevel],
        'JobRole': [JobRole],
        'JobSatisfaction': [JobSatisfaction],
        'MaritalStatus': [MaritalStatus],
        'MonthlyIncome': [MonthlyIncome],
        'MonthlyRate': [MonthlyRate],
        'NumCompaniesWorked': [NumCompaniesWorked],
        'OverTime': [OverTime],
        'PercentSalaryHike': [PercentSalaryHike],
        'PerformanceRating': [PerformanceRating],
        'RelationshipSatisfaction': [RelationshipSatisfaction],
        'StockOptionLevel': [StockOptionLevel],
        'TotalWorkingYears': [TotalWorkingYears],
        'TrainingTimesLastYear': [TrainingTimesLastYear],
        'WorkLifeBalance': [WorkLifeBalance],
        'YearsAtCompany': [YearsAtCompany],
        'YearsInCurrentRole': [YearsInCurrentRole],
        'YearsSinceLastPromotion': [YearsSinceLastPromotion],
        'YearsWithCurrManager': [YearsWithCurrManager]
    })

    # Encode categorical variables
    for column in input_data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        input_data[column] = le.fit_transform(input_data[column])

    
    # Predict
    prediction = random_forest_model.predict(input_data)
    return "Yes" if prediction[0] == 1 else "No"

# Create the Gradio interface
iface = gr.Interface(
    fn=predict_attrition,
    inputs=[
        gr.Number(label="Age"),
        gr.Dropdown(choices=list(dataset_df['BusinessTravel'].unique()), label="BusinessTravel"),
        gr.Number(label="DailyRate"),
        gr.Dropdown(choices=list(dataset_df['Department'].unique()), label="Department"),
        gr.Number(label="DistanceFromHome"),
        gr.Dropdown(choices=sorted(list(dataset_df['Education'].unique()),reverse=False), label="Education"),
        gr.Dropdown(choices=list(dataset_df['EducationField'].unique()), label="EducationField"),
        gr.Dropdown(choices=sorted(list(dataset_df['EnvironmentSatisfaction'].unique()),reverse=False), label="EnvironmentSatisfaction"),
        gr.Dropdown(choices=list(dataset_df['Gender'].unique()), label="Gender"),
        gr.Number(label="HourlyRate"),
        gr.Dropdown(choices=sorted(list(dataset_df['JobInvolvement'].unique()),reverse=False), label="JobInvolvement"),
        gr.Dropdown(choices=sorted(list(dataset_df['JobLevel'].unique()),reverse=False), label="JobLevel"),
        gr.Dropdown(choices=list(dataset_df['JobRole'].unique()), label="JobRole"),
        gr.Dropdown(choices=sorted(list(dataset_df['JobSatisfaction'].unique()),reverse=False), label="JobSatisfaction"),
        gr.Dropdown(choices=list(dataset_df['MaritalStatus'].unique()), label="MaritalStatus"),
        gr.Number(label="MonthlyIncome"),
        gr.Number(label="MonthlyRate"),
        gr.Number(label="NumCompaniesWorked"),
        gr.Dropdown(choices=list(dataset_df['OverTime'].unique()), label="OverTime"),
        gr.Number(label="PercentSalaryHike"),
        gr.Dropdown(choices=sorted(list(dataset_df['WorkLifeBalance'].unique()),reverse=False), label="PerformanceRating"),
        gr.Dropdown(choices=sorted(list(dataset_df['RelationshipSatisfaction'].unique()),reverse=False), label="RelationshipSatisfaction"),
        gr.Dropdown(choices=sorted(list(dataset_df['StockOptionLevel'].unique()),reverse=False), label="StockOptionLevel"),
        gr.Number(label="TotalWorkingYears"),
        gr.Number(label="TrainingTimesLastYear"),
        gr.Dropdown(choices=sorted(list(dataset_df['WorkLifeBalance'].unique()),reverse=False), label="WorkLifeBalance"),
        gr.Number(label="YearsAtCompany"),
        gr.Number(label="YearsInCurrentRole"),
        gr.Number(label="YearsSinceLastPromotion"),
        gr.Number(label="YearsWithCurrManager")
    ],
    outputs=gr.Textbox(label="Attrition Prediction"),
    title="Employee Attrition Prediction",
    description="Predict if an employee will leave the company based on various features."
)

# Launch the Gradio interface
iface.launch()