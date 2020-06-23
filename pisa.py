"""
Proyecto Demo python
Simulador de examen de PISA.
El programa realiza una serie de preguntas con semillas aleatorias
y compara las respuesta con las del usuario para evaluarlo.
Al final le da un marcador al usuario y muestra sus errores.
"""

#bibliotecas
import random

"""
================== funciones de preguntas  =====================================
"""

def evalua_mult(val_1, val_2):
    """
    (uso de operadores, uso de funciones)
    recibe: val_1 valor numérico, val_2 valor numérico
    multiplica 2 valores
    devuelve: resultado de operación numérico
    """
    return val_1 * val_2

def evalua_resta(val_1, val_2):
    """
    (uso de operadores, uso de funciones)
    recibe: val_1 valor numérico, val_2 valor numérico
    resta val_1  a val_2
    devuelve: resultado de operación numérico
    """
    return val_1 - val_2

def evalua_producto_punto(val_1, val_2):
    """
    (operadores, funciones, listas, listas anidadas, ciclos y ciclos anidados)
    recibe: val_1 matriz de enteros, val_2 matriz de enteros
    Saca el producto punto de 2 matrices, multiplica cada elemento de las 2
    matrices y después los suma (hace una reducción)
    devuelve: producto punto acumulado entero
    """
    acum = 0
    for ren in range(3):
        for col in range(3):
            acum = acum + val_1[ren][col] * val_2[ren][col]
    return acum


"""
================== funciones auxiliares  =======================================
"""

def califica(respuesta, respuesta_usuario, calificacion, muestra = 1):

    """
    (uso de condicionales, funciones)
    recibe: respuesta variable numérica, respuesta_usuario variable numérica
            calficación varibale entera, muestra 0/1
    funcion auxiliar para manejar calificacion. Comprueba la respuesta, si el
    usario respondio lo mismo que la computadora  se le suma 1 punto a su
    calificación. Adicionalmente imprime los resultados al usuario si muestra
    es 1 y no los imprime si muestra es 0.
    devuelve: calificación entero
    """

    if respuesta == respuesta_usuario :
        calificacion = calificacion + 1

    if muestra == 1 :
        resultados(respuesta, respuesta_usuario, calificacion)

    return calificacion

def resultados(respuesta, respuesta_usuario, calificacion):

    """
    funcion auxiliar para imprimir
    Muestra en pantalla la respueta correcta, la respuesta de usuario y la
    calificacion acumulada actual.
    """

    print("Respuesta correcta: ", respuesta)
    print("Tu respuesta fue: ", respuesta_usuario)
    print("Calficacion actual ", calificacion)

def llena_mat(valor):
    """
    (uso de funciones, lista, listas anidadas, ciclos y ciclos anidados)
    iniciliza una lista anidada que representa una matriz de 3 x 3 a partir del
    valor recibido
    """
    lineas = []
    for ren in range(3):
        linea = []
        for col in range(3):
                linea.append(valor)
                valor = valor + 1
        lineas.append(linea)
    return lineas


def agrega_preguntas_operadores(pregunta):
    """
    función de integración, esta funcion solo integra a las demás para código
    ordenado y pid
    """
    pregunta = pregunta + 1
    print("\npregunta ", pregunta, ":")

    val_1 = random.randint(-50, 50)
    val_2 = random.randint(-50, 50)

    print(val_1, " * ", val_2, ":")
    return evalua_mult(val_1, val_2), pregunta

def agrega_preguntas_matrices(pregunta):
    """
    función de integración, esta funcion solo integra a las demás para código
    ordenado y pid
    """
    pregunta = pregunta + 1
    print("\npregunta ", pregunta, ":")

    val_1 = random.randint(-10, 50)
    val_2 = random.randint(-10, 50)
    mat_1  = llena_mat(val_1)
    mat_2  = llena_mat(val_2)

    print("el producto punto de las siguientes dos matrcies:")
    print("mat 1",mat_1)
    print("")
    print("mat2", mat_2)

    return evalua_producto_punto(mat_1, mat_2), pregunta


def muestra_arhivo():
    """
    (archivos de texto)
    imprime en consola el archivo del contenido
    """
    f = open("registro.txt", "r")
    print(f.read())
    f.close()

def guarda_archivo(nombre, texto):
    """
    (archivos de texto)
    recibe: nombre cadena de texto, texto cadena de texto
    agrega el nombre y el texto al archivo registro.txt
    """
    f = open("registro.txt", "a")
    f.write(nombre + "\t\t" + texto + "\n")
    f.close()

"""
========  parte principal del programa ========================================
"""

#se inicilizaon números aleatorios para ser usado en las funciones
calificacion = 0
pregunta = 0

resp_preg, pregunta =  agrega_preguntas_operadores(pregunta)
resp_usr = int(input("respuesta : "))
calificacion = califica(resp_preg, resp_usr, calificacion)

pausa = input("\n\npresiona enter para continuar\n\n")

resp_preg, pregunta =  agrega_preguntas_operadores(pregunta)
resp_usr = int(input("respuesta : "))
calificacion = califica(resp_preg, resp_usr, calificacion)

pausa = input("\n\npresiona enter para continuar\n\n")

resp_preg, pregunta = agrega_preguntas_matrices(pregunta)
resp_usr = int(input("respuesta : "))
calificacion = califica(resp_preg, resp_usr, calificacion)

pausa = input("\n\npresiona enter para continuar\n\n")

resp_preg, pregunta = agrega_preguntas_matrices(pregunta)
resp_usr = int(input("respuesta : "))
calificacion = califica(resp_preg, resp_usr, calificacion)

pausa = input("\n\npresiona enter para continuar\n\n")

#resumen
texto = str(calificacion) + " / " + str(pregunta)
texto = texto + " : " + str(float(calificacion)/pregunta)

print("tu calificación final es " + texto)

#guardar y ver scores
salvar = input("¿salvar resultado? s/n ")
if salvar == "s" :
    nombre = input("captura tu nombre ")
    guarda_archivo(nombre, texto)

resultados = input("¿deseas ver los demás resultados? s/n ")
if resultados == "s" :
    muestra_arhivo()

pausa = input("\n\npresiona enter para terminar el programa")
print("gracias por participar! hasta luego")
