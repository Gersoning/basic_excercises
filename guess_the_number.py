import random

def run():
    aleatorio = random.randint(1,10)
    print("")
    numero = int(input("Digite un numero del 1 al 100: "))
    while numero != aleatorio:
        if numero < aleatorio:
            print("Creo que te aun te falta")
            print("")
        else:
            print("Creo que te pasaste")
            print("")
        numero = int(input("Digita otro numero: ")) 
    print("Ganaste!!!")

if __name__ == "__main__":
    run()