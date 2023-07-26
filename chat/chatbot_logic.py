def get_weather(location: str) -> str:
    weather = {"weather": "晴れ", "temperature": 38.0}
    print(f"location: {location} / weather: {weather}")
    return f"{location}の天気は、{weather['weather']}。最高気温は{weather['temperature']}度の見込みだよ。"

def add_reminder(remind_at: str, note: str) -> str:
    reminder = {"remind_at": remind_at, "note": note}
    print(f"remind_at: {remind_at} / note: {note} / reminder: {reminder}")
    return f"{reminder['note']}を、{reminder['remind_at']}にお知らせします。"

def chat(text: str) -> str:
    return text

skills = {"get_weather": get_weather, "add_reminder": add_reminder, "chat": chat}

# インテント・エンティティの抽出処理
def extract_intent(text: str) -> tuple:
    if "天気" in text:
        entities = {"location": "佐賀"}
        return ("get_weather", entities)
    elif "リマインド" in text:
        entites = {"remind_at": "2023-07-22T12:34:56", "note": text}
        return ("add_reminder", entites)
    else:
        return ("chat", {"text": text})