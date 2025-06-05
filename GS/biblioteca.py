import random 
import os

logado = False
# e-mail, senha
usuario = []

# recebe inputs do usuário e os armazena na lista usuário
def criar_usuario(email: str = "", senha: str = "", cidade: str = "", regiao: str = "") -> None:

    print("============================= Menu login ============================")
    # Pergunta o E-mail até que seja digitado algo
    while email == "":
        email = input("E-mail: ")
        # Caso não tenha digitado nada
        if email == "":
            os.system("cls")
            print("Digite seu E-mail\n")

    # Pergunta a senha até que seja digitado algo
    while senha == "":
        senha = input("Senha: ")
        # Caso não tenha digitado nada
        if senha == "":
            os.system("cls")
            print("Digite uma senha")
            
    # Pergunta a cidade até que seja digitado algo
    while cidade == "":
        cidade = input("Cidade: ")
        # Caso não tenha digitado nada
        if cidade == "":
            os.system("cls")
            print("Digite a sua cidade")
    # Pergunta a regiao até que seja digitado algo
    while regiao == "":
        regiao = input("Região: ")
        # Caso não tenha digitado nada
        if regiao == "":
            os.system("cls")
            print("Digite a sua região")

    # Armazena os dados na lista usuario
    usuario.append({"email": email, "senha": senha, "cidade": cidade, "regiao": regiao})
    print("\nUsuário criado com sucesso!\n")

# função que recebe duas strings e gera aleatóriamente 3 mensagens diferentes 
def aviso(cidade: str, regiao: str) -> None:

    aviso = random.randint(1,3)
    match aviso:
        case 1:
            msg = "o clima está normal"
        case 2:
            msg = "há chance de alagamento"
        case 3:
            msg = "alerta de calor extremo"

    print(f"\nEm {cidade} na {regiao} {msg}")

# Verifica se o e-mail e senha são iguais a lista, se forem, função aviso será aplicada
def login() -> None:

    # Vê se o usuário já logou antes
    global logado
    email = input("\nE-mail: ")
    senha = input("Senha: ")

    # Verifica se o E-mail foi cadastrado
    for u in usuario:
        if u["email"] != email:
            print("\nE-mail não encontrado...")
    # Verifica se a senha está correta
        elif u["senha"] != senha:
            print("\nSenha incorreta...")
    # Aplica função aviso()
        elif u["email"] == email and u["senha"] == senha:
            aviso(cidade = u["cidade"], regiao = u["regiao"])
            logado = True

# Menu para o scanner
def scanner_menu() -> None:
    os.system("cls")

    global logado
    print("""
============================== Scanner ==============================
Já possui login? Login é completamente opcional porém você não será
necessario colocar manualmente seu endereço.
          
0 - VOLTAR
1 - Com login
2 - Sem login""")
    
    opcao = input("Escolha: ")

    match opcao:
        # Volta para a página principal
        case "0":
            return
        case "1":
        # Aplica a função login, caso já esteja logado, função aviso será aplicada diretamente
            for u in usuario:
                if logado == False:
                    login()
                else:
                    aviso(cidade = u["cidade"], regiao = u["regiao"])
        # Recebe duas variáveis e a plica a função aviso()
        case "2":
            cidade = ""
            regiao = ""

            while cidade == "":
                cidade = input("Digite a sua cidade: ")
                if cidade == "":
                    os.system("cls")
                    continue
            
            while regiao == "":
                regiao = input("Digite sua região: ")
                if regiao == "":
                    os.system("cls")
                    continue
            
            aviso(cidade = cidade, regiao = regiao)
        # Caso seja digitado outra coisa
        case _:
            print("Opção selecionada não existe, tente novamente.")

# Menu notificação
def notificação() -> None :
    print("""
****************************Atenção*********************************
1 - Fim da frente fria: temperaturas voltam a subir na região neste 
final de semana; veja a previsão no site da "G1" 
          
2 - Alagamento reportado na Zona Oeste desde 12:15 
""")
