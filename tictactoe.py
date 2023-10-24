import random
def playCachipum(humano, computadora):

    if(humano=="piedra" and computadora=="tijera"):
        return "Ganaste al computador"
    elif humano==computadora:
        return "Empate"
    else:
        return "Te ganó el computador"
    
if __name__=="__main__":
    print("Opciones: Piedra, papel, tijera")

    opciones=["piedra", "papel", "tijera"]

    humano = input("Ingrese su jugada \n")
    while humano not in opciones:
        print("Opcion invalida, intente nuevamente")
        humano = input("elige tu jugada: \n")
    computador= random.choice(opciones)

    print("el computador eligio", computador)

    resultado = playCachipum(humano, computador)
    print("Resultado", resultado)
    
