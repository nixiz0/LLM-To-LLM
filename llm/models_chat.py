import keyboard
from llm.model import start_llm_chat
from llm.save_llm_text import save_conversation
from voices.voice_system import NarratorVoice


def start_two_llm_chat(llm1, llm2, language='fr'):
    conversation_history = []
    working = True

    def toggle_program(e):
        nonlocal working
        working = not working

    if language=='fr':
        print("Apuuyez sur * sur votre clavier pour arrêter et sauvegarder la conversation")
    else: 
        print("Press * on your keyboard to stop and save the conversation")

    visual_talk_1 = NarratorVoice(voice_color=(0, 189, 255))
    visual_talk_2 = NarratorVoice(voice_color=(255, 0, 0))

    keyboard.on_press_key('*', toggle_program)

    prompt = "Bonjour"
    while working:
        response1, conversation_history = start_llm_chat("Assistant #1", llm1, prompt, conversation_history, visual_talk_1)
        prompt = response1

        response2, conversation_history = start_llm_chat("Assistant #2", llm2, prompt, conversation_history, visual_talk_2)
        prompt = response2

        save_conversation(conversation_history)