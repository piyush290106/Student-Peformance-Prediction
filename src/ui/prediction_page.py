import streamlit as st
from src.predictor import predict_student
from src.database.history import save_prediction
from src.reports.pdf_report import generate_pdf


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

    st.markdown("---")

    if st.button(
        "🚀 Predict Performance",
        use_container_width=True
    ):

        result = predict_student(
            {
                "gender": gender,
                "race/ethnicity": race,
                "parental level of education": education,
                "lunch": lunch,
                "test preparation course": prep
            }
        )
        st.write(result)

        # Save Prediction History
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

        st.success("✅ Prediction Completed Successfully")

        st.subheader("📊 Predicted Scores")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Math Score",
            result["Math"]
        )

        c2.metric(
            "Reading Score",
            result["Reading"]
        )

        c3.metric(
            "Writing Score",
            result["Writing"]
        )

        st.markdown("---")

        c4, c5 = st.columns(2)

        c4.metric(
            "Average Score",
            result["Average"]
        )

        with c5:

            if result["Status"] == "PASS":

                st.success("✅ PASS")

            else:

                st.error("❌ FAIL")

        st.markdown("---")

        category = result["Category"]

        if category == "Excellent":

            st.success(
                f"🏆 Performance Category: {category}"
            )

        elif category == "Good":

            st.info(
                f"📈 Performance Category: {category}"
            )

        elif category == "Average":

            st.warning(
                f"⚠️ Performance Category: {category}"
            )

        else:

            st.error(
                f"🚨 Performance Category: {category}"
            )

        st.markdown("---")

        
        # PDF Report
        filename = "student_report.pdf"

        generate_pdf(
            filename,
            st.session_state.username,
            result["Math"],
            result["Reading"],
            result["Writing"],
            result["Average"],
            result["Category"]
        )

        with open(filename, "rb") as pdf_file:

            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_file,
                file_name="Student_Report.pdf",
                mime="application/pdf"
            )

       
       