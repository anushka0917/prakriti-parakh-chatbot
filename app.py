import html

import streamlit as st

from auth.session import init_session_state, is_logged_in, restore_user_from_token
from backend.prakriti_service import get_response
from database.chat_history import save_chat_message
from database.users import init_db
from frontend.auth.panel import render_auth_panel
from frontend.components import render_bot_message, render_controls, render_footer, render_hero, render_reading_area
from frontend.styles import app_css
from frontend.theme import active_theme


st.set_page_config(
    page_title="Prakriti Parakh",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="collapsed",
)


init_session_state()
init_db()
restore_user_from_token()

theme_mode, _ = active_theme(st.session_state.theme)
st.markdown(app_css(theme_mode), unsafe_allow_html=True)

render_hero()
render_controls(theme_mode)

if not is_logged_in():
    render_auth_panel()
    render_footer()
    st.stop()

render_reading_area()
render_footer()

user_input = st.chat_input("Describe your body, mood, digestion, sleep, appetite, or energy...")
if "user_input" in st.session_state:
    user_input = st.session_state.pop("user_input")

if user_input:
    safe_input = html.escape(user_input)
    st.session_state.messages.append({"role": "user", "content": safe_input})
    save_chat_message(st.session_state.user["id"], "user", safe_input)
    with st.chat_message("user", avatar="🧑🏽"):
        st.markdown(safe_input)

    with st.spinner("Reading your prakriti..."):
        data = get_response(user_input)

    bot_content = render_bot_message(data)
    st.session_state.messages.append({"role": "assistant", "content": bot_content})
    save_chat_message(st.session_state.user["id"], "assistant", bot_content)

    with st.chat_message("assistant", avatar="🪷"):
        st.markdown(bot_content, unsafe_allow_html=True)
