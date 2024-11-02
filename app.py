import os
import pickle
import streamlit as st  # type: ignore
from streamlit_option_menu import option_menu  # type: ignore

st.set_page_config(
    page_title="Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️",
    initial_sidebar_state="expanded",
)
#css
st.markdown("""
    <style>
        /* Set a blue background for the main app */
        .stApp {
            background-color: #e0f7fa;
        }

        /* Set sidebar background color and remove default box shadow */
        .css-1d391kg {  /* This may vary, use browser inspector to confirm class */
            background-color: #005b96 !important;  /* Dark blue for the sidebar */
            border-right: 3px solid #388e3c !important;  /* Green border on the right */
            box-shadow: none !important;
        }

        /* Style sidebar title text and other elements */
        .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg p {
            color: #ffffff !important;
        }

        /* Sidebar menu items */
        .css-17eq0hr a {
            color: #ffffff !important; /* White text color for items */
        }
        .css-17eq0hr a:hover {
            background-color: #00796b !important; /* Green on hover */
        }

        /* Highlight selected button in green */
        .css-1v3fvcr {
            background-color: #4caf50 !important;
            color: #ffffff !important;
        }

        /* Title styling */
        .stTitle {
            color: #01579b;
        }

        /* Form fields styling */
        .stTextInput>div>div>input {
            background-color: #e0f2f1;
            color: #006064;
            border: 1px solid #00838f;
        }

        /* Button styling */
        .stButton>button {
            background-color: #388e3c; /* Green for main buttons */
            color: white;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #66bb6a; /* Lighter green on hover */
        }
    </style>
""", unsafe_allow_html=True)


# Working directory and model paths
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f"{working_dir}/saved_models/diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open(f"{working_dir}/saved_models/heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open(f"{working_dir}/saved_models/parkinsons_model.sav", "rb"))

# Sidebar
with st.sidebar:
    st.image("/Users/akshitasachdeva/Desktop/muMLproject/drimg.webp", width=200)  # Replace with a relevant health-related image
    selected = option_menu(
        "Multiple Disease Prediction System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        menu_icon="hospital-fill",
        icons=["activity", "heart", "person"],
        default_index=0,
    )

# handle  errors
def convert_to_float(input_data):
    try:
        return [float(x) for x in input_data]
    except ValueError:
        st.error("Please enter valid numeric values for all fields.")
        return None

# Diabetes
if selected == "Diabetes Prediction":
    st.title("🩺 Diabetes Prediction")

    with st.expander("Enter Details for Diabetes Prediction", expanded=True):
        with st.form("diabetes_form"):
            col1, col2, col3 = st.columns(3)
            with col1:
                Pregnancies = st.text_input("Number of Pregnancies")
            with col2:
                Glucose = st.text_input("Glucose Level")
            with col3:
                BloodPressure = st.text_input("Blood Pressure Value")
            with col1:
                SkinThickness = st.text_input("Skin Thickness Value")
            with col2:
                Insulin = st.text_input("Insulin Level")
            with col3:
                BMI = st.text_input("BMI Value")
            with col1:
                DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
            with col2:
                Age = st.text_input("Age")

            if st.form_submit_button("Predict Diabetes"):
                user_input = convert_to_float([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
                if user_input:
                    diab_prediction = diabetes_model.predict([user_input])
                    diab_diagnosis = "The person is diabetic" if diab_prediction[0] == 1 else "The person is not diabetic"
                    st.success(diab_diagnosis)

# Heart Disease 
if selected == "Heart Disease Prediction":
    st.title("💖 Heart Disease Prediction")

    with st.expander("Enter Details for Heart Disease Prediction", expanded=True):
        with st.form("heart_disease_form"):
            col1, col2, col3 = st.columns(3)
            with col1:
                age = st.text_input("Age")
            with col2:
                sex = st.text_input("Sex")
            with col3:
                cp = st.text_input("Chest Pain Type")
            with col1:
                trestbps = st.text_input("Resting Blood Pressure")
            with col2:
                chol = st.text_input("Serum Cholesterol in mg/dl")
            with col3:
                fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
            with col1:
                restecg = st.text_input("Resting Electrocardiographic Results")
            with col2:
                thalach = st.text_input("Maximum Heart Rate Achieved")
            with col3:
                exang = st.text_input("Exercise Induced Angina")
            with col1:
                oldpeak = st.text_input("ST Depression Induced by Exercise")
            with col2:
                slope = st.text_input("Slope of the Peak Exercise ST Segment")
            with col3:
                ca = st.text_input("Major Vessels Colored by Fluoroscopy")
            with col1:
                thal = st.text_input("Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect")

            if st.form_submit_button("Predict Heart Disease"):
                user_input = convert_to_float([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
                if user_input:
                    heart_prediction = heart_disease_model.predict([user_input])
                    heart_diagnosis = "The person has heart disease" if heart_prediction[0] == 1 else "The person does not have heart disease"
                    st.success(heart_diagnosis)

# Parkinson's Prediction 
if selected == "Parkinson's Prediction":
    st.title("🧠 Parkinson's Disease Prediction")

    with st.expander("Enter Details for Parkinson's Prediction", expanded=True):
        with st.form("parkinsons_form"):
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                fo = st.text_input("MDVP:Fo(Hz)")
            with col2:
                fhi = st.text_input("MDVP:Fhi(Hz)")
            with col3:
                flo = st.text_input("MDVP:Flo(Hz)")
            with col4:
                Jitter_percent = st.text_input("MDVP:Jitter(%)")
            with col5:
                Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
            with col1:
                RAP = st.text_input("MDVP:RAP")
            with col2:
                PPQ = st.text_input("MDVP:PPQ")
            with col3:
                DDP = st.text_input("Jitter:DDP")
            with col4:
                Shimmer = st.text_input("MDVP:Shimmer")
            with col5:
                Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
            with col1:
                APQ3 = st.text_input("Shimmer:APQ3")
            with col2:
                APQ5 = st.text_input("Shimmer:APQ5")
            with col3:
                APQ = st.text_input("MDVP:APQ")
            with col4:
                DDA = st.text_input("Shimmer:DDA")
            with col5:
                NHR = st.text_input("NHR")
            with col1:
                HNR = st.text_input("HNR")
            with col2:
                RPDE = st.text_input("RPDE")
            with col3:
                DFA = st.text_input("DFA")
            with col4:
                spread1 = st.text_input("Spread1")
            with col5:
                spread2 = st.text_input("Spread2")
            with col1:
                D2 = st.text_input("D2")
            with col2:
                PPE = st.text_input("PPE")

            if st.form_submit_button("Predict Parkinson's Disease"):
                user_input = convert_to_float([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE])
                if user_input:
                    parkinsons_prediction = parkinsons_model.predict([user_input])
                    parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
                    st.success(parkinsons_diagnosis)
