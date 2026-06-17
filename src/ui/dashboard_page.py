import streamlit as st
import pandas as pd
import plotly.express as px


def show_dashboard_page():

    # ==========================
    # LOAD DATA
    # ==========================

    df = pd.read_csv("data/students.csv")

    # ==========================
    # PAGE HEADER
    # ==========================

    st.title("📊 Student Analytics Dashboard")
    st.markdown("Comprehensive analysis of student performance data")

    chart_layout = dict(
        height=500,
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(size=14)
    )

    # ==========================
    # KPI CARDS
    # ==========================

    st.subheader("📌 Key Performance Indicators")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "👥 Total Students",
            len(df)
        )

    with c2:
        st.metric(
            "📐 Avg Math",
            round(df["math score"].mean(), 1)
        )

    with c3:
        st.metric(
            "📖 Avg Reading",
            round(df["reading score"].mean(), 1)
        )

    with c4:
        st.metric(
            "✍️ Avg Writing",
            round(df["writing score"].mean(), 1)
        )

    st.markdown("---")

    # ==========================
    # SCORE DISTRIBUTION
    # ==========================

    st.subheader("📈 Score Distribution")

    col1, col2 = st.columns(2)

    with col1:

        fig_math = px.histogram(
            df,
            x="math score",
            nbins=20,
            title="Math Score Distribution",
            color_discrete_sequence=["#14b8a6"]
        )

        fig_math.update_layout(**chart_layout)

        st.plotly_chart(
            fig_math,
            use_container_width=True
        )

    with col2:

        fig_reading = px.histogram(
            df,
            x="reading score",
            nbins=20,
            title="Reading Score Distribution",
            color_discrete_sequence=["#0ea5e9"]
        )

        fig_reading.update_layout(**chart_layout)

        st.plotly_chart(
            fig_reading,
            use_container_width=True
        )

    st.markdown("---")

    # ==========================
    # GENDER ANALYSIS
    # ==========================

    st.subheader("👨‍🎓 Gender Analysis")

    col1, col2 = st.columns(2)

    with col1:

        fig_gender = px.pie(
            df,
            names="gender",
            title="Gender Distribution",
            hole=0.45
        )

        fig_gender.update_layout(**chart_layout)

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

        fig_gender_bar.update_layout(**chart_layout)

        st.plotly_chart(
            fig_gender_bar,
            use_container_width=True
        )

    st.markdown("---")

    # ==========================
    # READING VS WRITING
    # ==========================

    st.subheader("📚 Reading vs Writing Relationship")

    fig_scatter = px.scatter(
        df,
        x="reading score",
        y="writing score",
        color="gender",
        size="math score",
        title="Reading vs Writing Scores"
    )

    fig_scatter.update_layout(**chart_layout)

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # CORRELATION HEATMAP
    # ==========================

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
        title="Correlation Between Scores",
        color_continuous_scale="Blues"
    )

    fig_heatmap.update_layout(**chart_layout)

    st.plotly_chart(
        fig_heatmap,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # LUNCH ANALYSIS
    # ==========================

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

    fig_lunch.update_layout(**chart_layout)

    st.plotly_chart(
        fig_lunch,
        use_container_width=True
    )

    st.dataframe(
        lunch_avg,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # TEST PREPARATION ANALYSIS
    # ==========================

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

    fig_prep.update_layout(**chart_layout)

    st.plotly_chart(
        fig_prep,
        use_container_width=True
    )

    st.dataframe(
        prep_avg,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================
    # TOP STUDENTS
    # ==========================

    st.subheader("🏆 Top 10 Students")

    df["Average Score"] = (
        df["math score"] +
        df["reading score"] +
        df["writing score"]
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

    # ==========================
    # DATASET PREVIEW
    # ==========================

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )