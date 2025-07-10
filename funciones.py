#funciones.py

stock = 20
pagar_adicional = ("s/n")
def comprar_entrada():
    print("===reservar zapatillas===")
    nombre = input("nombre del comprador: ")
    codigo = input("digite la palabra secreta para confirmar la reserva: ").isalpha()
    lista = {
        "nombre": nombre,
        "codigo": codigo,
        "stock": stock
    }
    print("reserva confirmada para:{nombre}")

def buscar_zapatilla_reservada():
    print("===buscar zapallida reservada===")
    nombre_comprador = input("nombre del comprador a bucar: ")
    print("reserva encontrada:{nombre_comprador}-1par(es)(estanadar)")


    
 
    
def cancelar_reserva():
    print("cacelar la reserva de zapatillas")
    nombre = input("nombre del comprador que desea cancelar: ")
    print("nombre cancelado")

    

#validacion

def validar_nombre():
    nombre = input("nombre del comprador: ").strip().title()
    if nombre=={nombre}:
        return True
    return False
print("reserva realizada perfectamente")

def validar_codigo():
    codigo_secreto = ["estoyenlaliostadereserva"]
    codigo = input("digite la palabra secreta para confirmar la reserva: ")
    while True:
        if codigo and codigo_secreto==True or False:
            print("nombre correcto")
            break      
        else:
            print("ingrese denuevo")

def validar_nombre_comprador():
    nombre_comprador = input("nombre del comprador a buscar: ")
    while True:
        if nombre_comprador():
            pass
        


