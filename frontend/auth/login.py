import streamlit as st

from auth.session import login_user
from database.users import verify_user


def render_login_form():
    with st.form("login_form", clear_on_submit=False):
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        submitted = st.form_submit_button("Login", use_container_width=True)

    if submitted:
        ok, message, user = verify_user(email, password)
        if ok:
            login_user(user)
            st.success(message)
            st.rerun()
        else:
            st.error(message)

    st.markdown("Don’t have an account?")
    if st.button("Create one", key="switch_to_signup", use_container_width=True):
        st.session_state.auth_view = "signup"
        st.rerun()
