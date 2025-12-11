# Jogo da Forca em Python

print("-" * 40)
print("Bem-vindo ao Jogo da Forca!")
print("Tente adivinhar a palavra secreta letra por letra.")
print("Você tem 6 tentativas. Boa sorte!")
print("-" * 40)

# Configurações iniciais
palavra_secreta = "PYTHON"
tentativas = 6

# Cria uma lista dinâmica de "_" com o mesmo tamanho da palavra secreta
letras_acertadas = ["_"] * len(palavra_secreta)

# O jogo continua enquanto houver vidas E houver letras ocultas ("_")
while tentativas > 0 and "_" in letras_acertadas:
    
    # Exibe a palavra formatada (separada por espaços) e vidas restantes
    print("\n" + " ".join(letras_acertadas))
    print(f"Vidas: {tentativas}")
    
    # Recebe o chute, remove espaços extras e converte para maiúscula
    chute = input("Qual letra? ").strip().upper()
    
    if chute in palavra_secreta:
        # Se acertou, percorre a palavra para achar as posições (índices) da letra
        for indice, letra in enumerate(palavra_secreta):
            if chute == letra:
                letras_acertadas[indice] = chute # Substitui o "_" pela letra correta
    else:
        # Se errou, penaliza o jogador
        tentativas -= 1
        print("Você errou!")

# Verificação final de vitória ou derrota
if "_" not in letras_acertadas:
    print("\nParabéns! Você ganhou. A palavra era:", palavra_secreta)
else:
    print("\nVocê perdeu! A palavra era:", palavra_secreta)