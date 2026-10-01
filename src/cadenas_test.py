from cadenas import estiliza_mensaje
from cadenas import invierte_cadena
from cadenas import es_palindromo


def test_invierte_cadena():
    print("Probando invierte_cadena...")
    assert invierte_cadena(" ")
    assert invierte_cadena("Texto de prueba")
    assert invierte_cadena("seres")

def test_es_palinfromo():
    print("Probando invierte_cadena...")
    assert es_palindromo("reconocer") == True
    assert es_palindromo("rotor") == True
    assert es_palindromo("radar") == True
    assert es_palindromo("Amor a Roma") == True
    assert es_palindromo("Luz azul") == True



def test_estiliza_mensaje():
    print("Probando estiliza_mensaje...")
    assert estiliza_mensaje("Fundamentos de programación 1") == "FuNdAmEnToS dE pRoGrAmAcIóN 1"
    assert estiliza_mensaje("Murciélago", usa_dieresis=True) == "MüRcÏéLäGö"
    assert estiliza_mensaje("Soy un programador experto", sustituye_espacios="*") == "SoY*uN*pRoGrAmAdOr*ExPeRtO"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=False, usa_dieresis=True, sustituye_espacios="-") == "Hölä-Mündö"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=True, usa_dieresis=False, sustituye_espacios="_") == "HoLa_MuNdO"

test_estiliza_mensaje()
test_invierte_cadena()
test_es_palinfromo()
print("Todas las pruebas pasaron correctamente.")