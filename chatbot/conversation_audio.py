from models.language_model import load_model, generate_response
from speech.speech_recognition import get_audio
from speech.text_to_speech import speak

def start_conversation():
    model = load_model()
    while True:
        user_input = get_audio()
        if user_input.lower() == 'sair':
            break
        response = generate_response(model, user_input)
        print(f"Chatbot: {response}")
        speak(response)