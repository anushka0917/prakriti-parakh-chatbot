import streamlit as st

from frontend.auth.login import render_login_form
from frontend.auth.signup import render_signup_form


def render_auth_panel():
    left, right = st.columns([0.82, 1.18], gap="large")

    with left:
        st.markdown(
            """
<div class="auth-card">
  <div class="section-label">Private Account</div>
  <h2>Your readings stay with you.</h2>
  <p>Create an account to keep this app ready for your own prakriti reflections. The local database stores your account securely on this machine.</p>
  <div class="dosha-stack">
    <div class="dosha-line"><div>🔐</div><div><b>Secure signup</b><span>Passwords are salted and hashed before storage.</span></div></div>
    <div class="dosha-line"><div>🪷</div><div><b>Calm entry</b><span>Login once, then begin your reading.</span></div></div>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

    with right:
        if st.session_state.auth_view == "signup":
            st.markdown(
                """
<div class="auth-card auth-heading-card">
  <div class="section-label">Create Account</div>
  <h2>Sign up</h2>
  <p>Use your name, email, and a password of at least 8 characters.</p>
</div>
""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
<div class="auth-card auth-heading-card">
  <div class="section-label">Welcome Back</div>
  <h2>Log in</h2>
  <p>Enter your account details to continue your prakriti reading.</p>
</div>
""",
                unsafe_allow_html=True,
            )

        if st.session_state.auth_view == "signup":
            render_signup_form()
        else:
            render_login_form()
