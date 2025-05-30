import os
os.system("cls")
import biblioteca as _b

escolha = 1
while escolha != 0:
    #Página inicial com menu
    os.system("cls")
    print(
"""
========================= Global solution =========================
Bem Vindo bdsafaefeafdsafsadfdafsadfasdfafdasfdsafdsafdfafdasfsdafa
fdsafdsafadsfdsafsdaffafdafdsafadfafasdfdsafafasddescricaomuitofoda

0 - SAIR
1 - Fazer login  
2 - Scanner(escaneie sua area para possiveis desastres)
3 - Serviços de emergencia 

********************** 2 novas notificações **********************
5 - Notificações
""")

    escolha = int(input("Escolha: "))

    #Decisões
    match escolha:
        case 0:
            os.system("cls")
            print("Obrigado por utilizar o nosso programa!\n")
            break
        case 1:
            #Login
            break
        case 2:
            os.system("cls")
            print("============================= Scanner =============================")
            print("Já possui login? Login é completamente opcional porém você não será")
            print("necessario colocar manualmente seu endereço.\n")
            print("1 - Com login")
            print("2 - Sem login\n")

            opcao = input("Escolha: ")
            if opcao == "1":
                print("")

            elif opcao == "2":
                os.system("cls")
                _b.aviso(cidade = input("\nDigite sua cidade: "), regiao = input(f"\nEm qual região você mora? "))
                

        case _:
            os.system("cls")
            print("Opção com este número não existe, tente novamente.")
                
                
    input("\nPressione qualquer enter para continuar...")