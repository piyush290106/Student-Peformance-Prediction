import streamlit as st
import pandas as pd

from src.auth.database import (
    get_all_users,
    delete_user,
    update_user_role,
    get_all_prediction_history
)


def show_admin_dashboard():

    if "role" not in st.session_state:
        st.error("Please Login First")
        st.stop()

    if st.session_state.role != "admin":
        st.error("❌ Access Denied")
        st.stop()

    st.title("👨‍💼 Admin Dashboard")

    users = get_all_users()

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "👥 Total Users",
            len(users)
        )

    with c2:
        st.metric(
            "📜 Total Predictions",
            len(get_all_prediction_history())
        )

    st.markdown("---")

    tab1, tab2 = st.tabs(
        [
            "👥 User Management",
            "📜 All Predictions"
        ]
    )

    # Rest of your code here...    )
    # ==========================
    # USER MANAGEMENT
    # ==========================

    with tab1:

        st.subheader("Registered Users")

        users = get_all_users()

        df_users = pd.DataFrame(
            users,
            columns=[
                "ID",
                "Username",
                "Role"
            ]
        )

        st.dataframe(
            df_users,
            use_container_width=True
        )

        st.markdown("---")

        st.subheader("Manage User")

        user_ids = df_users["ID"].tolist()

        selected_id = st.selectbox(
            "Select User",
            user_ids
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("Make Admin"):

                update_user_role(
                    selected_id,
                    "admin"
                )

                st.success(
                    "Role updated."
                )

                st.rerun()

        with col2:

            if st.button("Delete User"):

                delete_user(
                    selected_id
                )

                st.success(
                    "User deleted."
                )

                st.rerun()

    # ==========================
    # ALL PREDICTIONS
    # ==========================

    with tab2:

        st.subheader(
            "All Prediction History"
        )

        history = get_all_prediction_history()

        st.dataframe(
            history,
            use_container_width=True
        )