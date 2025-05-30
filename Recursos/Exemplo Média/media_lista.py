import os
os.system("cls")
import biblioteca as _b

avaliacao = []

escolha = 1
while escolha != 0:

    os.system("cls")
    print(
        """==================== Menu de seleção ====================

0 - SAIR
1 - Criar lista
2 - Mostrar lista
3 - Média da lista
        """)

    escolha = int(input("Escolha:"))

    match escolha:

        case 0:
            print("Obrigado por ter ulitlizado o programa!")
        case 1:
            os.system("cls")
        
            n = int(input("Digite sua avaliação:"))
            if n < 0 or n > 10:
                print("Nota inválida... Números apenas entre 0 e 10")
            else:
                print("Obrigado pela coperação")
                avaliacao.append(n)
        case 2:
            os.system("cls")
            print(avaliacao)
        case 3:
            os.system("cls")
            media = _b.media_lista(avaliacao)
            print(f"Média: {media}")
    
    input("Pressione qualquer tecla para continuar...")
    
