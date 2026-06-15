import streamlit as st
import pandas as pd


def show_home():

    df = pd.read_csv(
        "data/students.csv"
    )

    st.title(
        "📊 Student Analytics Dashboard"
    )

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Students",
        len(df)
    )

    c2.metric(
        "Avg Math",
        round(
            df["math score"].mean(),
            2
        )
    )

    c3.metric(
        "Avg Reading",
        round(
            df["reading score"].mean(),
            2
        )
    )

    c4.metric(
        "Avg Writing",
        round(
            df["writing score"].mean(),
            2
        )
    )

    st.success(
        "Student Performance Prediction System"
    )