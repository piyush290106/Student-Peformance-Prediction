import streamlit as st

# ALL IMPORTS HERE
from src.ui.home import show_home
from src.ui.prediction_page import show_prediction_page
from src.ui.dashboard_page import show_dashboard_page
from src.ui.model_comparison_page import show_model_comparison
from src.ui.history_page import show_history_page
from src.ui.admin_dashboard import show_admin_dashboard

from src.auth.database import create_users_table
from src.auth.register import register_user
from src.auth.login import login_user




# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Student Performance Prediction System",
    page_icon="🎓",
    layout="wide"
)


# ==========================================
# LOAD CSS
# ==========================================

def load_css():
    try:
        with open("src/styles/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except:
        pass


load_css()


# ==========================================
# DATABASE
# ==========================================

create_users_table()


# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = ""

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "Login"


# ==========================================
# LOGIN / REGISTER PAGE
# ==========================================

# ==================================================
# AUTHENTICATION PAGES
# ==================================================

if not st.session_state.logged_in:

    # ---------------- LOGIN PAGE ----------------

    if st.session_state.auth_page == "Login":

        st.markdown("""
<div class="auth-card">

<h1 class="main-title">
🎓 Student Performance Prediction System
</h1>



<hr style="border:1px solid #e2e8f0;">



</div>
""", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,2,1])

        with col2:

            st.subheader("🔐 Login")

            username = st.text_input(
                "👤 Username"
            )

            password = st.text_input(
                "🔑 Password",
                type="password"
            )

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

                    st.session_state.username = user[0]

                    st.session_state.role = user[1]

                    st.rerun()

                else:

                    st.error(
                        "Invalid username or password"
                    )

            st.markdown("---")

            if st.button(
                "📝 Create New Account",
                use_container_width=True
            ):

                st.session_state.auth_page = "Register"

                st.rerun()

    # ---------------- REGISTER PAGE ----------------

    elif st.session_state.auth_page == "Register":

        st.markdown("""
        <div class="auth-card">
            <h1 class="main-title">
                🎓 Student Performance Prediction
            </h1>

            
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,2,1])

        with col2:

            st.subheader("📝 Register")

            username = st.text_input(
                "👤 Choose Username"
            )

            password = st.text_input(
                "🔑 Choose Password",
                type="password"
            )

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
                            "Account created successfully."
                        )

                        # Automatically go to login page
                        st.session_state.auth_page = "Login"

                        st.rerun()

                    else:

                        st.error(
                            "Username already exists"
                        )

            st.markdown("---")

            if st.button(
                "⬅ Back To Login",
                use_container_width=True
            ):

                st.session_state.auth_page = "Login"

                st.rerun()

    st.stop()
# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.success(
    f"👤 Logged in as: {st.session_state.username}"
)
st.sidebar.info(
    f"🔐 Role: {st.session_state.role.upper()}"
)

if st.sidebar.button("🚪 Logout"):

    st.session_state.logged_in = False

    st.session_state.username = ""

    st.session_state.role = ""

    st.rerun()

st.sidebar.title("🎓 Student Analytics")

menu = [
    "🏠 Home",
    "🎯 Prediction",
    "📜 History",
    "📊 Dashboard",
    "🤖 Model Comparison"
]

if st.session_state.role == "admin":
    menu.append(
        "👨‍💼 Admin Dashboard"
    )

page = st.sidebar.radio(
    "Navigation",
    menu
)


# ==========================================
# PAGE ROUTING
# ==========================================

if page == "🏠 Home":

    show_home()
elif page == "👨‍💼 Admin Dashboard":

    show_admin_dashboard()

elif page == "🎯 Prediction":

    show_prediction_page()

elif page == "📜 History":

    show_history_page()

elif page == "📊 Dashboard":

    show_dashboard_page()

elif page == "🤖 Model Comparison":

    show_model_comparison()