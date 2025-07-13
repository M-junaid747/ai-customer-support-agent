import json
import os

# Load FAQ data once at module import
FAQ_PATH = os.path.join(os.path.dirname(__file__), '../../data/faq.json')
with open(FAQ_PATH, 'r') as f:
    faq_data = json.load(f)

def retrieve_context(user_question: str) -> str | None:
    user_words = set(user_question.lower().split())
    for entry in faq_data:
        entry_words = set(entry["question"].lower().split())
        if user_words & entry_words:
            return entry["answer"]
    return None
