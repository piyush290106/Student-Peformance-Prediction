import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard():

    df = pd.read_csv(
        "data/students.csv"
    )

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(df.head())

    st.subheader(
        "Math Score Distribution"
    )

    fig = px.histogram(
        df,
        x="math score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "Gender Distribution"
    )

    fig2 = px.pie(
        df,
        names="gender"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader(
        "Reading vs Writing"
    )

    fig3 = px.scatter(
        df,
        x="reading score",
        y="writing score"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )