import streamlit as st

from auth.session import login_user
from database.users import create_user


def render_signup_form():
    with st.form("signup_form", clear_on_submit=False):
        name = st.text_input("Name", key="signup_name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")
        confirm = st.text_input("Confirm password", type="password", key="signup_confirm")
        submitted = st.form_submit_button("Create Account", use_container_width=True)

    if submitted:
        if password != confirm:
            st.error("Passwords do not match.")
        else:
            ok, message, user = create_user(name, email, password)
            if ok:
                login_user(user)
                st.session_state.messages = []
                st.success(message)
                st.rerun()
            else:
                st.error(message)

    st.markdown("Already have an account?")
    if st.button("Log in instead", key="switch_to_login", use_container_width=True):
        st.session_state.auth_view = "login"
        st.rerun()
