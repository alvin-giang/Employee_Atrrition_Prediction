# Employee_Atrrition_Prediction

## Group_5_Project_4

### Collaborators:
Thanh Vinh (Alvin) Giang, Mason seifaddini, Rekha renukappa, Uma Selvaraj

### Project Overview

Employee attrition is a critical issue for businesses, impacting productivity, morale, and financial performance. Predicting which employees are likely to leave a company can help HR departments proactively address retention risks. This project aims to build a machine learning model to predict employee attrition using a dataset from Kaggle. The project includes data preprocessing, exploratory data analysis (EDA), model selection, model optimization using GridSearchCV, and deployment of the final model using Gradio for interactive predictions.

 ### Dataset Description

The dataset used in this project is HR-Employee-Attrition.csv, sourced from Kaggle. It contains data on employee demographics, job roles, salary, performance metrics, and whether they have left the company (attrition).

Key features include:

* Employee Information: Age, Gender, Marital Status, Education
* Job Role: Department, Job Level, Job Role, Over Time
* Compensation: Monthly Income, Hourly Rate, Percent Salary Hike
* Performance: Job Satisfaction, Performance Rating, Work-Life Balance
* Other: Distance from Home, Total Working Years, Years at Company
* The target variable is Attrition, which indicates whether an employee has left the company (Yes/No).

All features in the dataset:

* Age: The age of the employee (integer).
* Attrition: Whether the employee has left the company or not (object).
* BusinessTravel: Frequency of business travel (object).
* DailyRate: The daily rate of pay for the employee (integer).
* Department: Department in which the employee works (object).
* DistanceFromHome: Distance from home to work in miles (integer).
* Education: Level of education of the employee (integer).
* EducationField: Field of education of the employee (object).
* EmployeeCount: Number of employees (always 1) (integer).
* EmployeeNumber: Unique identifier for each employee (integer).
* EnvironmentSatisfaction: Satisfaction level with the work environment (integer).
* Gender: Gender of the employee (object).
* HourlyRate: Hourly rate of pay for the employee (integer).
* JobInvolvement: Level of job involvement (integer).
* JobLevel: Level of job within the company (integer).
* JobRole: Role of the employee in the company (object).
* JobSatisfaction: Satisfaction level with the job (integer).
* MaritalStatus: Marital status of the employee (object).
* MonthlyIncome: Monthly income of the employee (integer).
* MonthlyRate: Monthly rate of pay for the employee (integer).
* NumCompaniesWorked: Number of companies the employee has worked for (integer).
* Over18: Whether the employee is over 18 years old (object).
* OverTime: Whether the employee works overtime or not (object).
* PercentSalaryHike: Percentage increase in salary (integer).
* PerformanceRating: Performance rating of the employee (integer).
* RelationshipSatisfaction: Satisfaction level with work relationships (integer).
* StandardHours: Standard number of working hours (always 80) (integer).
* StockOptionLevel: Level of stock option (integer).
* TotalWorkingYears: Total number of years worked (integer).
* TrainingTimesLastYear: Number of training sessions attended last year (integer).
* WorkLifeBalance: Level of work-life balance (integer).
* YearsAtCompany: Number of years spent at the company (integer).
* YearsInCurrentRole: Number of years in the current role (integer).
* YearsSinceLastPromotion: Number of years since the last promotion (integer).
* YearsWithCurrManager: Number of years with the current manager (integer).

