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
<div style="
    background: linear-gradient(135deg,#14b8a6,#0ea5e9);
    padding:50px;
    border-radius:25px;
    text-align:center;
    box-shadow:0 15px 40px rgba(0,0,0,0.15);
">

<h1 style="
    color:white;
    font-size:60px;
    font-weight:800;
    margin-bottom:10px;
">
🎓 Student Performance Prediction System
</h1>


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

    st.markdown("""
<hr>

<div style="
    text-align:center;
    color:#64748b;
    font-size:100000px;
">

🎓 Student Performance Prediction System<br>

Developed by <b>Piyush Jain and Payal Panwar</b><br>


</div>
""", unsafe_allow_html=True)

    
   

   