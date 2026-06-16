import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard_page():

    df = pd.read_csv("data/students.csv")

    st.title("📊 Student Analytics Dashboard")
    st.markdown("Comprehensive analysis of student performance data")

    # ==========================================
    # KPI CARDS
    # ==========================================

    st.subheader("📌 Key Performance Indicators")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Students",
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

    # ==========================================
    # SCORE DISTRIBUTION
    # ==========================================

    st.subheader("📈 Score Distribution")

    col1, col2 = st.columns(2)

    with col1:

        fig_math = px.histogram(
            df,
            x="math score",
            nbins=20,
            title="Math Score Distribution"
        )

        st.plotly_chart(
            fig_math,
            use_container_width=True
        )

    with col2:

        fig_reading = px.histogram(
            df,
            x="reading score",
            nbins=20,
            title="Reading Score Distribution"
        )

        st.plotly_chart(
            fig_reading,
            use_container_width=True
        )

    st.markdown("---")

    # ==========================================
    # GENDER ANALYSIS
    # ==========================================

    st.subheader("👨‍🎓 Gender Analysis")

    col1, col2 = st.columns(2)

    with col1:

        fig_gender = px.pie(
            df,
            names="gender",
            title="Gender Distribution"
        )

        st.plotly_chart(
            fig_gender,
            use_container_width=True
        )

    with col2:

        gender_scores = (
            df.groupby("gender")[
                [
                    "math score",
                    "reading score",
                    "writing score"
                ]
            ]
            .mean()
            .reset_index()
        )

        fig_gender_bar = px.bar(
            gender_scores,
            x="gender",
            y=[
                "math score",
                "reading score",
                "writing score"
            ],
            barmode="group",
            title="Average Scores by Gender"
        )

        st.plotly_chart(
            fig_gender_bar,
            use_container_width=True
        )

    st.markdown("---")

    # ==========================================
    # READING VS WRITING
    # ==========================================

    st.subheader("📚 Reading vs Writing Relationship")

    fig_scatter = px.scatter(
        df,
        x="reading score",
        y="writing score",
        color="gender",
        title="Reading vs Writing Scores"
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # CORRELATION HEATMAP
    # ==========================================

    st.subheader("🔥 Correlation Heatmap")

    corr = df[
        [
            "math score",
            "reading score",
            "writing score"
        ]
    ].corr()

    fig_heatmap = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Between Scores"
    )

    st.plotly_chart(
        fig_heatmap,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # LUNCH ANALYSIS
    # ==========================================

    st.subheader("🍽 Lunch Type Impact")

    lunch_avg = (
        df.groupby("lunch")[
            [
                "math score",
                "reading score",
                "writing score"
            ]
        ]
        .mean()
        .reset_index()
    )

    fig_lunch = px.bar(
        lunch_avg,
        x="lunch",
        y=[
            "math score",
            "reading score",
            "writing score"
        ],
        barmode="group",
        title="Performance by Lunch Type"
    )

    st.plotly_chart(
        fig_lunch,
        use_container_width=True
    )

    st.dataframe(
        lunch_avg,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # TEST PREPARATION ANALYSIS
    # ==========================================

    st.subheader("📝 Test Preparation Analysis")

    prep_avg = (
        df.groupby("test preparation course")[
            [
                "math score",
                "reading score",
                "writing score"
            ]
        ]
        .mean()
        .reset_index()
    )

    fig_prep = px.bar(
        prep_avg,
        x="test preparation course",
        y=[
            "math score",
            "reading score",
            "writing score"
        ],
        barmode="group",
        title="Impact of Test Preparation"
    )

    st.plotly_chart(
        fig_prep,
        use_container_width=True
    )

    st.dataframe(
        prep_avg,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # TOP PERFORMERS
    # ==========================================

    st.subheader("🏆 Top 10 Students")

    df["Average Score"] = (
        df["math score"]
        + df["reading score"]
        + df["writing score"]
    ) / 3

    top_students = df.sort_values(
        by="Average Score",
        ascending=False
    ).head(10)

    st.dataframe(
        top_students,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # DATASET PREVIEW
    # ==========================================

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )