def get_weather(location: str) -> str:
    weather = {"weather": "晴れ", "temperature": 30.0}
    return f"{location}の天気は、{weather['weather']}。最高気温は{weather['temperature']}度の見込みだよ。"

def whats_this() -> str:
    return f"私は、この日のためにpythonで作成されたchatbotアプリです。\n怠惰な発表者に代わりお返事します。"

def made_by_python() -> str:
    return f"はい、pythonで作成されました。\nインターネット記事と、この後発表する小関さんにもご協力いただき作成できました。"

def hard() -> str:
    return "一番大変だったのは環境系のエラーが出たときとのことです。"

def how_long() -> str:
    return "オリジナルアプリの作成に2～3週間。\n私の作成に2日間かかったようです。\n私の開発は手抜きがされているようです。"

def use_ai() -> str:
    return "いえ、私には使われておりません。\n例えばopenAIのAPIが使用されていれば、より高性能なアプリが作成できます。\n使用にお金がかかるため、私には使っていただけませんでした。"

def lang() -> str:
    return "Python以外では、Javaも少し勉強しています。\nJavaはカリキュラムが用意されているのでMacの方はやりやすいのではないでしょうか。"

def master() -> str:
    return "お答えできません。事務所を通してください。"

def stb() -> str:
    return "抹茶クリームフラペチーノが好物です。\n寒いときは、アールグレイティーラテのヴェンティサイズで、カスタムはオールミルク、ホイップ追加、はちみつ追加が好物です。"

def chat(text: str) -> str:
    return "お答えが用意されていません。発表者の想定を上回る質問でした。\n感服いたしました。"

skills = {"get_weather": get_weather,
          "whats_this": whats_this,
          "made_by_python": made_by_python,
          "hard": hard,
          "how_long": how_long,
          "hard": hard,
          "use_ai": use_ai,
          "master": master,
          "stb": stb,
          "chat": chat}

# インテント・エンティティの抽出処理
def extract_intent(text: str) -> tuple:
    if "天気" in text:
        entities = {"location": "東京"}
        return ("get_weather", entities)
    elif "なにこれ" in text or "なにそれ" in text or "何これ" in text or "何それ" in text:
        return ("whats_this", {})
    elif "python？" in text or "python?" in text:
        return ("made_by_python", {})
    elif "大変だった" in text:
        return ("hard", {})
    elif "どれくらいかかった" in text:
        return ("how_long", {})
    elif "AI" in text or "ai" in text:
        return ("use_ai", {})
    elif "言語" in text or "ai" in text:
        return ("lang", {})
    elif "発表者" in text:
        return ("master", {})
    elif "スタバ" in text:
        return ("stb", {})
    else:
        return ("chat", {"text": text})