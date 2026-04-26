import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = Path(os.getenv("PRAKRITI_DATA_DIR", BASE_DIR / "data")).expanduser()
DB_PATH = DATA_DIR / os.getenv("PRAKRITI_DB_NAME", "prakriti_users.db")

BACKEND = os.getenv("PRAKRITI_BACKEND_URL", "http://127.0.0.1:5000")
OLLAMA = os.getenv("PRAKRITI_OLLAMA_URL", "http://127.0.0.1:11434")
OLLAMA_MODEL = os.getenv("PRAKRITI_OLLAMA_MODEL", "mistral:latest")

DARK = {
    "bg": "#080B09",
    "bg_2": "#101610",
    "panel": "rgba(20, 27, 21, 0.84)",
    "panel_2": "rgba(31, 40, 31, 0.72)",
    "text": "#F4F7EF",
    "text_soft": "#C8D3C2",
    "muted": "#81907E",
    "line": "rgba(215, 225, 205, 0.16)",
    "line_strong": "rgba(215, 225, 205, 0.34)",
    "accent": "#D6A72A",
    "accent_2": "#42A382",
    "accent_3": "#D96B5B",
    "blue": "#76B7D8",
    "shadow": "rgba(0, 0, 0, 0.42)",
    "input": "rgba(12, 17, 14, 0.96)",
    "tile": "rgba(255, 255, 255, 0.055)",
    "tile_hover": "rgba(255, 255, 255, 0.10)",
    "user": "linear-gradient(135deg, rgba(66, 163, 130, 0.22), rgba(118, 183, 216, 0.12))",
    "assistant": "linear-gradient(180deg, rgba(23, 31, 24, 0.96), rgba(13, 18, 15, 0.96))",
}

LIGHT = {
    "bg": "#F4F7EF",
    "bg_2": "#E6EEE3",
    "panel": "rgba(255, 255, 252, 0.96)",
    "panel_2": "rgba(244, 249, 241, 0.94)",
    "text": "#111B14",
    "text_soft": "#304132",
    "muted": "#5D6B5B",
    "line": "rgba(21, 35, 24, 0.20)",
    "line_strong": "rgba(21, 35, 24, 0.36)",
    "accent": "#B77D0B",
    "accent_2": "#16745E",
    "accent_3": "#B94E43",
    "blue": "#327DA8",
    "shadow": "rgba(35, 54, 36, 0.18)",
    "input": "#FFFFFF",
    "tile": "rgba(255, 255, 255, 0.96)",
    "tile_hover": "rgba(238, 247, 235, 0.98)",
    "user": "linear-gradient(135deg, rgba(22, 116, 94, 0.12), rgba(50, 125, 168, 0.10))",
    "assistant": "linear-gradient(180deg, rgba(255, 255, 250, 0.96), rgba(237, 244, 233, 0.96))",
}

DOSHA = {
    "vata": {"icon": "🌬", "color": "#5BA9D2", "title": "Vata"},
    "pitta": {"icon": "🔥", "color": "#D96B5B", "title": "Pitta"},
    "kapha": {"icon": "🌿", "color": "#42A382", "title": "Kapha"},
}

STATIC = {
    "vata": (
        "Your constitution reflects **Vata**: the airy current of movement and change. "
        "Favor warm, nourishing meals like soups, khichdi, root vegetables, sesame, dates, and ghee. "
        "Reduce excess cold, dryness, irregular eating, and overstimulation. "
        "A steady routine, warm oils, grounding herbs, and early sleep will help your system feel held."
    ),
    "pitta": (
        "Your constitution reflects **Pitta**: the fire of digestion, drive, and transformation. "
        "Choose cooling foods such as cucumber, mint, coconut, coriander, fennel, sweet fruits, and leafy greens. "
        "Reduce very spicy, fried, fermented, and acidic foods when heat builds. "
        "Gentle walks in greenery, cooling pranayama, and herbs like Brahmi or Amalaki can soothe your inner flame."
    ),
    "kapha": (
        "Your constitution reflects **Kapha**: the earthy, stabilizing force of structure and calm. "
        "Lean into warm, light, spiced foods like ginger, tulsi, black pepper, millet, lentils, and bitter greens. "
        "Reduce heaviness from excess dairy, cold desserts, oversleeping, and inactivity. "
        "Dynamic movement, earlier mornings, and stimulating herbs can rekindle vitality and clarity."
    ),
}

COMPLETION = {
    "vata": (
        "For now, keep the plan simple: choose warm food, warm drinks, gentle oiling, "
        "a quieter evening, and a consistent sleep time."
    ),
    "pitta": (
        "For now, keep the plan simple: choose cooling meals, slow the pace, avoid excess spice, "
        "and give yourself shade, water, and softness."
    ),
    "kapha": (
        "For now, keep the plan simple: choose warm light meals, add movement early in the day, "
        "reduce heaviness, and invite a little freshness into your routine."
    ),
}
