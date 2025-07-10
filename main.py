#main.py

from funciones import *

while True:
    print("\n=====TOTEM AUTOATENCIÓN RESERVA STRIKE=====")
    print("1.-reservar zapatillas")
    print("2.-buscar zapatillas reservadas ")
    print("3.-cancelara reserva de zapatillas")
    print("4.-salir")

    opciones = input("ingrese una opcionen (1-4): ")
    
    if opciones=='1':
        comprar_entrada()
    elif opciones=='2':
        buscar_zapatilla_reservada()
    elif opciones=='3':
        cancelar_reserva()
    elif opciones=='4':
        print("programa terminado")
        break
    else:
        print("debe ingresar una opcion valida")