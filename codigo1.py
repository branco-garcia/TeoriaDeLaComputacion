def realizarOperacion(lenguaje1, lenguaje2):
    resultado = []
    for i in lenguaje1:
        for x in lenguaje2:
            dato = i + x
            dato = dato.replace("_lambda_", "")
            if dato == "":
                resultado.append("_lambda_")
            else:
                resultado.append(dato)

    # Sacar elementos repetidos
    resultadoFinal = []
    for i in range(0, len(resultado)):
        for x in range(0, len(resultado)):
            if resultado[i] == resultado[x] and i != x:
                resultado[x] = ""

    for i in resultado:
        if i != "":
            resultadoFinal.append(i)

    return resultadoFinal


def deArrayAString(array):
    resultado = "{"
    for i in range(0, len(array)):
        resultado += array[i]
        if i < len(array) - 1:
            resultado += ", "
    resultado += "}"
    return resultado


L = ["_lambda_", "c", "hhh", "a", "b", "z"]

print("L =", deArrayAString(L))

n = int(input("Valor de n: "))
respuesta = []

if n == 0:
    respuesta = ["_lambda_"]
elif n == 1:
    respuesta = L
else:
    respuesta = L
    cont = 1
    while cont < n:
        respuesta = realizarOperacion(L, respuesta)
        cont += 1

respuesta = deArrayAString(respuesta)
print(respuesta)

# Transcribe en archivo
archivo = open("L_" + str(n) + ".txt", "w")
escribir = ""
cont = 0
for i in range(0, len(respuesta)):
    escribir += respuesta[i:i + 1]
    cont += 1
    if cont == 80:
        escribir += "\n"
        cont = 0

archivo.write(escribir)
archivo.close()
