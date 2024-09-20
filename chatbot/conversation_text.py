from models.language_model import load_model, generate_response


def start_conversation():
    # Carrega o modelo de linguagem
    model = load_model()

    while True:
        # Captura o input de texto do usuário
        user_input = input("Você: ")

        # Condição para encerrar o chat
        if user_input.lower() == 'sair':
            print("Encerrando a conversa. Até mais!")
            break

        # Gera a resposta com base no input do usuário
        response = generate_response(model, user_input)

        # Exibe a resposta no terminal
        print(f"Mr. Gepeto: {response}")