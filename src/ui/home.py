import streamlit as st
import pandas as pd


def show_home():

    df = pd.read_csv("data/students.csv")

    # ==========================
    # CUSTOM CSS - CREATIVE DESIGN
    # ==========================

    st.markdown("""
    <style>

    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 60px 40px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0px 15px 40px rgba(102, 126, 234, 0.4);
        animation: fadeInDown 0.8s ease-out;
    }

    .hero h1 {
        font-size: 48px;
        font-weight: 800;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }

    .hero .tagline {
        font-size: 22px;
        color: rgba(255, 255, 255, 0.95);
        margin-top: 15px;
        font-weight: 300;
        letter-spacing: 0.5px;
    }

    .hero .description {
        font-size: 16px;
        color: rgba(255, 255, 255, 0.85);
        margin-top: 15px;
        line-height: 1.6;
    }

    /* Feature Cards */
    .feature-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-left: 5px solid #667eea;
        margin-bottom: 20px;
    }

    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0px 15px 35px rgba(102, 126, 234, 0.3);
    }

    .feature-card h3 {
        color: #2d3748;
        font-size: 24px;
        margin-bottom: 10px;
    }

    .feature-card p {
        color: #4a5568;
        font-size: 15px;
        line-height: 1.6;
    }

    /* Stats Cards */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 8px 20px rgba(102, 126, 234, 0.3);
        transition: transform 0.3s ease;
    }

    [data-testid="metric-container"]:hover {
        transform: scale(1.05);
    }

    [data-testid="metric-container"] > div:first-child {
        color: rgba(255, 255, 255, 0.9);
        font-size: 14px;
        font-weight: 600;
    }

    [data-testid="metric-container"] > div:last-child {
        color: white;
        font-size: 32px;
        font-weight: 800;
    }

    /* Section Headers */
    .section-header {
        font-size: 28px;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 25px;
        padding-bottom: 10px;
        border-bottom: 3px solid #667eea;
        display: inline-block;
    }

    /* CTA Button Style */
    .cta-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 40px;
        border-radius: 10px;
        font-weight: 600;
        text-align: center;
        display: inline-block;
        margin-top: 10px;
        box-shadow: 0px 5px 15px rgba(102, 126, 234, 0.3);
        transition: transform 0.2s ease;
    }

    .cta-button:hover {
        transform: scale(1.05);
    }

    /* Info Boxes */
    .info-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0px 8px 20px rgba(245, 87, 108, 0.3);
    }

    .success-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0px 8px 20px rgba(79, 172, 254, 0.3);
    }

    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #718096;
        font-size: 13px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 2px solid #e2e8f0;
    }

    .footer b {
        color: #2d3748;
        font-size: 15px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # HERO SECTION
    # ==========================

    st.markdown("""
<<<<<<< HEAD
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
    
    
=======
    <div class="hero">
        <h1>🎓 Student Performance Prediction</h1>
        <div class="tagline">Intelligent Academic Analytics Platform</div>
        <div class="description">
            Harness the power of AI and Machine Learning to predict student performance,
            uncover hidden patterns, and make data-driven educational decisions.
        </div>
    </div>
    """, unsafe_allow_html=True)
>>>>>>> 10e204914c61ed8ccbd1c7d246d882410804dad7

    # ==========================
    # KEY STATISTICS
    # ==========================

    st.markdown("<div class='section-header'>📊 Key Statistics</div>", unsafe_allow_html=True)
    st.markdown("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("👥 Total Students", len(df))

    with c2:
        st.metric("📐 Avg Math Score", f"{df['math score'].mean():.1f}")

    with c3:
        st.metric("📖 Avg Reading Score", f"{df['reading score'].mean():.1f}")

    with c4:
        st.metric("✍️ Avg Writing Score", f"{df['writing score'].mean():.1f}")

    st.markdown("---")

<<<<<<< HEAD
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

    
   

   
=======
    # ==========================
    # FEATURES & CAPABILITIES
    # ==========================

    st.markdown("<div class='section-header'>🚀 Platform Features</div>", unsafe_allow_html=True)
    st.markdown("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Smart Prediction</h3>
            <p>
            Leverage advanced ML models to forecast student academic performance with high accuracy. Get personalized insights for each student.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 Interactive Analytics</h3>
            <p>
            Visualize student data through beautiful charts, dashboards, and real-time analytics. Identify trends and patterns instantly.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>📄 Smart Reports</h3>
            <p>
            Generate professional PDF reports with predictions, charts, and insights. Download and share with stakeholders easily.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>💾 Data History</h3>
            <p>
            Track all predictions and model outputs over time. Access complete audit trails and historical analysis data.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>⚖️ Model Comparison</h3>
            <p>
            Compare multiple ML models side-by-side. View performance metrics and choose the best model for your needs.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🔐 Secure Access</h3>
            <p>
            User authentication system with secure login and registration. Protect sensitive student data with account management.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ==========================
    # GET STARTED
    # ==========================

    st.markdown("<div class='section-header'>🌟 Get Started</div>", unsafe_allow_html=True)
    st.markdown("")

    col_left, col_middle, col_right = st.columns([1, 2, 1])

    with col_middle:
        st.markdown("""
        <div class="success-box" style="text-align: center;">
            <h3>✅ System Ready!</h3>
            <p>Your Student Performance Prediction System is running smoothly.</p>
            <p>Use the sidebar menu to explore all features and get started.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: #f8f9fa; border-radius: 10px;">
            <h4>🔮 Make Predictions</h4>
            <p style="font-size: 13px; color: #666;">Use ML to predict student performance</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: #f8f9fa; border-radius: 10px;">
            <h4>📈 View Dashboard</h4>
            <p style="font-size: 13px; color: #666;">Explore interactive analytics & insights</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: #f8f9fa; border-radius: 10px;">
            <h4>📑 Generate Reports</h4>
            <p style="font-size: 13px; color: #666;">Create downloadable PDF reports</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ==========================
    # TECHNOLOGY STACK
    # ==========================

    st.markdown("""
    <div class="footer">
        <b>🛠️ Built With</b><br>
        Python • Streamlit • Scikit-Learn • Pandas • SQLite • Plotly • Reportlab
    </div>
    """, unsafe_allow_html=True)
>>>>>>> 10e204914c61ed8ccbd1c7d246d882410804dad7
