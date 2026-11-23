from agente import criar_agente

def main():

    agente = criar_agente()
    config = {"configurable": {"thread_id": "conta_digital_1"}}

    print("Assistente de Conta Digital Simulada")
    print("Digite 'sair' para encerrar.")
    print("Todos os dados financeiros são fictícios.")

    while True:

        pergunta = input("\nVocê: ").strip()

        if pergunta.lower() == "sair":
            print("Conversa encerrada.")
            break

        if not pergunta:
            continue

        try:
            resposta = agente.invoke(
                {"messages": [{"role": "user", "content": pergunta}]},
                config=config
            )

            print("\nAssistente:", resposta["messages"][-1].content)

            ferramentas_usadas = []

            for mensagem in reversed(resposta["messages"]):

                if mensagem.type == "human":
                    break

                if mensagem.type == "tool":
                    ferramentas_usadas.append(mensagem.name)

            ferramentas_usadas.reverse()

            if ferramentas_usadas:
                print("Ferramentas utilizadas:", ", ".join(ferramentas_usadas))

        except Exception as erro:
            print("Erro ao consultar o agente:", type(erro).__name__)


if __name__ == "__main__":
    main()