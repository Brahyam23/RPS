
#Piedra=1
#Papel=2
#Tijera=3
def evaluar(jugador, pc):

    if jugador == 1:
        if pc == 1:
            print("El rival ha elegido piedra\n")
            print("Han empatado! Vamos por otra")

        elif pc == 2:
            print("El rival ha elegido papel\n")
            print("Has perdido =(")

        else:
            print("El rival ha elegido tijeras\n")
            print("Has ganado! =D")

    elif jugador == 2:
        if pc == 1:
            print("El rival ha elegido piedra\n")
            print("Has ganado! =D")

        elif pc == 2:
            print("El rival ha elegido papel\n")
            print("Han empatado! Vamos por otra")

        else:
            print("El rival ha elegido tijeras\n")
            print("Has perdido =(")
    else:
        if pc == 1:
            print("El rival ha elegido piedra\n")
            print("Has perdido =(")

        elif pc == 2:
            print("El rival ha elegido papel\n")
            print("Has ganado! =D")

        else:
            print("El rival ha elegido tijeras\n")
            print("Han empatado! Vamos por otra")
