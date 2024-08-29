# Employee_Atrrition_Prediction

## Group_5_Project_4

### Collaborators:
Thanh Vinh (Alvin) Giang, Mason seifaddini, Rekha renukappa, Uma Selvaraj

https://cdnl.iconscout.com/lottie/premium/preview-watermark/incentive-and-welfare-program-for-employee-retention-11425110-9249760.mp4

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

### Repository Structure

* Data_Analysis: Stores all Jypyter notebooks detailling preprocessing, data analysis, model training, model optimizing, evaluation steps, and model deployment.
* Outputs: Stores all visualizations, models, and endcoder files.
* Resource: The initial datset
* README.md: Overview of the project, including a step-by-step process.

### Installation and Requirements

To set up the environment and run this project, you'll need to have Python installed along with several libraries. You can install the required packages using the following command:

`pip install pandas numpy matplotlib seaborn scikit-learn gradio`

1. Data Preprocessing

Data preprocessing is a crucial step to prepare the dataset for machine learning modeling. The key tasks involved in preprocessing include:

* Handling Missing Values: Although the dataset is relatively clean, we will check for any missing values and handle them appropriately.
* Encoding Categorical Variables: The dataset contains categorical variables (e.g., Gender, Job Role). These will be encoded using techniques like One-Hot Encoding or Label Encoding to convert them into a numerical format suitable for modeling.
* Data balancing: Use SMOTE to create synthetic examples of minority class to reduce class imbalance.
* Feature Scaling: Some algorithms require features to be on the same scale. We will use techniques like StandardScaler or MinMaxScaler to normalize the data.
* Data Splitting: The dataset will be split into training and testing sets. Typically, 70-80% of the data is used for training, and the remaining 20-30% for testing.
