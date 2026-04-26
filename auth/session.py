import streamlit as st

from database.chat_history import load_chat_history
from database.users import create_login_token, delete_login_token, get_user_by_token


def _query_token() -> str | None:
    token = st.query_params.get("session")
    if isinstance(token, list):
        return token[0] if token else None
    return token


def restore_user_from_token():
    if st.session_state.user:
        return

    token = _query_token()
    user = get_user_by_token(token) if token else None
    if user:
        st.session_state.user = user
        st.session_state.auth_token = token
        st.session_state.messages = load_chat_history(user["id"])


def init_session_state():
    defaults = {
        "theme": "auto",
        "messages": [],
        "auth_view": "login",
        "user": None,
        "auth_token": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def login_user(user: dict):
    st.session_state.user = user
    token = create_login_token(user["id"])
    st.session_state.auth_token = token
    st.query_params["session"] = token
    st.session_state.messages = load_chat_history(user["id"])


def logout_user():
    delete_login_token(st.session_state.get("auth_token") or _query_token())
    st.query_params.clear()
    st.session_state.user = None
    st.session_state.auth_token = None
    st.session_state.messages = []
    st.session_state.auth_view = "login"


def is_logged_in() -> bool:
    return bool(st.session_state.user)
