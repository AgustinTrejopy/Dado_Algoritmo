import random

numero_minimo = 1
numero_maximo = 6

jugar_otra_vez = "s"

while jugar_otra_vez == "s":
    print("Tiraste los dados...")
    print("el numero que salio es...")
    print(random.randint(numero_minimo ,numero_maximo))
    jugar_otra_vez = input("Jugar de nuevo? [s] o [n]")
    if jugar_otra_vez == "n":
        break
