import streamlit as st

from src.ui.home import show_home
from src.ui.prediction_page import show_prediction_page
from src.ui.dashboard_page import show_dashboard_page
from src.ui.model_comparison_page import show_model_comparison

from src.auth.database import create_users_table
from src.auth.register import register_user
from src.auth.login import login_user
from src.ui.history_page import show_history_page


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Student Performance Prediction System",
    page_icon="🎓",
    layout="wide"
)
def load_css():

    with open(
        "src/styles/style.css"
    ) as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ==================================================
# DATABASE SETUP
# ==================================================

create_users_table()

# ==================================================
# SESSION STATE
# ==================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ==================================================
# LOGIN / REGISTER PAGE
# ==================================================

# ==================================================
# LOGIN / REGISTER PAGE
# ==================================================

# ==================================================
# LOGIN / REGISTER PAGE
# ==================================================

if not st.session_state.logged_in:

    st.markdown("""
    <div class="auth-card">

    <h1 class="main-title">
    🎓 Student Performance Prediction
    </h1>

    <p class="sub-title">
    Machine Learning Based Student Analytics Platform
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("## 🔐 Account Access")

        auth_option = st.radio(
            "Select Option",
            ["Login", "Register"]
        )

        username = st.text_input(
            "👤 Username"
        )

        password = st.text_input(
            "🔑 Password",
            type="password"
        )

        # ---------------- REGISTER ----------------

        if auth_option == "Register":

            if st.button(
                "✨ Create Account",
                use_container_width=True
            ):

                if username.strip() == "" or password.strip() == "":

                    st.warning(
                        "Please fill all fields"
                    )

                else:

                    success = register_user(
                        username,
                        password
                    )

                    if success:

                        st.success(
                            "✅ Account created successfully. Please login."
                        )

                    else:

                        st.error(
                            "❌ Username already exists."
                        )

        # ---------------- LOGIN ----------------

        else:

            if st.button(
                "🚀 Login",
                use_container_width=True
            ):

                user = login_user(
                    username,
                    password
                )

                if user:

                    st.session_state.logged_in = True
                    st.session_state.username = username

                    st.rerun()

                else:

                    st.error(
                        "❌ Invalid username or password."
                    )

    st.stop()# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.success(
    f"👤 Logged in as: {st.session_state.username}"
)

if st.sidebar.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.session_state.username = ""

    st.rerun()

st.sidebar.title("🎓 Student Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🎯 Prediction",
        "📜 History",
        "📊 Dashboard",
        "🤖 Model Comparison"
    ]
)

# ==================================================
# PAGE ROUTING
# ==================================================

if page == "🏠 Home":

    show_home()

elif page == "🎯 Prediction":

    show_prediction_page()

elif page == "📊 Dashboard":

    show_dashboard_page()

elif page == "🤖 Model Comparison":

    show_model_comparison()
elif page == "📜 History":

    show_history_page()