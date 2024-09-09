# Employee_Atrrition_Prediction

## Group_5_Project_4

## :writing_hand: Collaborators:
Thanh Vinh (Alvin) Giang, Mason seifaddini, Rekha renukappa, Uma Selvaraj

![image](https://github.com/user-attachments/assets/ffaf04dc-2cae-4328-8408-e3840c704585)


## :round_pushpin: Project Overview

Employee attrition is a critical issue for businesses, impacting productivity, morale, and financial performance. Predicting which employees are likely to leave a company can help HR departments proactively address retention risks. This project aims to build a machine learning model to predict employee attrition using a dataset from Kaggle. The project includes data preprocessing, exploratory data analysis (EDA), model selection, model optimization using GridSearchCV, and deployment of the final model using Gradio for interactive predictions.

 ## :file_folder: Dataset Description

The dataset used in this project is HR-Employee-Attrition.csv, sourced from Kaggle. It contains data on employee demographics, job roles, salary, performance metrics, and whether they have left the company (attrition).

Key features include:

* **Employee Information**: Age, Gender, Marital Status, Education
* **Job Role: Department**, Job Level, Job Role, Over Time
* **Compensation**: Monthly Income, Hourly Rate, Percent Salary Hike
* **Performance**: Job Satisfaction, Performance Rating, Work-Life Balance
* **Other**: Distance from Home, Total Working Years, Years at Company
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

## :memo: Repository Structure

* **Data_Analysis**: Stores all Jypyter notebooks detailling preprocessing, data analysis, model training, model optimizing, evaluation steps, and model deployment.
* **Outputs**: Stores all visualizations, models, and endcoder files.
* **Resource**: The initial datset
* **README.md**: Overview of the project, including a step-by-step process.

## :warning: Installation and Requirements

To set up the environment and run this project, you'll need to have Python installed along with several libraries. You can install the required packages using the following command:

```python
ip install pandas numpy matplotlib seaborn scikit-learn gradio
```

## Data Preprocessing

Data preprocessing is a crucial step to prepare the dataset for machine learning modeling. The key tasks involved in preprocessing include:

* **Handling Missing Values**: Although the dataset is relatively clean, we will check for any missing values and handle them appropriately.
* **Encoding Categorical Variables**: The dataset contains categorical variables (e.g., Gender, Job Role). These will be encoded using techniques like One-Hot Encoding or Label Encoding to convert them into a numerical format suitable for modeling.
* **Data balancing**: Use SMOTE to create synthetic examples of minority class to reduce class imbalance.
* **Feature Scaling**: Some algorithms require features to be on the same scale. We will use techniques like StandardScaler or MinMaxScaler to normalize the data.
* **Data Splitting**: The dataset will be split into training and testing sets. Typically, 70-80% of the data is used for training, and the remaining 20-30% for testing.
<<<<<<< HEAD

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) helps in understanding the dataset and identifying patterns, trends, and relationships between features and the target variable. The following steps will be performed during EDA:

* **Descriptive Statistics**: We will compute summary statistics for numerical features (e.g., mean, median, standard deviation) and distribution of categorical features.
* **Correlation Analysis**: We will examine the correlation between numerical features and the target variable (Attrition) to identify potential predictors.
* **Data Visualization**: Various plots such as histograms, box plots, bar charts, and heatmaps will be used to visualize the distribution of features and their relationship with Attrition.
* **Feature Importance**: Techniques like feature importance from tree-based models (e.g., Random Forest) will be used to identify the most influential features on employee attrition.

## Model Selection and Modeling

We will explore multiple machine learning models to find the best one for predicting employee attrition. The models considered include:

* **Logistic Regression**: A baseline model that is easy to interpret and quick to train. It's useful for binary classification problems like this one.
* **Random Forest**: A robust ensemble method that can handle a large number of features and is less prone to overfitting.
* **Neural Network**: A powerful classifier that works well with high-dimensional data and can find non-linear decision boundaries.

Each model will be evaluated using cross-validation and metrics such as:

* **Accuracy**: The proportion of correctly predicted instances among all instances.
* **Precision**: The proportion of true positives among all predicted positives.
* **Recall**: The proportion of true positives among all actual positives.
* **F1-Score**: The harmonic mean of precision and recall, providing a balance between the two.

## Model Optimization with GridSearchCV

To fine-tune the selected models, we will use GridSearchCV to perform hyperparameter optimization. This step involves:

* **Defining the Parameter Grid**: Specifying a grid of hyperparameters for each model (e.g., number of trees in Random Forest, regularization strength in Logistic Regression).
* **Cross-Validation**: GridSearchCV performs cross-validation on each combination of hyperparameters to evaluate model performance.
* **Selecting the Best Model**: The model with the best cross-validated performance is selected as the final model.

## Model Deployment Using Gradio

After finalizing the best model, we will deploy it using Gradio, an easy-to-use Python library that creates web-based interfaces for machine learning models. The steps include:

* **Building the Gradio Interface**: Designing an interface that allows users to input employee data and receive a prediction on whether the employee is likely to leave.
* **Deploying Locally or on the Web**: The Gradio interface can be deployed locally for testing or hosted online for wider access.
* **User Interaction**: Users can interact with the model through the Gradio interface, making predictions and understanding which factors influence attrition in their inputs.

## :sparkles: Future Work and Improvements

While this project provides a robust model for predicting employee attrition, there are several areas for future work:

* **Feature Engineering**: Creating new features based on domain knowledge or interaction terms between existing features could improve model performance.
* **Advanced Models**: Exploring advanced models such as XGBoost, LightGBM, or deep learning techniques like neural networks could yield better results.
* **Model Interpretability**: Using tools like SHAP (SHapley Additive exPlanations) to explain individual predictions and understand model decisions at a granular level.
* **Deployment on Scalable Platforms**: Deploying the model on cloud platforms like AWS, Google Cloud, or Azure for scalability and wider accessibility.

## :key: Conclusion

This project successfully demonstrates the application of a machine learning pipeline to predict employee attrition. By using data preprocessing, EDA, model selection, optimization, and deployment, we have built a model that can help businesses predict which employees are at risk of leaving. This information can be used to take proactive steps in improving employee retention, ultimately benefiting the organization.

