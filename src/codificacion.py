def cifra_cesar(cadena, cifra):
    alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    longitud = len(cadena)
    longitud_alfabeto = len(alfabeto)
    resultado = ""
    for i in range(longitud):
        if cadena[i] in alfabeto:
            posicion = alfabeto.find(cadena[i])+cifra
            while posicion >= longitud_alfabeto:
                posicion -= longitud_alfabeto
            resultado += alfabeto[i]
        else:
            resultado += cadena[i]
    return resultado

def rompe_cesar(cadena):
    alfabeto = "abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
    for i in range(len(alfabeto)):
        print (cifra_cesar(cadena, i))

texto_cifrado = cifra_cesar("Muy buenos días 24", 23)
print (texto_cifrado)

rompe_cesar(texto_cifrado)
