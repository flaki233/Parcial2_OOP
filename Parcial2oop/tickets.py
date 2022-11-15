def cpelicula():
    global p
    p = p+1
    print("¿Que pelicula desea ver?")
    print("1, pelicula 1")
    print("2, pelicula 2")
    print("3, pelicula 3")
    print("4, pelicula 4")
    pelicula = int(input("Escoja su pelicula"))
    if pelicula < 1 or > 4:
        print("Escoja un numero del 1 al 4")
    else:
        print("Escoja la hora de su pelicula")


def hora():
    pelicula1 = {
        "1": "16.00-18.00"
        "2": "18.00-20.00"
        "3": "20.00-22.00"
    }
    pelicula2 = {
        "1": "17.00-19.00"
        "2": "19.00-21.00"
        "3": "21.00-23.00"
    }
    pelicula3 = {
        "1": "16.00-19.00"
        "2": "19.00-22.00"
        "3": "22.00-1.00"
    }
    pelicula4 = {
        "1": "18.00-29.00"
        "2": "20.00-22.00"
        "3": "22.00-00.00"
    }
    if pelicula == 1:
        print(pelicula1)
        t = input("escoja la hora:")
        h = pelicula1[t]
        print("listo, su pelicula sera a las  "+h)
    if pelicula == 2:
        print(pelicula2)
        t = input("escoja la hora:")
        h = pelicula2[t]
        print("listo, su pelicula sera a las  "+h)
    if pelicula == 3:
        print(pelicula3)
        t = input("escoja la hora:")
        h = pelicula3[t]
        print("listo, su pelicula sera a las  "+h)
    if pelicula == 4:
        print(pelicula4)
        t = input("escoja la hora:")
        h = pelicula4[t]
        print("listo, su pelicula sera a las  "+h)


abcdefg
hij


def puesto(t):
    print("Tiquetes regulares de la linea 1 hasta la 7, con valor de 5 dolares")
    print("Tiquetes VIP de la linea 8 hasta la 10, con valor de 10 dolares")
    tiquete = int(input("Seleccione su linea"))
    if tiquete >= 1 o <= 7:
    posicion = int(
        input("Ahora escoja un numero del 1 al 10 para su posicion"))
    if posicion < 1 or > 10:
        print("Recuerde que el numero debe ser entre el 1 y el 10")
    elif posisicion >= 1 or <= 10:
        print("Felicidades puede seguir a su funcion")

    elif tiquete > 7 o <= 10:
    posicion = int(input("Ahora escoja un numero del 1 al 10 para su columna"))
    if posicion < 1 or > 10:
        print("Recuerde que el numero debe ser entre el 1 y el 10")
    elif posisicion >= 1 or <= 10:
        print("Felicidades puede seguir a su funcion")

    elif:
        print("recuerde que debe ser un numero del 1 al 10")


if pelicula == 1:
with open("pelicula1.txt", "w") as file:
    file.write(tiquete, posicion)
elif pelicula == 2:
with open("pelicula2.txt", "w") as file:
    file.write(tiquete, posicion)
elif pelicula == 3:
with open("pelicula3.txt", "w") as file:
    file.write(tiquete, posicion)
elif pelicula == 4:
with open("pelicula4.txt", "w") as file:
    file.write(tiquete, posicion)
