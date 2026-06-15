import streamlit as st

from src.database.history import get_history


def show_history_page():

    st.title(
        "📜 Prediction History"
    )

    df = get_history(
        st.session_state.username
    )

    st.dataframe(
        df,
        use_container_width=True
    )