import streamlit as st
import pandas as pd


def show_model_comparison():

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

    st.subheader("Model Comparison")

    st.dataframe(results)

    best = results.loc[
        results["R2 Score"].idxmax()
    ]

    st.success(
        f"Best Model: {best['Model']}"
    )