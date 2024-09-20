import speech_recognition as sr

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        # Ajustar o nível de ruído para melhorar a precisão
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        # Retornar o texto reconhecido
        return recognizer.recognize_google(audio, language='pt-BR')
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
        return ""
    except sr.RequestError as e:
        print(f"Erro ao se conectar ao serviço de reconhecimento: {e}")
        return ""
