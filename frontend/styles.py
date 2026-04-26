from frontend.theme import root_theme_css


def app_css(theme_mode: str) -> str:
    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,650&display=swap');

{root_theme_css(theme_mode)}

* {{ box-sizing: border-box; }}

html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
  background:
    radial-gradient(circle at 12% 8%, rgba(66, 163, 130, 0.20), transparent 24rem),
    radial-gradient(circle at 86% 4%, rgba(217, 107, 91, 0.13), transparent 22rem),
    radial-gradient(circle at 58% 88%, rgba(118, 183, 216, 0.12), transparent 25rem),
    linear-gradient(135deg, var(--bg), var(--bg-2)) !important;
  color: var(--text) !important;
  font-family: Inter, sans-serif !important;
}}

body::before {{
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  opacity: 0.34;
  background-image:
    linear-gradient(var(--line) 1px, transparent 1px),
    linear-gradient(90deg, var(--line) 1px, transparent 1px);
  background-size: 56px 56px;
  mask-image: radial-gradient(circle at center, black, transparent 78%);
}}

#MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stStatusWidget"], .stDeployButton {{
  display: none !important;
}}

[data-testid="stMainBlockContainer"] {{
  max-width: 1180px !important;
  padding: 1.1rem 1.2rem 7.2rem !important;
}}

.block-container {{ padding-top: 0 !important; }}
[data-testid="stVerticalBlock"] {{ gap: 0.7rem !important; }}

.app-shell {{
  position: relative;
  border: 1px solid var(--line);
  background: linear-gradient(180deg, var(--panel), rgba(255,255,255,0.025));
  box-shadow: 0 24px 80px var(--shadow), inset 0 1px 0 rgba(255,255,255,0.08);
  backdrop-filter: blur(22px);
  border-radius: 8px;
  overflow: hidden;
}}

.app-shell::before {{
  content: "";
  position: absolute;
  inset: 0 0 auto 0;
  height: 4px;
  background: linear-gradient(90deg, var(--accent-2), var(--accent), var(--accent-3), var(--blue));
}}

.hero-grid {{
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(260px, 0.8fr);
  gap: 1rem;
  padding: 2rem;
  align-items: stretch;
}}

.hero-copy {{
  min-height: 390px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

.brand-row, .mini-row, .result-topline {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}}

.brand-lockup {{
  display: flex;
  align-items: center;
  gap: 0.75rem;
}}

.mark {{
  width: 44px;
  height: 44px;
  border-radius: 8px;
  border: 1px solid var(--line-strong);
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, rgba(66, 163, 130, 0.28), rgba(214, 167, 42, 0.18));
  font-size: 1.35rem;
}}

.brand-name {{
  color: var(--text);
  font-weight: 800;
  letter-spacing: 0.01em;
}}

.brand-sub, .eyebrow, .micro-label, .result-kicker, .footer-note {{
  color: var(--muted);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}}

.eyebrow {{
  margin: 2.4rem 0 0.9rem;
  color: var(--accent);
}}

.hero-title {{
  max-width: 780px;
  margin: 0;
  color: var(--text);
  font-family: Newsreader, serif;
  font-size: clamp(3.2rem, 7vw, 6.7rem);
  font-weight: 650;
  line-height: 0.88;
  letter-spacing: 0;
}}

.hero-title span {{ color: var(--accent-2); }}

.hero-sub {{
  max-width: 640px;
  margin: 1.1rem 0 0;
  color: var(--text-soft);
  font-family: Newsreader, serif;
  font-size: clamp(1.22rem, 2vw, 1.55rem);
  line-height: 1.45;
}}

.hero-stat-row {{
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.7rem;
  margin-top: 2rem;
}}

.hero-stat, .dosha-line {{
  border: 1px solid var(--line-strong);
  border-radius: 8px;
  background: var(--tile);
  box-shadow: 0 10px 24px rgba(0,0,0,0.04);
}}

.hero-stat {{ padding: 0.85rem; }}

.hero-stat strong {{
  display: block;
  color: var(--text);
  font-family: Newsreader, serif;
  font-size: 1.25rem;
  font-weight: 650;
}}

.hero-stat span {{
  display: block;
  margin-top: 0.25rem;
  color: var(--muted);
  font-size: 0.78rem;
  line-height: 1.35;
}}

.visual-card {{
  position: relative;
  min-height: 390px;
  border-left: 1px solid var(--line);
  background:
    radial-gradient(circle at 50% 35%, rgba(214, 167, 42, 0.26), transparent 8rem),
    radial-gradient(circle at 25% 80%, rgba(66, 163, 130, 0.18), transparent 10rem),
    linear-gradient(160deg, rgba(255,255,255,0.07), transparent);
  overflow: hidden;
}}

.visual-card::before {{
  content: "";
  position: absolute;
  inset: 2rem;
  border: 1px solid var(--line-strong);
  border-radius: 50%;
  background:
    repeating-conic-gradient(from 0deg, transparent 0deg 10deg, rgba(255,255,255,0.10) 10deg 11deg),
    radial-gradient(circle, transparent 0 34%, var(--line) 35% 35.6%, transparent 36% 100%);
  animation: breathe 16s ease-in-out infinite;
}}

.visual-card::after {{
  content: "🪷";
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: 6rem;
  filter: drop-shadow(0 18px 30px var(--shadow));
}}

.visual-caption {{
  position: absolute;
  left: 1rem;
  right: 1rem;
  bottom: 1rem;
  border: 1px solid var(--line-strong);
  border-radius: 8px;
  padding: 0.9rem;
  background: color-mix(in srgb, var(--panel) 84%, transparent);
  backdrop-filter: blur(16px);
  color: var(--text-soft);
  font-size: 0.86rem;
  line-height: 1.45;
}}

@keyframes breathe {{
  0%, 100% {{ transform: scale(0.96) rotate(0deg); opacity: 0.62; }}
  50% {{ transform: scale(1.02) rotate(8deg); opacity: 0.9; }}
}}

.control-strip {{
  margin-top: 1rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 0.55rem 0.75rem 0.35rem;
  background: linear-gradient(180deg, var(--panel), rgba(255,255,255,0.025));
  box-shadow: 0 16px 52px var(--shadow);
}}

.control-strip [data-testid="stHorizontalBlock"] {{
  align-items: center !important;
  gap: 0.45rem !important;
}}

.control-strip [data-testid="column"] {{
  padding: 0 0.12rem !important;
}}

.control-strip [data-testid="stButton"] {{
  margin-bottom: 0 !important;
}}

.control-strip .stButton > button {{
  height: 44px !important;
  min-height: 44px !important;
  padding: 0.35rem 0.65rem !important;
  font-size: 0.86rem !important;
  line-height: 1 !important;
  margin: 0 !important;
}}

.stButton > button {{
  min-height: 42px !important;
  border-radius: 8px !important;
  border: 1px solid var(--line-strong) !important;
  background: var(--tile) !important;
  color: var(--text-soft) !important;
  -webkit-text-fill-color: var(--text-soft) !important;
  font-family: Inter, sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: 0.02em !important;
  padding: 0.55rem 0.75rem !important;
  transition: transform 0.18s ease, border-color 0.18s ease, background 0.18s ease !important;
  box-shadow: 0 10px 24px rgba(0,0,0,0.06) !important;
}}

.stButton > button:hover {{
  transform: translateY(-1px) !important;
  border-color: var(--line-strong) !important;
  background: var(--tile-hover) !important;
  color: var(--text) !important;
  -webkit-text-fill-color: var(--text) !important;
}}

.theme-active .stButton > button,
.primary-action .stButton > button {{
  background: linear-gradient(135deg, var(--accent-2), var(--accent)) !important;
  color: #06100C !important;
  -webkit-text-fill-color: #06100C !important;
  border-color: transparent !important;
}}

.user-chip {{
  height: 44px;
  min-height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--line-strong);
  border-radius: 8px;
  background: var(--tile);
  color: var(--text-soft);
  font-size: 0.82rem;
  font-weight: 800;
}}

[data-testid="stTabs"] {{
  margin-top: 0;
}}

[data-testid="stTabs"] [role="tablist"] {{
  gap: 0.45rem;
  border-bottom: 1px solid var(--line);
}}

[data-testid="stTabs"] [role="tab"] {{
  color: var(--text-soft);
  font-weight: 800;
}}

.history-empty,
.history-item {{
  border: 1px solid var(--line-strong);
  border-radius: 8px;
  background: var(--tile);
  box-shadow: 0 10px 24px rgba(0,0,0,0.04);
}}

.history-empty {{
  padding: 1rem;
  color: var(--text-soft);
}}

.history-list {{
  display: grid;
  gap: 0.75rem;
  margin-top: 0.75rem;
}}

.history-item {{
  padding: 0.9rem;
}}

.history-label {{
  color: var(--accent);
  font-size: 0.68rem;
  font-weight: 900;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 0.45rem;
}}

.history-copy,
.history-copy p {{
  color: var(--text-soft) !important;
  font-size: 0.92rem !important;
  line-height: 1.55 !important;
}}

.reading-copy, .auth-card {{
  height: 100%;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 1.15rem;
  background: linear-gradient(180deg, var(--panel), rgba(255,255,255,0.025));
  box-shadow: 0 16px 52px var(--shadow);
}}

.section-label {{
  color: var(--accent);
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}}

.section-title {{
  margin: 0.45rem 0 0.4rem;
  color: var(--text);
  font-family: Newsreader, serif;
  font-size: clamp(1.9rem, 3vw, 2.8rem);
  line-height: 1;
  letter-spacing: 0;
}}

.section-copy {{
  margin: 0 0 1rem;
  color: var(--text-soft);
  font-size: 0.98rem;
  line-height: 1.6;
}}

.dosha-stack {{
  display: grid;
  gap: 0.65rem;
  margin-top: 1rem;
}}

.dosha-line {{
  display: grid;
  grid-template-columns: 2.2rem 1fr;
  gap: 0.65rem;
  align-items: center;
  padding: 0.75rem;
}}

.dosha-line b {{
  color: var(--text);
  font-size: 0.95rem;
}}

.dosha-line span {{
  display: block;
  margin-top: 0.15rem;
  color: var(--muted);
  font-size: 0.78rem;
}}

.suggestion-panel {{
  border: 1px solid var(--line-strong);
  border-radius: 8px;
  background: linear-gradient(180deg, var(--panel-2), var(--panel));
  padding: 1rem;
  box-shadow: 0 16px 52px var(--shadow);
}}

.suggestion-panel [data-testid="stHorizontalBlock"] {{
  gap: 0.65rem !important;
}}

.sug-col .stButton > button {{
  min-height: 76px !important;
  justify-content: flex-start !important;
  text-align: left !important;
  padding: 0.9rem 1rem !important;
  white-space: normal !important;
  line-height: 1.35 !important;
  font-size: 0.93rem !important;
}}

.auth-grid {{
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(320px, 1.1fr);
  gap: 1rem;
  margin-top: 1rem;
}}

.auth-card {{
  padding: 1.25rem;
}}

.auth-heading-card {{
  height: auto;
  min-height: 0;
  margin-bottom: 0.8rem;
}}

.auth-card h2 {{
  margin: 0.35rem 0 0.4rem;
  color: var(--text);
  font-family: Newsreader, serif;
  font-size: clamp(2rem, 4vw, 3.2rem);
  line-height: 0.95;
}}

.auth-card p {{
  color: var(--text-soft);
  line-height: 1.6;
}}

[data-testid="stTextInput"] input {{
  border-radius: 8px !important;
  border: 1px solid var(--line-strong) !important;
  background: var(--input) !important;
  color: var(--text) !important;
  font-weight: 600 !important;
}}

[data-testid="stTextInput"] label p {{
  color: var(--text-soft) !important;
  font-weight: 800 !important;
}}

[data-testid="stChatMessage"] {{
  background: transparent !important;
}}

[data-testid="stChatMessage"] [data-testid="stChatMessageContent"] {{
  border-radius: 8px !important;
  border: 1px solid var(--line) !important;
  box-shadow: 0 14px 34px var(--shadow) !important;
  padding: 1rem 1.05rem !important;
}}

[data-testid="stChatMessage"]:has([aria-label="Chat message from user"]) [data-testid="stChatMessageContent"] {{
  background: var(--user-bubble) !important;
}}

[data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) [data-testid="stChatMessageContent"] {{
  background: var(--assistant-bubble) !important;
}}

[data-testid="stChatMessageContent"] p,
[data-testid="stChatMessageContent"] li,
[data-testid="stChatMessageContent"] strong {{
  color: var(--text) !important;
  font-family: Inter, sans-serif !important;
  font-size: 0.98rem !important;
  line-height: 1.65 !important;
}}

.result-shell {{
  display: grid;
  gap: 0.9rem;
}}

.result-topline {{
  color: var(--muted);
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}}

.result-head {{
  display: flex;
  align-items: center;
  gap: 0.85rem;
}}

.result-icon {{
  width: 52px;
  height: 52px;
  border-radius: 8px;
  display: grid;
  place-items: center;
  border: 1px solid color-mix(in srgb, var(--dosha), transparent 55%);
  background: color-mix(in srgb, var(--dosha), transparent 86%);
  font-size: 1.5rem;
}}

.result-title {{
  color: var(--text);
  font-family: Newsreader, serif;
  font-size: 1.55rem;
  line-height: 1.1;
}}

.meter {{
  height: 10px;
  border-radius: 8px;
  background: rgba(255,255,255,0.08);
  overflow: hidden;
  border: 1px solid var(--line);
}}

.meter-fill {{
  height: 100%;
  background: linear-gradient(90deg, var(--dosha), var(--accent));
  box-shadow: 0 0 18px color-mix(in srgb, var(--dosha), transparent 35%);
}}

.result-copy {{
  border-left: 3px solid var(--dosha);
  padding-left: 0.9rem;
}}

.result-copy h4 {{
  margin: 0 0 0.45rem;
  color: var(--text) !important;
  font-family: Inter, sans-serif !important;
  font-size: 0.76rem !important;
  font-weight: 800 !important;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}}

.result-copy p {{
  margin: 0;
  color: var(--text-soft) !important;
}}

[data-testid="stBottom"],
[data-testid="stBottom"] > div,
[data-testid="stBottomBlockContainer"],
div[data-testid="stChatInput"],
.stChatInput {{
  background: linear-gradient(180deg, transparent, var(--bg) 42%) !important;
  border: none !important;
  box-shadow: none !important;
}}

[data-testid="stChatInputContainer"] {{
  max-width: 1080px !important;
  margin: 0 auto 1rem !important;
  border-radius: 8px !important;
  border: 1px solid var(--line-strong) !important;
  background: var(--input) !important;
  box-shadow: 0 18px 52px var(--shadow), 0 0 0 1px rgba(255,255,255,0.55), inset 0 1px 0 rgba(255,255,255,0.18) !important;
  overflow: hidden !important;
}}

[data-testid="stChatInputContainer"]:focus-within {{
  border-color: var(--accent-2) !important;
  box-shadow: 0 18px 52px var(--shadow), 0 0 0 3px color-mix(in srgb, var(--accent-2), transparent 78%) !important;
}}

[data-testid="stChatInputContainer"] textarea {{
  min-height: 58px !important;
  padding: 1rem !important;
  color: var(--text) !important;
  -webkit-text-fill-color: var(--text) !important;
  font-family: Inter, sans-serif !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
}}

[data-testid="stChatInputContainer"] textarea::placeholder {{
  color: var(--text-soft) !important;
  -webkit-text-fill-color: var(--text-soft) !important;
  opacity: 0.78 !important;
}}

[data-testid="stChatInputContainer"] button {{
  margin-right: 0.55rem !important;
  border-radius: 8px !important;
  background: linear-gradient(135deg, var(--accent-2), var(--accent)) !important;
  color: #06100C !important;
}}

.footer-note {{
  margin-top: 1rem;
  padding: 1rem 2rem 1.4rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255,255,255,0.025);
  text-align: center;
}}

@media (max-width: 900px) {{
  [data-testid="stMainBlockContainer"] {{
    padding: 0.8rem 0.75rem 7.2rem !important;
  }}

  .hero-grid, .auth-grid {{
    grid-template-columns: 1fr;
    padding: 1.15rem;
  }}

  .visual-card {{
    min-height: 260px;
    border-left: none;
    border-top: 1px solid var(--line);
  }}

  .hero-copy {{
    min-height: auto;
  }}

  .hero-stat-row {{
    grid-template-columns: 1fr;
  }}

  .control-strip {{
    padding: 0.6rem;
  }}
}}
</style>
"""
