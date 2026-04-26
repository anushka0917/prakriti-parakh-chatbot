import html

import streamlit as st

from config import COMPLETION, DOSHA, STATIC
from auth.session import logout_user
from database.chat_history import clear_chat_history, load_chat_history
from frontend.theme import active_label


def confidence_value(raw) -> int:
    try:
        return max(35, min(98, int(float(raw))))
    except Exception:
        return 64


def complete_advice(advice: str, prakriti: str) -> str:
    text = str(advice or STATIC.get(prakriti, STATIC["vata"])).strip()
    if not text:
        text = STATIC.get(prakriti, STATIC["vata"])

    if text.endswith((".", "!", "?", "।")):
        return text

    last_sentence_end = max(text.rfind("."), text.rfind("!"), text.rfind("?"), text.rfind("।"))
    if last_sentence_end > 80:
        text = text[: last_sentence_end + 1]

    return f"{text} {COMPLETION.get(prakriti, COMPLETION['vata'])}"


def render_bot_message(payload: dict) -> str:
    prakriti = str(payload.get("prakriti", "vata")).lower()
    confidence = confidence_value(payload.get("confidence", 64))
    advice_text = complete_advice(payload.get("advice", STATIC.get(prakriti, STATIC["vata"])), prakriti)
    advice = html.escape(advice_text).replace("**", "")
    source = html.escape(payload.get("source", "Guided Fallback"))
    dosha = DOSHA.get(prakriti, DOSHA["vata"])

    return f"""
<div class="result-shell" style="--dosha:{dosha["color"]};">
  <div class="result-topline">
    <span>{source}</span>
    <span>{confidence}% resonance</span>
  </div>
  <div class="result-head">
    <div class="result-icon">{dosha["icon"]}</div>
    <div>
      <div class="result-kicker">Prakriti reflection</div>
      <div class="result-title">{dosha["title"]} is most present today</div>
    </div>
  </div>
  <div class="meter" aria-label="Confidence {confidence}%">
    <div class="meter-fill" style="width:{confidence}%"></div>
  </div>
  <div class="result-copy">
    <h4>Personalised Wisdom</h4>
    <p>{advice}</p>
  </div>
</div>
"""


def render_hero():
    st.markdown(
        """
<div class="app-shell">
  <section class="hero-grid">
    <div class="hero-copy">
      <div>
        <div class="brand-row">
          <div class="brand-lockup">
            <div class="mark">🪷</div>
            <div>
              <div class="brand-name">Prakriti Parakh</div>
              <div class="brand-sub">Ayurvedic constitution guide</div>
            </div>
          </div>
        </div>
        <div class="eyebrow">Body signals · Mind patterns · Daily rhythm</div>
        <h1 class="hero-title">Find the dosha pattern <span>speaking through today.</span></h1>
        <p class="hero-sub">A calm diagnostic chat for Vata, Pitta, and Kapha tendencies, shaped into simple food, routine, and lifestyle guidance.</p>
      </div>
      <div class="hero-stat-row">
        <div class="hero-stat"><strong>Vata</strong><span>Dryness, restlessness, light sleep</span></div>
        <div class="hero-stat"><strong>Pitta</strong><span>Heat, acidity, sharp hunger</span></div>
        <div class="hero-stat"><strong>Kapha</strong><span>Heaviness, calm, slow energy</span></div>
      </div>
    </div>
    <div class="visual-card">
      <div class="visual-caption">Begin with how your body feels. The reading returns a likely prakriti tendency with a confidence signal and practical next steps.</div>
    </div>
  </section>
</div>
""",
        unsafe_allow_html=True,
    )


def render_controls(theme_mode: str):
    st.markdown('<div class="control-strip">', unsafe_allow_html=True)
    columns = st.columns([1, 1, 1, 1.1, 1, 1, 1])
    theme_light, theme_dark, theme_auto, new_chat, clear_chat, auth_left, auth_right = columns

    with theme_light:
        if st.button(active_label(theme_mode, "light", "Light"), key="theme_light", use_container_width=True):
            st.session_state.theme = "light"
            st.rerun()

    with theme_dark:
        if st.button(active_label(theme_mode, "dark", "Dark"), key="theme_dark", use_container_width=True):
            st.session_state.theme = "dark"
            st.rerun()

    with theme_auto:
        if st.button(active_label(theme_mode, "auto", "Auto"), key="theme_auto", use_container_width=True):
            st.session_state.theme = "auto"
            st.rerun()

    with new_chat:
        if st.button("New Chat", key="new_chat", use_container_width=True):
            st.session_state.messages = []
            if st.session_state.user:
                clear_chat_history(st.session_state.user["id"])
            st.rerun()

    with clear_chat:
        if st.button("Clear", key="clear_chat", use_container_width=True):
            st.session_state.messages = []
            if st.session_state.user:
                clear_chat_history(st.session_state.user["id"])
            st.rerun()

    if st.session_state.user:
        with auth_left:
            st.markdown(f'<div class="user-chip">Hi, {html.escape(st.session_state.user["name"].split()[0])}</div>', unsafe_allow_html=True)
        with auth_right:
            if st.button("Logout", key="logout", use_container_width=True):
                logout_user()
                st.rerun()
    else:
        with auth_left:
            if st.button("Login", key="show_login", use_container_width=True):
                st.session_state.auth_view = "login"
                st.rerun()
        with auth_right:
            if st.button("Sign Up", key="show_signup", use_container_width=True):
                st.session_state.auth_view = "signup"
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def render_reading_area():
    left, right = st.columns([0.82, 1.18], gap="large")

    with left:
        st.markdown(
            """
<div class="reading-copy">
  <div class="section-label">Begin The Reading</div>
  <h2 class="section-title">Choose a starting signal.</h2>
  <p class="section-copy">Pick the phrase closest to your present state, or type a fuller description below. Short, honest body cues work best.</p>
  <div class="dosha-stack">
    <div class="dosha-line"><div>🌬</div><div><b>Vata cues</b><span>Cold, dry, anxious, irregular, scattered</span></div></div>
    <div class="dosha-line"><div>🔥</div><div><b>Pitta cues</b><span>Hot, sharp, acidic, driven, irritated</span></div></div>
    <div class="dosha-line"><div>🌿</div><div><b>Kapha cues</b><span>Heavy, slow, steady, sleepy, grounded</span></div></div>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

    with right:
        chat_tab, history_tab = st.tabs(["Chat", "History"])

        with chat_tab:
            if not st.session_state.messages:
                st.markdown('<div class="suggestion-panel">', unsafe_allow_html=True)
                suggestions = [
                    ("🌬", "Cold hands, dry skin, restless thoughts"),
                    ("🔥", "Acidity, overheating, sharp hunger"),
                    ("🌿", "Heavy body, deep sleep, slow energy"),
                    ("🫧", "Anxiety, low appetite, scattered mind"),
                    ("💧", "Oily skin, hot flashes, irritability"),
                    ("🌙", "Steady energy, calm mood, love of sleep"),
                ]
                col1, col2 = st.columns(2, gap="small")
                for index, (icon, label) in enumerate(suggestions):
                    column = col1 if index % 2 == 0 else col2
                    with column:
                        st.markdown('<div class="sug-col">', unsafe_allow_html=True)
                        if st.button(f"{icon}  {label}", key=f"suggestion_{index}", use_container_width=True):
                            st.session_state.user_input = label
                        st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            for message in st.session_state.messages:
                avatar = "🧑🏽" if message["role"] == "user" else "🪷"
                with st.chat_message(message["role"], avatar=avatar):
                    st.markdown(message["content"], unsafe_allow_html=True)

        with history_tab:
            history = load_chat_history(st.session_state.user["id"]) if st.session_state.user else []
            if not history:
                st.markdown(
                    '<div class="history-empty">No saved readings yet. Start a chat and it will appear here.</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown('<div class="history-list">', unsafe_allow_html=True)
                for index, message in enumerate(history, start=1):
                    label = "You" if message["role"] == "user" else "Prakriti Parakh"
                    st.markdown(
                        f"""
<div class="history-item">
  <div class="history-label">{index}. {label}</div>
  <div class="history-copy">{message["content"]}</div>
</div>
""",
                        unsafe_allow_html=True,
                    )
                st.markdown("</div>", unsafe_allow_html=True)


def render_footer():
    st.markdown(
        '<div class="footer-note">Rooted in Charaka Samhita · Made for calm daily reflection</div>',
        unsafe_allow_html=True,
    )
