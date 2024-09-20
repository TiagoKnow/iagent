from chatbot.conversation_text import start_conversation
import torch

if __name__ == "__main__":
    # Inicia o chat com o modelo

    print(torch.cuda.get_device_name(0))

    print(torch.cuda.device_count())
    for i in range(torch.cuda.device_count()):
        print(f"Device {i}: {torch.cuda.get_device_name(i)}")

    # exit(0)
    start_conversation()