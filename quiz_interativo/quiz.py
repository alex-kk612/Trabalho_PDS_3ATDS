def executar_quiz(perguntas):
    pontuacao = 0
    for i, pergunta_data in enumerate(perguntas):
        print(f"\nPergunta {i + 1}: {pergunta_data['pergunta']}")
        for j, opcao in enumerate(pergunta_data['opcoes']):
            print(f"{j + 1}. {opcao}")

        while True:
            escolha = input("Escolha o número da sua resposta: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(pergunta_data['opcoes']):
                break
            else:
                print("Opção inválida. Digite o número correspondente à sua resposta.")

        resposta_usuario = pergunta_data['opcoes'][int(escolha) - 1]
        if resposta_usuario == pergunta_data['resposta']:
            print("Resposta correta!")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta correta era: {pergunta_data['resposta']}")

    print(f"\n--- Resultado Final ---")
    print(f"Sua pontuação foi de: {pontuacao} de {len(perguntas)}.")

if __name__ == "__main__":
    # Este bloco de código só será executado se este arquivo for rodado diretamente
    # Você pode adicionar testes ou chamadas de função aqui, se desejar.
    pass