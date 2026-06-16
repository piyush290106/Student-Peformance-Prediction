import streamlit as st
import pandas as pd


def show_home():

    df = pd.read_csv("data/students.csv")

    # ==========================
    # CUSTOM CSS
    # ==========================

    st.markdown("""
    <style>

    .hero{
        background: linear-gradient(
            135deg,
            #2563eb,
            #7c3aed
        );
        padding:35px;
        border-radius:20px;
        color:white;
        text-align:center;
        margin-bottom:25px;
        box-shadow:0px 8px 25px rgba(0,0,0,0.15);
    }

    .feature-card{
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 4px 15px rgba(0,0,0,0.1);
        text-align:center;
        margin-bottom:15px;
    }

    [data-testid="metric-container"]{
        background:white;
        border:1px solid #e5e7eb;
        padding:15px;
        border-radius:15px;
        box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # HERO SECTION
    # ==========================

    st.markdown("""
    <div class="hero">

    <h1>🎓 Student Performance Prediction System</h1>

    <h4>
    Machine Learning Based Academic Analytics Platform
    </h4>

    <p>
    Predict student performance using AI,
    visualize analytics and generate reports.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ==========================
    # KPI CARDS
    # ==========================

    st.subheader("📊 Overview")

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

    # ==========================
    # FEATURES
    # ==========================

    st.subheader("🚀 Platform Features")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="feature-card">
        <h3>🎯 Prediction</h3>
        <p>
        Predict student academic performance
        using Machine Learning.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="feature-card">
        <h3>📊 Analytics</h3>
        <p>
        Interactive dashboard with charts,
        insights and visualizations.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="feature-card">
        <h3>📄 Reports</h3>
        <p>
        Generate downloadable PDF reports
        for predictions.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ==========================
    # PROJECT INFO
    # ==========================

    st.success(
        "✅ Student Performance Prediction System is running successfully."
    )

    st.info(
        "Use the sidebar to access Prediction, Dashboard, History, and Model Comparison modules."
    )

    # ==========================
    # FOOTER
    # ==========================

    st.markdown("""
    <hr>

    <center>

    <b>Student Performance Prediction System</b>

    <br>

    Python • Streamlit • Scikit-Learn • SQLite • Plotly

    </center>
    """, unsafe_allow_html=True)