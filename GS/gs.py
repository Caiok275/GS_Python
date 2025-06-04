import os
os.system("cls")
import biblioteca as _b

notificacao = True

# Menu de escolha
escolha = 1
while escolha != 0:
    #Página inicial com menu
    os.system("cls")
    print(
"""
========================== Global solution ==========================
                    Bem-vindo ao Scanner CEN! 

Fique sabendo que qualquer perigo local, basta informar 
sua cidade e bairro ou cadastre-se para uma experiencia mais prática.

*Recomendado tela cheia para visualizar melhor o programa.

0 - SAIR
1 - Fazer login  
2 - Scanner(escaneie sua area para possiveis desastres)""")

    # Checar se as notificações foram lidas ou não
    if notificacao == True:
        print("""
*********************** 2 novas notificações ***********************""")
        
    print("3 - Notificações\n")

    escolha = input("Escolha: ")
    # Decisões
    match escolha:
        # Sair
        case "0":
            os.system("cls")
            print("Obrigado por utilizar o nosso programa!\n")
            break

        # Fazer login
        case "1":
            os.system("cls")
            _b.criar_usuario()

        # Scanner
        case "2":
            os.system("cls")
            _b.scanner_menu()

        # Notificação
        case "3":
            os.system("cls")
            notificacao = False
            _b.notificação()

        # Nenhuma das opções
        case _:
            os.system("cls")
            print("Opção selecionada não existe, tente novamente.")
                
                
    input("\nPressione enter para continuar...")