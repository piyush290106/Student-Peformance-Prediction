import streamlit as st
import pandas as pd


def show_home():

    df = pd.read_csv("data/students.csv")

    st.markdown("""
    <style>

    .hero {
        background: linear-gradient(
            135deg,
            #14b8a6,
            #0ea5e9
        );
        padding: 60px 40px;
        border-radius: 25px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0px 15px 40px rgba(14,165,233,0.25);
    }

    .hero h1{
        font-size: 55px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .tagline{
        font-size: 22px;
        margin-bottom: 15px;
        color: rgba(255,255,255,0.95);
    }

    .description{
        font-size: 17px;
        color: rgba(255,255,255,0.9);
    }

    .section-header{
        font-size: 28px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 20px;
        border-bottom: 3px solid #14b8a6;
        display: inline-block;
        padding-bottom: 8px;
    }

    .feature-card{
        background: white;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
        border-top: 5px solid #14b8a6;
        margin-bottom: 15px;
    }

    .feature-card h3{
        color: #0f172a;
    }

    .feature-card p{
        color: #475569;
    }

    .success-box{
        background: linear-gradient(
            135deg,
            #14b8a6,
            #0ea5e9
        );
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
    }

    .footer{
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        color: #64748b;
        border-top: 2px solid #e2e8f0;
    }

    </style>
    """, unsafe_allow_html=True)

    # HERO SECTION

    st.markdown("""
<div style="
    background: linear-gradient(135deg,#14b8a6,#0ea5e9);
    padding:50px;
    border-radius:25px;
    text-align:center;
    box-shadow:0 15px 40px rgba(0,0,0,0.15);
    margin-bottom:40px;
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
    


    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "👥 Students",
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


    

    # FOOTER

    st.markdown("""
    <div class="footer">

    <b>🎓 Student Performance Prediction System</b><br><br>

    👨‍💻 Developed By<br>

    <b>Piyush Jain & Payal Panwar</b><br><br>


    </div>
    """, unsafe_allow_html=True)