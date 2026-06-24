import streamlit as st
import pandas as pd
import plotly.express as px


def show_model_comparison():

    st.title("🤖 Machine Learning Model Comparison")
    st.markdown(
        "Compare the performance of different Machine Learning models used for Student Performance Prediction."
    )


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

    # ==========================================
    # BEST MODEL CARD
    # ==========================================

    best_model = results.loc[
        results["R2 Score"].idxmax()
    ]

    st.success(
        f"🏆 Best Model: {best_model['Model']} | R² Score = {best_model['R2 Score']}"
    )

    st.markdown("---")

    st.subheader("📈 Accuracy Comparison")

    fig = px.bar(
        results,
        x="Model",
        y="R2 Score",
        text="R2 Score",
        color="R2 Score",
        color_continuous_scale="Viridis",
        title="Model Accuracy Comparison"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        height=500,
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(size=14),
        xaxis_title="Machine Learning Models",
        yaxis_title="R² Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🥇 Model Ranking")

    ranking = results.sort_values(
        by="R2 Score",
        ascending=False
    ).reset_index(drop=True)

    ranking.index = ranking.index + 1

    st.table(ranking)

    st.markdown("---")


    # ==========================================
    # FINAL CONCLUSION
    # ==========================================

    st.subheader("📝 Final Conclusion")

    st.success(
        """
        Based on model evaluation, Random Forest achieved the highest predictive accuracy (R² = 0.91).

        Therefore, Random Forest is selected as the final model for Student Performance Prediction due to:

        • Higher Accuracy

        • Better Generalization

        • Reduced Overfitting

        • Strong Performance on Student Dataset
        """
    )

    st.markdown("---")

    