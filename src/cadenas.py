def invierte_cadena(cadena):
    resultado = ""
    for c in cadena:
        resultado = c+resultado
    return resultado

#cadena = input("¿Qué cadena quieres invertir? ")
#print(invierte_cadena(cadena))

def es_palindromo(cadena, ignora_espacios = True, ignora_mayusculas = True):
    resultado = True
    if ignora_espacios == True:
        cadena = cadena.replace(" ", "")
    if ignora_mayusculas == True:
        cadena = cadena.lower()
    longitud = len(cadena)
    for i in range(longitud//2):
        if (cadena[i] != cadena[(longitud-1)-i]):
            resultado = False
    return resultado

def estiliza_mensaje(cadena, alterna_may_min = True, usa_dieresis = False, sustituye_espacios = " "):
    longitud = len(cadena)
    last_upper = False
    resultado = ""
    if alterna_may_min:
        for i in range(longitud):
            current_char = cadena[i]
            if current_char.isalpha():
                if last_upper == False:
                    resultado += current_char.upper()
                    last_upper = True
                else:
                    resultado += current_char.lower()
                    last_upper = False
            else:
                resultado += current_char
    else:
        resultado = cadena

    if usa_dieresis:
        resultado = resultado.replace("a", "ä").replace("A","Ä").replace("e", "ë").replace("E", "Ë").replace("i", "ï").replace("I", "Ï").replace("o", "ö").replace("O", "Ö").replace("u", "ü").replace("U", "Ü")

    resultado = resultado.replace(" ", sustituye_espacios)
    return resultado

