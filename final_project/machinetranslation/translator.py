""""importing google translator from deep translator"""
from deep_translator import GoogleTranslator


def english_to_french(english_text):
    """Translate English to French"""
    french_text = GoogleTranslator('en', 'fr').translate(text=english_text)
    return french_text


def french_to_english(french_text):
    """Translate French to English"""
    english_text = GoogleTranslator('fr', 'en').translate(text=french_text)
    return english_text
