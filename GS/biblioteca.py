import random 

def aviso(cidade: str, regiao: str) -> str:

    aviso = random.randint(1,3)
    match aviso:
        case 1:
            msg = "o clima está normal"
        case 2:
            msg = "há chance de alagamento"
        case 3:
            msg = "alerta de calor extremo"

    print(f"\nEm {cidade} na {regiao} {msg}")
    return {cidade}