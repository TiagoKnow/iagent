from transformers import pipeline
from deep_translator import GoogleTranslator


def load_model():
    return pipeline('text-generation', model="gpt2-xl", device=-1)  # use device=-1 para CPU


def translate_text(text, src='pt', dest='en'):
    # Traduzir o texto do português para inglês
    return GoogleTranslator(source=src, target=dest).translate(text)


def generate_response(model, prompt):
    # Traduzir o prompt para inglês
    translated_prompt = translate_text(prompt, src='pt', dest='en')

    # print('translated prompt', translated_prompt)

    # Gerar a resposta usando o modelo
    response = model(translated_prompt, max_length=350, truncation=True, clean_up_tokenization_spaces=True)[0][
        'generated_text']

    # print('original response', response)

    # Traduzir a resposta de volta para português
    translated_response = translate_text(response, src='en', dest='pt')

    return translated_response


if __name__ == "__main__":
    model = load_model()
    user_input = "Como posso resolver meu problema?"
    response = generate_response(model, user_input)
    print(f"Chatbot: {response}")
