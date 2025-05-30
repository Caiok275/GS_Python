import os
os.system("cls")

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
3 - Servições de emergencia 

********************** 2 novas notificações **********************
5 - Notificações
""")
    escolha = input("Escolha: ")

    #Decisões
    match escolha:
        case 0:
            print("Obrigado por utilizar o nosso programa!")
        
    print("Pressione qualquer enter para continuar...")