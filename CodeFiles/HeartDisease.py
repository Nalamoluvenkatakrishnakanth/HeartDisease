import streamlit as st
import pandas as pd
import joblib
import numpy as np


#Streamlit UI configuration - Must be the first Streamlit command in your script
st.set_page_config(page_title=" Heart Disease Predictor",page_icon="🫀", layout="centered")


# Title of the app
st.markdown("""
    <h1 style='text-align: center; color: #c0392b;'>🫀 Heart Disease Risk Predictor</h1>
    <p style='text-align: center; font-size: 18px;'>Fill in the details below to check for potential heart disease risk.</p>
    <hr style='border: 1px solid #ccc;'>
""", unsafe_allow_html=True)


# Custom styles
st.markdown("""
<style>
    .stSelectbox label, .stRadio label, .stNumberInput label, .stSlider label {
        font-weight: 600;
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #e74c3c;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        height: 3em;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)


# Load the trained model (should be a pipeline)
model = joblib.load("HeartDisease_svm_model.pkl")

# Streamlit UI to take inputs
with st.form("HeartDisease_form"):
    st.subheader("📝 Patient Information")
    age = st.number_input("Age of the patient", min_value=29,format="%d")
    sex = st.selectbox("Gender", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["0: Typical angina","1: Atypical angina","2: Non-anginal pain","3: Asymptomatic"])
    trestbps = st.slider("Resting blood pressure (in mm Hg)", min_value=0.0, max_value=500.0,value=20.0)
    chol = st.slider("cholesterol in mg/dl", min_value=0.0, max_value=500.0,value=20.0)
    fbs = st.selectbox("Fasting blood sugar level > 120 mg/dl (1 = true, 0 = false)", ["True", "False"])
    restecg = st.selectbox("Resting electrocardiographic results:",["0: Normal","1: ST-T wave abnormality","2: Left ventricular hypertrophy"])
    thalach = st.number_input("Maximum heart rate achieved during a stress test", min_value=0.0, max_value=500.0,value=50.0)
    exang = st.selectbox("Exercise-induced angina (1 = yes, 0 = no)", ["Yes", "No"])
    oldpeak = st.number_input("ST depression induced by exercise relative to rest", min_value=0.0, max_value=40.0,value=2.0)
    slope = st.selectbox("Slope of the peak exercise ST segment:",["0: Upsloping","1: Flat","2: Downsloping"])
    ca = st.number_input("Number of major vessels (0–4) colored by fluoroscopy", min_value=0,value=0)
    thal = st.number_input("Thalium stress test result (0: Normal 1: Fixed defect 2: Reversible defect 3: Not described)", min_value=0, max_value=3,value=0)


    # Submit button
    submitted = st.form_submit_button("🔍 Predict Risk")



# Convert categorical inputs to numeric values
sex_numeric = 1 if sex == "Male" else 0
cp_numeric = int(cp.split(":")[0])
fbs_numeric = 1 if fbs == "True" else 0
restecg_numeric = int(restecg.split(":")[0])
exang_numeric = 1 if exang == "Yes" else 0
slope_numeric = int(slope.split(":")[0])



   # Prediction on form submission
if submitted:
    input_df = pd.DataFrame([{
    'age': age,
    'sex': sex_numeric,
    'cp': cp_numeric,
    'trestbps': trestbps,
    'chol': chol,
    'fbs': fbs_numeric,
    'restecg': restecg_numeric,
    'thalach': thalach,
    'exang': exang_numeric,
    'oldpeak': oldpeak,
    'slope': slope_numeric,
    'ca': ca,
    'thal': thal
}])

    # Print input data
    st.subheader("🔬 Input Summary")
    st.dataframe(input_df)
    

    try:
        # Predict the tip
        prediction = model.predict(input_df)

        # Ensure the output is a scalar value
        predicted = prediction[0] if isinstance(prediction, (list, np.ndarray)) else prediction


        if predicted == 1:
            # Display the predicted tip
            st.error("💥 **Result: High Risk of Heart Disease Detected!** \nPlease consult a cardiologist immediately.")
        else :
            # Display the predicted tip
             st.success("✅ **Result: No Heart Disease Detected.** \nStay healthy and maintain regular check-ups.")
    except Exception as e:
        st.error(f" Error: {str(e)}")