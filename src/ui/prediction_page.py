import streamlit as st
from src.predictor import predict_student
from src.insights import generate_insights
from src.database.history import save_prediction


def show_prediction_page():

    st.title("🎯 Student Performance Prediction")

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["male", "female"]
        )

        race = st.selectbox(
            "Race/Ethnicity",
            [
                "group A",
                "group B",
                "group C",
                "group D",
                "group E"
            ]
        )

        education = st.selectbox(
            "Parental Education",
            [
                "high school",
                "some high school",
                "some college",
                "associate's degree",
                "bachelor's degree",
                "master's degree"
            ]
        )

    with col2:

        lunch = st.selectbox(
            "Lunch",
            [
                "standard",
                "free/reduced"
            ]
        )

        prep = st.selectbox(
            "Test Preparation",
            [
                "none",
                "completed"
            ]
        )

    if st.button("Predict", use_container_width=True):

        result = predict_student(
            {
                "gender": gender,
                "race/ethnicity": race,
                "parental level of education": education,
                "lunch": lunch,
                "test preparation course": prep
            }
        )

        st.success("Prediction Complete")

        c1, c2, c3 = st.columns(3)

        c1.metric("Math", result["Math"])
        c2.metric("Reading", result["Reading"])
        c3.metric("Writing", result["Writing"])

        st.metric(
            "Average",
            result["Average"]
        )

        st.metric(
            "Status",
            result["Status"]
        )

        st.metric(
            "Category",
            result["Category"]
        )

        insights = generate_insights(
            lunch,
            prep,
            result["Average"]
        )

        for item in insights:
            st.info(item)
    save_prediction(
    st.session_state.username,
    gender,
    race,
    education,
    lunch,
    prep,
    result["Math"],
    result["Reading"],
    result["Writing"],
    result["Average"]
)