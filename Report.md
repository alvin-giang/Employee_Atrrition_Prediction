# Employee Attrition Prediction Analysis Report

## Overview of the Analysis

Employee attrition poses significant challenges for organizations, leading to disruptions in workflow, increased hiring costs, and potential losses in knowledge and skills. Predicting employee attrition can empower companies to implement proactive strategies to retain valuable employees. In this analysis, a Random Forest model was employed to predict employee attrition using a dataset sourced from Kaggle. The model was initially trained using default parameters, followed by hyperparameter tuning to enhance its performance.

This report details the machine learning process, presents the results before and after tuning, and summarizes the overall findings.

## Machine Learning Process

### Data Preprocessing

Before modeling, the dataset was carefully preprocessed to ensure high-quality input data:

* Handling Missing Values: The dataset was checked for any missing values. Any gaps were addressed either by imputation or exclusion to prevent inaccuracies during model training.
* Encoding Categorical Variables: Categorical features such as job roles, education levels, and marital status were converted into numerical format using One-Hot Encoding. This step allowed the Random Forest model to process these features effectively.
* Data balancing: Use SMOTE to create synthetic examples of minority class to reduce class imbalance.
* Feature Scaling: Although Random Forest does not require feature scaling, numerical features were standardized to maintain consistency in the data.
* Data Splitting: The dataset was split into training and testing sets using a typical 80/20 ratio to evaluate the model's performance on unseen data.

### Exploratory Data Analysis (EDA)

Exploratory Data Analysis was conducted to uncover patterns and relationships within the data:

* Descriptive Statistics: We will compute summary statistics for numerical features (e.g., mean, median, standard deviation) and distribution of categorical features.
* Correlation Analysis: We will examine the correlation between numerical features and the target variable (Attrition) to identify potential predictors.
* Data Visualization: Various plots such as histograms, box plots, bar charts, and heatmaps will be used to visualize the distribution of features and their relationship with Attrition.
* Feature Importance: Techniques like feature importance from tree-based models (e.g., Random Forest) will be used to identify the most influential features on employee attrition.

### Model Selection and Initial Training

The Random Forest algorithm was chosen for this analysis due to its robustness, ability to handle large datasets with numerous features, and resistance to overfitting. The model was initially trained with default hyperparameters:

* Number of Trees: 100 (default)
* Criterion: Gini Impurity
* Maximum Depth: None (default, allowing trees to grow until all leaves are pure)
* Minimum Samples Split: 2

### Initial Model Performance

The initial performance of the model was assessed using the classification report generated from the test data:

* No Attrition (Class 0):
    * Precision: 0.86
    * Recall: 0.92
    * F1-Score: 0.89
* Attrition (Class 1):
    * Precision: 0.92
    * Recall: 0.86
    * F1-Score: 0.89
* Overall Metrics:
    * Accuracy: 0.89
    * Macro Average (Precision, Recall, F1-Score): 0.89
    * Weighted Average (Precision, Recall, F1-Score): 0.89

### Hyperparameter Tuning
To improve the model’s performance, hyperparameter tuning was conducted using GridSearchCV. The following parameters were optimized:

* Number of Trees (n_estimators): The number of trees was adjusted to 200 to provide a better balance between model complexity and computational cost.
* Maximum Depth (max_depth): The maximum depth of each tree was set to 10 to prevent overfitting while still capturing important patterns in the data.
* Minimum Samples Split (min_samples_split): The minimum number of samples required to split an internal node was adjusted to 4, enhancing the model’s generalizability.
* Criterion: Both Gini Impurity and Entropy were considered, with Entropy providing a slight improvement in performance.

### Model Performance After Tuning
After tuning, the model's performance improved, as indicated by the following metrics:
* No Attrition (Class 0):
    * Precision: 0.88
    * Recall: 0.94
    * F1-Score: 0.91
* Attrition (Class 1):
    * Precision: 0.94
    * Recall: 0.88
    * F1-Score: 0.91
* Overall Metrics:
    * Accuracy: 0.91
    * Macro Average (Precision, Recall, F1-Score): 0.91
    * Weighted Average (Precision, Recall, F1-Score): 0.91

## Results

### Before Hyperparameter Tuning

The Random Forest model initially performed well, achieving an overall accuracy of 89%. However, the model exhibited slight imbalances in recall and precision between the two classes. The recall for No Attrition (Class 0) was higher than for Attrition (Class 1), indicating that the model was better at predicting employees who would stay rather than those who would leave.

### After Hyperparameter Tuning

After tuning, the model's performance improved:

* Increased Accuracy: The overall accuracy increased to 91%, indicating that the model was more accurate in its predictions.
* Balanced Performance: The precision, recall, and F1-scores for both classes were balanced, suggesting that the model is equally proficient in predicting both employees who would stay and those who would leave.
* Higher Recall for No Attrition: The recall for No Attrition (Class 0) improved to 0.94, reducing the likelihood of false negatives (employees predicted to leave but who actually stayed).
* Improved Precision for Attrition: The precision for predicting Attrition (Class 1) increased to 0.94, minimizing the chances of false positives (employees predicted to stay but who actually left).

## Summary

This analysis successfully demonstrated the application of a Random Forest model to predict employee attrition. The initial model provided a solid baseline with an accuracy of 89%, but hyperparameter tuning further enhanced the model's performance, increasing accuracy to 91% and balancing precision and recall across both classes.

The optimized model is now more reliable and capable of providing actionable insights for HR departments to identify employees at risk of leaving. By implementing such a model, organizations can proactively address attrition risks, thereby reducing turnover and retaining key talent.

Future work could explore more advanced techniques, such as feature engineering or ensemble methods, to further refine the model’s performance. Additionally, deploying the model in a real-world setting using platforms like Gradio could provide an interactive interface for users to make predictions and interpret the results.