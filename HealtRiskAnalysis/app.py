import pickle
from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(page_title="Insurance Charge Predictor", page_icon="💡", layout="centered")

st.markdown(
    """
    <style>
        .hero-card {
            background: linear-gradient(135deg, #0ea5e9, #2563eb);
            padding: 1.1rem 1.2rem;
            border-radius: 14px;
            color: white;
            margin-bottom: 1rem;
        }
        .hero-card h2 {
            margin: 0;
            font-size: 1.35rem;
        }
        .hero-card p {
            margin: 0.35rem 0 0 0;
            opacity: 0.95;
            font-size: 0.95rem;
        }
        .result-card {
            background: #f0fdf4;
            border: 1px solid #86efac;
            border-radius: 12px;
            padding: 1rem;
            margin-top: 0.75rem;
        }
        .result-value {
            font-size: 2rem;
            font-weight: 700;
            color: #15803d;
            margin-top: 0.25rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <h2>Insurance Charge Prediction</h2>
        <p>Enter personal and health details to estimate expected insurance charges.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "insurance_model.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"


def load_pickle(path: Path):
    with path.open("rb") as f:
        return pickle.load(f)


if not MODEL_PATH.exists() or not SCALER_PATH.exists():
    st.error(
        "Model or scaler file not found. Please place both "
        "`insurance_model.pkl` and `scaler.pkl` in the same folder as this app."
    )
    st.stop()

model = load_pickle(MODEL_PATH)
scaler = load_pickle(SCALER_PATH)

# UI inputs
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Age", min_value=18, max_value=100, value=30)
        bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=30.0, step=0.1)
        children = st.slider("Children", min_value=0, max_value=10, value=0)
    with col2:
        sex_label = st.radio("Sex", options=["female", "male"], horizontal=True)
        smoker_label = st.radio("Smoker", options=["no", "yes"], horizontal=True)
        region = st.selectbox("Region", options=["northeast", "northwest", "southeast", "southwest"])

    st.caption("Tip: Smoker='yes' and higher BMI values usually increase predicted charges.")
    predict_clicked = st.form_submit_button("Predict", type="primary")

# Same encoding logic as training phase:
# sex: female=0, male=1 (LabelEncoder alphabetical order)
# smoker: no=0, yes=1 (LabelEncoder alphabetical order)
sex = 1 if sex_label == "male" else 0
smoker = 1 if smoker_label == "yes" else 0

input_data = {
    "age": age,
    "sex": sex,
    "bmi": bmi,
    "children": children,
    "smoker": smoker,
    "region_northwest": 1 if region == "northwest" else 0,
    "region_southeast": 1 if region == "southeast" else 0,
    "region_southwest": 1 if region == "southwest" else 0,
}

default_columns = [
    "age",
    "sex",
    "bmi",
    "children",
    "smoker",
    "region_northwest",
    "region_southeast",
    "region_southwest",
]

input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=getattr(scaler, "feature_names_in_", default_columns), fill_value=0)

if predict_clicked:
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    risk_level = "Low"
    if prediction >= 30000:
        risk_level = "High"
    elif prediction >= 15000:
        risk_level = "Medium"

    st.success("Prediction completed successfully.")
    met1, met2 = st.columns(2)
    met1.metric("Risk Segment", risk_level)
    met2.metric("Smoker", "Yes" if smoker == 1 else "No")

    st.markdown(
        f"""
        <div class="result-card">
            <div style="font-weight:600;">Estimated Insurance Charge</div>
            <div class="result-value">${prediction:,.2f}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
