def invierte_numero(numero):
    res = 0
    while(numero != 0):
        res = res*10 + (numero%10)
        numero = numero//10
    return res

def convierte_binario(numero):
    res = ""
    if numero == 0:
        return "0"
    while numero != 0:
        res = str(numero%2) + res
        numero = numero //2
    return res

def sumar_divisores_propios(n):
    suma_factores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_factores += i
    return suma_factores

def clasifica_numero(n):
    if sumar_divisores_propios(n) == n:
        return("Perfecto")
    elif sumar_divisores_propios(n) < n:
        return("Deficiente")
    else:
        return("Abundante")

def clasifica_rango(numero):
    for j in range(numero + 1):
        print(f"{j}: {clasifica_numero(j)}")

def busca_perfecto(n):
    i = 0
    j = 1
    while i < n:
        if clasifica_numero(j) == "Perfecto":
            i += 1
        j += 1
    return j-1

def test_invierte_numero():
    print("Probando invierte_numero...")
    assert invierte_numero(0) == 0
    assert invierte_numero(12345) == 54321
    assert invierte_numero(1000) == 1
    assert invierte_numero(987654321) == 123456789

def test_convierte_binario():
    print("Probando convierte_binario...")
    assert convierte_binario(0) == "0"
    assert convierte_binario(5) == "101"
    assert convierte_binario(10) == "1010"
    assert convierte_binario(255) == "11111111"

print(busca_perfecto(1))