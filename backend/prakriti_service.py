import json
import re

import requests

from config import BACKEND, OLLAMA, OLLAMA_MODEL, STATIC


def guess_prakriti(text: str) -> str:
    value = text.lower()
    if any(word in value for word in ["hot", "anger", "angry", "burn", "fire", "heat", "oily", "pitta", "sweat"]):
        return "pitta"
    if any(word in value for word in ["heavy", "slow", "calm", "kapha", "deep sleep", "lethargic", "sleep"]):
        return "kapha"
    return "vata"


def extract_json(text: str) -> dict:
    try:
        return json.loads(text)
    except Exception:
        pass

    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in Ollama response")
    return json.loads(match.group(0))


def get_ollama_response(user_input: str):
    prompt = f"""
You are an Ayurvedic prakriti reflection assistant.
Classify the user's current pattern as exactly one of: vata, pitta, kapha.
Return only valid JSON with these keys:
prakriti: one of vata, pitta, kapha
confidence: integer from 55 to 98
advice: a complete, warm, practical paragraph of 110-150 words. End with a full sentence.

User: {user_input}
"""
    response = requests.post(
        f"{OLLAMA}/api/generate",
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {"temperature": 0.45},
        },
        timeout=90,
    )
    response.raise_for_status()
    payload = extract_json(response.json().get("response", "{}"))
    prakriti = str(payload.get("prakriti", guess_prakriti(user_input))).lower()
    if prakriti not in STATIC:
        prakriti = guess_prakriti(user_input)

    return {
        "prakriti": prakriti,
        "confidence": payload.get("confidence", 76),
        "advice": payload.get("advice", STATIC[prakriti]),
        "source": f"Ollama · {OLLAMA_MODEL}",
    }


def get_response(user_input: str):
    try:
        response = requests.post(f"{BACKEND}/chat", json={"message": user_input}, timeout=45)
        response.raise_for_status()
        payload = response.json()
        payload["source"] = "ML · Ollama" if payload.get("ollama_active") else "ML · Static"
        return payload
    except Exception:
        try:
            return get_ollama_response(user_input)
        except Exception:
            pass

        prakriti = guess_prakriti(user_input)
        return {
            "prakriti": prakriti,
            "confidence": 64,
            "advice": STATIC[prakriti],
            "source": "Guided Fallback",
        }
