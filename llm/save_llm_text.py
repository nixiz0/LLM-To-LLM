import csv
import string
from pathlib import Path


def save_conversation(conversation_history):
    desktop = Path.home() / 'Desktop'
    conversation_model_folder = desktop / 'conversations_model'
    conversation_model_folder.mkdir(parents=True, exist_ok=True)

    # Use the user's first 6 words as the file title
    first_user_message = conversation_history[0][0]
    first_five_words = ' '.join(first_user_message.split()[:6])
    filename = f"{first_five_words}.csv"

    # Remove all punctuation from filename
    filename = ''.join(ch for ch in filename if ch not in string.punctuation or ch == '.')

    # Save conversation to file
    with open(conversation_model_folder / filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Prompt", "Response"])
        for chat in conversation_history:
            writer.writerow([chat[0], chat[1]])