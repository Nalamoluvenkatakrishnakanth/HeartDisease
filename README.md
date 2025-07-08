# 🫀 Heart Disease Risk Assessment

## 🎯 Aim and Objectives
**Aim:**  
To build an interactive web application that assesses a person’s heart disease risk based on key medical parameters using machine learning.

**Objectives:**
- Create a UI to collect health information from users.
- Train and evaluate multiple classification models.
- Deploy the best-performing model using Streamlit.
- Educate users about important cardiovascular risk indicators.

---

## ✨ Features of the Application
- Clean and intuitive UI for user data entry.
- Real-time prediction of heart disease risk.
- Display of input summary before prediction.
- Interactive visuals and warning alerts for high-risk patients.
- Backend model integration for fast and accurate predictions.

---

## 💻 Technologies Used
- **MySQL**
- **Python**
- **Streamlit** (for UI)
- **Scikit-Learn** (for ML model training)
- **NumPy, Pandas** (for data manipulation)
- **Joblib** (for model serialization)
- **Matplotlib/Seaborn** (optional for EDA & visualization)

---

## 📊 Dataset Information
- **Source:** Kaggle.com
- **Features:**
  - Age, Sex, Chest Pain Type, Blood Pressure, Cholesterol
  - Fasting Blood Sugar, ECG results, Max Heart Rate, Exercise-induced Angina
  - ST Depression, Slope, Number of Major Vessels, Thalium Stress Test result
- **Target:**
  - `1`: Heart Disease Present
  - `0`: No Heart Disease

---

## 🧹 Preprocessing & Feature Engineering
- Handled missing values 
- Encoded categorical variables numerically
- Normalized continuous features

---

## 🤖 Model Development & Evaluation
Multiple models were trained and evaluated:
- Decision Tree
- Random Forest
- XGBoost
- **Support Vector Machine (SVM)** - *i have chosen for deployment "After evaluating multiple classification models including Decision Tree, Random Forest, and XGBoost, the Support Vector Machine (SVM) classifier was selected for deployment due to its superior performance and consistent accuracy in predicting heart disease risk on the test data."*

**Evaluation Metrics:**

| Metric       | Score           |
| ------------ | --------------- |
| Accuracy     | 0.78            |
| Precision    | 0.77            |
| Recall       | 0.78            |
| F1-Score     | 0.77            |
|ROC-AUC Score | 0.87            |            



---

## 🖥️ UI Design & Integration
- Built using **Streamlit**
- Form-style input fields for health metrics
- Real-time prediction using the SVM model (`HeartDisease_svm_model.pkl`)
- Display of result as **Success (No Heart Disease)** or **Error (High Risk)** with appropriate messages and styling

---
