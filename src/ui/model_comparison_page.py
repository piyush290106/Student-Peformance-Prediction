import streamlit as st
import pandas as pd
import plotly.express as px


def show_model_comparison():

    st.title("🤖 Machine Learning Model Comparison")

    results = pd.DataFrame(
        {
            "Model": [
                "Linear Regression",
                "Decision Tree",
                "Gradient Boosting",
                "Random Forest"
            ],
            "R2 Score": [
                0.82,
                0.79,
                0.88,
                0.91
            ]
        }
    )

    st.subheader("📊 Model Performance Table")

    st.dataframe(
        results,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("📈 Accuracy Comparison")

    fig = px.bar(
        results,
        x="Model",
        y="R2 Score",
        text="R2 Score",
        title="Model Accuracy Comparison"
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    best_model = results.loc[
        results["R2 Score"].idxmax()
    ]

    st.success(
        f"🏆 Best Model: {best_model['Model']} "
        f"(R² Score = {best_model['R2 Score']})"
    )

    st.subheader("📋 Model Ranking")

    ranking = results.sort_values(
        by="R2 Score",
        ascending=False
    )

    ranking.index = range(
        1,
        len(ranking) + 1
    )

    st.table(ranking)

    st.markdown("---")

    st.subheader("📝 Interpretation")

    st.info(
        """
        Random Forest achieved the highest R² score,
        indicating superior predictive performance.

        Gradient Boosting also performed strongly.

        Decision Tree showed the lowest accuracy,
        likely due to overfitting.

        Therefore, Random Forest is selected as the
        final model for student score prediction.
        """
    )