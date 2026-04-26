from config import DARK, LIGHT


def active_theme(selected: str):
    if selected == "light":
        return "light", LIGHT
    if selected == "dark":
        return "dark", DARK
    return "auto", DARK


def active_label(current: str, value: str, label: str) -> str:
    return f"✓ {label}" if current == value else label


def css_vars(theme: dict) -> str:
    return f"""
  --bg: {theme["bg"]};
  --bg-2: {theme["bg_2"]};
  --panel: {theme["panel"]};
  --panel-2: {theme["panel_2"]};
  --text: {theme["text"]};
  --text-soft: {theme["text_soft"]};
  --muted: {theme["muted"]};
  --line: {theme["line"]};
  --line-strong: {theme["line_strong"]};
  --accent: {theme["accent"]};
  --accent-2: {theme["accent_2"]};
  --accent-3: {theme["accent_3"]};
  --blue: {theme["blue"]};
  --shadow: {theme["shadow"]};
  --input: {theme["input"]};
  --tile: {theme["tile"]};
  --tile-hover: {theme["tile_hover"]};
  --user-bubble: {theme["user"]};
  --assistant-bubble: {theme["assistant"]};
"""


def root_theme_css(mode: str) -> str:
    if mode == "light":
        return f":root {{\n{css_vars(LIGHT)}}}\n"
    if mode == "dark":
        return f":root {{\n{css_vars(DARK)}}}\n"
    return f"""
:root {{
{css_vars(DARK)}}}

@media (prefers-color-scheme: light) {{
  :root {{
{css_vars(LIGHT)}  }}
}}
"""
