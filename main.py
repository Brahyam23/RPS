from evaluacion import evaluar
import random
print("--------------------------------------")
print("Bienvenidos a piedra, papel o tijeras!")
print("--------------------------------------")

while True:
    while True:
        try:
            j=int(input("""\nQue vas a elegir?:
1° para Piedra
2° para Papel
3° para Tijeras
4° para Finalizar juego\n"""))

        except ValueError:
            print("Ha introducido un valor inválido. Inténtalo de nuevo.\n")
            continue
        if j == 4:
            print("Adiós!")
            break

        elif j > 4:
            print("Ha introducido un valor inválido. Inténtalo de nuevo.\n")

        else:
            opciones = [1, 2, 3] 

            p = (random.choice(opciones))
            print("\n")
            evaluar(j, p)
    break
