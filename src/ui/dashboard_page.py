import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard_page():

    df = pd.read_csv("data/students.csv")

    st.title("📊 Analytics Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Students",
        len(df)
    )

    c2.metric(
        "Avg Math",
        round(df["math score"].mean(), 2)
    )

    c3.metric(
        "Avg Reading",
        round(df["reading score"].mean(), 2)
    )

    c4.metric(
        "Avg Writing",
        round(df["writing score"].mean(), 2)
    )

    st.markdown("---")

    st.subheader("Math Score Distribution")

    fig1 = px.histogram(
        df,
        x="math score"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.subheader("Gender Distribution")

    fig2 = px.pie(
        df,
        names="gender"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader("Reading vs Writing")

    fig3 = px.scatter(
        df,
        x="reading score",
        y="writing score"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )